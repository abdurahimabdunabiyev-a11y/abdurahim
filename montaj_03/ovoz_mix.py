#!/usr/bin/env python3
"""Montaj 03 (Tesla): ovoz + musiqa + SFX -> video bilan birlashtirish."""
import json, subprocess, os
W = os.path.dirname(os.path.abspath(__file__)); os.chdir(W)
TOTAL = 74.4
SFXBIN = os.path.expanduser('~/earshot-venv/bin/earshot')
MUSIC = '/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/music/M3.m4a'
MSTART = 84.0  # M3 dagi 1:57 'drop' 45.7 s (1954 burilishi) ga to'g'ri keladi
VOICE = 'ovoz/ovoz5.wav'
def run(c): subprocess.run(c, check=True)

CUTS = (5.0, 9.95, 15.3, 24.4, 30.0, 32.95, 40.15, 43.6, 49.4, 58.45, 69.1)
SFX = [('whoosh_fast/crisp', a, 0.131, -13) for a in CUTS]
SFX += [
    ('glitch/burst', 0.25, 0.361, -16), ('glitch/hit', 1.05, 0.252, -17), ('pop/4', 1.47, 0.004, -12), ('glitch/hit', 2.6, 0.252, -17),
    ('downlifter/tape', 4.12, 0.103, -10), ('cut_hit/sub', 4.18, 0.021, -7), ('impact/punch', 4.22, 0.066, -11),
    ('pop/2', 5.12, 0.009, -12), ('ui_pop/blip', 5.62, 0.017, -13), ('pop/4', 7.12, 0.004, -12), ('ui_pop/wide', 8.87, 0.044, -12),
    ('pop/4', 10.07, 0.004, -12), ('ui_pop/soft', 12.32, 0.042, -13), ('swish/zing', 13.3, 0.065, -14), ('notify/mid_tine', 14.72, 0.038, -14),
    ('pop/2', 15.52, 0.009, -12), ('riser/build', 16.5, 1.202, -16), ('ui_pop/wide', 16.32, 0.044, -13), ('whoosh_big/swell', 18.1, 0.436, -14),
    ('cut_hit/punch', 20.85, 0.058, -11), ('whoosh_fast/heavy', 21.9, 0.135, -12), ('cut_hit/kick', 21.92, 0.013, -9),
    ('impact/metal', 23.0, 0.117, -12), ('cut_hit/rumble', 22.85, 0.072, -12), ('cut_hit/kick', 23.32, 0.013, -11),
    ('pop/2', 24.52, 0.009, -12), ('ui_pop/soft', 25.92, 0.042, -13), ('swish/soft', 28.6, 0.110, -14), ('cut_hit/punch', 29.32, 0.058, -10),
    ('downlifter/sub_sink', 30.2, 0.152, -16), ('ui_pop/soft', 31.35, 0.042, -14),
    ('pop/4', 33.12, 0.004, -12), ('pop/2', 36.42, 0.009, -12), ('swish/zing', 36.9, 0.065, -15), ('pop/2', 37.22, 0.009, -12),
    ('riser/snatch', 39.0, 0.386, -15), ('fit/snap/switch_flip', 39.62, 0.035, -9), ('notify/mid_tine', 39.66, 0.038, -15),
    ('cut_hit/punch', 40.3, 0.058, -11), ('pop/2', 40.32, 0.009, -12), ('pop/2', 41.12, 0.009, -12), ('ui_pop/wide', 41.92, 0.044, -11),
    ('pop/4', 43.72, 0.004, -12), ('pop/2', 44.22, 0.009, -12), ('pop/2', 45.62, 0.009, -12), ('pop/2', 46.32, 0.009, -12), ('pop/2', 47.12, 0.009, -12),
    ('cut_hit/kick', 48.42, 0.013, -9),
    ('pop/4', 49.52, 0.004, -12), ('pop/2', 50.92, 0.009, -12), ('riser/snatch', 54.2, 0.386, -15), ('notify/m5', 54.3, 0.004, -17),
    ('cut_hit/punch', 55.35, 0.058, -11), ('riser/snatch', 58.0, 0.386, -14), ('impact/punch', 58.05, 0.066, -13),
    ('pop/2', 58.8, 0.009, -12), ('ui_pop/wide', 60.77, 0.044, -12), ('fit/pop/lip_pop', 61.67, 0.009, -11),
    ('logo_sting/whoosh_glass', 62.75, 0.201, -11), ('cut_hit/punch', 62.75, 0.058, -10), ('whoosh_big/swell', 63.6, 0.436, -13),
    ('ui_pop/wide', 65.37, 0.044, -12), ('pop/4', 66.37, 0.004, -12), ('notify/m1', 66.9, 0.004, -17),
    ('cut_hit/kick', 69.27, 0.013, -10), ('swish/blade', 69.4, 0.059, -14), ('pop/4', 71.42, 0.004, -11), ('pop/2', 73.02, 0.009, -12),
]
SFX += [('hover_tick/ping', 65.45 + i * 0.1, 0.004, -19) for i in range(12)]
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
