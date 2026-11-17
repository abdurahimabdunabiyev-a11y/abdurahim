#!/usr/bin/env python3
"""Avtomatik jump-cut: pauzalar va "ee/mmm" kabi to'ldiruvchi so'zlarni kesadi.
Ishlatish: ~/claude-video-kit/.venv/bin/python jumpcut.py xom.mp4 chiqish.mp4 [--pauza 0.35] [--zaxira 0.08] [--sozlar sozlar.json]
Natija: chiqish.mp4 (kesilgan video+ovoz) + chiqish.words.json (yangi vaqtlar bilan so'zlar — subtitr uchun).
Agar --sozlar berilsa, qayta transkripsiya qilinmaydi."""
import json, subprocess, argparse, re, tempfile, os
import numpy as np
ap = argparse.ArgumentParser(); ap.add_argument('inp'); ap.add_argument('out')
ap.add_argument('--pauza', type=float, default=0.35, help='shundan uzun pauza kesiladi')
ap.add_argument('--zaxira', type=float, default=0.08, help="so'z oldi/orqasida qoldiriladigan zaxira")
ap.add_argument('--sozlar'); a = ap.parse_args()
FILLER = re.compile(r"^(e+|ee+|eh+|mm+|hmm+|a+h*|ı+|uh+|um+|xm+|xo'sh\.\.\.)[.,!?]*$", re.I)
if a.sozlar:
    W = json.load(open(a.sozlar))
else:
    from faster_whisper import WhisperModel
    t = tempfile.mktemp(suffix='.wav'); subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.inp, '-ac', '1', '-ar', '16000', t], check=True)
    import soundfile as sf; y, _ = sf.read(t, dtype='float32'); os.remove(t)
    m = WhisperModel('large-v3', device='cpu', compute_type='int8')
    segs, _ = m.transcribe(y, language='uz', word_timestamps=True, initial_prompt="O'zbekcha nutq. Premium Solar, quyosh panellari.")
    W = [[w.word.strip(), w.start, w.end] for s in segs for w in (s.words or [])]
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', a.inp], capture_output=True, text=True).stdout)
keep = [w for w in W if not FILLER.match(w[0])]
# saqlanadigan oraliqlar
segs = []
for w, s, e in keep:
    s, e = max(0, s - a.zaxira), min(dur, e + a.zaxira)
    if segs and s - segs[-1][1] <= a.pauza: segs[-1][1] = max(segs[-1][1], e)
    else: segs.append([s, e])
# yangi vaqtlar
out_words, acc = [], 0.0
for s0, e0 in segs:
    for w, s, e in keep:
        if s >= s0 - 1e-3 and e <= e0 + 1e-3: out_words.append([w, round(acc + s - s0, 3), round(acc + e - s0, 3)])
    acc += e0 - s0
fc = ''.join(f"[0:v]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={max(0,e-s-0.012):.3f}:d=0.012[a{i}];" for i, (s, e) in enumerate(segs))
fc += ''.join(f'[v{i}][a{i}]' for i in range(len(segs))) + f'concat=n={len(segs)}:v=1:a=1[v][a]'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.inp, '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-c:a', 'aac', '-b:a', '256k', a.out], check=True)
json.dump(out_words, open(a.out.rsplit('.', 1)[0] + '.words.json', 'w'), ensure_ascii=False)
print(f'OK {a.out}: {dur:.1f}s -> {acc:.1f}s ({len(segs)} bo\'lak, {len(W) - len(keep)} to\'ldiruvchi so\'z kesildi)')
