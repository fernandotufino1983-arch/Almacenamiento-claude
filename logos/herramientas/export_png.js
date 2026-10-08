// Exporta cada SVG de logos/final a PNG con fondo transparente y arma una hoja de vista previa.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const dir = process.argv[2];
const sheetOut = process.argv[3];
const widths = { horizontal: 2400, vertical: 1500, isotipo: 1000, avatar: 1024, favicon: 512 };

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const svgs = fs.readdirSync(dir).filter(f => f.endsWith('.svg')).sort();
  for (const f of svgs) {
    const src = fs.readFileSync(path.join(dir, f), 'utf8');
    const [, , w, h] = src.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
    const W = widths[f.split('-')[2].replace('.svg', '')];
    const H = Math.round(W * h / w);
    await page.setViewportSize({ width: W, height: H });
    await page.setContent(`<html><body style="margin:0;background:transparent">
      <img src="data:image/svg+xml;base64,${Buffer.from(src).toString('base64')}" width="${W}" height="${H}" style="display:block"></body></html>`);
    await page.screenshot({ path: path.join(dir, f.replace('.svg', '.png')), omitBackground: true });
  }
  // Hoja de vista previa: cada variante sobre un fondo donde se lee bien
  const bg = f => /negativo|blanco/.test(f) ? '#0B1F3A' : '#F7F4EE';
  const cells = svgs.map(f => `<figure style="margin:0;background:${bg(f)};padding:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:8px">
      <img src="data:image/svg+xml;base64,${fs.readFileSync(path.join(dir, f)).toString('base64')}" style="max-width:100%;height:${/horizontal/.test(f) ? 110 : 150}px">
      <figcaption style="font:12px Arial;color:${/negativo|blanco/.test(f) ? '#F7F4EE' : '#0B1F3A'};margin-top:10px">${f.replace('jurix-global-', '').replace('.svg', '')}</figcaption></figure>`).join('');
  await page.setViewportSize({ width: 1200, height: 800 });
  await page.setContent(`<html><body style="margin:0;padding:20px;background:#ddd;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">${cells}</body></html>`);
  await page.screenshot({ path: sheetOut, fullPage: true });
  await browser.close();
})();
