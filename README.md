# Almacenamiento-claude
Almacenamiento digital de trabajos

## Agente jurídico: `abogado-civil-ecuador`

Subagente de Claude Code especializado en Derecho Civil ecuatoriano, Código
Orgánico General de Procesos (COGEP), garantías jurisdiccionales y acciones
constitucionales (CRE y LOGJCC), y normativa conexa. Está definido en
`.claude/agents/abogado-civil-ecuador.md`.

### Estructura

- `.claude/agents/abogado-civil-ecuador.md` — definición del agente.
- `guias/acciones-civiles.md` — catálogo de acciones del Código Civil:
  legitimación, elementos, prescripción y vía procesal.
- `guias/garantias-constitucionales.md` — requisitos, improcedencia, plazos
  y estrategia de cada acción constitucional.
- `plantillas/civil/` — demandas (ordinaria, sumaria, ejecutiva, monitoria),
  contestación con excepciones, apelación, casación, providencias preventivas,
  y acciones del Código Civil (reivindicatoria, prescripción adquisitiva,
  nulidad, resolución, daños y perjuicios, pauliana, lesión enorme,
  posesorias, simulación).
- `plantillas/constitucional/` — acción de protección, medidas cautelares,
  hábeas corpus, hábeas data, acceso a la información, apelación de
  garantías, acción extraordinaria de protección, acción por incumplimiento,
  incumplimiento de sentencias e inconstitucionalidad.
- `normativa/` — textos legales vigentes para que el agente los consulte.

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
- Selección y redacción de garantías jurisdiccionales y acciones ante la
  Corte Constitucional, con análisis de procedencia (arts. 40 y 42 LOGJCC),
  admisibilidad (art. 62 LOGJCC) y reparación integral.

### Mejorar la precisión

Agrega los textos legales vigentes en la carpeta [`normativa/`](normativa/);
el agente los consultará antes de citar artículos.

> Los documentos generados son de apoyo y deben ser revisados y suscritos por
> un/a abogado/a habilitado/a.
