#!/usr/bin/env python3
"""Montaj 01 — Panelbek "Zavodda svet ketsa". Hammasi shu skriptdan yig'iladi."""
import json, subprocess, os, re
W = os.path.dirname(os.path.abspath(__file__)); os.chdir(W)
B, G, O = 'broll', 'grafika', 'out'
FPS = 30; TOTAL = 32.0
SFXBIN = os.path.expanduser('~/earshot-venv/bin/earshot')
MUSIC = '/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/music/M2.m4a'
FONTDIR = os.path.expanduser('~/.fonts/montaj')

def run(c): subprocess.run(c, check=True)

# ---------- 1. Video segmentlari ----------
GRADE = 'eq=contrast=1.08:saturation=1.05,colorbalance=rs=.03:bs=-.03'
SEG = [  # (t0, t1, manba, offset, rejim)
    (0.00, 1.10, 'mixkit_17675', 2.0, 'n'),
    (1.10, 2.00, 'mixkit_47241', 5.05, 'n'),
    (2.00, 4.00, 'mixkit_20958', 0.3, 'dark'),
    (4.00, 4.30, 'mixkit_20770', 1.0, 'n'),
    (4.30, 5.10, 'mixkit_20770', 1.3, 'freeze'),
    (5.10, 6.30, 'mixkit_20958', 3.0, 'desat'),
    (6.30, 7.40, 'mixkit_20770', 5.0, 'freezered'),
    (7.40, 11.45, 'g3_tanishuv', 0.0, 'g'),
    (11.45, 15.10, 'g4_hisob', 0.0, 'g'),
    (15.10, 18.75, 'mixkit_14631', 3.0, 'push'),
    (18.75, 21.50, 'mixkit_23491', 2.0, 'n'),
    (21.50, 24.30, 'mixkit_46623', 6.0, 'push'),
    (24.30, 25.40, 'mixkit_47241', 0.2, 'n'),
    (25.40, 27.00, 'mixkit_22032', 3.0, 'n'),
    (27.00, 32.00, 'g8_cta', 0.0, 'g'),
]
parts = []
for i, (t0, t1, src, off, mode) in enumerate(SEG):
    d = round(t1 - t0, 3); out = f'{O}/seg{i:02d}.mp4'; parts.append(out)
    inp = f'{O}/{src}.mp4' if mode == 'g' else f'{B}/{src}_9x16.mp4'
    vf = {'n': GRADE, 'dark': GRADE + ',eq=brightness=-0.06',
          'desat': 'eq=saturation=0.25:contrast=1.1:brightness=-0.03',
          'freeze': f'trim=end_frame=1,tpad=stop_mode=clone:stop_duration={d},eq=saturation=0.2:contrast=1.15,scale=1134:2016,crop=1080:1920',
          'freezered': f'trim=end_frame=1,tpad=stop_mode=clone:stop_duration={d},eq=saturation=0.15:contrast=1.2,colorbalance=rs=.25:gs=-.05:bs=-.05,scale=1166:2073,crop=1080:1920',
          'push': GRADE + f",scale=w='1080*(1+0.07*t/{d})':h=-2:eval=frame,crop=1080:1920",
          'g': 'null'}[mode]
    run(['ffmpeg', '-v', 'error', '-y', '-ss', str(off), '-i', inp, '-t', str(d), '-vf', f'{vf},fps={FPS},format=yuv420p,setsar=1',
         '-an', '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', out])
with open(f'{O}/concat.txt', 'w') as f: f.writelines(f"file '{os.path.basename(p)}'\n" for p in parts)
run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{O}/concat.txt', '-c', 'copy', f'{O}/video_raw.mp4'])

# ---------- 2. Subtitr + sarlavhalar (ASS) ----------
def ts(t): t = max(0, t); return f'{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}'
WH, SUN, RED, DARK = '&H00EFF1F2', '&H002FB5F6', '&H002E48E5', '&H00121504'
ass = [f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,General Sans SemiBold,74,{WH},{WH},&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,4,3,5,60,60,0,1
Style: Head,Archivo Expanded Black,96,{WH},{WH},&H00000000,&H64000000,0,0,0,0,100,100,-2,0,1,0,6,5,50,50,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"""]
words = json.load(open('ovoz/words.json'))
VO = 0.0  # ovoz boshlanish siljishi
groups, cur = [], []
for w in words:
    cur.append(w)
    if re.search(r'[.,?!—]$', w[0]) or len(cur) == 3: groups.append(cur); cur = []
if cur: groups.append(cur)
for gi, g in enumerate(groups):
    gend = groups[gi + 1][0][1] if gi + 1 < len(groups) else g[-1][2] + 0.5
    gend = min(gend, g[-1][2] + 0.6)
    for k, w in enumerate(g):
        s = w[1] if k else g[0][1]; e = g[k + 1][1] if k + 1 < len(g) else gend
        txt = ' '.join((r'{\c' + SUN + r'\fscx106\fscy106}' + x[0].strip('"') + r'{\c' + WH + r'\fscx100\fscy100}') if j == k else x[0].strip('"') for j, x in enumerate(g))
        pop = r'{\fad(60,0)}' if k == 0 else ''
        ass.append(f'Dialogue: 1,{ts(s+VO)},{ts(e+VO)},Sub,,0,0,0,,{{\\pos(540,1420)}}{pop}{txt}')
HEAD = [  # (t0, t1, matn, rang)
    (1.95, 4.00, 'SVET\\NKETDI.', WH), (4.25, 5.10, "STANOK\\NTO'XTAYDI", WH), (5.10, 6.30, 'ISHCHILAR\\NKUTADI', WH),
    (6.30, 7.40, 'BUYURTMA\\NKECHIKADI', RED), (15.50, 17.30, 'ENG KATTA\\NXARAJAT', WH), (17.35, 18.75, "BO'SH\\NTOM", SUN),
    (18.80, 20.90, 'QUYOSH\\NSTANSIYASI', WH), (21.00, 22.45, '−70%', SUN), (22.45, 24.30, '3–4 YILDA\\NOQLANADI', WH),
    (25.10, 27.00, 'SVET\\NKETMAYDI.', SUN)]
for t0, t1, txt, col in HEAD:
    ml = max(len(x) for x in txt.split('\\N'))
    size = min(170, int(960 / (0.80 * ml))) if txt != '−70%' else 280
    ass.append(f'Dialogue: 2,{ts(t0)},{ts(t1)},Head,,0,0,0,,{{\\pos(540,380)\\c{col}\\fs{size}\\fad(0,80)\\fscx70\\fscy70\\t(0,150,\\fscx100\\fscy100)}}{txt}')
open(f'{O}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# ---------- 3. Mini Panelbek overlay + subtitr ----------
MINI = [('hayron', 4.30, 7.40), ('kozqisish', 15.10, 18.75), ('r70', 18.75, 24.30), ('salom', 24.30, 27.00)]
cmd = ['ffmpeg', '-v', 'error', '-y', '-i', f'{O}/video_raw.mp4']
for f, _, _ in MINI: cmd += ['-loop', '1', '-i', f'{G}/mini_{f}.png']
fc = []; last = '0:v'
for k, (f, t0, t1) in enumerate(MINI):
    fc.append(f'[{k+1}:v]scale=290:-1,format=rgba[m{k}]')
    x = f"if(lt(t-{t0}\\,0.22)\\,-300+340*(t-{t0})/0.22\\,40)"
    y = f"1530+10*sin(7*t)"
    fc.append(f"[{last}][m{k}]overlay=x='{x}':y='{y}':enable='between(t,{t0},{t1-0.001})':shortest=1[v{k}]"); last = f'v{k}'
fc.append(f"[{last}]subtitles={O}/subs.ass:fontsdir={FONTDIR}[vout]")
cmd += ['-filter_complex', ';'.join(fc), '-map', '[vout]', '-t', str(TOTAL), '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', f'{O}/video.mp4']
run(cmd)

# ---------- 4. SFX ----------
SFX = [  # (id, cho'qqi vaqti, apex/peak, dB)
    ('downlifter/tape', 1.95, 0.103, -10), ('cut_hit/sub', 1.98, 0.021, -8),
    ('cut_hit/punch', 4.27, 0.058, -9), ('click/thock', 5.10, 0.004, -12), ('cut_hit/kick', 6.30, 0.013, -9),
    ('whoosh_fast/crisp', 7.42, 0.131, -10), ('cut_hit/punch', 7.84, 0.058, -10), ('pop/2', 8.20, 0.009, -12),
    ('ui_pop/blip', 8.97, 0.017, -12), ('fit/pop/lip_pop', 10.22, 0.009, -10),
    ('swish/soft', 11.47, 0.110, -12), ('riser/snatch', 12.70, 0.386, -14), ('whoosh_fast/tight', 13.55, 0.162, -13),
    ('impact/punch', 14.22, 0.066, -14),
    ('whoosh_big/swell', 15.12, 0.436, -11), ('swish/zing', 18.77, 0.065, -12), ('ui_pop/wide', 21.02, 0.044, -11),
    ('notify/mid_tine', 21.05, 0.038, -16), ('fit/snap/switch_flip', 24.65, 0.035, -8), ('whoosh_fast/tight', 27.02, 0.162, -11),
    ('pop/4', 28.52, 0.004, -11), ('notify/m5', 30.76, 0.004, -15), ('logo_sting/whoosh_glass', 30.85, 0.201, -13),
] + [('fit/key/lubed', 30.20 + 0.08 * k, 0.075, -16) for k in range(5)]
os.makedirs(f'{O}/sfx', exist_ok=True)
ins, flt = [], []
for k, (sid, t, pk, db) in enumerate(SFX):
    p = f"{O}/sfx/{sid.replace('/', '_')}.wav"
    if not os.path.exists(p): run([SFXBIN, 'sfx', 'render', sid, '-o', p, '--sr', '48000'])
    ins += ['-i', p]; ms = max(0, int((t - pk) * 1000))
    flt.append(f'[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n = len(SFX)
mix = (f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={int(VO*1000)}|{int(VO*1000)},apad[vo];"
       f"[1:a]atrim=start=20:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
       f"equalizer=f=250:t=q:w=1:g=-4,equalizer=f=2500:t=q:w=1:g=-4,volume=-17dB,afade=t=in:d=0.4,afade=t=out:st={TOTAL-1.5}:d=1.5[mu];"
       + ';'.join(flt) + ';' + ''.join(f'[s{k}]' for k in range(n)) + f'amix=inputs={n}:normalize=0[fx];'
       f"[vo]asplit[vo1][vo2];[mu][vo2]sidechaincompress=threshold=0.05:ratio=4:attack=20:release=300[mud];"
       f"[vo1][mud][fx]amix=inputs=3:normalize=0,equalizer=f=2000:t=q:w=1.2:g=-2.5,atrim=duration={TOTAL}[mx]")
run(['ffmpeg', '-v', 'error', '-y', '-i', 'ovoz/ovoz.wav', '-i', MUSIC] + ins + ['-filter_complex', mix, '-map', '[mx]', '-ar', '48000', f'{O}/mix.wav'])
# ikki bosqichli loudnorm -14 LUFS
r = subprocess.run(['ffmpeg', '-hide_banner', '-i', f'{O}/mix.wav', '-af', 'loudnorm=I=-14:TP=-1:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
m = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{O}/mix.wav', '-af',
     f"apad=pad_dur=2,loudnorm=I=-14:TP=-1:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,atrim=duration={TOTAL}",
     '-ar', '48000', f'{O}/mix_norm.wav'])
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{O}/video.mp4', '-i', f'{O}/mix_norm.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k',
     '-movflags', '+faststart', '-shortest', f'{O}/panelbek_01_svet.mp4'])
print('TAYYOR', f'{O}/panelbek_01_svet.mp4')
