#!/usr/bin/env python3
"""Calculadora estimativa de liquidación laboral (Código del Trabajo de Ecuador).

Es una estimación para análisis de casos: usa la última remuneración como base de
todos los rubros. Confirme siempre el SBU del año y el texto vigente de cada norma.
"""

import argparse
import json
import sys
from datetime import date, timedelta

CAUSAS = {
    "despido_intempestivo": "Despido intempestivo",
    "ineficaz": "Despido ineficaz (arts. 195.1-195.3)",
    "visto_bueno_trabajador": "Visto bueno a favor del trabajador (art. 173)",
    "desahucio": "Desahucio (art. 184)",
    "mutuo_acuerdo": "Mutuo acuerdo",
    "renuncia": "Renuncia / desahucio del trabajador",
    "visto_bueno_empleador": "Visto bueno a favor del empleador (art. 172)",
}

CON_INDEMNIZACION_188 = {"despido_intempestivo", "ineficaz", "visto_bueno_trabajador"}
CON_BONIFICACION_185 = CON_INDEMNIZACION_188 | {"desahucio", "mutuo_acuerdo", "renuncia"}


def fecha(texto):
    try:
        return date.fromisoformat(texto)
    except ValueError:
        raise argparse.ArgumentTypeError(f"fecha inválida '{texto}', use AAAA-MM-DD")


def aniversario(inicio, anios):
    """Fecha en que se cumplen `anios` desde `inicio` (29-feb pasa a 28-feb)."""
    try:
        return inicio.replace(year=inicio.year + anios)
    except ValueError:
        return inicio.replace(year=inicio.year + anios, day=28)


def tiempo_servicio(ingreso, salida):
    """Devuelve (años completos, días restantes, años en decimal)."""
    anios = salida.year - ingreso.year
    if aniversario(ingreso, anios) > salida:
        anios -= 1
    ultimo = aniversario(ingreso, anios)
    resto = (salida - ultimo).days
    siguiente = aniversario(ingreso, anios + 1)
    return anios, resto, anios + resto / (siguiente - ultimo).days


def inicio_periodo(salida, mes_inicio):
    """Primer día del período anual de beneficio que contiene la fecha de salida."""
    anio = salida.year if salida.month >= mes_inicio else salida.year - 1
    return date(anio, mes_inicio, 1)


def dias_en_periodo(ingreso, salida, mes_inicio):
    inicio = max(inicio_periodo(salida, mes_inicio), ingreso)
    return (salida - inicio).days + 1, inicio


def calcular(a):
    if a.salida < a.ingreso:
        raise SystemExit("La fecha de salida es anterior a la de ingreso.")
    rem = a.remuneracion
    anios, resto, anios_dec = tiempo_servicio(a.ingreso, a.salida)
    rubros, notas = [], []

    def rubro(nombre, valor, base, norma):
        rubros.append({"rubro": nombre, "base": base, "norma": norma, "valor": round(valor, 2)})

    # Indemnización por despido intempestivo (art. 188)
    if a.causa in CON_INDEMNIZACION_188:
        anios_188 = anios + (1 if resto > 0 else 0)
        meses = 3 if anios_188 <= 3 else min(anios_188, 25)
        rubro("Indemnización por despido intempestivo", meses * rem,
              f"{meses} remuneraciones ({anios_188} años; fracción = año completo)", "Art. 188 CT")
        if 20 <= anios < 25:
            notas.append("Tiene entre 20 y 25 años de servicio: reclamar la parte proporcional "
                         "de la jubilación patronal (arts. 188 y 216 CT); requiere cálculo actuarial.")
    if anios >= 25:
        notas.append("Tiene 25 años o más de servicio: tiene derecho a jubilación patronal (art. 216 CT).")

    # Indemnizaciones adicionales (arts. 195.3 y 187)
    if a.causa == "ineficaz" or a.dirigente_sindical:
        norma = "Art. 195.3 CT" if a.causa == "ineficaz" else "Art. 187 CT"
        rubro("Indemnización adicional (un año de remuneración)", 12 * rem, "12 remuneraciones", norma)
        if a.causa == "ineficaz" and a.dirigente_sindical:
            notas.append("Despido ineficaz de dirigente sindical: se computa una sola indemnización "
                         "anual adicional; verifique si procede acumular la del art. 187.")
        if a.causa == "ineficaz":
            notas.append("Despido ineficaz: plazo de 30 días desde el despido para demandar (art. 195.2). "
                         "Si hay reintegro, se pagan además remuneraciones pendientes con 10 % de recargo.")

    # Bonificación por desahucio (art. 185)
    if a.causa in CON_BONIFICACION_185:
        rubro("Bonificación por desahucio (25 % por año)", 0.25 * rem * anios_dec,
              f"25 % × {rem:.2f} × {anios_dec:.4f} años (proporcional)", "Art. 185 CT")
        if a.causa in CON_INDEMNIZACION_188:
            notas.append("Bonificación por desahucio en despido: verifique el criterio vigente de la "
                         "Corte Nacional sobre su procedencia y si se calcula por años completos o proporcional.")
        if a.causa == "renuncia":
            notas.append("En renuncia, la bonificación del art. 185 procede si se formalizó como "
                         "desahucio ante el inspector del trabajo.")

    # Décima tercera (art. 111): período 1 dic – 30 nov
    if not a.decimos_mensualizados:
        dias, desde = dias_en_periodo(a.ingreso, a.salida, 12)
        rubro("Décima tercera remuneración proporcional", rem * dias / 360,
              f"{rem:.2f} × {dias} días / 360 (desde {desde})", "Art. 111 CT")
        # Décima cuarta (art. 113)
        mes = 8 if a.region == "sierra" else 3
        dias, desde = dias_en_periodo(a.ingreso, a.salida, mes)
        rubro("Décima cuarta remuneración proporcional", a.sbu * dias / 360,
              f"SBU {a.sbu:.2f} × {dias} días / 360 (desde {desde}, región {a.region})", "Art. 113 CT")

    # Vacaciones (arts. 69, 71): 15 días + 1 por cada año que exceda de 5, máximo 15 adicionales
    adicional = min(max(anios - 5, 0), 15)
    dias_vac = 15 + adicional
    valor_dia = rem / 30
    fraccion = resto / (aniversario(a.ingreso, anios + 1) - aniversario(a.ingreso, anios)).days
    rubro("Vacaciones proporcionales no gozadas", dias_vac * valor_dia * fraccion,
          f"{dias_vac} días × {valor_dia:.2f} × {fraccion:.4f} del período en curso", "Arts. 69, 71 CT")
    if a.periodos_vacaciones_pendientes:
        rubro(f"Vacaciones no gozadas ({a.periodos_vacaciones_pendientes} período/s completo/s)",
              a.periodos_vacaciones_pendientes * dias_vac * valor_dia,
              f"{a.periodos_vacaciones_pendientes} × {dias_vac} días × {valor_dia:.2f}", "Arts. 69, 71, 75 CT")

    # Fondos de reserva (art. 196)
    if a.meses_fondos_pendientes:
        rubro("Fondos de reserva no pagados", 0.0833 * rem * a.meses_fondos_pendientes,
              f"8,33 % × {rem:.2f} × {a.meses_fondos_pendientes} meses", "Art. 196 CT")
        if anios < 1:
            notas.append("Los fondos de reserva se generan a partir del segundo año de servicio.")

    # Horas suplementarias y extraordinarias (art. 55)
    valor_hora = rem / 240
    if a.horas_suplementarias:
        rubro("Horas suplementarias (recargo 50 %)", a.horas_suplementarias * valor_hora * 1.5,
              f"{a.horas_suplementarias} h × {valor_hora:.4f} × 1,5", "Art. 55 CT")
    if a.horas_extraordinarias:
        rubro("Horas extraordinarias (recargo 100 %)", a.horas_extraordinarias * valor_hora * 2,
              f"{a.horas_extraordinarias} h × {valor_hora:.4f} × 2", "Art. 55 CT")

    # Remuneraciones impagas (art. 94)
    if a.remuneraciones_impagas:
        rubro("Remuneraciones impagas", a.remuneraciones_impagas, "monto adeudado", "Art. 94 CT")
        rubro("Recargo por mora (triple de lo no pagado)", 3 * a.remuneraciones_impagas,
              f"3 × {a.remuneraciones_impagas:.2f}", "Art. 94 CT")
        notas.append("Recargo del art. 94: verifique el texto vigente y su alcance antes de reclamarlo.")

    total = round(sum(r["valor"] for r in rubros), 2)
    resultado = {
        "causa": CAUSAS[a.causa],
        "ingreso": a.ingreso.isoformat(),
        "salida": a.salida.isoformat(),
        "tiempo_servicio": f"{anios} años y {resto} días",
        "remuneracion_base": rem,
        "sbu": a.sbu,
        "rubros": rubros,
        "total": total,
        "notas": notas + ["Estimación: confirme SBU del año, base de cálculo (art. 95 CT) y texto vigente."],
    }
    if a.pagado is not None:
        resultado["pagado"] = a.pagado
        resultado["diferencia"] = round(total - a.pagado, 2)
    return resultado


def imprimir(r):
    print(f"## Liquidación estimada — {r['causa']}\n")
    print(f"- Ingreso: {r['ingreso']} | Salida: {r['salida']} | Tiempo: {r['tiempo_servicio']}")
    print(f"- Remuneración base: USD {r['remuneracion_base']:,.2f} | SBU: USD {r['sbu']:,.2f}\n")
    print("| Rubro | Base / fórmula | Norma | Valor USD |")
    print("|---|---|---|---:|")
    for x in r["rubros"]:
        print(f"| {x['rubro']} | {x['base']} | {x['norma']} | {x['valor']:,.2f} |")
    print(f"| **Total** | | | **{r['total']:,.2f}** |")
    if "pagado" in r:
        print(f"| Pagado en finiquito | | | {r['pagado']:,.2f} |")
        print(f"| **Diferencia reclamable** | | | **{r['diferencia']:,.2f}** |")
    print("\n**Notas:**")
    for n in r["notas"]:
        print(f"- {n}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ingreso", type=fecha, required=True, help="fecha de ingreso AAAA-MM-DD")
    p.add_argument("--salida", type=fecha, required=True, help="fecha de terminación AAAA-MM-DD")
    p.add_argument("--remuneracion", type=float, required=True, help="última remuneración mensual (art. 95)")
    p.add_argument("--sbu", type=float, required=True, help="Salario Básico Unificado del año de salida")
    p.add_argument("--region", choices=["sierra", "costa"], default="sierra",
                   help="sierra = Sierra/Amazonía; costa = Costa/Galápagos (décima cuarta)")
    p.add_argument("--causa", choices=sorted(CAUSAS), required=True)
    p.add_argument("--dirigente-sindical", action="store_true", help="indemnización adicional art. 187")
    p.add_argument("--decimos-mensualizados", action="store_true",
                   help="los décimos se pagaban mensualmente en el rol (no se liquidan)")
    p.add_argument("--periodos-vacaciones-pendientes", type=int, default=0,
                   help="períodos anuales completos de vacaciones no gozadas")
    p.add_argument("--meses-fondos-pendientes", type=int, default=0,
                   help="meses de fondos de reserva no pagados ni depositados")
    p.add_argument("--horas-suplementarias", type=float, default=0, help="total de horas al 50 %%")
    p.add_argument("--horas-extraordinarias", type=float, default=0, help="total de horas al 100 %%")
    p.add_argument("--remuneraciones-impagas", type=float, default=0, help="monto de remuneraciones adeudadas")
    p.add_argument("--pagado", type=float, help="valor recibido en el acta de finiquito")
    p.add_argument("--json", action="store_true", help="salida en JSON")
    a = p.parse_args(argv)
    r = calcular(a)
    if a.json:
        json.dump(r, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        imprimir(r)


if __name__ == "__main__":
    main()
