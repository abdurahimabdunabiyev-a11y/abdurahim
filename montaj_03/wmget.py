import hashlib, urllib.request, sys, time
UA={'User-Agent':'Mozilla/5.0 (compatible; edu-video-bot/1.0)'}
for n in sys.argv[1:]:
    h=hashlib.md5(n.encode()).hexdigest()
    u=f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{n}/1200px-{n}"
    for k in range(6):
        try:
            d=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read(); open('foto/wm/'+n,'wb').write(d); print('OK',n,len(d)); break
        except Exception as e:
            c=getattr(e,'code',e)
            if c==404 or c==400:
                u=f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{n}"; continue
            print('retry',n,c); time.sleep(25)
    time.sleep(22)
