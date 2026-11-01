// Genera PNG y PDF de las portadas a partir de los HTML de libro/portada
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = path.join(__dirname, '..', '..', 'libro', 'portada');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 576, height: 864 }, deviceScaleFactor: 3.125 });
  for (const n of ['a', 'b', 'c']) { if (!fs.existsSync(`${dir}/portada-${n}.html`)) continue;
    await p.goto(`file://${dir}/portada-${n}.html`); await p.waitForTimeout(300);
    await p.screenshot({ path: `${dir}/portada-${n}.png` });
    await p.pdf({ path: `${dir}/portada-${n}.pdf`, width: '6in', height: '9in', printBackground: true }); }
  const q = await b.newPage({ viewport: { width: 1240, height: 900 }, deviceScaleFactor: 1.5 }); const tmp = dir + '/_cmp.html';
  fs.writeFileSync(tmp, `<html><body style="margin:0;background:#e9e6df;display:flex;gap:40px;justify-content:center;align-items:center;height:900px;font-family:Inter">
   ${['a','c'].map((n,i)=>`<figure style="margin:0;text-align:center"><img src="portada-${n}.png" style="height:780px;box-shadow:0 10px 30px rgba(0,0,0,.35)"><figcaption style="margin-top:14px;font-size:18px;font-weight:600">${['A · Azul noche','C · Negro'][i]}</figcaption></figure>`).join('')}</body></html>`);
  await q.goto('file://' + tmp); await q.waitForTimeout(300); await q.screenshot({ path: `${dir}/comparacion-azul-negro.png` }); fs.unlinkSync(tmp);
  await b.close(); })();
