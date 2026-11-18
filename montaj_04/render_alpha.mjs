import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { spawn } from 'node:child_process'; import path from 'node:path';
const [, , scene, out, durS] = process.argv; const N = Math.round(+durS * 30);
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
p.on('pageerror', e => console.log('ERR', e.message));
await p.goto('file://' + path.resolve(scene));
await p.waitForFunction(() => !!(window.tl && window.renderFrame), null, {polling: 100});
await p.evaluate(() => document.fonts.ready);
const ff = spawn('ffmpeg', ['-v','error','-y','-f','image2pipe','-framerate','30','-c:v','png','-i','-','-c:v','qtrle','-pix_fmt','argb',out], {stdio:['pipe','inherit','inherit']});
for (let i = 0; i < N; i++) { await p.evaluate(i => window.renderFrame(i), i);
  const buf = await p.screenshot({ type: 'png', omitBackground: true });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('OK', out, N);
