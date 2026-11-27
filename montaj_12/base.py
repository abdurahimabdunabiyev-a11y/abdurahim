#!/usr/bin/env python3
"""Uy-joy reels sinovi: yaqin/keng plan (sekin push-in), B-roll qo'yilmalar (yumshoq zoom-dissolve), karta foni uchun xira B-roll."""
import json, os, numpy as np, cv2, subprocess
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
T1, FPS, OW, OH = 23.95, 30, 1080, 1920
def ease(x): x = min(1, max(0, x)); return 4 * x**3 if x < .5 else 1 - (-2 * x + 2)**3 / 2
BR = 'broll/mixkit_%s_9x16.mp4'
# (boshi, turi, param, B-roll manba boshi)
SH = [(0.00, 'close', 1.62, 0), (1.06, 'broll', 32529, 1.0), (2.95, 'wide', 1.04, 0), (5.44, 'close', 1.5, 0), (7.60, 'wide', 1.12, 0),
      (9.45, 'close', 1.52, 0), (10.80, 'broll', 5020, 2.0), (12.90, 'broll', 28071, 1.0), (15.60, 'close', 1.6, 0), (16.25, 'wide', 1.06, 0),
      (17.50, 'card', 32529, 6.0), (20.80, 'close', 1.55, 0)]
ENDS = [s[0] for s in SH[1:]] + [T1]
YZ = json.load(open('yuz.json')); YT = np.array([p[0] for p in YZ['pts']]); YX = np.array([p[1] for p in YZ['pts']]); YY = np.array([p[2] for p in YZ['pts']])
FX, FY = np.median(YX), np.median(YY)
class Clip:
    def __init__(s, p, st):
        s.cap = cv2.VideoCapture(p); s.cap.set(cv2.CAP_PROP_POS_MSEC, st * 1000); s.last = None
    def next(s):
        ok, f = s.cap.read()
        if ok: s.last = f
        return s.last
clips = {i: Clip(BR % sh[2], sh[3]) for i, sh in enumerate(SH) if sh[1] in ('broll', 'card')}
def crop(f, z, ax, ay, py):
    h, w = f.shape[:2]; cw, ch = w / z, h / z
    x0 = np.clip(ax * w - cw / 2, 0, w - cw); y0 = np.clip(ay * h - py * ch, 0, h - ch)
    M = np.array([[OW / cw, 0, -x0 * OW / cw], [0, OH / ch, -y0 * OH / ch]], np.float32)
    return cv2.warpAffine(f, M, (OW, OH), flags=cv2.INTER_AREA)
def aroll(f, t, kind, z, t0, t1):
    push = 1 + .035 * (t - t0) / max(.5, t1 - t0)   # sekin push-in (kamera "tirik")
    fx = float(np.clip(np.interp(t, YT, YX), FX - .06, FX + .06)); fy = float(np.clip(np.interp(t, YT, YY), FY - .05, FY + .05))
    if kind == 'close': return crop(f, z * push, fx, fy, .36)
    return crop(f, z * push, .5, fy, .30)
cap = cv2.VideoCapture('proxy.mp4'); prev = None
for n in range(int(round(T1 * FPS))):
    ok, f = cap.read()
    if not ok: f = last
    last = f; t = n / FPS
    i = max(k for k, s in enumerate(SH) if s[0] <= t + 1e-6); t0, kind, p, _ = SH[i]; t1 = ENDS[i]
    if kind in ('close', 'wide'): fr = aroll(f, t, kind, p, t0, t1)
    else:
        b = clips[i].next(); u = (t - t0) / max(.5, t1 - t0)
        fr = crop(b, 1.0 + .06 * u, .5, .5, .5)
        if kind == 'card':
            fr = cv2.GaussianBlur(fr, (0, 0), 22); fr = (fr.astype(np.float32) * .55).astype(np.uint8)
    # B-roll / karta kirish-chiqishida yumshoq (8 kadr) zoom-dissolve
    if prev is not None and abs(t - t0) < 1e-6 is False: pass
    k = (t - t0) * FPS
    if 0 < k < 8 and (kind in ('broll', 'card') or SH[i - 1][1] in ('broll', 'card')):
        a = ease(k / 8); fr = cv2.addWeighted(cv2.resize(prev[40:-40, 22:-22], (OW, OH)), 1 - a, fr, a, 0)
    prev = fr
    cv2.imwrite(f'kadr/b_{n + 1:04d}.jpg', fr, [cv2.IMWRITE_JPEG_QUALITY, 93])
print('OK', n + 1)
