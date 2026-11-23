import json, re
W = json.load(open('an/words.json'))
# (start, matn)  -- start = whisper bo'yicha gap boshlanishi
S = [
 (0.00,"Instagramda rekka chiqish uchun videoni oxirigacha ko'rishlari shart deb o'ylaysizmi?"),
 (5.28,"Adashasiz!"),
 (6.34,"Instagram rahbari algoritmning haqiqiy sirini ochdi!"),
 (10.04,"Adam Mosserining aytishicha, hozir hatto noldan ochilgan yangi profil ham bitta video bilan millionlab prosmotr olishi mumkin"),
 (18.62,"faqat bitta ko'rsatkichni to'g'ri ishlatsangiz bas."),
 (21.90,"Ko'pchilik layk va komment yig'ishga harakat qiladi."),
 (25.38,"Lekin Instagram boshqa platformalarga qaraganda videoni ko'rish vaqtiga kamroq e'tibor beradi."),
 (31.30,"Uning o'rniga uchta narsani tekshiradi: birinchisi originallik,"),
 (35.54,"ikkinchisi esa mavzuning bugungi kunda qanchalik dolzarbligi."),
 (39.48,"Lekin sizga obuna bo'lmagan begona odamlarga chiqish uchun"),
 (43.62,"eng asosiy uchinchi signal bor"),
 (45.86,"va u layk ham, prosmotr ham emas!"),
 (48.70,"Bu Sends per reach, ya'ni videoni ko'rgan odamlardan nechtasi uni do'stiga yuborgani!"),
 (52.80,"Odamlar videongizni samolyotcha orqali tanishiga jo'natsa, algoritm buni eng qiziq kontent deb hisoblaydi va yangi auditoriyaga portlatib chiqaradi."),
 (61.16,"Xo'sh, odamlar videongizni shunchaki ko'rib ketmasdan, do'stiga yuborishi uchun nima qilish kerak?"),
 (67.54,"Videongizda odam o'zining do'stini, hamkasbini yoki mijozini taniydigan hayotiy og'riqni ko'rsating"),
 (73.44,"va video oxirida Buni aniq shu holatdagi tanishingizga yuboring deb ayting."),
 (78.12,"Reels olaman lekin prosmotr chiqmayapti deydigan tanishingizga shu videoni hoziroq yuborib qo'ying"),
 (84.06,"va shunday foydali marketing bilimlari uchun sahifamga obuna bo'ling!"),
]
TOTAL = 88.61
sents=[]
for i,(s,t) in enumerate(S):
    nxt = S[i+1][0] if i+1<len(S) else TOTAL
    ws=[w for w in W if w['s']>=s-0.05 and w['s']<nxt-0.05]
    e = ws[-1]['e'] if ws else nxt-0.1
    e = min(e, nxt-0.05)
    sents.append({"s":s,"e":round(e,2),"t":t})
subs=[]
for sn in sents:
    words=sn['t'].split()
    tot=sum(len(w)+1 for w in words)
    span=sn['e']-sn['s']
    pos=0; chunks=[]; cur=[]; curc=0
    for w in words:
        cur.append((w,pos)); curc+=len(w)+1; pos+=len(w)+1
        if curc>=13 or len(cur)>=3:
            chunks.append(cur); cur=[]; curc=0
    if cur:
        if chunks and sum(len(x[0])+1 for x in cur)<7: chunks[-1]+=cur
        else: chunks.append(cur)
    for ch in chunks:
        a=ch[0][1]; b=ch[-1][1]+len(ch[-1][0])+1
        subs.append({"s":round(sn['s']+span*a/tot,2),"e":round(sn['s']+span*b/tot,2),"t":" ".join(x[0] for x in ch)})
# subs ketma-ket, orasini yopish (gap<0.25 -> keyingi boshigacha)
for i in range(len(subs)-1):
    if subs[i+1]['s']-subs[i]['e']<0.3: subs[i]['e']=subs[i+1]['s']
json.dump({"sents":sents,"subs":subs},open('timing.json','w'),ensure_ascii=False,indent=1)
open('timing.js','w').write("var SENTS="+json.dumps(sents,ensure_ascii=False)+";\nvar SUBS="+json.dumps(subs,ensure_ascii=False)+";\n")
print(len(sents),len(subs))
for sn in sents: print(sn['s'],sn['e'])
