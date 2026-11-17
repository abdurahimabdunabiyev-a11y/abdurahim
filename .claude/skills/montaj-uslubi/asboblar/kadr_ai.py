#!/usr/bin/env python3
"""Kadr bilan ishlash (MediaPipe, CPU):
  yuz   video.mp4 yuz.json            — har 0.2 s da yuz markazi (x,y,w,h, 0..1), silliqlangan
  kes   video.mp4 chiqish.mp4 [--zoom 1.0] [--yuz yuz.json]
                                      — 16:9 yoki 4:3 videoni 9:16 ga yuzni kuzatib aqlli kesish (1080x1920)
  niqob video.mp4 niqob.mp4           — odam niqobi (oq=odam, qora=fon), oq-qora video; matnni odam orqasiga
                                        qo'yish yoki fonni xiralashtirish uchun (ffmpeg alphamerge/maskedmerge)
Ishlatish: ~/montaj-venv/bin/python kadr_ai.py <buyruq> ...
"""
import sys, json, subprocess, argparse
import numpy as np, cv2, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
M = '/root/montaj-models/'

def frames(path, step=1):
    cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS) or 30; i = 0
    while True:
        ok, f = cap.read()
        if not ok: break
        if i % step == 0: yield i, i / fps, f
        i += 1
    cap.release()

def info(path):
    cap = cv2.VideoCapture(path); r = (int(cap.get(3)), int(cap.get(4)), cap.get(5) or 30, int(cap.get(7))); cap.release(); return r

def yuz(path, out=None):
    det = vision.FaceDetector.create_from_options(vision.FaceDetectorOptions(base_options=BaseOptions(model_asset_path=M + 'blaze_face_short_range.tflite'), min_detection_confidence=0.5))
    W, H, fps, n = info(path); step = max(1, round(fps * 0.2)); res = []
    for i, t, f in frames(path, step):
        r = det.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(f, cv2.COLOR_BGR2RGB)))
        if r.detections:
            b = max(r.detections, key=lambda d: d.bounding_box.width * d.bounding_box.height).bounding_box
            res.append([round(t, 3), (b.origin_x + b.width / 2) / W, (b.origin_y + b.height / 2) / H, b.width / W, b.height / H])
        else: res.append([round(t, 3), None, None, None, None])
    # bo'shliqlarni to'ldirish + silliqlash (kamera "suzib" yuradi, sakramaydi)
    xs = np.array([r[1] if r[1] is not None else np.nan for r in res]); ys = np.array([r[2] if r[2] is not None else np.nan for r in res])
    for a in (xs, ys):
        idx = np.arange(len(a)); ok = ~np.isnan(a)
        a[:] = np.interp(idx, idx[ok], a[ok]) if ok.any() else 0.5
    k = np.ones(7) / 7
    xs = np.convolve(np.pad(xs, 3, mode='edge'), k, 'valid'); ys = np.convolve(np.pad(ys, 3, mode='edge'), k, 'valid')
    data = {'w': W, 'h': H, 'fps': fps, 'pts': [[r[0], float(x), float(y)] for r, x, y in zip(res, xs, ys)], 'topildi': sum(r[1] is not None for r in res) / max(1, len(res))}
    if out: json.dump(data, open(out, 'w'))
    return data

def kes(path, out, zoom=1.0, yuzjson=None):
    d = json.load(open(yuzjson)) if yuzjson else yuz(path)
    W, H, fps = d['w'], d['h'], d['fps']
    ch = int(H / zoom); cw = int(ch * 9 / 16)
    if cw > W: cw = W; ch = int(cw * 16 / 9)
    ts = np.array([p[0] for p in d['pts']]); xs = np.array([p[1] for p in d['pts']]); ys = np.array([p[2] for p in d['pts']])
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'1080x1920', '-r', str(fps), '-i', '-',
                           '-i', path, '-map', '0:v', '-map', '1:a?', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', out], stdin=subprocess.PIPE)
    for i, t, f in frames(path):
        cx = np.interp(t, ts, xs) * W; cy = np.interp(t, ts, ys) * H
        x0 = int(np.clip(cx - cw / 2, 0, W - cw)); y0 = int(np.clip(cy - ch * 0.38, 0, H - ch))
        ff.stdin.write(cv2.resize(f[y0:y0 + ch, x0:x0 + cw], (1080, 1920), interpolation=cv2.INTER_LANCZOS4).tobytes())
    ff.stdin.close(); ff.wait(); print('OK', out)

def niqob(path, out):
    seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(base_options=BaseOptions(model_asset_path=M + 'selfie_segmenter.tflite'),
                                                    running_mode=vision.RunningMode.VIDEO, output_confidence_masks=True))
    W, H, fps, n = info(path)
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'gray', '-s', f'{W}x{H}', '-r', str(fps), '-i', '-',
                           '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    prev = None
    for i, t, f in frames(path):
        r = seg.segment_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(f, cv2.COLOR_BGR2RGB)), int(t * 1000))
        m = r.confidence_masks[0].numpy_view().astype(np.float32)
        m = cv2.GaussianBlur(m, (0, 0), 1.5)
        if prev is not None: m = 0.6 * m + 0.4 * prev  # titrashni kamaytirish
        prev = m
        ff.stdin.write((np.clip(m, 0, 1) * 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait(); print('OK', out)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd'); ap.add_argument('inp'); ap.add_argument('out'); ap.add_argument('--zoom', type=float, default=1.0); ap.add_argument('--yuz')
    a = ap.parse_args()
    if a.cmd == 'yuz': d = yuz(a.inp, a.out); print('OK', a.out, f"yuz topildi: {d['topildi']:.0%}")
    elif a.cmd == 'kes': kes(a.inp, a.out, a.zoom, a.yuz)
    elif a.cmd == 'niqob': niqob(a.inp, a.out)
