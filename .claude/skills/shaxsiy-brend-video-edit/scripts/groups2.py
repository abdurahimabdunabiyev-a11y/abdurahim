import json, re
G = """|Biznesingiz|uchun
alohida|target,|
|dizayner,|
yoki|SMM|yollashga
|byudjetingiz|yetmayaptimi?
Unda shuncha|odamga|pul to'lab
yollash|shart emas-ku.|
Bitta|odam|o'zi AI yordamida
|5 kishining|ishini
bemalol|qila oladi.|
Masalan,|g'oyalarni|
|[ChatGPT'da,]|
puxta|tekstni [Claude'da]|yozdirasiz,
dizayn va|vizualni|[Nano Banana Pro]
yoki [Flux'da]|tayyorlaysiz.|
Bu orqali|oyiga|
|[millionlab so'm] pulingizni|
|tejab qolasiz.|
O'zimdan|misol:|
|brend ham,|
|kontent ham,|
|reklama ham —|
|komandasiz,|
bitta|o'zim|yuritaman.
Buni o'z|blogimda|sizlarga
|bepul|o'rgatmoqchiman.
Menga|obuna|bo'ling va
kommentda|eng ko'p|
|qiziqtirgan|yo'nalishni
yozib|qoldiring,|
keyingi|video|
aynan shu|haqda|bo'ladi.""".split("\n")
words = json.load(open("src/words_fixed.json"))
i = 0
full, shown = [], []
for line in G:
    pre, hero, post = line.split("|")
    parts_all, parts_shown = [], []
    for kind, txt in (("pre", pre), ("hero", hero), ("post", post)):
        toks = re.findall(r"\[[^\]]*\]|\S+", txt)
        if not toks: continue
        n = sum(len(t.strip("[]").split()) for t in toks)
        seg = words[i:i+n]
        expect = " ".join(t.strip("[]") for t in toks).split()
        assert [w["w"] for w in seg] == expect, (line, [w["w"] for w in seg], expect)
        # rendered text and its first/last rendered word times
        k = 0; rs = re_ = None; shown_words = []
        for t in toks:
            cnt = len(t.strip("[]").split())
            if not t.startswith("["):
                if rs is None: rs = seg[k]["s"]
                re_ = seg[k + cnt - 1]["e"]
                shown_words.append(t)
            k += cnt
        parts_all.append({"k": kind, "t": " ".join(t.strip("[]") for t in toks), "s": seg[0]["s"], "e": seg[-1]["e"]})
        if shown_words:
            parts_shown.append({"k": kind, "t": " ".join(shown_words), "s": rs, "e": re_})
        i += n
    full.append(parts_all)
    if parts_shown:
        if not any(p["k"] == "hero" for p in parts_shown):
            # promote first part to hero
            parts_shown[0]["k"] = "hero"
        shown.append(parts_shown)
assert i == len(words)
json.dump(full, open("groups_full.json", "w"), ensure_ascii=False)
json.dump(shown, open("groups.json", "w"), ensure_ascii=False)
print(len(full), "full,", len(shown), "shown")
for g in shown:
    print(" | ".join(f"{p['k']}:{p['t']}" for p in g), round(g[0]["s"], 2))
