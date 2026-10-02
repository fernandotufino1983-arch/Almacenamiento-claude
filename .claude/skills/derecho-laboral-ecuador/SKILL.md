---
name: derecho-laboral-ecuador
description: Conocimiento práctico de derecho laboral ecuatoriano para litigio y asesoría - impugnación de actas de finiquito, demandas por despido intempestivo y despido ineficaz, visto bueno, desahucio, reclamo de haberes, horas suplementarias y extraordinarias, jubilación patronal, prescripción, procedimiento sumario del COGEP y cálculo de liquidaciones. Úsalo cuando el usuario plantee un caso laboral en Ecuador o pida redactar un escrito laboral.
---

# Derecho laboral ecuatoriano — guía de trabajo

Material de apoyo del agente `abogado-laboral`. Léelo según lo que pida el caso:

| Necesidad | Archivo |
|---|---|
| Normas clave, rubros y fórmulas | `referencias/marco-normativo.md` |
| Impugnar un acta de finiquito | `referencias/impugnacion-finiquito.md` |
| Despido intempestivo / ineficaz / indirecto | `referencias/despido-intempestivo.md` |
| Otras acciones (visto bueno, haberes, horas extra, jubilación, acoso, afiliación) | `referencias/otras-acciones.md` |
| Prescripción, competencia y procedimiento (COGEP) | `referencias/procedimiento.md` |
| **Requisitos del art. 142 COGEP (demanda y contestación)** | `referencias/requisitos-art-142-cogep.md` |
| Demanda por despido intempestivo | `plantillas/demanda-despido-intempestivo.md` |
| Demanda de impugnación de acta de finiquito | `plantillas/demanda-impugnacion-finiquito.md` |
| Contestación a la demanda (arts. 142 y 151 COGEP) | `plantillas/contestacion-demanda.md` |
| Recurso de apelación (fundamentación de agravios) | `plantillas/recurso-apelacion.md` |
| Lista de datos a pedir al cliente | `plantillas/ficha-de-caso.md` |
| Cálculo de liquidación | `scripts/liquidacion.py` |

## Uso de la calculadora

```bash
python3 .claude/skills/derecho-laboral-ecuador/scripts/liquidacion.py \
  --ingreso 2018-03-15 --salida 2026-09-30 \
  --remuneracion 850 --sbu 482 --region sierra \
  --causa despido_intempestivo \
  --pagado 1200
```

`python3 .../liquidacion.py --help` muestra todas las opciones (vacaciones gozadas, décimos acumulados mensualmente, despido ineficaz, dirigente sindical, remuneraciones impagas, etc.).

La calculadora es una **estimación**: usa la última remuneración como base de todos los rubros. Cuando haya remuneraciones variables (comisiones, horas extra habituales), recalcula la base con el promedio que corresponda (art. 95 CT) y pásala en `--remuneracion`.

## Advertencias

- **Toda demanda y toda contestación debe cumplir el art. 142 del COGEP** (la contestación, también por el art. 151). Verifica cada escrito con `referencias/requisitos-art-142-cogep.md` antes de entregarlo.

- Confirma siempre el **SBU del año** y el **texto vigente** de cada artículo; el Código del Trabajo se reforma con frecuencia.
- No cites resoluciones de la Corte Nacional sin verificar su número; marca `[VERIFICAR CITA]`.
- Los datos desconocidos se dejan como `[COMPLETAR: …]`, nunca se inventan.
