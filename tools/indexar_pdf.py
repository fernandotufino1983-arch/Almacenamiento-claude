#!/usr/bin/env python3
"""Convierte un PDF de la biblioteca a texto buscable.

Uso:
    python3 tools/indexar_pdf.py biblioteca/ecuador/COIP.pdf
    python3 tools/indexar_pdf.py biblioteca/ecuador/COIP.pdf --articulos

Genera junto al PDF un archivo .md con el texto. Con --articulos, además
inserta un encabezado "### Art. N" antes de cada artículo, para que el agente
pueda localizar un artículo con grep (p. ej. `grep -n "^### Art. 534" ...`).
Requiere `pdftotext` (paquete poppler-utils).
"""
import re
import subprocess
import sys
from pathlib import Path

ARTICULO = re.compile(r"^\s*(Art(?:í|i)culo|Art\.)\s*(\d+(?:\.\d+)?)(?=[\s.\-–—:])", re.IGNORECASE)


def extraer_texto(pdf: Path) -> str:
    resultado = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"],
        check=True, capture_output=True, text=True,
    )
    return resultado.stdout


def marcar_articulos(texto: str) -> str:
    lineas = []
    for linea in texto.splitlines():
        m = ARTICULO.match(linea)
        if m:
            lineas.append(f"\n### Art. {m.group(2)}\n")
        lineas.append(linea.rstrip())
    return "\n".join(lineas)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pdf = Path(sys.argv[1])
    texto = extraer_texto(pdf)
    if "--articulos" in sys.argv:
        texto = marcar_articulos(texto)
    salida = pdf.with_suffix(".md")
    salida.write_text(f"# {pdf.stem}\n\nFuente: `{pdf.name}`\n\n{texto}\n", encoding="utf-8")
    print(f"Texto escrito en {salida} ({len(texto):,} caracteres)")


if __name__ == "__main__":
    main()
