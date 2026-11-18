#!/usr/bin/env python3
"""Asosiy video: hook B-roll + A-roll (yuzga bog'langan silliq zoom) + B-roll qo'yilmalar (yumshoq o'tishlar) + LUT.
Ishlatish: ~/montaj-venv/bin/python base.py [--dan 0 --gacha TOTAL] -> base.mp4"""
import os, sys, json, subprocess, argparse
import numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan import *
os.chdir(D)
ap = argparse.ArgumentParser(); ap.add_argument('--dan', type=float, default=0); ap.add_argument('--gacha', type=float, default=TOTAL)
ap.add_argument('--out', default='base.mp4'); a = ap.parse_args()
LUT = '/home/user/abdurahim/.claude/skills/montaj-uslubi/lut/iliq_premium.cube'
OW, OH = 1080, 1920

def ease_io(x): x = min(1, max(0, x)); return 4 * x**3 if x < .5 else 1 - (-2 * x + 2)**3 / 2
def ease_out(x): x = min(1, max(0, x)); return 1 - (1 - x)**3

# --- B-roll bo'laklarini 30 fps ga oldindan kesish (indeks = kadr) ---
os.makedirs('cache', exist_ok=True)
class Clip:
    def __init__(s, path, start, dur):
        s.p = f"cache/{os.path.basename(path)[:-4]}_{start:.2f}_{dur:.2f}.mp4"
        if not os.path.exists(s.p):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(start), '-i', path, '-t', str(dur + 0.6), '-vf', 'fps=30,scale=1080:1920,setsar=1',
                            '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', s.p], check=True)
        s.cap = cv2.VideoCapture(s.p); s.i = -1; s.f = None
    def frame(s, k):
        k = max(0, k)
        if k < s.i: s.cap.set(cv2.CAP_PROP_POS_FRAMES, k); s.i = k - 1
        while s.i < k:
            ok, f = s.cap.read()
            if not ok: break
            s.f = f; s.i += 1
        return s.f

HC = [(s, e, Clip(p, ss, e - s)) for s, e, p, ss in HOOK]
BC = [(s, e, Clip(p, ss, e - s)) for s, e, p, ss in BROLL]
AR = Clip('aroll_hi.mp4', 0, 0); AR.cap = cv2.VideoCapture('aroll_hi.mp4')  # to'g'ridan-to'g'ri
YZ = json.load(open('kes/yuz.json')); YT = np.array([p[0] for p in YZ['pts']]); YX = np.array([p[1] for p in YZ['pts']]); YY = np.array([p[2] for p in YZ['pts']])

def zoom_at(t):
    for (n, o, d) in PARTS:
        if o - 1e-6 <= t < o + d or n == PARTS[-1][0]:
            K = ZOOM[n]; break
    if t <= K[0][0]: return K[0][1]
    for (t0, z0), (t1, z1) in zip(K, K[1:]):
        if t0 <= t <= t1: return z0 + (z1 - z0) * ease_io((t - t0) / max(1e-6, t1 - t0))
    return K[-1][1]

def scaled(img, z, ax=0.5, ay=0.5):
    """img ni z marta kattalashtirib (ax,ay nuqta atrofida) OWxOH ga keltirish."""
    h, w = img.shape[:2]; cw, ch = w / z, h / z
    x0 = np.clip(ax * w - cw / 2, 0, w - cw); y0 = np.clip(ay * h - ch / 2, 0, h - ch)
    M = np.array([[OW / cw, 0, -x0 * OW / cw], [0, OH / ch, -y0 * OH / ch]], dtype=np.float32)
    return cv2.warpAffine(img, M, (OW, OH), flags=cv2.INTER_LINEAR)

def aroll(t, extra=1.0):
    f = AR.frame(int(round(t * FPS)))
    z = zoom_at(t) * extra
    fx = np.interp(t, YT, YX); fy = np.interp(t, YT, YY)
    h, w = f.shape[:2]; ch = h / z
    # yuz kadrda (0.5, 0.31) da tursin
    ay = (fy * h - 0.31 * ch + ch / 2) / h
    return scaled(f, z, fx, ay)

def broll(clip, s, t, e):
    f = clip.frame(int(round((t - s) * FPS)))
    z = 1.0 + 0.12 * (1 - ease_out((t - s) / 0.6)) + 0.05 * (t - s) / max(0.5, e - s)  # kirishda 1.12->1, keyin sekin push
    return scaled(f, z)

XIN, XOUT = 0.18, 0.16
def talk_frame(t, skip=None):
    for k, (s, e, c) in enumerate(BC):
        if k != skip and s <= t < e:
            fr = broll(c, s, t, e)
            if t - s < XIN:  # kirish: oldingi manbadan aralashtirish
                prev = talk_frame(t, skip=k) if skip is None else aroll(t)
                al = ease_io((t - s) / XIN); fr = cv2.addWeighted(prev, 1 - al, fr, al, 0)
            return fr
    fr = aroll(t)
    for s, e, c in BC:  # B-roll tugagandan keyin A-roll ga yumshoq qaytish
        if e <= t < e + XOUT and not any(abs(s2 - e) < 1e-3 for s2, _, _ in BC):
            al = ease_io((t - e) / XOUT)
            fr = cv2.addWeighted(broll(c, s, t, e), 1 - al, aroll(t, 1 + 0.06 * (1 - al)), al, 0)
    return fr

def hook_frame(T):
    for k, (s, e, c) in enumerate(HC):
        if s <= T < e:
            f = c.frame(int(round((T - s) * FPS)))
            z = 1.0 + 0.1 * (1 - ease_out((T - s) / 0.5)) + 0.06 * (T - s) / (e - s)
            fr = scaled(f, z)
            if k and T - s < 0.12:
                p = HC[k - 1]; pf = p[2].frame(int(round((T - p[0]) * FPS)))
                fr = cv2.addWeighted(scaled(pf, 1.06 + 0.04 * (T - s) / 0.12), 1 - (T - s) / 0.12, fr, (T - s) / 0.12, 0)
            return fr
    return scaled(HC[-1][2].frame(int(round((T - HC[-1][0]) * FPS))), 1.06)

ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{OW}x{OH}', '-r', str(FPS), '-i', '-',
                       '-vf', f"split[a][b];[b]lut3d=file={LUT}[l];[a][l]blend=all_mode=normal:all_opacity=0.55,eq=contrast=1.04:saturation=1.05,vignette=angle=0.42",
                       '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', a.out], stdin=subprocess.PIPE)
N0, N1 = int(round(a.dan * FPS)), int(round(a.gacha * FPS))
for n in range(N0, N1):
    T = n / FPS
    if T < H:
        fr = hook_frame(T)
    else:
        t = T - H
        fr = talk_frame(t)
        if t < 0.3:  # hook -> nutq: yumshoq aralashuv + zoom-out
            al = ease_io(t / 0.3)
            fr = cv2.addWeighted(scaled(HC[-1][2].frame(int(round((T - HC[-1][0]) * FPS))), 1.08), 1 - al, aroll(t, 1 + 0.12 * (1 - ease_out(t / 0.6))), al, 0)
        elif t < 0.6:
            fr = aroll(t, 1 + 0.12 * (1 - ease_out(t / 0.6))) if not any(s <= t < e for s, e, _ in BC) else fr
    ff.stdin.write(np.ascontiguousarray(fr).tobytes())
ff.stdin.close(); ff.wait(); print('OK', a.out, N1 - N0, 'kadr')
