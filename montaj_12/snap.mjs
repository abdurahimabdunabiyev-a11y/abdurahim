import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright'); import path from 'node:path';
const [, , scene, out, ...ts] = process.argv;
const b = await chromium.launch({args:['--disable-dev-shm-usage','--allow-file-access-from-files']}); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
p.on('pageerror', e => console.log('ERR', e.message));
await p.goto('file://' + path.resolve(scene)); await p.waitForFunction(() => !!window.renderFrame, null, {polling: 100}); await p.evaluate(() => document.fonts.ready);
for (const t of ts) { await p.evaluate(i => window.renderFrame(i), Math.round(+t * 30)); await p.screenshot({ path: `${out}_${t}.jpg`, type: 'jpeg', quality: 80 }); }
await b.close();
