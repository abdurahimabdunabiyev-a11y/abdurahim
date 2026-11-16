#!/usr/bin/env python3
"""Ovoz v2: earshot bank SFX (kesishga aniq), stereo panorama, yumshoq ducking, stop-down."""
import json, re, subprocess

OUT = "/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/m1"
MUSIC = OUT + "/../music/M2.m4a"
ES = "/root/earshot-venv/bin/earshot"
TOTAL = 17.53
C0 = 15.23  # CTA boshi

# (id, cue s, hizalash: onset|peak, offset ms, pan -1..1, dB, edits)
CUES = [
    ("cut_hit/punch", 1.59, "onset", 0, 0.0, -4, []),          # 3 ta sababi
    ("cut_hit/sub", 1.59, "onset", 0, 0.0, -3, ["--pitch", "F1"]),  # bas qatlami
    ("ui_pop/soft", 2.41, "onset", -10, -0.35, -13, ["--pitch", "A4"]),  # Videoni (keng plan)
    ("shutter/snap", 5.70, "onset", -11, 0.3, -12, []),          # IKKINCHISI punch-in
    ("whoosh_fast/crisp", 6.38, "peak", 37, -0.5, -8, []),      # kema B-roll
    ("swish/bright", 8.42, "peak", 37, 0.5, -10, []),           # port B-roll
    ("shutter/quick", 11.66, "onset", -11, 0.35, -14, []),      # zoom cut
    ("ui_pop/boop", 12.52, "onset", 0, -0.2, -6, ["--pitch", "C5"]),  # ulgurji
    ("whoosh_fast/tight", 13.06, "peak", 37, 0.5, -9, []),      # qo'l siqish
    ("reverse_swell/short", C0, "peak", 42, 0.0, -7, []),       # CTA
    ("ui_pop/wide", C0 + 0.55, "onset", 0, 0.25, -7, ["--pitch", "A5"]),  # Obuna tugmasi
    ("fit/click/floss_lid", C0 + 1.3, "onset", -11, -0.2, -6, []),       # bosish
    ("cut_hit/sub", C0, "onset", 0, 0.0, -4, ["--pitch", "F1"]),         # CTA bas
    ("mallet/flourish", C0 + 0.55, "onset", 0, 0.0, -8, []),            # yakuniy sting
]
STOP_DOWNS = [(1.59, 0.35), (C0, 0.4)]  # musiqa 8 dB pastga, hit oldidan

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:]); raise SystemExit(1)
    return r.stdout

ins, fc, mix = ["-i", f"{OUT}/joined.mov", "-ss", "15", "-t", f"{TOTAL + 0.5}", "-i", MUSIC], "", []
# nutq: markazda, siqilgan, -16 LUFS atrofida
fc += (f"[0:a]pan=mono|c0=0.5*c0+0.5*c1,highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,"
       f"apad=pad_dur=4,loudnorm=I=-16:TP=-2:LRA=7,atrim=0:{TOTAL},asplit=2[v1][sc];[v1]pan=stereo|c0=c0|c1=c0[voice];")
# musiqa: stereo kengaytirilgan, yumshoq ducking (3-5 dB), stop-down hitlar oldidan
vol = "1"
for t, d in STOP_DOWNS:
    vol += f"-0.6*between(t,{t - d},{t})"
fc += (f"[1:a]aformat=channel_layouts=stereo,equalizer=f=70:t=q:w=1:g=4,extrastereo=m=2.2,volume=-17dB,volume='{vol}+1.6*between(t,{C0},{TOTAL})':eval=frame,"
       f"afade=in:st=0:d=0.5,afade=out:st={TOTAL - 0.5}:d=0.5[mus];"
       f"[sc]pan=stereo|c0=c0|c1=c0[sc2];"
       f"[sc2]anullsink;[mus]anull[duck];")
mix = ["[voice]", "[duck]"]
log = []
for k, (sid, cue, align, off, pan, db, edits) in enumerate(CUES, start=2):
    f = f"{OUT}/sfx/s{k}.wav"
    meta = json.loads(run([ES, "sfx", "render", sid, "-o", f, "--seed", str(k), *edits, "--json"]))["meta"]
    ref = meta["onset_s"] if align == "onset" else meta["peak_s"]
    start = max(0.0, cue + off / 1000 - ref)
    ms = int(start * 1000)
    pan = max(-0.85, min(0.85, pan * 1.6))
    lg, rg = (1 - max(0, pan)), (1 + min(0, pan))
    ins += ["-i", f]
    fc += (f"[{k}:a]aformat=channel_layouts=stereo,pan=stereo|c0={lg:.2f}*c0|c1={rg:.2f}*c1,"
           f"volume={db}dB,adelay={ms}|{ms},apad[s{k}];")
    mix.append(f"[s{k}]")
    log.append(f"{sid:22s} cue {cue:5.2f}s {align}{off:+d}ms -> start {start:5.3f}s pan {pan:+.2f} {db}dB")
fc += f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first,atrim=0:{TOTAL}[aout]"
run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[aout]", "-c:a", "pcm_s16le",
     f"{OUT}/mix2_raw.wav"])
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"{OUT}/mix2_raw.wav", "-af",
                    "loudnorm=I=-14:TP=-1:LRA=7:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))
run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}/mix2_raw.wav", "-af",
     f"apad=pad_dur=3,loudnorm=I=-14:TP=-1:LRA=7:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
     f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,"
     f"atrim=0:{TOTAL},aresample=48000", "-c:a", "pcm_s16le", f"{OUT}/mix2.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}/joined.mov", "-i", f"{OUT}/mix2.wav",
     "-vf", f"ass={OUT}/subs.ass", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "17",
     "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "256k",
     "-shortest", f"{OUT}/premium_solar_3sabab_qoralama_v2.mp4"])
print("\n".join(log)); print("TAYYOR v2")
