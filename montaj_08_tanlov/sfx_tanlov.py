import subprocess, os
L = [('Whoosh','m1489'),('Whoosh','m1491'),('Whoosh','swoosh-1461'),('Whoosh','swoosh-1465'),('Whoosh','swoosh-1471'),('Whoosh','swoosh-166'),('Whoosh','transition-1490'),('Whoosh','m1492'),
     ('Zarba','impact-2182'),('Zarba','impact-1143'),('Zarba','impact-2198'),('Zarba','impact-2782'),
     ('Pop','m2356'),('Pop','m2364'),('Pop','m2354'),('Pop','click-1109'),
     ('Klik','click-1133'),('Klik','click-275'),('Klik','click-3124'),('Klik','click-900')]
SL = 2.2; F = '/root/.fonts/montaj/ArchivoBlackRegular.ttf'
ins, fc, dt = [], [], []
for k, (cat, n) in enumerate(L):
    ins += ['-i', f'sfx/{n}.mp3']; ms = int(k * SL * 1000 + 250)
    fc.append(f'[{k+1}:a]atrim=0:{SL-0.3},afade=t=out:st={SL-0.6}:d=0.3,aformat=sample_rates=48000:channel_layouts=stereo,loudnorm=I=-18:TP=-2,adelay={ms}|{ms}[s{k}]')
    dt.append(f"drawtext=fontfile={F}:text='{k+1}':fontsize=420:fontcolor=white:x=(w-tw)/2:y=620:enable='between(t,{k*SL},{(k+1)*SL})',drawtext=fontfile={F}:text='{cat}':fontsize=90:fontcolor=0xF6B52F:x=(w-tw)/2:y=1150:enable='between(t,{k*SL},{(k+1)*SL})'")
n = len(L); T = n * SL
fc.append(''.join(f'[s{k}]' for k in range(n)) + f'amix=inputs={n}:normalize=0,atrim=0:{T}[a]')
fc.append('[0:v]' + ','.join(dt) + '[v]')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'color=c=0x0B0B0B:s=1080x1920:r=30:d={T}'] + ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', 'SFX_tanlov.mp4'], check=True)
print('OK', T)
