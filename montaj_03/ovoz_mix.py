#!/usr/bin/env python3
"""Montaj 03 (Tesla): ovoz + musiqa + SFX -> video bilan birlashtirish."""
import json, subprocess, os
W = os.path.dirname(os.path.abspath(__file__)); os.chdir(W)
TOTAL = 88.6
SFXBIN = os.path.expanduser('~/earshot-venv/bin/earshot')
MUSIC = '/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/music/M3.m4a'
MSTART = 71.3  # M3 dagi 1:57 'drop' 45.7 s (1954 burilishi) ga to'g'ri keladi
VOICE = 'ovoz/ovoz.wav'
def run(c): subprocess.run(c, check=True)

CUTS = (4.7, 14.9, 21.2, 34.8, 41.1, 45.7, 55.6, 64.3, 70.9, 78.7, 82.9)
SFX = [('whoosh_fast/crisp', a, 0.131, -13) for a in CUTS]
SFX += [
    # S1 hook: chaqmoqlar, to'xtatildi
    ('glitch/burst', 0.25, 0.361, -16), ('glitch/hit', 1.05, 0.252, -17), ('pop/4', 1.32, 0.004, -12), ('glitch/hit', 1.85, 0.252, -17),
    ('downlifter/tape', 3.72, 0.103, -10), ('cut_hit/sub', 3.76, 0.021, -7), ('impact/punch', 3.8, 0.066, -11),
    # S2
    ('pop/2', 5.12, 0.009, -12), ('ui_pop/blip', 5.52, 0.017, -13), ('pop/4', 6.62, 0.004, -12), ('ui_pop/wide', 8.42, 0.044, -12),
    ('swish/soft', 9.85, 0.110, -15), ('cut_hit/kick', 11.62, 0.013, -11), ('riser/snatch', 13.4, 0.386, -15), ('pop/2', 13.62, 0.009, -12),
    # S3
    ('pop/4', 15.02, 0.004, -12), ('ui_pop/soft', 16.62, 0.042, -13), ('swish/zing', 19.0, 0.065, -14), ('notify/mid_tine', 20.45, 0.038, -14),
    # S4
    ('pop/2', 21.62, 0.009, -12), ('riser/build', 23.6, 1.202, -16), ('ui_pop/wide', 23.42, 0.044, -13),
    ('whoosh_big/swell', 26.0, 0.436, -14), ('notify/m1', 26.65, 0.004, -18),
    # S5
    ('cut_hit/punch', 29.05, 0.058, -11), ('whoosh_fast/heavy', 30.95, 0.135, -12), ('cut_hit/kick', 31.02, 0.013, -9),
    ('impact/metal', 34.0, 0.117, -12), ('cut_hit/rumble', 33.8, 0.072, -12),
    # S6
    ('pop/2', 35.02, 0.009, -12), ('ui_pop/soft', 36.42, 0.042, -13), ('swish/soft', 39.3, 0.110, -14), ('cut_hit/punch', 40.12, 0.058, -10),
    # S7 qayg'u
    ('downlifter/sub_sink', 41.3, 0.152, -16), ('ui_pop/soft', 41.72, 0.042, -14),
    # S8
    ('pop/4', 46.22, 0.004, -12), ('pop/2', 49.52, 0.009, -12), ('swish/zing', 50.0, 0.065, -15), ('pop/2', 50.22, 0.009, -12), ('ui_pop/blip', 50.52, 0.017, -13),
    ('riser/snatch', 52.6, 0.386, -15), ('glitch/chirp', 53.5, 0.076, -18), ('fit/snap/switch_flip', 54.12, 0.035, -9), ('notify/mid_tine', 54.2, 0.038, -15),
    # S9
    ('cut_hit/punch', 55.75, 0.058, -11), ('pop/2', 56.02, 0.009, -12), ('pop/2', 57.27, 0.009, -12), ('pop/2', 58.22, 0.009, -12),
    ('ui_pop/wide', 59.17, 0.044, -11), ('notify/m2', 59.2, 0.004, -18), ('pop/4', 61.92, 0.004, -12),
    # S10
    ('pop/4', 64.37, 0.004, -12), ('ui_pop/soft', 65.77, 0.042, -12), ('pop/2', 66.82, 0.009, -12), ('pop/4', 68.02, 0.004, -12), ('click/thock', 69.9, 0.004, -11),
    # S11
    ('pop/2', 71.02, 0.009, -12), ('ui_pop/wide', 72.52, 0.044, -12), ('pop/4', 74.12, 0.004, -12), ('riser/snatch', 77.2, 0.386, -15), ('notify/m5', 77.4, 0.004, -16),
    # S12
    ('whoosh_big/swell', 79.0, 0.436, -14), ('ui_pop/wide', 80.62, 0.044, -12), ('logo_sting/whoosh_glass', 81.3, 0.201, -14),
    # S13 bahs
    ('cut_hit/kick', 83.02, 0.013, -10), ('swish/blade', 83.3, 0.059, -14), ('pop/4', 85.62, 0.004, -11), ('pop/2', 87.02, 0.009, -12),
]
SFX += [('hover_tick/ping', 71.6 + k * 0.3, 0.004, -20) for k in range(5)]
os.makedirs('sfx', exist_ok=True)
ins, flt = [], []
for k, (sid, t, pk, db) in enumerate(SFX):
    p = f"sfx/{sid.replace('/', '_')}.wav"
    if not os.path.exists(p): run([SFXBIN, 'sfx', 'render', sid, '-o', p, '--sr', '48000'])
    ins += ['-i', p]; ms = max(0, int((t - pk) * 1000))
    flt.append(f'[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n = len(SFX)
mix = (f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,apad[vo];"
       f"[1:a]atrim=start={MSTART}:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
       f"equalizer=f=250:t=q:w=1:g=-4,equalizer=f=2500:t=q:w=1:g=-4,volume=-15dB,afade=t=in:d=0.3,afade=t=out:st={TOTAL-0.9}:d=0.9[mu];"
       + ';'.join(flt) + ';' + ''.join(f'[s{k}]' for k in range(n)) + f'amix=inputs={n}:normalize=0[fx];'
       f"[vo]asplit[vo1][vo2];[mu][vo2]sidechaincompress=threshold=0.05:ratio=4:attack=20:release=300[mud];"
       f"[vo1][mud][fx]amix=inputs=3:normalize=0,equalizer=f=2000:t=q:w=1.2:g=-2.5,atrim=duration={TOTAL}[mx]")
run(['ffmpeg', '-v', 'error', '-y', '-i', VOICE, '-i', MUSIC] + ins + ['-filter_complex', mix, '-map', '[mx]', '-ar', '48000', 'mix.wav'])
r = subprocess.run(['ffmpeg', '-hide_banner', '-i', 'mix.wav', '-af', 'loudnorm=I=-14:TP=-1:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
m = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
run(['ffmpeg', '-v', 'error', '-y', '-i', 'mix.wav', '-af',
     f"apad=pad_dur=2,loudnorm=I=-14:TP=-1:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,atrim=duration={TOTAL}",
     '-ar', '48000', 'mix_norm.wav'])
run(['ffmpeg', '-v', 'error', '-y', '-i', 'video.mp4', '-i', 'mix_norm.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k',
     '-movflags', '+faststart', '-t', str(TOTAL), 'tesla_orzu.mp4'])
print('TAYYOR')
