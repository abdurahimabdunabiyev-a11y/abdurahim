#!/usr/bin/env python3
"""Montaj 02 (birfoiz uslubi): ovoz + musiqa + SFX -> video bilan birlashtirish."""
import json, subprocess, os
W = os.path.dirname(os.path.abspath(__file__)); os.chdir(W)
TOTAL = 33.0
SFXBIN = os.path.expanduser('~/earshot-venv/bin/earshot')
MUSIC = '/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/music/M2.m4a'
VOICE = '../montaj_01/ovoz/ovoz.wav'
def run(c): subprocess.run(c, check=True)

SFX = [('whoosh_fast/crisp', a, 0.131, -12) for a in (3.8, 7.3, 11.35, 15.0, 22.3, 25.35, 27.7)]
SFX += [
    ('downlifter/tape', 1.30, 0.103, -9), ('cut_hit/sub', 1.35, 0.021, -8), ('cut_hit/punch', 1.56, 0.058, -9),
    ('pop/2', 3.95, 0.009, -13), ('click/thock', 4.27, 0.004, -12), ('pop/2', 4.95, 0.009, -13), ('click/thock', 5.09, 0.004, -12),
    ('pop/2', 6.0, 0.009, -13), ('cut_hit/kick', 6.68, 0.013, -9),
    ('cut_hit/punch', 7.77, 0.058, -10), ('pop/4', 8.25, 0.004, -11), ('ui_pop/blip', 9.0, 0.017, -12), ('ui_pop/soft', 10.15, 0.042, -11),
    ('fit/pop/lip_pop', 10.5, 0.009, -10),
    ('fit/hit/bamboo_tok', 11.8, 0.011, -10), ('riser/snatch', 13.0, 0.386, -14), ('whoosh_fast/tight', 13.5, 0.162, -13),
    ('impact/punch', 14.5, 0.066, -13),
    ('ui_pop/soft', 15.2, 0.042, -12), ('pop/2', 15.5, 0.009, -13), ('cut_hit/kick', 17.82, 0.013, -9),
    ('riser/swell', 19.0, 2.192, -20),
    ('ui_pop/wide', 20.6, 0.044, -11), ('notify/mid_tine', 20.62, 0.038, -16),
    ('cut_hit/punch', 22.6, 0.058, -11), ('cut_hit/sub', 24.45, 0.021, -10), ('pop/4', 24.5, 0.004, -12),
    ('fit/snap/switch_flip', 25.55, 0.035, -8), ('cut_hit/punch', 25.95, 0.058, -10),
    ('pop/4', 27.95, 0.004, -11), ('pop/2', 29.3, 0.009, -12), ('swish/soft', 30.35, 0.110, -13),
    ('notify/m5', 31.4, 0.004, -15), ('logo_sting/whoosh_glass', 31.75, 0.201, -13),
]
SFX += [('click/thock', 19.1 + i * 0.14 + 0.2, 0.004, -15) for i in range(6)]
SFX += [('hover_tick/ping', 23.2 + i * 0.25 + 0.1, 0.004, -16) for i in range(5)]
SFX += [('fit/key/lubed', 30.95 + 0.08 * k, 0.075, -16) for k in range(5)]
os.makedirs('sfx', exist_ok=True)
ins, flt = [], []
for k, (sid, t, pk, db) in enumerate(SFX):
    p = f"sfx/{sid.replace('/', '_')}.wav"
    if not os.path.exists(p): run([SFXBIN, 'sfx', 'render', sid, '-o', p, '--sr', '48000'])
    ins += ['-i', p]; ms = max(0, int((t - pk) * 1000))
    flt.append(f'[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n = len(SFX)
mix = (f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,apad[vo];"
       f"[1:a]atrim=start=20:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
       f"equalizer=f=250:t=q:w=1:g=-4,equalizer=f=2500:t=q:w=1:g=-4,volume=-16dB,afade=t=in:d=0.4,afade=t=out:st={TOTAL-0.9}:d=0.9[mu];"
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
     '-movflags', '+faststart', '-t', str(TOTAL), 'panelbek_02_svet_illyustratsiya.mp4'])
print('TAYYOR')
