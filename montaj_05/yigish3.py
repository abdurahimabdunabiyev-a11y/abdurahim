"""3 variantni yig'ish: Blender kadrlari (+ quyosh variantida haqiqiy quyosh botishi foni) + logo kartasi + musiqa + SFX.
Ishlatish: python yigish3.py [oltin oq quyosh]"""
import subprocess, os, sys, numpy as np, soundfile as sf
os.chdir(os.path.dirname(os.path.abspath(__file__)))
EAR = os.path.expanduser('~/earshot-venv/bin/earshot'); M = os.path.expanduser('~/montaj-musiqa/')
TOTAL = 11.2
MUSIQA = {'oltin': ('mixkit_music_676.mp3', 85.0), 'oq': ('mixkit_music_1167.mp3', 80.5), 'quyosh': ('mixkit_music_871.mp3', 40.0)}
NOM = {'oltin': 'Ronma_1_oltin_studiya.mp4', 'oq': 'Ronma_2_oq_showroom.mp4', 'quyosh': 'Ronma_3_quyosh_botishi.mp4'}
S = [('mallet/glock', .35, -18), ('whoosh_big/swell', 3.0, -16), ('cut_hit/kick', 3.0, -18), ('whoosh_big/swell', 6.0, -15), ('cut_hit/sub', 6.05, -15),
     ('reverse_swell/cymbal', 9.45, -19), ('cut_hit/sub', 9.5, -12), ('mallet/flourish', 9.55, -16)]
def sfx_inputs(base):
    ins, flt = [], []
    for k, (sid, t, db) in enumerate(S):
        p = f"sfx/{sid.replace('/', '_')}.wav"
        if not os.path.exists(p): subprocess.run([EAR, 'sfx', 'render', sid, '-o', p, '--sr', '48000'], check=True, capture_output=True)
        y, sr = sf.read(p); y = y if y.ndim == 1 else y.mean(1)
        pk = len(y) / sr if ('swell' in sid or 'riser' in sid) else int(np.argmax(abs(y))) / sr
        ms = max(0, int((t - pk) * 1000)); ins += ['-i', p]
        flt.append(f'[{k + base}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
    return ins, flt
for v in (sys.argv[1:] or ['oltin', 'oq', 'quyosh']):
    mf, mst = MUSIQA[v]
    ins = ['-framerate', '25', '-i', f'blender/frames_{v}/f_%04d.png', '-i', 'yakun.mov', '-i', M + mf]
    base = 3
    if v == 'quyosh':
        ins += ['-stream_loop', '-1', '-ss', '2', '-i', '../montaj_04/broll_panel_zavod/mixkit_46623_9x16.mp4']; base = 4
        bg = (f"[3:v]fps=25,scale=1080:1920,gblur=sigma=14,eq=brightness=-0.06:saturation=1.15,trim=duration={TOTAL},setpts=PTS-STARTPTS[pl];"
              f"[0:v]fps=25,scale=1080:1920:flags=lanczos,tpad=stop_mode=clone:stop_duration=1.2,trim=duration={TOTAL}[p3];[pl][p3]overlay=format=auto[bgv];")
    else:
        bg = f"[0:v]fps=25,scale=1080:1920:flags=lanczos,tpad=stop_mode=clone:stop_duration=1.2,trim=duration={TOTAL}[bgv];"
    si, flt = sfx_inputs(base); n = len(S)
    fc = (bg + "[bgv][1:v]overlay=format=auto,format=yuv420p[v];"
          f"[2:a]atrim=start={mst}:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:d=0.5,afade=t=out:st={TOTAL - 1.3}:d=1.3[m];"
          + ';'.join(flt) + ';' + ''.join(f'[s{k}]' for k in range(n)) + f"amix=inputs={n}:normalize=0[fx];[m][fx]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5,atrim=duration={TOTAL}[a]")
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + si + ['-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow',
                    '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', '-t', str(TOTAL), NOM[v]], check=True)
    print('OK', NOM[v])
