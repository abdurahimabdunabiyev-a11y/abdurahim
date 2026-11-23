#!/usr/bin/env python3
# Ishlatish: review_sheet.py <video.mp4> <chiqish_papka> t1 t2 t3 ...   -> sheet0.png, sheet1.png (har birida 16 kadr, 8x2)
import sys,subprocess,os
v,out=sys.argv[1],sys.argv[2]; ts=sys.argv[3:]
os.makedirs(out,exist_ok=True); fs=[]
for t in ts:
    f=os.path.join(out,"f_%07.2f.png"%float(t)); fs.append(f)
    subprocess.run(["ffmpeg","-v","error","-y","-ss",t,"-i",v,"-frames:v","1","-vf","scale=330:-1",f])
for i in range(0,len(fs),16):
    ch=fs[i:i+16]; n=len(ch)
    args=["ffmpeg","-v","error","-y"]
    for f in ch: args+=["-i",f]
    args+=["-filter_complex","".join("[%d:v]"%k for k in range(n))+"xstack=inputs=%d:layout="%n+"|".join("%d_%d"%((k%8)*330,(k//8)*587) for k in range(n)),"-frames:v","1",os.path.join(out,"sheet%d.png"%(i//16))]
    subprocess.run(args)
print("tayyor:",out)
