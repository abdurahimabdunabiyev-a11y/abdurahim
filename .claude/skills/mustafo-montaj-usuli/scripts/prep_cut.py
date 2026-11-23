#!/usr/bin/env python3
"""Xom videoni 1080x1920/30fps proksiga aylantiradi, to'xtashlarni kesadi (jump-cut), yumshoq rang + ovoz tozalash.

Ishlatish:
  python3 prep_cut.py INPUT.MOV --out ~/Movies/ae/<loyiha> --segments "0.22-3.52,4.10-6.98,7.87-12.78"
Natija: out/raw_proxy.mp4 (bir marta), out/cut.mp4 (graded + tozalangan ovoz), out/cuts.json ({K:[(a,b,out_offset)],dur}).
Segmentlarni ovoz energiyasi (RMS) bo'yicha tanlang: Whisper vaqtlari ~0.4 s oldinda chiqadi.
Rang: faqat yumshoq (contrast 1.05, saturation 1.12, yengil highlight siqish). Kuchli grade terini 'kuydiradi'.
"""
import argparse, json, os, subprocess, sys
ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("--out", required=True)
ap.add_argument("--segments", help="'a-b,a-b,...' manba soniyalari; bo'sh bo'lsa butun video")
ap.add_argument("--no-clean-audio", action="store_true")
a = ap.parse_args()
out = os.path.expanduser(a.out); os.makedirs(out, exist_ok=True)
proxy = os.path.join(out, "raw_proxy.mp4")
if not os.path.exists(proxy):
    subprocess.run(["ffmpeg","-v","error","-y","-i",a.inp,"-map","0:v:0","-map","0:a:0","-vf","scale=1080:1920:flags=lanczos,fps=30",
                    "-c:v","libx264","-crf","17","-preset","fast","-pix_fmt","yuv420p","-c:a","aac","-b:a","256k","-ar","48000",proxy], check=True)
dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",proxy],capture_output=True,text=True).stdout)
K = [tuple(map(float, s.split("-"))) for s in a.segments.split(",")] if a.segments else [(0.0, dur)]
off = 0; mp = []
for x, y in K: mp.append((x, y, round(off, 3))); off += y - x
fc = []
for i, (x, y) in enumerate(K):
    fc.append(f"[0:v]trim={x}:{y},setpts=PTS-STARTPTS[v{i}]")
    fc.append(f"[0:a]atrim={x}:{y},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={max(0,y-x-0.03)}:d=0.03[a{i}]")
n = len(K)
fc.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[vo][ao]")
fc.append("[vo]eq=contrast=1.05:saturation=1.12,format=gbrp,curves=all='0/0 0.25/0.238 0.50/0.50 0.80/0.795 0.95/0.935 1/0.975',format=yuv420p[vf]")
fc.append("[ao]anull[af]" if a.no_clean_audio else "[ao]highpass=f=70,afftdn=nr=10:nf=-45,acompressor=threshold=-24dB:ratio=3:attack=5:release=80:makeup=4,loudnorm=I=-16:TP=-1.5:LRA=7[af]")
subprocess.run(["ffmpeg","-v","error","-y","-i",proxy,"-filter_complex",";".join(fc),"-map","[vf]","-map","[af]",
                "-colorspace","bt709","-color_primaries","bt709","-color_trc","bt709","-c:v","libx264","-crf","15","-preset","fast",
                "-pix_fmt","yuv420p","-c:a","aac","-b:a","256k","-ar","48000",os.path.join(out,"cut.mp4")], check=True)
json.dump({"K": mp, "dur": off}, open(os.path.join(out, "cuts.json"), "w"))
print("cut.mp4 tayyor, davomiylik", round(off, 2), "s;", n, "bo'lak")
