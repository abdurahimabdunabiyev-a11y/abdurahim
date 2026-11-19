import subprocess, os, numpy as np, soundfile as sf
os.chdir(os.path.dirname(os.path.abspath(__file__)))
EAR=os.path.expanduser('~/earshot-venv/bin/earshot')
S=[('cut_hit/sub',0.02,-14),('whoosh_big/swell',0.32,-17),('ui_pop/wide',0.3,-19)]
def letters(t,n,per,ids=('drip/bubble','ui_pop/blip')): return [(ids[k%2], t+k*per+0.02, -25) for k in range(n)]
S+=letters(.25,4,.03)+letters(.35,7,.07)+letters(1.1,3,.03)+letters(1.5,7,.07)
S+=[('ui_pop/soft',2.02,-20),('whoosh_fast/whip',2.3,-16),('notify/mid_tine',2.42,-21),('cut_hit/kick',2.42,-18)]
for n,t in [('LONGi',2.39),('Jinko',3.08),('ERA',3.68),('Ronma',4.0),('Deye',5.28)]: S+=letters(t,len(n),.05)+[('swish/flick',t,-23)]
S+=[('ui_pop/soft',4.3,-22),('ui_pop/wide',5.65,-20)]
ins=[]; flt=[]
for k,(sid,t,db) in enumerate(S):
    p=f"../sfx/{sid.replace('/','_')}.wav"
    if not os.path.exists(p): subprocess.run([EAR,'sfx','render',sid,'-o',p,'--sr','48000'],check=True,capture_output=True)
    y,sr=sf.read(p); y=y if y.ndim==1 else y.mean(1); pk=len(y)/sr if 'swell' in sid else int(np.argmax(abs(y)))/sr
    ms=max(0,int((t-pk)*1000)); ins+=['-i',p]
    flt.append(f'[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{k}]')
n=len(S); M=os.path.expanduser('~/montaj-musiqa/mixkit_music_729.mp3')
fc=(f"[0:a]atrim=0:6.5,aformat=sample_rates=48000:channel_layouts=stereo,apad[vo];[1:a]atrim=start=8:duration=6.5,asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
    f"equalizer=f=250:t=q:w=1:g=-4,equalizer=f=2500:t=q:w=1:g=-5,volume=-18dB,afade=t=in:d=0.2,afade=t=out:st=5.9:d=0.6[mu];"+';'.join(flt)+';'+''.join(f'[s{k}]' for k in range(n))+f"amix=inputs={n}:normalize=0[fx];"
    "[vo]asplit[a][b];[mu][b]sidechaincompress=threshold=0.04:ratio=4:attack=15:release=300[md];[a][md][fx]amix=inputs=3:normalize=0,atrim=duration=6.5,loudnorm=I=-14:TP=-1.5[mx]")
subprocess.run(['ffmpeg','-v','error','-y','-i','../kes/talk_sync.wav','-i',M]+ins+['-filter_complex',fc,'-map','[mx]','-ar','48000','mix.wav'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','video.mp4','-i','mix.wav','-map','0:v','-map','1:a','-c:v','libx264','-crf','18','-preset','slow','-c:a','aac','-b:a','256k','-movflags','+faststart','-shortest','Demo_uslub_Claude.mp4'],check=True)
print('OK',n)
