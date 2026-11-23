#!/usr/bin/env python3
"""3-uslub sinovi: A-roll (asl rang), yuzga bog'langan doimiy kadr, zoom zarbasi FAQAT ta'kid so'zlarda (100->111%)."""
import json, subprocess, os, numpy as np, cv2
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
M4 = '../montaj_04/'
S = json.load(open(M4 + 'sozlar.json')); W = S['words']
T0, T1 = 0.0, 9.1333          # 1-sabab: "Birinchisi ... Hammasi bor!"
FPS, OW, OH = 30, 1080, 1920
BASEZ = 1.16
def w(i): return W[i][1]
PUNCH = [w(16), w(18)]        # "500 tami?" va "Hammasi bor!"
def ease(x): x = min(1, max(0, x)); return 4 * x**3 if x < .5 else 1 - (-2 * x + 2)**3 / 2
def zoom(t):
    z = 1.0
    for p in PUNCH:
        if p - .3 <= t < p: z = max(z, 1 + .11 * ease((t - (p - .3)) / .3))
        elif p <= t < p + .9: z = max(z, 1.11)
        elif p + .9 <= t < p + 1.25: z = max(z, 1 + .11 * (1 - ease((t - p - .9) / .35)))
    return BASEZ * z
YZ = json.load(open(M4 + 'kes/yuz.json')); YT = np.array([p[0] for p in YZ['pts']]); YX = np.array([p[1] for p in YZ['pts']]); YY = np.array([p[2] for p in YZ['pts']])
cap = cv2.VideoCapture(M4 + 'aroll_hi.mp4')
ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{OW}x{OH}', '-r', str(FPS), '-i', '-',
                       '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', 'base.mp4'], stdin=subprocess.PIPE)
for n in range(int(round((T1 - T0) * FPS))):
    ok, f = cap.read()
    if not ok: break
    t = T0 + n / FPS; z = zoom(t); h, wd = f.shape[:2]; cw, ch = wd / z, h / z
    fx = np.interp(t, YT, YX) * wd; fy = np.interp(t, YT, YY) * h
    x0 = np.clip(fx - cw / 2, 0, wd - cw); y0 = np.clip(fy - .40 * ch, 0, h - ch)   # ko'zlar ~ y 810 (0.42)
    Mx = np.array([[OW / cw, 0, -x0 * OW / cw], [0, OH / ch, -y0 * OH / ch]], np.float32)
    ff.stdin.write(cv2.warpAffine(f, Mx, (OW, OH), flags=cv2.INTER_AREA).tobytes())
ff.stdin.close(); ff.wait(); print('OK base.mp4')
