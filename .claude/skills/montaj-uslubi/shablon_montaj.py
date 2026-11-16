#!/usr/bin/env python3
"""Premium Solar — '3 ta sabab' qoralama montaji (hook + 2-sabab + CTA)."""
import os, subprocess

S = "/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad"
W, H, FPS = 1080, 1920, 30
OUT = f"{S}/m1"
A, B = f"{S}/xom/A9768.mp4", f"{S}/xom/A9787.mp4"
BR = f"{S}/broll"
SFX = "/root/.claude/plugins/cache/hyperframes/hyperframes/0.9.57/skills/media-use/audio/assets/sfx"
MUSIC = f"{S}/music/M2.m4a"
LOGO = "/home/user/abdurahim/.claude/skills/montaj-uslubi/assets/logo_premium_solar.png"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:]); raise SystemExit(1)

GRADE = "eq=contrast=1.06:saturation=1.04:gamma=0.98,vignette=PI/5"

# ---------- 1. Spiker segmentlari (manba, boshlanish, tugash, zoom) ----------
SEGS = [
    (A, 1.45, 3.04, 1.00), (A, 3.04, 3.86, 1.35), (A, 3.86, 5.10, 1.00), (A, 5.10, 7.15, 1.15),
    (B, 8.62, 9.30, 1.25), (B, 9.30, 13.52, 1.00), (B, 13.52, 14.58, 1.00), (B, 14.58, 15.95, 1.25),
    (B, 15.95, 18.15, 1.00),
]
parts = []
for i, (src, a, b, z) in enumerate(SEGS):
    p = f"{OUT}/seg{i}.mov"
    crop = (f"crop=iw/{z}:ih/{z}:(iw-iw/{z})/2:"
            f"max(0\\,min(ih-ih/{z}\\,ih*0.35-ih/{z}*0.36))")
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", src,
         "-vf", f"{crop},scale={W}:{H}:flags=lanczos,fps={FPS},{GRADE},format=yuv420p",
         "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-c:a", "pcm_s16le", "-ar", "48000", p])
    parts.append(p)
with open(f"{OUT}/list.txt", "w") as f:
    f.writelines(f"file '{p}'\n" for p in parts)
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt",
     "-c", "copy", f"{OUT}/speaker.mov"])
SPK_DUR = sum(b - a for _, a, b, _ in SEGS)  # ~15.23

# ---------- 2. B-roll (letterbox, haqiqiy Mixkit kadrlar) ----------
BROLLS = [  # (fayl, manba boshi, chiqish boshi, chiqish oxiri)
    ("mixkit_46623.mp4", 3.0, 0.00, 1.59),
    ("mixkit_4011.mp4", 2.0, 6.38, 8.42),
    ("mixkit_30979.mp4", 0.0, 8.42, 10.58),
    ("mixkit_24047.mp4", 0.2, 13.06, 14.28),
]
inputs, fc, last = ["-i", f"{OUT}/speaker.mov"], "", "0:v"
for k, (fn, ss, t0, t1) in enumerate(BROLLS, start=1):
    inputs += ["-ss", str(ss), "-t", f"{t1 - t0 + 0.1:.2f}", "-i", f"{BR}/{fn}"]
    fc += (f"[{k}:v]fps={FPS},{GRADE},split[x{k}][y{k}];"
           f"[x{k}]scale=-2:{H},crop={W}:{H},boxblur=28:2,eq=brightness=-0.18:saturation=0.8[bg{k}];"
           f"[y{k}]scale={W}:-2:flags=lanczos[fg{k}];"
           f"[bg{k}][fg{k}]overlay=0:(H-h)/2,setpts=PTS-STARTPTS+{t0}/TB[b{k}];"
           f"[{last}][b{k}]overlay=0:0:eof_action=pass:enable='between(t,{t0},{t1})'[v{k}];")
    last = f"v{k}"
fc = fc.rstrip(";")
run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", f"[{last}]",
     "-map", "0:a", "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-c:a", "copy",
     f"{OUT}/main.mov"])

# ---------- 3. CTA kartasi ----------
CTA = 2.3
run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
     f"gradients=s={W}x{H}:r={FPS}:d={CTA}:c0=0x0B2A23:c1=0x031210:x0=540:y0=700:x1=540:y1=1900:type=radial",
     "-loop", "1", "-t", str(CTA), "-i", LOGO,
     "-f", "lavfi", "-t", str(CTA), "-i", "anullsrc=r=48000:cl=stereo",
     "-filter_complex",
     f"[1:v]crop=1060:560:238:240,format=rgba,colorkey=0x0A1F1A:0.16:0.08,scale=940:-1,"
     f"fade=in:st=0:d=0.35:alpha=1[lg];"
     f"[0:v][lg]overlay=(W-w)/2:360,format=yuv420p[v]",
     "-map", "[v]", "-map", "2:a", "-c:v", "libx264", "-crf", "14", "-preset", "fast",
     "-c:a", "pcm_s16le", f"{OUT}/cta.mov"])
with open(f"{OUT}/list2.txt", "w") as f:
    f.write(f"file '{OUT}/main.mov'\nfile '{OUT}/cta.mov'\n")
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list2.txt",
     "-c", "copy", f"{OUT}/joined.mov"])
TOTAL = SPK_DUR + CTA

# ---------- 4. Subtitrlar (ASS, so'zma-so'z) ----------
def bgr(hexrgb, a="00"):
    r, g, b = hexrgb[0:2], hexrgb[2:4], hexrgb[4:6]
    return f"&H{a}{b}{g}{r}".upper()

WHITE, SUN, DARK = bgr("F2F1EF"), bgr("F6B52F"), bgr("041512")
STYLES = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Key,Inter Display Black,150,{WHITE},{WHITE},&H00000000,&H64000000,0,0,0,0,100,100,-2,0,1,0,5,5,40,40,0,1
Style: Ctx,Inter Display SemiBold,64,{WHITE},{WHITE},&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,0,4,5,40,40,0,1
Style: Label,Michroma,74,{SUN},{SUN},&H00000000,&H50000000,0,0,0,0,100,100,10,0,1,0,4,5,40,40,0,1
Style: Pill,Inter Display SemiBold,60,{WHITE},{WHITE},&H00264A3E,&H00000000,0,0,0,0,100,100,1,0,3,26,0,5,40,40,0,1
Style: Btn,Inter Display ExtraBold,72,{DARK},{DARK},{SUN},&H00000000,0,0,0,0,100,100,1,0,3,30,0,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

events = []

def line(words, y, style, end, accent=(), size=None, x=W // 2):
    """words: [(text, out_time)]; har bir so'z alohida qatlam — tartib bir xil, faqat o'sha so'z ko'rinadi."""
    full = [w for w, _ in words]
    fs = f"\\fs{size}" if size else ""
    for i, (w, t) in enumerate(words):
        col = f"\\c{SUN}" if w in accent else ""
        pre = " ".join(full[:i]); post = " ".join(full[i + 1:])
        hide = "{\\alpha&HFF&\\t(0,1,\\alpha&HFF&)}"
        txt = (f"{{\\an5\\pos({x},{y}){fs}}}"
               + (hide + pre + " " if pre else "")
               + f"{{\\alpha&HFF&\\blur6{col}\\t(0,140,\\alpha&H00&\\4a&H78&\\blur0)}}{w}"
               + (" " + hide + post if post else ""))
        events.append(f"Dialogue: 1,{ts(t)},{ts(end)},{style},,0,0,0,,{txt}")

def fit(text, base):  # uzun kalit so'zlar ekranga sig'sin (~980px; Inter Black o'rtacha 0.5em)
    est = len(text) * base * 0.5
    return base if est <= 980 else int(base * 980 / est)

# Hook (B-roll, quyosh fermasi) — matn klip ostida
events.append(f"Dialogue: 1,{ts(0)},{ts(1.59)},Label,,0,0,0,,{{\\an5\\pos({W//2},520)\\fad(150,0)}}PREMIUM SOLAR")
line([("Premium", 0.05), ("Solar'dan", 0.37)], 1350, "Ctx", 1.59)
line([("quyosh", 0.79), ("paneli", 1.05)], 1470, "Key", 1.59, size=fit("quyosh paneli", 150))
line([("olishning", 1.23)], 1590, "Ctx", 1.59)
# 3 ta sababi (punch-in, barmoqlar)
line([("3", 1.59), ("ta", 1.75), ("sababi", 2.01)], 1330, "Key", 2.41, accent=("3", "ta", "sababi"), size=190)
# Videoni oxirigacha ko'rsangiz
line([("Videoni", 2.41)], 1150, "Ctx", 3.65)
line([("oxirigacha", 2.87)], 1270, "Key", 3.65)
line([("ko'rsangiz", 3.09)], 1390, "Ctx", 3.65)
# xatoga yo'l qo'ymay xarid qilishingiz mumkin (matn tasdiqlanishi kerak)
line([("xatoga", 3.65), ("yo'l", 4.07), ("qo'ymay", 4.41)], 1260, "Key", 5.70, size=fit("xatoga yo'l qo'ymay", 150))
line([("xarid", 4.67), ("qilishingiz", 4.87), ("mumkin", 5.13)], 1380, "Ctx", 5.70)
# IKKINCHISI yorlig'i
events.append(f"Dialogue: 2,{ts(5.72)},{ts(13.03)},Label,,0,0,0,,{{\\an5\\pos({W//2},330)\\fad(120,120)\\blur4\\t(0,160,\\blur0)}}IKKINCHISI")
# Birinchi qo'ldan va kafolat bilan (kema B-roll)
line([("birinchi", 6.38), ("qo'ldan", 7.02)], 1420, "Key", 8.42, size=fit("birinchi qo'ldan", 150))
line([("va", 7.34), ("kafolat", 7.48), ("bilan", 8.06)], 1545, "Ctx", 8.42, accent=("kafolat",))
# Panellarni to'g'ridan-to'g'ri o'zimiz import qilamiz (port B-roll)
line([("panellarni", 8.44), ("to'g'ridan-to'g'ri", 9.00)], 1340, "Ctx", 10.58)
line([("o'zimiz", 9.40), ("import", 9.78), ("qilamiz", 10.12)], 1460, "Key", 10.58,
     accent=("import",), size=fit("o'zimiz import qilamiz", 150))
# O'rtada hech kim yo'q
line([("o'rtada", 10.60)], 1150, "Ctx", 11.66)
line([("hech", 11.04), ("kim", 11.22), ("yo'q", 11.38)], 1275, "Key", 11.66)
# shuning uchun narxlar ULGURJI
line([("shuning", 11.66), ("uchun", 11.95), ("narxlar", 12.26)], 1150, "Ctx", 13.03)
line([("ulgurji", 12.52)], 1290, "Key", 13.03, accent=("ulgurji",), size=190)
# Chek ham beramiz (qo'l siqish B-roll)
line([("chek", 13.10), ("ham", 13.64), ("beramiz", 13.84)], 1440, "Key", 14.28, size=fit("chek ham beramiz", 150))
# kafolat ham
line([("kafolat", 14.30), ("ham", 14.94)], 1280, "Key", 15.23, accent=("kafolat",), size=170)
# CTA
c0 = SPK_DUR
events.append(f"Dialogue: 1,{ts(c0+0.25)},{ts(TOTAL)},Pill,,0,0,0,,{{\\an5\\pos({W//2},1060)\\fad(200,0)}}  @premiumsolar.uz  ")
events.append(f"Dialogue: 1,{ts(c0+0.55)},{ts(TOTAL)},Btn,,0,0,0,,{{\\an5\\pos({W//2},1230)\\fscx70\\fscy70\\alpha&HFF&\\t(0,180,\\fscx100\\fscy100\\alpha&H00&)}}  Obuna bo'ling  ")
events.append(f"Dialogue: 1,{ts(c0+0.9)},{ts(TOTAL)},Ctx,,0,0,0,,{{\\an5\\pos({W//2},1400)\\fs54\\fad(200,0)}}Ariza va B2B katalog — profilda")

with open(f"{OUT}/subs.ass", "w") as f:
    f.write(STYLES + "\n".join(events) + "\n")

# ---------- 5. Ovoz: nutq + musiqa (ducking) + SFX ----------
SFXS = [("impact-bass-1.mp3", 1.57, -6), ("whoosh-short.mp3", 5.62, -10), ("whoosh.mp3", 6.25, -10),
        ("whoosh-short.mp3", 8.35, -12), ("pop.mp3", 12.50, -8), ("whoosh.mp3", 12.95, -11),
        ("whoosh-cinematic.mp3", c0 - 0.15, -8), ("pop.mp3", c0 + 0.55, -8), ("click-soft.mp3", c0 + 1.3, -6)]
ain = ["-i", f"{OUT}/joined.mov", "-ss", "15", "-t", f"{TOTAL + 0.5}", "-i", MUSIC]
afc = ("[0:a]highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,"
       f"apad=pad_dur=4,loudnorm=I=-16:TP=-2:LRA=7,atrim=0:{TOTAL},asplit=2[voice][sc];"
       f"[1:a]volume=-15dB,afade=in:st=0:d=0.6,afade=out:st={TOTAL - 0.8}:d=0.8[mus];"
       "[mus][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[duck];")
mix = ["[voice]", "[duck]"]
for j, (fn, t, db) in enumerate(SFXS, start=2):
    ain += ["-i", f"{SFX}/{fn}"]
    ms = int(t * 1000)
    afc += f"[{j}:a]volume={db}dB,adelay={ms}|{ms},apad[s{j}];"
    mix.append(f"[s{j}]")
afc += (f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first,"
        f"atrim=0:{TOTAL},aresample=48000[aout]")
run(["ffmpeg", "-v", "error", "-y", *ain, "-filter_complex", afc, "-map", "[aout]",
     "-c:a", "pcm_s16le", f"{OUT}/mix_raw.wav"])
# Ikki bosqichli loudnorm: o'lchab, keyin chiziqli (aniq -14 LUFS)
import json, re
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"{OUT}/mix_raw.wav", "-af",
                    "loudnorm=I=-14:TP=-1:LRA=7:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))
run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}/mix_raw.wav", "-af",
     f"apad=pad_dur=3,loudnorm=I=-14:TP=-1:LRA=7:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
     f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,"
     f"atrim=0:{TOTAL},aresample=48000", "-c:a", "pcm_s16le", f"{OUT}/mix.wav"])

# ---------- 6. Yakuniy render ----------
run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}/joined.mov", "-i", f"{OUT}/mix.wav",
     "-vf", f"ass={OUT}/subs.ass", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "17",
     "-preset", "slow", "-profile:v", "high", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
     "-c:a", "aac", "-b:a", "256k", "-shortest", f"{OUT}/premium_solar_3sabab_qoralama.mp4"])
print("TAYYOR", f"{OUT}/premium_solar_3sabab_qoralama.mp4", f"{TOTAL:.2f}s")
