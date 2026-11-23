"""fon -> orqa yozuv -> odam (niqob) -> old grafika"""
import subprocess, numpy as np, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W, H, N = 1080, 1920, 274
def rd(p, pix, ch):
    pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-f', 'rawvideo', '-pix_fmt', pix, '-'], stdout=subprocess.PIPE); n = W * H * ch; last = None
    while True:
        b = pr.stdout.read(n)
        if len(b) < n:
            while True: yield last
        last = np.frombuffer(b, np.uint8).reshape(H, W, ch); yield last
bg, mk, ob, of = rd('base.mp4', 'bgr24', 3), rd('niqob.mp4', 'gray', 1), rd('orqa.mov', 'bgra', 4), rd('old.mov', 'bgra', 4)
def over(b, r): a = r[..., 3:4].astype(np.float32) / 255; return b * (1 - a) + r[..., :3] * a
ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', '30', '-i', '-', '-c:v', 'libx264', '-crf', '15', '-pix_fmt', 'yuv420p', 'video.mp4'], stdin=subprocess.PIPE)
for i in range(N):
    f = next(bg).astype(np.float32); m = next(mk).astype(np.float32)[..., :1] / 255
    c = over(f, next(ob)); c = c * (1 - m) + f * m; c = over(c, next(of))
    ff.stdin.write(np.clip(c, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait(); print('OK')
