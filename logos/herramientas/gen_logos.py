"""Genera los SVG finales de Jurix Global con el texto convertido a trazos."""
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS_DIR, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
SERIF = TTFont(os.path.join(FONTS_DIR, "cormorant.ttf"))
SANS = TTFont(os.path.join(FONTS_DIR, "inter.ttf"))

NAVY, GOLD, IVORY, BLACK, WHITE = "#0B1F3A", "#B8955A", "#F7F4EE", "#1C1C1E", "#FFFFFF"


def text_width(font, text, size, ls):
    upm = font["head"].unitsPerEm
    cmap, hmtx = font.getBestCmap(), font["hmtx"]
    adv = sum(hmtx[cmap[ord(c)]][0] for c in text) * size / upm
    return adv + ls * (len(text) - 1)


def text_path(font, text, x, y, size, ls=0, anchor="start"):
    upm = font["head"].unitsPerEm
    cmap, hmtx, gs = font.getBestCmap(), font["hmtx"], font.getGlyphSet()
    s = size / upm
    if anchor == "middle":
        x -= text_width(font, text, size, ls) / 2
    pen = SVGPathPen(gs)
    for c in text:
        name = cmap[ord(c)]
        gs[name].draw(TransformPen(pen, (s, 0, 0, -s, x, y)))
        x += hmtx[name][0] * s + ls
    return pen.getCommands()


def iso(main, accent, tx=0, ty=0, k=1):
    return f'''<g transform="translate({tx} {ty}) scale({k})">
    <circle r="60" fill="none" stroke="{main}" stroke-width="5"/>
    <ellipse rx="25" ry="60" fill="none" stroke="{accent}" stroke-width="2.5"/>
    <line x1="-55" y1="-24" x2="55" y2="-24" stroke="{accent}" stroke-width="2.5"/>
    <line x1="-55" y1="24" x2="55" y2="24" stroke="{accent}" stroke-width="2.5"/>
    <rect x="-10" y="-80" width="44" height="8" fill="{accent}"/>
    <path d="M12 -72 V18 A24 24 0 0 1 -36 18" fill="none" stroke="{main}" stroke-width="15"/>
  </g>'''


def svg(view_box, body, comment):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}">\n'
            f'  <!-- Jurix Global — {comment}. Texto convertido a trazos (no requiere fuentes). -->\n'
            f'  {body}\n</svg>\n')


def horizontal(main, accent, text):
    return (iso(main, accent, 100, 110)
            + f'\n  <path fill="{text}" d="{text_path(SERIF, "JURIX", 190, 112, 60, 6)}"/>'
            + f'\n  <rect x="192" y="127.25" width="280" height="1.5" fill="{accent}"/>'
            + f'\n  <path fill="{text}" d="{text_path(SANS, "GLOBAL · ABOGADOS", 192, 154, 15, 7)}"/>')


def vertical(main, accent, text):
    return (iso(main, accent, 0, 0)
            + f'\n  <path fill="{text}" d="{text_path(SERIF, "JURIX", 0, 140, 64, 8, "middle")}"/>'
            + f'\n  <rect x="{-TAG_W / 2}" y="161" width="{TAG_W}" height="2" fill="{accent}"/>'
            + f'\n  <path fill="{text}" d="{text_path(SANS, "GLOBAL · ABOGADOS", 0, 194, 17, 8, "middle")}"/>')


TAG_W = round(text_width(SANS, "GLOBAL · ABOGADOS", 17, 8))
H_VB, V_VB, I_VB = "28 18 456 164", f"{-TAG_W / 2 - 12} -92 {TAG_W + 24} 300", "-66 -86 132 152"
variants = {
    "color": (NAVY, GOLD, NAVY, "a color, para fondos claros"),
    "negativo": (IVORY, GOLD, IVORY, "negativo, para fondos azul marino u oscuros"),
    "negro": (BLACK, BLACK, BLACK, "un solo color negro"),
    "blanco": (WHITE, WHITE, WHITE, "un solo color blanco"),
}
for key, (m, a, t, desc) in variants.items():
    open(f"{OUT}/jurix-global-horizontal-{key}.svg", "w").write(svg(H_VB, horizontal(m, a, t), f"logo horizontal {desc}"))
    open(f"{OUT}/jurix-global-vertical-{key}.svg", "w").write(svg(V_VB, vertical(m, a, t), f"logo vertical {desc}"))
    open(f"{OUT}/jurix-global-isotipo-{key}.svg", "w").write(svg(I_VB, iso(m, a), f"isotipo {desc}"))

# Avatar redondo (WhatsApp / redes) y favicon cuadrado
open(f"{OUT}/jurix-global-avatar.svg", "w").write(svg(
    "-100 -100 200 200", f'<circle r="100" fill="{NAVY}"/>\n  ' + iso(IVORY, GOLD, 0, 8, 0.95),
    "avatar redondo para WhatsApp y redes"))
open(f"{OUT}/jurix-global-favicon.svg", "w").write(svg(
    "-100 -100 200 200", f'<rect x="-100" y="-100" width="200" height="200" rx="36" fill="{NAVY}"/>\n  '
    + iso(IVORY, GOLD, 0, 10, 1.05), "ícono para web y aplicaciones"))
print("ok")
