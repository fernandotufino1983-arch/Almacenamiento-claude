# Biblioteca del agente jurista-penal

Aquí van los textos completos (leyes, libros, ensayos, estudios) que el agente consulta antes que su conocimiento general.

```
biblioteca/
├── ecuador/          # COIP, Constitución, LOGJCC, COFJ, sentencias de la Corte Constitucional y la CNJ
├── colombia/         # Libros, manuales y ensayos de criminalística y criminología
└── otros/            # Doctrina general, informes internacionales, etc.
```

## Cómo agregar un documento

1. Sube el PDF a la carpeta que corresponda. Desde el celular puedes hacerlo en la app o la web de GitHub: repositorio → rama `ccr-941774a8-fvrcex` → carpeta → **Add file → Upload files**. También puedes adjuntarlo en el chat con Claude.
2. Conviértelo a texto buscable:
   ```bash
   python3 tools/indexar_pdf.py biblioteca/ecuador/COIP.pdf --articulos
   ```
   Esto genera `COIP.md`, con un encabezado `### Art. N` por artículo.
3. Para PDFs escaneados (imágenes) primero hace falta OCR (por ejemplo `ocrmypdf`).

## Cuidado con la privacidad

No subas expedientes reales, datos de víctimas o de procesados, ni documentos reservados si el repositorio es público o compartido. En el caso de libros con derechos de autor, guárdalos solo para uso personal en un repositorio **privado**.
