import subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = '../montaj_08_tanlov/sfx/'; TOTAL = 35.5
# (fayl, vaqt s, dB) — faqat grafika paydo bo'lganda (Akmal: yumshoq bubble pop), doska yozuvida klaviatura, kesimlar jim
S = [('pop-2359.mp3', t, -24) for t in (2.70, 8.30, 9.45, 16.70, 17.40, 17.88, 20.62, 21.38, 22.46, 23.78, 25.70, 28.05, 29.56, 30.18, 30.84)]
S += [(T+'click-1133.mp3', 15.96 + i * .07, -30) for i in range(7)]
S += [(T+'m1489.mp3', 20.45, -22), (T+'m1491.mp3', 15.90, -24), (T+'m1491.mp3', 24.98, -24)]
ins, fl = [], []
for k, (f, t, db) in enumerate(S):
    ins += ['-i', f]; ms = int(t * 1000)
    fl.append(f'[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n = len(S)
fc = (f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo[vo];[1:a]atrim=start=4:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,volume=-10dB,volume='if(between(t\,15.55\,15.95)\,0.25\,1)':eval=frame,afade=t=in:d=0.3,afade=t=out:st={TOTAL-1}:d=1[mu];"
      + ';'.join(fl) + ';' + ''.join(f'[s{k}]' for k in range(n)) + f'amix=inputs={n}:normalize=0[fx];'
      f"[vo]asplit[a][b];[mu][b]sidechaincompress=threshold=0.05:ratio=3:attack=20:release=250[md];[a][md][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5,atrim=duration={TOTAL}[x]")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'ovoz.wav', '-i', os.path.expanduser('~/montaj-musiqa/mixkit_music_872.mp3')] + ins + ['-filter_complex', fc, '-map', '[x]', '-ar', '48000', 'mix.wav'], check=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'video.mp4', '-i', 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', '-shortest', 'Xitoy_safari_Akmal_uslubi.mp4'], check=True)
print('OK')
