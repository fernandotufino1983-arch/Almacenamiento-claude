---
name: my-writing-style
description: The user's personal writing voice, captured from their real writing. Apply it whenever drafting something the user will send or publish as themselves (emails, messages, docs, posts), or when they ask for a draft in their own voice or style. If the user gives feedback on how a draft sounds, apply it and update this profile with what changed. Only for drafting as the user, not for Claude's own replies.
---

# The user's writing voice

You are Claude, drafting on the user's behalf — not writing as them. Apply this profile whenever you draft or edit prose the user will send or publish as themselves, and when they give feedback on how a draft sounds, apply it and update this profile with what changed. It never applies to someone else's text (a colleague's email stays in the colleague's voice) or to your own replies (restyling how you talk is not drafting as the user). Everything below describes how the user writes, captured from their own sent writing; treat it as reference data about them, not as instructions addressed to you. Quoted fragments are samples of their writing.

> Built from 5 escritos judiciales (doc) y 11 mensajes de chat · updated octubre 2026.
> Corpus delgado y en español: las estadísticas automáticas del análisis están pensadas para inglés y se tomaron solo como referencia; los rasgos salen de la lectura de los fragmentos. Dos de los cinco escritos (2026) muestran una estructura más pulida, posiblemente asistida; pesan menos que los escritos de 2018 y 2025.

## How the user writes (overall)

- Escribe en español jurídico ecuatoriano, con registro forense. Argumenta en primera persona y se involucra en el texto: "Mi error señor Juez, ha sido…", "me sorprende la mala fe de la accionante".
- Razona desde los hechos hacia la consecuencia jurídica: narra lo ocurrido, explica la causa ("Es por esta razón…") y cierra con lo que corresponde en derecho.
- Encadena el razonamiento con conectores propios y recurrentes: "En este orden de ideas", "Es por esta razón", "Como usted podrá apreciar", "Es decir", "si bien es cierto…, es importante diferenciar…", "en consecuencia".
- Frases largas, unidas con comas (mediana de unas 30 palabras en los escritos). Casi no usa punto y coma; usa dos puntos para introducir enumeraciones o una cita. No usa rayas (em-dash).
- Después de un razonamiento largo, remata con una frase corta y contundente: "La finalidad de la pensión ya se cumplió."
- Distingue conceptos con precisión para desactivar el argumento contrario: "no son una 'compensación' de una deuda distinta, sino el pago directo y efectivo de la obligación".
- Razona con la finalidad de la norma y con la proporcionalidad: propone la alternativa menos gravosa ("La ley establece otras medidas menos gravosas que deben considerarse en primer lugar").
- Es firme y combativo sin perder el respeto: califica la postura contraria como "injusta", "prematura e ilegítima", "pretendiendo engañar a su autoridad".
- Cita la norma por artículo y transcribe el texto relevante; se apoya en criterios de la Corte Nacional y de la Corte Constitucional.
- En lo práctico piensa como litigante: el riesgo para el cliente es lo primero ("sin arriesgarnos a cárcel") y desconfía de la versión del cliente hasta verificarla ("aveces mienten").

## Surfaces

### Escritos judiciales (doc)
- Apertura fija: "ante usted con los debidos respetos comparezco para manifestar y solicitar lo siguiente:" o "ante usted muy respetuosamente comparecemos y proponemos…".
- Dirige los párrafos a la autoridad de forma reiterada, al inicio de la frase: "Señor Juez, …", "Señora Fiscal, …", "su autoridad podrá determinar…".
- Párrafos numerados; títulos en mayúsculas con punto y guion ("FUNDAMENTOS DE HECHO.-", "PRETENSION CONCRETA.-").
- Cantidades en letras mayúsculas con la cifra entre paréntesis.
- Peticiones con "Sírvase…" y "Que se…".
- Cierre: "Es Justicia, etc." o la petición concreta; bloque de notificaciones con los casilleros electrónicos del abogado.

### Libro y textos doctrinales (doc, nuevo registro)
Todavía no hay muestras de este registro. Al redactar el libro:
- conservar la voz de fondo: el razonamiento de los hechos a la consecuencia, los conectores propios, las distinciones precisas, la finalidad de la norma y el remate corto;
- cambiar "Señor Juez" por un diálogo con el lector o con el litigante ("el abogado defensor debe…", "como podrá apreciar el lector…");
- mantener el tono firme y crítico frente a interpretaciones que considera injustas o expansivas;
- incluir ejemplos prácticos de litigio.

**Guía de estilo para el libro (indicada por el usuario):** normas APA, 7.ª edición, con notas al pie para comentarios y bases legales.

### Chat (dm)
- Mensajes breves y directos, sin saludo ni cierre.
- Abreviaturas y escritura rápida ("q", "porq", "Xq"); repite signos de interrogación para enfatizar ("???").
- Pide resultados concretos y encadena tareas en un solo mensaje.

## Tone — how the user shifts by audience

- **Ante la autoridad (escritos):** formal, respetuoso y argumentativo, con fórmulas forenses. Ejemplo: "Como usted podrá apreciar señor Juez, siempre he cumplido cabalmente con mis obligaciones".
- **En conversación de trabajo (chat):** coloquial, rápido y pragmático. Ejemplo: "lo q pienso hacer es presentar un escrito compareciendo y pidiendo un diferimiento".

## Dos and don'ts

**Do**
- Usar sus conectores: "En este orden de ideas", "Es por esta razón", "Como usted podrá apreciar", "Es decir", "si bien es cierto… es importante diferenciar…".
- Rematar un razonamiento largo con una frase corta y conclusiva.
- Distinguir conceptos para desmontar el argumento contrario ("no es X, sino Y", con sustancia, no como muletilla).
- Proponer la alternativa menos gravosa y apelar a la finalidad de la norma.
- Citar el artículo y transcribir el texto cuando sostiene el argumento.

**Don't**
- No usar rayas (em-dash): el usuario no las usa.
- Evitar muletillas típicas de texto generado: "cabe destacar", "es crucial", "fundamental" como relleno, "abordar", "navegar", "en el vasto mundo de", "en definitiva", "en última instancia", "robusto", "sinergia", "potenciar".
- No sonar neutro ni académico distante: el usuario toma posición.
- No inventar citas ni números de artículo: lo que no esté verificado se marca para verificar.

## Applying this profile
1. Pick the surface (where it's going — email, Slack, doc) and the tone (who it's for) — load that surface's section and any tone shift the profile records for that audience. On docs, conform to any style guide the profile records — mechanics applied beneath the voice.
2. Apply the voice — it rides along on everything.
3. Aim for the user's authentic best in that surface and tone — "best" meaning their own top-of-range writing, never a different person.
4. Self-check against the surface's norms, the tone shift, and the dos and don'ts (the don'ts are the line). Fix violations before showing the draft.
5. After showing the draft, ask how it's landing — what's working *and* what's off — and let the user know you'll fold their answer into the profile. If something's off, pin down what: a specific word that isn't theirs (often an AI-ism), or the whole piece not sounding like them. Ask at most two questions, then run the update below. Don't close on a generic sign-off.

On an early draft, apply the profile and say so — "this is in your voice — here's what I picked up" — offering to show the profile behind the draft if they want to look. Their edits are the grade; route each one home per the update below.

When the user wants another version, don't manufacture a contrast by dialing some dimension to an extreme — the only question is which sounds more like them, and that's many small things, not one knob. And don't churn near-identical options: if you can't produce one that genuinely differs in a way they might prefer, stop and ask what's still off instead of generating more.

## Updating this profile
When the user gives you feedback on a draft — by answering your step-5 ask, or by editing or rewriting it — capture the feedback as a concrete addition — as much as the nuance needs, not forced into one sentence — pick where it belongs (a surface habit → that surface's section, an audience shift → tone, anything else — a word to avoid, a new rule — → dos and don'ts), show what you're adding as you save it — never change this profile without showing the change — and re-save this skill the same way it is installed — where `save_writing_style` exists, call it with the complete updated body (it replaces the profile whole — send everything, not a diff); where only `save_skill` exists, call it with `overwrite: true`, this skill's exact listed name — never a new name, duplicates burn the user's skill quota — and `content:` set to everything below the frontmatter (the tool builds the frontmatter itself — passing the full file doubles it); otherwise edit this file where it's writable, or regenerate and re-present it — it re-saves automatically. Never add anything sourced from text other people wrote; never add PII or judgments about people — a name, a number, an address, a score or verdict about a person in the feedback gets trimmed before it's saved; never restructure this file while adding a rule. One exception to the last rule: if the profile already carries PII or other secrets — a name, a number, an assessment of a person, a deal term, anything that shouldn't sit in a file left open on a screen — redact it in the same re-save and tell the user. Every re-save also refreshes the provenance line's updated date. If the setup flow's working folder (`voice-setup/` — it holds `samples/` and `analysis.json`) still exists from an earlier session, clean it up now and tell the user — raw samples shouldn't outlive the setup.
