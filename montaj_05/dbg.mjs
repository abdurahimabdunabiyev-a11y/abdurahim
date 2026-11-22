import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
const b = await chromium.launch({args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
p.on('console', m => console.log('CON', m.type(), m.text())); p.on('pageerror', e => console.log('ERR', e.message));
p.on('requestfailed', r => console.log('FAIL', r.url()));
await p.goto(process.argv[2]); await p.waitForTimeout(3000);
console.log(await p.evaluate(() => typeof window.renderFrame));
await b.close();
