# Almacenamiento-claude
Almacenamiento digital de trabajos 

## Agente de derecho laboral (Ecuador)

Este repositorio incluye un agente de Claude Code especializado en derecho laboral ecuatoriano:

| Ruta | Contenido |
|---|---|
| `.claude/agents/abogado-laboral.md` | Definición del agente `abogado-laboral` (rol, método de trabajo, reglas de rigor y formato). |
| `.claude/skills/derecho-laboral-ecuador/SKILL.md` | Índice del conocimiento de apoyo. |
| `.claude/skills/derecho-laboral-ecuador/referencias/` | Marco normativo y fórmulas, impugnación de actas de finiquito, despido intempestivo/ineficaz/indirecto, otras acciones, prescripción y procedimiento (COGEP). |
| `.claude/skills/derecho-laboral-ecuador/plantillas/` | Demanda por despido intempestivo, demanda de impugnación de acta de finiquito, contestación a la demanda (art. 142 COGEP) y ficha de datos del caso. |
| `.claude/skills/derecho-laboral-ecuador/scripts/liquidacion.py` | Calculadora estimativa de liquidaciones e indemnizaciones. |

### Cómo usarlo

En Claude Code, dentro de este repositorio:

- Pídelo directamente: *"Usa el agente abogado-laboral para analizar este caso: …"*, o escribe `@abogado-laboral`.
- Para impugnar un finiquito, adjunta o describe el acta (fechas, remuneración, rubros pagados) y pide la demanda.
- Calculadora:

  ```bash
  python3 .claude/skills/derecho-laboral-ecuador/scripts/liquidacion.py \
    --ingreso 2018-03-15 --salida 2026-09-30 --remuneracion 850 --sbu 482 \
    --causa despido_intempestivo --pagado 1200
  ```

Los escritos generados se guardan en `casos/<nombre-del-caso>/`.

> Herramienta de apoyo: todo escrito debe ser revisado y firmado por un abogado habilitado, y las cifras (en especial el SBU del año) y el texto vigente de las normas deben verificarse antes de presentarse.
