import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import path from 'node:path';
const [, , scene, ...ts] = process.argv;
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
p.on('pageerror', e => console.log('ERR', e.message));
await p.goto('file://' + path.resolve(scene));
await p.waitForFunction(() => !!(window.tl && window.renderFrame), null, {polling: 100});
await p.evaluate(() => document.fonts.ready);
for (const t of ts) { await p.evaluate(i => window.renderFrame(i), Math.round(+t * 30)); await p.screenshot({ path: `/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/ov_${t}.png`, omitBackground: true }); }
await b.close();
