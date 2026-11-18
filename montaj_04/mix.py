#!/usr/bin/env python3
"""Montaj 04: ovoz + musiqa (2 bo'lim) + past SFX -> -14 LUFS, video bilan birlashtirish."""
import json, subprocess, os, sys
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan import *
os.chdir(D)
END = round(TOTAL + 0.6, 4)
EAR = os.path.expanduser('~/earshot-venv/bin/earshot')
M1, M1OFF = os.path.expanduser('~/montaj-musiqa/mixkit_music_729.mp3'), 4.0
M2, M2OFF = os.path.expanduser('~/montaj-musiqa/mixkit_music_400.mp3'), 12.3
SW = H + w(45) - 0.3          # musiqa almashuvi (3-sabab)
def run(c): subprocess.run(c, check=True)
G = lambda i: H + w(i)

S = []  # (id, global vaqt, dB)
S += [('ui_pop/soft', .08, -21), ('ui_pop/soft', .2, -21), ('cut_hit/punch', .44, -16), ('cut_hit/sub', .44, -15),
      ('whoosh_fast/crisp', .95, -21), ('whoosh_fast/crisp', 1.9, -21), ('ui_pop/wide', 1.47, -19), ('whoosh_fast/tight', 1.75, -21),
      ('swish/bright', H - .12, -18)]
for t in (H, G(20), G(45)): S += [('ui_pop/wide', t + .05, -17), ('cut_hit/kick', t + .05, -19)]
for s, e, _, _ in BROLL: S.append(('whoosh_fast/crisp', H + s, -22))
pops = [G(i) for i in (4, 5, 6, 7, 10, 12, 16, 40, 43, 58, 60, 63, 65, 66, 67, 71, 72, 73, 78, 82, 83, 85)] + [G(32), G(32) + .25, G(32) + .5, G(39)]
for k, t in enumerate(sorted(pops)): S.append((('ui_pop/blip', 'ui_pop/boop')[k % 2], t + .03, -21))
for i in (18, 55, 75): S += [('cut_hit/punch', G(i) + .05, -16)]
S += [('swish/flick', G(35) + .1, -21), ('swish/flick', G(79) + .35, -21), ('reverse_swell/short', SW + .25, -20),
      ('notify/mid_tine', G(93) + .05, -19), ('ui_pop/wide', G(96) + .1, -18), ('whoosh_fast/tight', G(27) - .05, -22)]

os.makedirs('sfx', exist_ok=True)
ins, flt = [], []
for k, (sid, t, db) in enumerate(S):
    p = f"sfx/{sid.replace('/', '_')}.wav"
    if not os.path.exists(p): run([EAR, 'sfx', 'render', sid, '-o', p, '--sr', '48000'])
    y, sr = sf.read(p); y = y if y.ndim == 1 else y.mean(1)
    pk = int(np.argmax(np.abs(y))) / sr
    if 'swell' in sid: pk = len(y) / sr  # swell oxiri vaqtga tushsin
    ms = max(0, int((t - pk) * 1000))
    ins += ['-i', p]
    flt.append(f'[{k+3}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n = len(S); hd = int(H * 1000)
mix = (f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={hd}|{hd},apad[vo];"
       f"[1:a]atrim=start={M1OFF}:duration={SW + .5},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:d=0.25,afade=t=out:st={SW}:d=0.45[m1];"
       f"[2:a]atrim=start={M2OFF - 0.3}:duration={END - SW + .3},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:d=0.3,afade=t=out:st={END - SW - 1.0}:d=1.2,"
       f"adelay={int((SW - .3) * 1000)}|{int((SW - .3) * 1000)}[m2];"
       f"[m1][m2]amix=inputs=2:normalize=0,equalizer=f=250:t=q:w=1:g=-4,equalizer=f=2500:t=q:w=1:g=-5,volume=-17dB[mu];"
       + ';'.join(flt) + ';' + ''.join(f'[s{k}]' for k in range(n)) + f'amix=inputs={n}:normalize=0[fx];'
       f"[vo]asplit[vo1][vo2];[mu][vo2]sidechaincompress=threshold=0.04:ratio=4:attack=15:release=350[mud];"
       f"[vo1][mud][fx]amix=inputs=3:normalize=0,atrim=duration={END}[mx]")
run(['ffmpeg', '-v', 'error', '-y', '-i', 'kes/talk_sync.wav', '-i', M1, '-i', M2] + ins + ['-filter_complex', mix, '-map', '[mx]', '-ar', '48000', 'mix.wav'])
r = subprocess.run(['ffmpeg', '-hide_banner', '-i', 'mix.wav', '-af', 'loudnorm=I=-14:TP=-1:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
m = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
run(['ffmpeg', '-v', 'error', '-y', '-i', 'mix.wav', '-af',
     f"loudnorm=I=-14:TP=-1:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,atrim=duration={END}",
     '-ar', '48000', 'mix_norm.wav'])
print('MIX OK', n, 'SFX', END)
