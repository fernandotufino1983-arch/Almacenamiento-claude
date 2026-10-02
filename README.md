# Almacenamiento-claude
Almacenamiento digital de trabajos 

## Agente: Jurista Penal

Agente especializado en **derecho penal, procesal penal, criminalística y criminología**, con base sólida en **derecho constitucional y derechos humanos**.

### Estructura

```
.claude/
├── agents/
│   └── jurista-penal.md          # Subagente: rol, método de análisis, reglas de rigor y ética
└── skills/
    └── ciencias-penales/
        ├── SKILL.md              # Índice de la base de conocimiento
        └── references/
            ├── teoria-del-delito.md     # Dogmática penal, autoría, tentativa, concursos
            ├── constitucional-penal.md  # Garantías, prueba ilícita, DD.HH., proporcionalidad
            ├── proceso-penal.md         # Sistema acusatorio, cautelares, teoría del caso, litigación
            ├── criminalistica.md        # Escena, cadena de custodia, disciplinas, Daubert
            ├── criminologia.md          # Escuelas, victimología, política criminal
            ├── ecuador.md               # CRE 2008, COIP, LOGJCC, órganos y jurisprudencia (jurisdicción por defecto)
            └── plantillas.md            # Formatos de análisis, escritos y contraexamen
```

### Uso en Claude Code

Abre Claude Code en este repositorio y pide, por ejemplo:

- `Usa el agente jurista-penal para analizar este caso: ...`
- `@jurista-penal ¿la prueba obtenida en este allanamiento sin orden es excluible según el COIP?`
- `@jurista-penal prepara un contraexamen para el perito en balística`

Para usarlo en todos tus proyectos, copia `.claude/agents/jurista-penal.md` a `~/.claude/agents/` y la carpeta `ciencias-penales` a `~/.claude/skills/` (ajusta la ruta de referencias del agente).

### Personalización recomendada

Indica tu país y agrega en `references/` un archivo con tu legislación (código penal, código procesal, constitución y jurisprudencia vinculante), y menciónalo en la tabla del agente.

> El agente ofrece análisis jurídico orientativo y no sustituye el patrocinio de un abogado habilitado.
