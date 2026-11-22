import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
const b = await chromium.launch({args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(process.argv[2]); await p.waitForFunction(() => !!window.renderFrame);
for (const f of [20, 40, 140]) { await p.evaluate(i => window.renderFrame(i), f); await p.screenshot({path: process.argv[3] + f + '.jpg'}); }
console.log(await p.evaluate(() => document.documentElement.outerHTML.includes('envMapIntensity: .12')));
await b.close();
