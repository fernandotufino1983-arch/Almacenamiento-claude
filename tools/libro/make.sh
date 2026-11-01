# Compila el libro (Word y PDF) con el índice paginado. Uso: bash tools/libro/make.sh [directorio_salida]
set -e
T=$(cd "$(dirname "$0")" && pwd); R=$T/../..; O=${1:-/tmp/libro_out}; mkdir -p $O
export NODE_PATH=/opt/node-tools/node_modules
TIT="¿De dónde salió el dinero? La defensa penal en el delito de lavado de activos"
COVER=$R/libro/portada/portada-a-a4.png; [ -f "$COVER" ] || COVER=""
rm -f $O/pg.json
for pass in 1 2 3 4; do
  python3 $T/build_compilado.py $O/pg.json $O/idx.json
  node $T/md2docx.js $R/libro/libro-compilado.md $O/Libro.docx "$TIT" $COVER >/dev/null
  (cd $O && soffice --headless --convert-to pdf --outdir $O $O/Libro.docx >/dev/null 2>&1)
  python3 $T/pages.py $O/Libro.pdf $O/pg.json $O/idx.json
done
python3 $T/build_compilado.py $O/pg.json $O/idx.json
node $T/md2docx.js $R/libro/libro-compilado.md $O/Libro.docx "$TIT" $COVER
(cd $O && soffice --headless --convert-to pdf --outdir $O $O/Libro.docx >/dev/null 2>&1)
pdfinfo $O/Libro.pdf | grep Pages
