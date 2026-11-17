#!/usr/bin/env python3
"""Kino rang LUTlari (.cube, 33^3). ffmpeg: -vf lut3d=file=lut/NOM.cube
Nomlar: kino_teal · tungi_kok (FERS uslubi, qorong'i ko'k-yashil) · iliq_premium · toza_tabiiy · brend_yashil (Premium Solar)"""
import numpy as np, os
D = os.path.join(os.path.dirname(__file__), '..', 'lut'); N = 33
g = np.linspace(0, 1, N); B, G, R = np.meshgrid(g, g, g, indexing='ij')  # .cube tartibi: R eng tez
rgb = np.stack([R, G, B], -1)
lum = lambda c: (c * [0.2126, 0.7152, 0.0722]).sum(-1, keepdims=True)
def sat(c, s): l = lum(c); return l + (c - l) * s
def curve(c, contrast=1.0, pivot=0.45): return np.clip((c - pivot) * contrast + pivot, 0, 1)
def split(c, sh, hi, amt=0.12):  # soyalarga sh rang, yorug'likka hi rang
    l = lum(c); w = np.clip(1 - l * 1.6, 0, 1); v = np.clip((l - 0.45) * 1.8, 0, 1)
    return np.clip(c + amt * (w * (np.array(sh) - 0.5) + v * (np.array(hi) - 0.5)), 0, 1)
def soft_s(c, k=1.0): return np.clip(c + k * 0.08 * np.sin((c - 0.5) * np.pi * 2) * -1 * -1, 0, 1)
L = {
  'kino_teal': lambda c: sat(split(curve(c, 1.12), [0.2, 0.55, 0.62], [0.78, 0.55, 0.38], 0.16), 1.05),
  'tungi_kok': lambda c: sat(split(curve(c * 0.82, 1.18, 0.4), [0.22, 0.5, 0.55], [0.6, 0.62, 0.55], 0.18), 0.78),
  'iliq_premium': lambda c: sat(split(curve(c, 1.06), [0.48, 0.45, 0.42], [0.72, 0.58, 0.42], 0.12), 1.04),
  'toza_tabiiy': lambda c: sat(curve(c, 1.08, 0.5), 1.08),
  'brend_yashil': lambda c: sat(split(curve(c, 1.1), [0.25, 0.52, 0.42], [0.72, 0.62, 0.40], 0.15), 0.98),
}
os.makedirs(D, exist_ok=True)
for name, f in L.items():
    out = np.clip(f(rgb.copy()), 0, 1).reshape(-1, 3)
    with open(f'{D}/{name}.cube', 'w') as fh:
        fh.write(f'TITLE "{name}"\nLUT_3D_SIZE {N}\n'); fh.writelines(f'{r:.5f} {gg:.5f} {b:.5f}\n' for r, gg, b in out)
    print('OK', name)
