const {chromium}=require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for (const [f,t] of [['g3_tanishuv.html',2.0],['g4_hisob.html',3.4],['g8_cta.html',4.5]]) {
 await p.goto('file://'+path.resolve(f)); await p.waitForFunction(()=>!!window.tl,null,{polling:100}); await p.evaluate(()=>document.fonts.ready);
 await p.evaluate(t=>window.renderFrame(Math.round(t*30)),t); await p.screenshot({path:'snap_'+f.replace('.html','.png')}); }
await b.close();})();
