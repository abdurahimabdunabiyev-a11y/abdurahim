import subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T='../montaj_08_tanlov/sfx/'; TOTAL=23.95
S=[(T+'m1491.mp3',0.95,-27),(T+'m1491.mp3',10.7,-27),(T+'m1489.mp3',12.82,-28),(T+'m1491.mp3',17.45,-27),
   (T+'impact-2182.mp3',0.02,-24),(T+'impact-2182.mp3',14.82,-25),
   ('../montaj_11/pop-2359.mp3',12.24,-27),('../montaj_11/pop-2359.mp3',18.18,-28),('../montaj_11/pop-2359.mp3',19.7,-27),('../montaj_11/pop-2359.mp3',8.28,-29)]
ins,fl=[],[]
for k,(f,t,db) in enumerate(S):
    ins+=['-i',f]; ms=int(t*1000); fl.append(f'[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n=len(S)
fc=(f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo[vo];[1:a]atrim=start=30:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,volume=-9dB,afade=t=in:d=0.4,afade=t=out:st={TOTAL-0.8}:d=0.8[mu];"
    +';'.join(fl)+';'+''.join(f'[s{k}]' for k in range(n))+f'amix=inputs={n}:normalize=0[fx];'
    f"[vo]asplit[a][b];[mu][b]sidechaincompress=threshold=0.04:ratio=4:attack=20:release=300[md];[a][md][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5,atrim=duration={TOTAL}[x]")
subprocess.run(['ffmpeg','-v','error','-y','-i','ovoz.wav','-i',os.path.expanduser('~/montaj-musiqa/mixkit_music_175.mp3')]+ins+['-filter_complex',fc,'-map','[x]','-ar','48000','mix.wav'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','video.mp4','-i','mix.wav','-map','0:v','-map','1:a','-c:v','libx264','-crf','17','-preset','slow','-c:a','aac','-b:a','256k','-movflags','+faststart','-shortest','Sinov_uy_narxi.mp4'],check=True)
print('OK')
