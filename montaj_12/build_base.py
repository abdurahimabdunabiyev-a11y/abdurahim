#!/usr/bin/env python3
"""1) Kesilgan bo'laklarni bitta proxy + ovozga yig'adi. 2) Kadr rejasi bo'yicha fon kadrlarini (JPG) chiqaradi:
 - yaqin/keng plan: yuzga QAT'IY bog'langan statik kesim (yuz har doim bir joyda), juda sekin push-in yuz atrofida;
 - B-roll: sekin Ken Burns; karta foni: xira + qoraytirilgan B-roll;
 - o'tish (A-roll<->B-roll/karta): 7 kadrli "zoom-through" (chiquvchi 1→1.10 + blur, kiruvchi 1.10→1 + blur)."""
import os, sys, subprocess, json, numpy as np, cv2
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D); sys.path.insert(0, D)
from plan import *
OW, OH = 1080, 1920
def run(c): subprocess.run(c, check=True)
if not os.path.exists('proxy_full.mp4'):
    os.makedirs('seg', exist_ok=True); L = []
    for k, (s, a, b) in enumerate(SEG):
        n = round((b - a) * FPS); o = f'seg/s{k:02d}.mp4'
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a), '-i', X + s + '.mov', '-t', str(n / FPS + .3), '-vf', f'fps={FPS},scale=1620:2880:flags=lanczos,setsar=1',
             '-frames:v', str(n), '-af', f'aresample=48000,atrim=0:{n / FPS},afade=t=in:d=0.015,afade=t=out:st={n / FPS - 0.02}:d=0.02', '-ac', '1',
             '-c:v', 'libx264', '-crf', '15', '-preset', 'fast', '-c:a', 'pcm_s16le', '-threads', '2', o.replace('.mp4', '.mov')])
        L.append(o.replace('.mp4', '.mov'))
    open('seg/list.txt', 'w').write(''.join(f"file '{os.path.basename(x)}'\n" for x in L))
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'seg/list.txt', '-map', '0:v', '-c:v', 'copy', 'proxy_full.mp4', '-map', '0:a', '-ar', '48000', 'ovoz_full_raw.wav'])
    run([os.path.expanduser('~/montaj-venv/bin/python'), '../.claude/skills/montaj-uslubi/asboblar/ovoz_tozala.py', 'ovoz_full_raw.wav', 'ovoz_full.wav', '--kuch', '0.6'])
# --- kadr rejasi
P = phrases()
SH = []
for k, p in enumerate(P):
    t0 = 0.0 if k == 0 else p['t0']
    SH.append([t0, p['kind'], p['prm'], p['src']])
ENDS = [s[0] for s in SH[1:]] + [TOTAL]
# yaqin/keng navbatini "close"/"wide" belgilaridan oladi; manba yuz nuqtasi
def ease(x): x = min(1, max(0, x)); return 4 * x**3 if x < .5 else 1 - (-2 * x + 2)**3 / 2
def src_at(t):
    acc = 0.0
    for s, a, b in SEG:
        d = round((b - a) * FPS) / FPS
        if t < acc + d: return s
        acc += d
    return SEG[-1][0]
def warp(f, z, ax, ay, fx_out, fy_out):
    """f ichidagi (ax,ay) nuqta chiqishda (fx_out,fy_out) ga tushadigan, z masshtabli kesim."""
    h, w = f.shape[:2]; base = OW / w                      # z=1 da kenglik to'liq
    s = base * z
    tx = fx_out * OW - ax * w * s; ty = fy_out * OH - ay * h * s
    # chetga chiqib ketmasin
    tx = min(0, max(OW - w * s, tx)); ty = min(0, max(OH - h * s, ty))
    M = np.array([[s, 0, tx], [0, s, ty]], np.float32)
    return cv2.warpAffine(f, M, (OW, OH), flags=cv2.INTER_AREA)
BR = 'broll/mixkit_%s_9x16.mp4'
caps = {}
def broll_frame(i, t):
    t0 = SH[i][0]; bid, st = (SH[i][2] if SH[i][1] == 'broll' else CARD_BG[SH[i][2]]).split(':')
    key = (i, bid)
    if key not in caps:
        c = cv2.VideoCapture(BR % bid); c.set(cv2.CAP_PROP_POS_MSEC, float(st) * 1000); caps[key] = [c, None]
    c = caps[key]; ok, f = c[0].read()
    if ok: c[1] = f
    return c[1]
CARD_BG = {'narx': '32529:7.0', 'uy400': '28071:2.0', 'brand': '5020:8.0'}
def frame_for(t, f_a):
    i = max(k for k, s in enumerate(SH) if s[0] <= t + 1e-6); t0, kind, prm, src = SH[i]; t1 = ENDS[i]; u = (t - t0) / max(.4, t1 - t0)
    if kind in ('close', 'wide'):
        s = src_at(t); fx, fy = FACE[s]
        if kind == 'close': return warp(f_a, 1.55 * (1 + .025 * u), fx, fy, .5, .37)
        return warp(f_a, 1.0 * (1 + .02 * u), fx, fy, .5, .30), i
    b = broll_frame(i, t); fr = warp(b, 1.0 + .05 * u, .5, .5, .5, .5)
    if kind == 'card':
        fr = cv2.GaussianBlur(fr, (0, 0), 18); fr = cv2.addWeighted(fr, .5, np.zeros_like(fr), .5, 0)
    return fr
TR = 7
cap = cv2.VideoCapture('proxy_full.mp4'); os.makedirs('kadr_full', exist_ok=True)
N = int(round(TOTAL * FPS)); hist = []
def zoomblur(fr, z, bl):
    M = cv2.getRotationMatrix2D((OW / 2, OH / 2), 0, z); o = cv2.warpAffine(fr, M, (OW, OH), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return cv2.GaussianBlur(o, (0, 0), bl) if bl > .3 else o
prev_fr = None
for n in range(N):
    ok, fa = cap.read()
    if not ok: fa = last
    last = fa; t = n / FPS
    r = frame_for(t, fa); fr = r[0] if isinstance(r, tuple) else r
    i = max(k for k, s in enumerate(SH) if s[0] <= t + 1e-6)
    # o'tish: B-roll/karta bilan chegarada zoom-through
    k = (t - SH[i][0]) * FPS
    if i > 0 and k < TR and ({SH[i][1], SH[i - 1][1]} & {'broll', 'card'}):
        a = ease(k / TR); inc = zoomblur(fr, 1.10 - .10 * a, 10 * (1 - a)); outg = zoomblur(prev_fr, 1.0 + .10 * a, 10 * a) if prev_fr is not None else inc
        fr = cv2.addWeighted(outg, 1 - a, inc, a, 0)
    else:
        prev_fr = fr
    if k >= TR or i == 0 or not ({SH[i][1], SH[i - 1][1]} & {'broll', 'card'}): prev_fr = fr
    cv2.imwrite(f'kadr_full/b_{n + 1:04d}.jpg', fr, [cv2.IMWRITE_JPEG_QUALITY, 92])
json.dump(dict(total=TOTAL, n=N, phrases=P, shots=SH), open('plan.json', 'w'), ensure_ascii=False)
print('OK', N)
