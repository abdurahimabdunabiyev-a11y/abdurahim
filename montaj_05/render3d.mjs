import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { spawn } from 'node:child_process';
const [, , url, out, durS] = process.argv; const N = Math.round(+durS * 30);
const b = await chromium.launch({args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
p.on('pageerror', e => console.log('ERR', e.message)); p.on('console', m => { if (m.type() === 'error') console.log('CON', m.text()); });
await p.goto(url); await p.waitForFunction(() => !!window.renderFrame, null, {polling: 100}); await p.evaluate(() => document.fonts.ready);
const ff = spawn('ffmpeg', ['-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',out], {stdio:['pipe','inherit','inherit']});
for (let i = 0; i < N; i++) { await p.evaluate(i => window.renderFrame(i), i); const buf = await p.screenshot({type:'jpeg', quality: 93});
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('OK', out, N);
