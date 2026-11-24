#!/usr/bin/env python3
"""Sinov (0–13 s): keng/yaqin "kamera" kesimlari + "Premium Solar" yozuviga silliq yaqinlashish. Asl rang. JPG kadrlar (HTML fon)."""
import json, os, numpy as np, cv2
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
T1, FPS, OW, OH = 12.94, 30, 1080, 1920
def ease(x): x = min(1, max(0, x)); return 4 * x**3 if x < .5 else 1 - (-2 * x + 2)**3 / 2
# (boshlanish, turi, parametrlar)
SHOTS = [(0.00, 'face', 1.55), (1.66, 'wide', 1.02), (5.00, 'face', 1.42), (5.94, 'sign', None), (8.00, 'wide', 1.15), (9.86, 'face', 1.48)]
YZ = json.load(open('yuz.json')); YT = np.array([p[0] for p in YZ['pts']]); YX = np.array([p[1] for p in YZ['pts']]); YY = np.array([p[2] for p in YZ['pts']])
def view(t):
    s = SHOTS[0]
    for x in SHOTS:
        if t >= x[0]: s = x
    t0, kind, z = s
    fx, fy = np.interp(t, YT, YX), np.interp(t, YT, YY)
    if kind == 'face': return z, fx, fy, .36
    if kind == 'wide': return z, .5, fy, .30
    # 'sign': 1.02 -> 1.45, bino yozuvi (x .5, y .33) markazga, 1.5 s silliq
    k = ease((t - t0) / 1.5); return 1.02 + .43 * k, .5, .33 + (fy - .33) * 0, .30 + .12 * k
cap = cv2.VideoCapture('proxy.mp4')
for n in range(int(round(T1 * FPS))):
    ok, f = cap.read()
    if not ok: break
    t = n / FPS; z, ax, ay, py = view(t); h, wd = f.shape[:2]; cw, ch = wd / z, h / z
    x0 = np.clip(ax * wd - cw / 2, 0, wd - cw); y0 = np.clip(ay * h - py * ch, 0, h - ch)
    Mx = np.array([[OW / cw, 0, -x0 * OW / cw], [0, OH / ch, -y0 * OH / ch]], np.float32)
    cv2.imwrite(f'kadr/b_{n + 1:04d}.jpg', cv2.warpAffine(f, Mx, (OW, OH), flags=cv2.INTER_AREA), [cv2.IMWRITE_JPEG_QUALITY, 94])
print('OK', n + 1)
