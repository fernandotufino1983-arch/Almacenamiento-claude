---
name: ciencias-penales
description: Base de conocimiento de derecho penal, procesal penal, constitucional-penal, criminalística y criminología. Úsala al analizar casos penales, calificar hechos delictivos, evaluar prueba pericial o cadena de custodia, detectar violaciones de garantías, explicar teorías criminológicas o redactar escritos penales.
---

# Ciencias penales — base de conocimiento

Esta skill reúne el marco doctrinal que usa el subagente `jurista-penal`. Lee solo los archivos que la consulta necesite:

- `references/teoria-del-delito.md` — estructura analítica del delito, escuelas dogmáticas, autoría, tentativa, concursos.
- `references/constitucional-penal.md` — principios limitadores, debido proceso, prueba ilícita, DD.HH., proporcionalidad.
- `references/proceso-penal.md` — sistema acusatorio, etapas, medidas cautelares, teoría del caso, litigación oral.
- `references/criminalistica.md` — método, lugar de los hechos, cadena de custodia, disciplinas y valoración pericial.
- `references/criminologia.md` — escuelas y teorías, victimología, política criminal y prevención.
- `references/ecuador.md` — CRE 2008, COIP, LOGJCC, órganos y jurisprudencia ecuatoriana.
- `references/casacion-penal-ecuador.md` — recurso de casación penal en Ecuador: causales, procedimiento, jurisprudencia y modelo de escrito.
- `references/colombia-criminalistica-criminologia.md` — doctrina comparada colombiana en criminalística y criminología.
- `references/colombia-doctrina-penal.md` — doctrina comparada colombiana: parte general, prueba y política criminal en conflicto armado.
- `references/plantillas.md` — formatos de análisis, dictamen, teoría del caso y escritos.

## Regla central

El contenido es **doctrina general y derecho comparado**. Antes de aplicarlo a un caso, identifica la jurisdicción y verifica la norma vigente (código penal, código procesal, constitución, jurisprudencia vinculante). No cites números de artículo nacionales sin verificarlos.

Si hay textos completos en `biblioteca/` (convertidos con `tools/indexar_pdf.py`), prevalecen sobre estas referencias.

## Formato obligatorio de los contraexámenes (preferencia del usuario)

Todo guion de contraexamen se redacta así:

- **Cada pregunta cita la fuente exacta del expediente y su texto literal**, con la fórmula: "Agente, en su informe, a foja ___ del expediente, usted escribió textualmente: '___'. ¿Correcto?". Si la cita está en el reverso, se escribe "foja ___ vuelta". Si viene de una pericia, se agrega la página de la pericia y el número de imagen.
- Las citas se transcriben tal como están en el documento, con sus errores, y se marcan con [sic].
- Se incluye la instrucción de mostrar la foja al testigo si duda o niega (COIP, art. 615, num. 4).
- Las contradicciones internas del documento (números, nombres, fechas) se ordenan en un cuadro con las dos fojas enfrentadas.
- Se indica cómo verificar la foliación en el expediente físico antes de la audiencia.
- Se mantienen las reglas de técnica: preguntas cerradas, una idea por pregunta, nunca preguntar "¿por qué?", y advertencias en los puntos de riesgo.
