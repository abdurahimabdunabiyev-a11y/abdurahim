#!/usr/bin/env python3
"""Akmal referensi uslubi: ikki "kamera" (keng / yaqin) orasida keskin kesimlar, asl rang. Kadrlar JPG ketma-ketligi (HTML fon uchun)."""
import json, os, numpy as np, cv2
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
M4 = '../montaj_04/'
T1, FPS, OW, OH = 9.1333, 30, 1080, 1920
W = json.load(open(M4 + 'sozlar.json'))['words']
def w(i): return W[i][1]
# (boshlanish, zoom, yuz y-ulushi): keng — yuz tepada, yaqin — yuz ~0.36
SHOTS = [(0.0, 1.05, .30), (w(1), 1.42, .36), (w(10) - .44, 1.05, .30), (w(12), 1.42, .36), (w(16), 1.12, .31), (w(18), 1.55, .37)]
def shot(t):
    s = SHOTS[0]
    for x in SHOTS:
        if t >= x[0]: s = x
    return s
YZ = json.load(open(M4 + 'kes/yuz.json')); YT = np.array([p[0] for p in YZ['pts']]); YX = np.array([p[1] for p in YZ['pts']]); YY = np.array([p[2] for p in YZ['pts']])
os.makedirs('kadr', exist_ok=True)
cap = cv2.VideoCapture(M4 + 'aroll_hi.mp4')
for n in range(int(round(T1 * FPS))):
    ok, f = cap.read()
    if not ok: break
    t = n / FPS; _, z, fyr = shot(t); h, wd = f.shape[:2]; cw, ch = wd / z, h / z
    fx = np.interp(t, YT, YX) * wd; fy = np.interp(t, YT, YY) * h
    x0 = np.clip(fx - cw / 2, 0, wd - cw); y0 = np.clip(fy - fyr * ch, 0, h - ch)
    Mx = np.array([[OW / cw, 0, -x0 * OW / cw], [0, OH / ch, -y0 * OH / ch]], np.float32)
    cv2.imwrite(f'kadr/b_{n + 1:04d}.jpg', cv2.warpAffine(f, Mx, (OW, OH), flags=cv2.INTER_AREA), [cv2.IMWRITE_JPEG_QUALITY, 94])
print('OK', n + 1)
