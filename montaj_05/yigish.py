import subprocess, os, numpy as np, soundfile as sf
os.chdir(os.path.dirname(os.path.abspath(__file__)))
EAR=os.path.expanduser('~/earshot-venv/bin/earshot'); TOTAL=17.0
S=[('whoosh_big/swell',3.5,-16),('cut_hit/kick',3.5,-17),('whoosh_big/swell',7.0,-15),('riser/build',7.0,-19),('cut_hit/sub',7.05,-15)]
S+=[('mallet/glock',t,-17) for t in (0.55,3.95,7.65,10.55,13.05)]
S+=[('cut_hit/sub',15.0,-12),('mallet/flourish',15.05,-16),('reverse_swell/cymbal',14.95,-19)]
os.makedirs('sfx',exist_ok=True); ins=[]; flt=[]
for k,(sid,t,db) in enumerate(S):
    p=f"sfx/{sid.replace('/','_')}.wav"
    if not os.path.exists(p): subprocess.run([EAR,'sfx','render',sid,'-o',p,'--sr','48000'],check=True,capture_output=True)
    y,sr=sf.read(p); y=y if y.ndim==1 else y.mean(1)
    pk=len(y)/sr if ('swell' in sid or 'riser' in sid) else int(np.argmax(abs(y)))/sr
    ms=max(0,int((t-pk)*1000)); ins+=['-i',p]
    flt.append(f'[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n=len(S)
fc=(f"[1:a]atrim=start=85:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,volume=-4dB,afade=t=in:d=0.6,afade=t=out:st={TOTAL-1.2}:d=1.2[m];"
    +';'.join(flt)+';'+''.join(f'[s{k}]' for k in range(n))+f"amix=inputs={n}:normalize=0[fx];[m][fx]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5,atrim=duration={TOTAL}[a];"
    f"[0:v]fps=25,scale=1080:1920:flags=lanczos,tpad=stop_mode=clone:stop_duration=1.2,trim=duration={TOTAL}[bg];[bg][2:v]overlay=format=auto,format=yuv420p[v]")
# 0: kadrlar, 1: musiqa, keyin SFX; yozuv qatlami oxirida
cmd=['ffmpeg','-v','error','-y','-framerate','25','-i','blender/frames/f_%04d.png','-i',os.path.expanduser('~/montaj-musiqa/mixkit_music_676.mp3')]+ins+['-i','yozuv.mov']
fc=fc.replace('[2:v]',f'[{n+2}:v]')
subprocess.run(cmd+['-filter_complex',fc,'-map','[v]','-map','[a]','-c:v','libx264','-crf','17','-preset','slow','-c:a','aac','-b:a','256k','-movflags','+faststart','Ronma_Skymax.mp4'],check=True)
print('OK')
