const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:576,height:864},deviceScaleFactor:3.125});
for(const n of ['a','b']){await p.goto('file:///home/user/Almacenamiento-claude/libro/portada/portada-'+n+'.html');await p.waitForTimeout(300);
await p.screenshot({path:'/home/user/Almacenamiento-claude/libro/portada/portada-'+n+'.png'});
await p.pdf({path:'/home/user/Almacenamiento-claude/libro/portada/portada-'+n+'.pdf',width:'6in',height:'9in',printBackground:true});}
await b.close();})();
