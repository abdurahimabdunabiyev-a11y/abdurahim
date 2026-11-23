#!/usr/bin/env python3
"""Yuz kuzatuvi (haar). Faqat gapiradigan oraliqlarda aniqlaydi, face.js yozadi (FACE=[[t,x,y],...]).

Ishlatish (opencv uchun uvx):
  uvx --quiet --python 3.12 --with "opencv-python-headless==4.10.0.84" --with "numpy<2" \
      python face_track.py cut.mp4 --ranges 0-3.9,23.5-36 --out face.js
--ranges bo'lmasa butun video. b-roll (ekran yozuvi) oraliqlarini kiritmang: u yerda yuz yo'q.
"""
import argparse, json
import cv2, numpy as np
ap = argparse.ArgumentParser(); ap.add_argument("video"); ap.add_argument("--ranges"); ap.add_argument("--out", default="face.js")
ap.add_argument("--step", type=float, default=0.5)
a = ap.parse_args()
R = [tuple(map(float, r.split("-"))) for r in a.ranges.split(",")] if a.ranges else None
cap = cv2.VideoCapture(a.video); fps = cap.get(cv2.CAP_PROP_FPS); dur = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
fc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
fp = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
T = []; t = 0.0
while t < dur - 0.05:
    if R and not any(x <= t <= y for x, y in R): t += a.step; continue
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(t * fps)); ok, im = cap.read()
    if not ok: break
    g = cv2.cvtColor(cv2.resize(im, (540, 960)), cv2.COLOR_BGR2GRAY)
    f = fc.detectMultiScale(g, 1.1, 5, minSize=(60, 60))
    if len(f) == 0: f = fp.detectMultiScale(g, 1.1, 4, minSize=(60, 60))
    if len(f) == 0:
        f = fp.detectMultiScale(cv2.flip(g, 1), 1.1, 4, minSize=(60, 60)); f = [(540 - x - w, y, w, h) for (x, y, w, h) in f]
    if len(f):
        x, y, w, h = max(f, key=lambda r: r[2] * r[3]); T.append((round(t, 2), (x + w / 2) * 2, (y + h / 2) * 2))
    else: T.append((round(t, 2), None, None))
    t += a.step
ok = [r for r in T if r[1] is not None]
print("aniqlandi", len(ok), "/", len(T))
ts = np.array([r[0] for r in ok]); xs = np.array([r[1] for r in ok]); ys = np.array([r[2] for r in ok]); tt = np.array([r[0] for r in T])
x = np.interp(tt, ts, xs); y = np.interp(tt, ts, ys)
sm = lambda v, k=5: np.convolve(np.pad(v, (k // 2, k // 2), mode="edge"), np.ones(k) / k, mode="valid")
x, y = sm(x), sm(y)
open(a.out, "w").write("FACE = " + json.dumps([[round(float(p), 2), round(float(q), 1), round(float(r), 1)] for p, q, r in zip(tt, x, y)]) + ";\n")
print("yozildi", a.out)
