#!/usr/bin/env python3
"""8 ta mashqni bitta reel'ga yig'ish: video concat + earshot bank SFX + musiqa + -14 LUFS."""
import json, re, subprocess, os
D = os.path.dirname(os.path.abspath(__file__))
OUT = f"{D}/out"
ES = "/root/earshot-venv/bin/earshot"
MUSIC = "/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/music/M2.m4a"
SCENES = [("s1_whip", 3.0), ("s2_card", 3.5), ("s3_push", 3.0), ("s4_zoom", 2.6),
          ("s5_arc", 3.2), ("s6_type", 3.8), ("s7_count", 3.5), ("s8_chat", 4.0)]
# (sahna, mahalliy vaqt, id, hizalash, dB, pan, edits)
CUES = [
    ("s1_whip", 1.20, "whoosh_fast/whip", "peak", -8, 0.5, []), ("s1_whip", 1.50, "ui_pop/soft", "onset", -12, -0.2, []),
    ("s2_card", 1.30, "swish/soft", "peak", -10, -0.3, []), ("s2_card", 1.55, "ui_pop/boop", "onset", -9, 0.2, ["--pitch", "C5"]),
    ("s3_push", 1.00, "whoosh_fast/tight", "peak", -10, -0.5, []), ("s3_push", 1.80, "whoosh_big/thump", "peak", -9, 0.0, []),
    ("s4_zoom", 1.28, "whoosh_big/thump", "peak", -7, 0.0, []), ("s4_zoom", 1.28, "cut_hit/punch", "onset", -8, 0.0, []),
    ("s5_arc", 0.40, "ui_pop/blip", "onset", -13, -0.3, ["--pitch", "C5"]), ("s5_arc", 0.75, "ui_pop/blip", "onset", -13, 0.0, ["--pitch", "E5"]),
    ("s5_arc", 1.05, "ui_pop/blip", "onset", -13, 0.3, ["--pitch", "G5"]), ("s5_arc", 1.50, "cut_hit/sub", "onset", -6, 0.0, ["--pitch", "F1"]),
    ("s5_arc", 1.50, "mallet/glock", "onset", -12, 0.0, ["--pitch", "C6"]),
    ("s6_type", 0.30, "ui_pop/soft", "onset", -11, 0.0, []),
    ("s7_count", 1.70, "reverse_swell/short", "peak", -9, 0.0, []), ("s7_count", 1.75, "cut_hit/sub", "onset", -5, 0.0, ["--pitch", "G1"]),
    ("s8_chat", 0.40, "ui_pop/boop", "onset", -10, -0.4, ["--pitch", "A4"]), ("s8_chat", 1.20, "ui_pop/wide", "onset", -10, 0.4, ["--pitch", "E5"]),
    ("s8_chat", 2.00, "ui_pop/boop", "onset", -10, -0.4, ["--pitch", "A4"]), ("s8_chat", 2.70, "ui_pop/wide", "onset", -10, 0.4, ["--pitch", "E5"]),
]
# har bir sahna boshiga urg'u (sahna kesishi) — earshot: "few salient hits"
for i, (sc, _) in enumerate(SCENES[1:], start=1):
    CUES.append((sc, 0.0, ["knock/snap", "cut_hit/kick", "shutter/snap", "knock/wood"][i % 4], "onset", -9, 0.0, []))
# typewriter klavish tovushlari
for k in range(17):
    CUES.append(("s6_type", 0.62 + k * 0.11, "fit/key/thock", "onset", -17, (-0.2 if k % 2 else 0.2), []))

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-1500:]); raise SystemExit(1)
    return r.stdout

start, t0 = {}, 0.0
for s, d in SCENES: start[s] = t0; t0 += d
TOTAL = t0
with open(f"{OUT}/concat.txt", "w") as f:
    f.writelines(f"file '{OUT}/{s}.mp4'\n" for s, _ in SCENES)
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{OUT}/concat.txt", "-c", "copy", f"{OUT}/reel_v.mp4"])

os.makedirs(f"{OUT}/sfx", exist_ok=True)
ins = ["-ss", "40", "-t", f"{TOTAL}", "-i", MUSIC]
fc = f"[0:a]aformat=channel_layouts=stereo,equalizer=f=150:t=q:w=1:g=-3,equalizer=f=500:t=q:w=1.5:g=4,volume=-14dB,volume='1-0.85*between(t,6.25,6.5)':eval=frame,afade=in:st=0:d=0.5,afade=out:st={TOTAL-0.6}:d=0.6[mus];"
mix = ["[mus]"]
for k, (s, lt, sid, al, db, pan, ed) in enumerate(CUES, start=1):
    f = f"{OUT}/sfx/c{k}.wav"
    meta = json.loads(run([ES, "sfx", "render", sid, "-o", f, "--seed", str(k), *ed, "--json"]))["meta"]
    ref = meta["onset_s"] if al == "onset" else meta["peak_s"]
    st = max(0, start[s] + lt - ref); ms = int(st * 1000)
    pan = max(-0.8, min(0.8, pan)); lg, rg = 1 - max(0, pan), 1 + min(0, pan)
    ins += ["-i", f]
    fc += f"[{k}:a]aformat=channel_layouts=stereo,pan=stereo|c0={lg:.2f}*c0|c1={rg:.2f}*c1,volume={db}dB,adelay={ms}|{ms},apad[s{k}];"
    mix.append(f"[s{k}]")
fc += f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first,atrim=0:{TOTAL}[a]"
run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[a]", "-c:a", "pcm_s16le", f"{OUT}/reel_raw.wav"])
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"{OUT}/reel_raw.wav", "-af", "loudnorm=I=-14:TP=-1:LRA=7:print_format=json",
                    "-f", "null", "-"], capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))
run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}/reel_raw.wav", "-af",
     f"apad=pad_dur=3,loudnorm=I=-14:TP=-1:LRA=7:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
     f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,atrim=0:{TOTAL},aresample=48000",
     "-c:a", "pcm_s16le", f"{OUT}/reel.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}/reel_v.mp4", "-i", f"{OUT}/reel.wav", "-map", "0:v", "-map", "1:a",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-shortest", "-movflags", "+faststart", f"{OUT}/mashq_kutubxonasi.mp4"])
print("TAYYOR", f"{OUT}/mashq_kutubxonasi.mp4", f"{TOTAL:.1f}s", len(CUES), "SFX")
