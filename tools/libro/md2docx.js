// Convierte libro-compilado.md en .docx. Uso: node md2docx.js entrada.md salida.docx "Título" [portada.png]
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, FootnoteReferenceRun, PageBreak, HeadingLevel, AlignmentType, LevelFormat,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, Footer, PageNumber, TabStopType, LeaderType, ImageRun } = require('docx');
const [,, inp, out, title, cover] = process.argv;
const FONT = 'Cambria', ACCENT = '1F3864';
const src = fs.readFileSync(inp, 'utf8').split('\n');
const footnotes = {}; const fnIds = {}; let fnN = 0; const lines = [];
for (const l of src) { const m = l.match(/^\[\^([\w-]+)\]:\s*(.*)$/); if (m) { footnotes[m[1]] = m[2]; } else lines.push(l); }
const fnDefs = {};
function fnRef(id) { if (!(id in fnIds)) { fnIds[id] = ++fnN; fnDefs[fnN] = { children: [new Paragraph({ children: runs(footnotes[id] || '[nota faltante]', { size: 17 }, true) })] }; } return new FootnoteReferenceRun(fnIds[id]); }
function runs(text, base = {}, inNote = false) {
  const out = []; const re = /(\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*\s][^*]*\*|\[\^[\w-]+\])/g; let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('[^')) { if (!inNote) out.push(fnRef(t.slice(2, -1))); }
    else if (t.startsWith('***')) out.push(new TextRun({ text: t.slice(3, -3), bold: true, italics: true, ...base }));
    else if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}
const para = l => new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 140, line: 288 }, children: runs(l) });
const children = []; let inRefs = false; let i = 0;
while (i < lines.length) {
  const l = lines[i];
  if (/^\|/.test(l)) {
    const rows = []; while (i < lines.length && /^\|/.test(lines[i])) { if (!/^\|[\s:|-]+\|\s*$/.test(lines[i])) rows.push(lines[i].trim().replace(/^\||\|$/g, '').split('|').map(s => s.trim())); i++; }
    const nc = Math.max(...rows.map(r => r.length));
    children.push(new Table({ width: { size: 100, type: WidthType.PERCENTAGE }, rows: rows.map((r, ri) => new TableRow({ tableHeader: ri === 0, children: Array.from({ length: nc }, (_, ci) => new TableCell({
      shading: ri === 0 ? { type: ShadingType.CLEAR, fill: ACCENT, color: 'auto' } : (ri % 2 === 0 ? { type: ShadingType.CLEAR, fill: 'EEF2F8', color: 'auto' } : undefined),
      children: [new Paragraph({ children: runs(r[ci] || '', ri === 0 ? { bold: true, color: 'FFFFFF', size: 18 } : { size: 18 }) })] })) })) }));
    children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
    continue;
  }
  if (l.trim() === '<<PAGEBREAK>>') { children.push(new Paragraph({ children: [new PageBreak()] })); i++; continue; }
  if (/^<<CENTER>>/.test(l)) { children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: runs(l.replace(/^<<CENTER>> ?/, '')) })); i++; continue; }
  { const m = l.match(/^<<IDX([0-3])>> (.*?)\|(.*)$/); if (m) { const lv = +m[1];
    children.push(new Paragraph({ indent: { left: [0, 0, 340, 680][lv] }, spacing: { before: lv === 0 ? 240 : (lv === 1 ? 120 : 0), after: 40 },
      tabStops: [{ type: TabStopType.RIGHT, position: 9000, leader: LeaderType.DOT }],
      children: [new TextRun({ text: m[2], bold: lv <= 1, size: lv === 0 ? 22 : (lv === 1 ? 21 : 20), color: lv === 0 ? ACCENT : undefined }), new TextRun({ text: '\t' + m[3], size: 20 })] })); i++; continue; } }
  if (/^#{1,4} /.test(l)) inRefs = /Referencias/.test(l);
  if (/^#### /.test(l)) children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 180, after: 80 }, children: [new TextRun(l.slice(5))] }));
  else if (/^# /.test(l)) children.push(new Paragraph({ heading: HeadingLevel.TITLE, alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [new TextRun(l.slice(2))] }));
  else if (/^## /.test(l)) children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 320, after: 140 }, children: [new TextRun(l.slice(3))] }));
  else if (/^### /.test(l)) children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 220, after: 100 }, children: [new TextRun(l.slice(4))] }));
  else if (/^> /.test(l)) children.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, indent: { left: 567, right: 567 }, spacing: { after: 140 },
      border: { left: { style: BorderStyle.SINGLE, size: 12, color: ACCENT, space: 10 } }, children: runs(l.slice(2), { italics: true }) }));
  else if (/^\s*- \[ \] /.test(l)) children.push(new Paragraph({ numbering: { reference: 'box', level: 0 }, spacing: { after: 60 }, children: runs(l.replace(/^\s*- \[ \] /, '')) }));
  else if (/^\s*- /.test(l)) { const lvl = l.match(/^\s*/)[0].length >= 2 ? 1 : 0; children.push(new Paragraph({ numbering: { reference: 'bul', level: lvl }, alignment: AlignmentType.JUSTIFIED, spacing: { after: 60, line: 276 }, children: runs(l.replace(/^\s*- /, '')) })); }
  else if (/^\s*\d+\. /.test(l)) { const lvl = l.match(/^\s*/)[0].length >= 2 ? 1 : 0; children.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, indent: { left: 567 + lvl * 567, hanging: 340 }, spacing: { after: 60, line: 276 }, children: runs(l.trim()) })); }
  else if (l.trim() && inRefs) children.push(new Paragraph({ indent: { left: 720, hanging: 720 }, spacing: { after: 120, line: 276 }, children: runs(l) }));
  else if (l.trim()) children.push(para(l));
  i++;
}
const A4 = { width: 11906, height: 16838 };
const footer = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'Mgtr. Fernando Tufiño Valladares · Pág. ', size: 16, color: '808080' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '808080' })] })] });
const sections = [];
if (cover) sections.push({ properties: { page: { size: A4, margin: { top: 0, bottom: 0, left: 0, right: 0, header: 0, footer: 0 } } },
  children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: [new ImageRun({ type: 'png', data: fs.readFileSync(cover), transformation: { width: 794, height: 1122 } })] })] });
sections.push({ properties: { page: { size: A4, margin: { top: 1418, bottom: 1418, left: 1418, right: 1418 } } }, footers: { default: footer }, children });
const doc = new Document({
  title, footnotes: fnDefs,
  styles: { default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: FONT, size: 36, bold: true, color: ACCENT } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 28, bold: true, color: ACCENT }, paragraph: { outlineLevel: 0, keepNext: true } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 24, bold: true, color: '2E5597' }, paragraph: { outlineLevel: 1, keepNext: true } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 22, bold: true, italics: true, color: '2E5597' }, paragraph: { outlineLevel: 2, keepNext: true } } ] },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 283 } } } },
                                 { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1134, hanging: 283 } } } }] },
    { reference: 'box', levels: [{ level: 0, format: LevelFormat.BULLET, text: '☐', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 340 } } } }] } ] },
  sections });
Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log('ok', fnN); });
