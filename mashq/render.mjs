// HTML+GSAP sahnani deterministik videoga aylantirish (HyperFrames tamoyili: pauzadagi timeline'ni kadrma-kadr seek qilish).
// Ishlatish: node render.mjs scenes/s1_whip.html out/s1_whip.mp4 3.0
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { spawn } from 'node:child_process';
import path from 'node:path';

const [, , scene, out, durS, fpsS] = process.argv;
const FPS = Number(fpsS || 30), DUR = Number(durS);
const N = Math.round(DUR * FPS);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto('file://' + path.resolve(scene));
await page.waitForFunction(() => window.tl && window.renderFrame);
await page.evaluate(() => document.fonts.ready);
const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
  '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
for (let i = 0; i < N; i++) {
  await page.evaluate(i => window.renderFrame(i), i);
  const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
console.log('OK', out, N, 'frames');
