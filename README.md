# Almacenamiento-claude
Almacenamiento digital de trabajos

## Agente jurídico: `abogado-civil-ecuador`

Subagente de Claude Code especializado en Derecho Civil ecuatoriano, Código
Orgánico General de Procesos (COGEP) y normativa conexa. Está definido en
`.claude/agents/abogado-civil-ecuador.md`.

### Cómo usarlo

Dentro de Claude Code, en este repositorio:

- Pídelo por nombre: *"Usa el agente abogado-civil-ecuador para analizar este
  contrato de arrendamiento."*
- O simplemente haz una consulta civil/procesal; Claude lo invocará
  automáticamente.
- Con `/agents` puedes ver y editar su configuración.

### Qué hace

- Dictámenes jurídicos (antecedentes, problema, normativa, análisis,
  conclusiones, plazos).
- Elección de vía procesal (ordinario, sumario, ejecutivo, monitorio,
  voluntario) y competencia.
- Cálculo y alerta de términos procesales y plazos de prescripción.
- Redacción de demandas (art. 142 COGEP), contestaciones, excepciones,
  recursos, escritos y contratos.

### Mejorar la precisión

Agrega los textos legales vigentes en la carpeta [`normativa/`](normativa/);
el agente los consultará antes de citar artículos.

> Los documentos generados son de apoyo y deben ser revisados y suscritos por
> un/a abogado/a habilitado/a.
