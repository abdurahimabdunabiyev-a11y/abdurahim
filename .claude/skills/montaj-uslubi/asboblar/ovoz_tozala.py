#!/usr/bin/env python3
"""Xom ovozni tozalash: shovqin/shamol/aks-sado (DeepFilterNet3) + yengil EQ va kompressor.
Ishlatish: ~/montaj-venv/bin/python ovoz_tozala.py kirish.(mp4|wav) chiqish.wav [--kuch 0..1]
--kuch: 1.0 = to'liq tozalash, 0.6 = tabiiyroq (asl ovozdan 40% aralashtiriladi)."""
import sys, subprocess, tempfile, os, argparse
import numpy as np, soundfile as sf, torch
from df.enhance import enhance, init_df
ap = argparse.ArgumentParser(); ap.add_argument('inp'); ap.add_argument('out'); ap.add_argument('--kuch', type=float, default=0.85)
a = ap.parse_args()
tmp = tempfile.mktemp(suffix='.wav')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.inp, '-vn', '-ac', '1', '-ar', '48000', tmp], check=True)
x, sr = sf.read(tmp, dtype='float32'); os.remove(tmp)
model, st, _ = init_df()
y = enhance(model, st, torch.from_numpy(x)[None]).squeeze(0).numpy()
y = a.kuch * y + (1 - a.kuch) * x[:len(y)]
t2 = tempfile.mktemp(suffix='.wav'); sf.write(t2, y, sr)
# nutq uchun: past g'uvillash kesiladi, tiniqlik, yumshoq kompressor
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', t2, '-af',
  'highpass=f=75,equalizer=f=220:t=q:w=1:g=-1.5,equalizer=f=3200:t=q:w=1.2:g=2,deesser=i=0.3,acompressor=threshold=0.1:ratio=2.5:attack=10:release=150:makeup=1.5',
  a.out], check=True); os.remove(t2)
print('OK', a.out, f'{len(y)/sr:.1f}s')
