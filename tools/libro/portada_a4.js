// Genera portada-a-a4.png (A4, a sangre) a partir de portada-a.png
const { chromium } = require('playwright'); const path = require('path');
const dir = path.join(__dirname, '..', '..', 'libro', 'portada');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2.5 });
  const fs = require('fs'); const tmp = dir + '/_a4.html';
  for (const n of ['portada-a', 'contraportada-a']) {
  fs.writeFileSync(tmp, '<html><body style="margin:0;background:#0e1726;height:1123px;display:flex;justify-content:center"><img src="' + n + '.png" style="height:1123px"></body></html>');
  await p.goto('file://' + tmp);
  await p.waitForTimeout(300); await p.screenshot({ path: dir + '/' + n + '-a4.png' }); } await b.close(); fs.unlinkSync(tmp); })();
