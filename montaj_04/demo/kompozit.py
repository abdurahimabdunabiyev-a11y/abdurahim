#!/usr/bin/env python3
"""Qatlamli kompozit: fon -> orqa grafika -> PIP karta -> ODAM (niqob) -> old grafika; boshida gologramma kirish."""
import subprocess, numpy as np, cv2, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS, N = 1080, 1920, 30, 195
def reader(p, pix, ch, size=(W, H)):
    pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'scale={size[0]}:{size[1]}', '-f', 'rawvideo', '-pix_fmt', pix, '-'], stdout=subprocess.PIPE)
    n = size[0] * size[1] * ch; last = None
    while True:
        b = pr.stdout.read(n)
        if len(b) < n:
            while True: yield last
        last = np.frombuffer(b, np.uint8).reshape(size[1], size[0], ch); yield last
bg, msk = reader('bg.mp4', 'bgr24', 3), reader('niqob.mp4', 'gray', 1)
orq, old = reader('orqa.mov', 'bgra', 4), reader('old.mov', 'bgra', 4)
CX, CY, CW, CH, R = 337, 157, 406, 506, 40      # karta ichki qismi (7px ramka ichida)
pip = reader('pip.mp4', 'bgr24', 3, (CW, int(CW * 16 / 9)))
rm = np.zeros((CH, CW), np.float32); cv2.rectangle(rm, (R, 0), (CW - R, CH), 1, -1); cv2.rectangle(rm, (0, R), (CW, CH - R), 1, -1)
for x, y in ((R, R), (CW - R, R), (R, CH - R), (CW - R, CH - R)): cv2.circle(rm, (x, y), R, 1, -1, cv2.LINE_AA)
def over(base, rgba):
    a = rgba[..., 3:4].astype(np.float32) / 255
    return base * (1 - a) + rgba[..., :3].astype(np.float32) * a
def ease(x): x = min(1, max(0, x)); return 1 - (1 - x) ** 3
ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                       '-c:v', 'libx264', '-crf', '15', '-pix_fmt', 'yuv420p', 'video.mp4'], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS
    f = next(bg).astype(np.float32); m = next(msk)[..., 0].astype(np.float32)[..., None] / 255; ob = next(orq); of = next(old); pv = next(pip)
    person = f.copy()
    comp = over(f, ob)
    if t >= 2.4:  # PIP karta odam orqasida
        k = ease((t - 2.4) / .35); s = .85 + .15 * k
        src = pv[(pv.shape[0] - CH) // 2:(pv.shape[0] - CH) // 2 + CH].astype(np.float32)
        if s < 1:
            M = cv2.getRotationMatrix2D((CW / 2, CH / 2), 0, s); src = cv2.warpAffine(src, M, (CW, CH)); mm = cv2.warpAffine(rm, M, (CW, CH))
        else: mm = rm
        a = (mm * k)[..., None]
        comp[CY:CY + CH, CX:CX + CW] = comp[CY:CY + CH, CX:CX + CW] * (1 - a) + src * a
    comp = comp * (1 - m) + person * m
    comp = over(comp, of)
    if t < .45:  # gologramma: qora fonda ko'k-yorqin siluet -> haqiqiy kadr
        m2 = m[..., 0]; glow = cv2.GaussianBlur(m2, (0, 0), 14)
        g = np.clip(m2 * .85 + glow * .9, 0, 1)[..., None]
        lum = cv2.cvtColor(person.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)[..., None] / 255
        lines = (0.75 + 0.25 * np.sin(np.arange(H) * .9 + t * 40))[:, None, None]
        holo = g * np.array([255, 190, 60], np.float32) * (0.45 + 0.55 * lum) * lines
        a = ease((t - .2) / .25) if t > .2 else 0
        comp = holo * (1 - a) + comp * a
    ff.stdin.write(np.clip(comp, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait(); print('OK video.mp4')
