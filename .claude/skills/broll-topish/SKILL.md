---
name: broll-topish
description: Montaj uchun haqiqiy (AI emas) kinematografik B-roll videolarni Mixkit'dan qidirib, tanlab, yuklab olish va 9:16 ga moslash. Xom videoga B-roll kerak bo'lganda, "B-roll top", "qo'shimcha kadr qo'y", "stok video" deyilganda yoki montaj planida B-roll ustuni to'ldirilayotganda ishlat.
---

# B-roll topish (haqiqiy kino kadrlar)

Foydalanuvchi talabi: **B-roll faqat haqiqiy, jonli suratga olingan kinematografik kadrlardan bo'ladi. AI yaratgan kadr ishlatilmaydi.**

Manba: **Mixkit** — bepul, kalitsiz, professional suratga olingan stok videolar
(Mixkit Free License: videolarda, shu jumladan tijorat maqsadida ishlatish mumkin).
Pexels yangi API kalit berishni to'xtatgan (2026-11), shuning uchun hozircha ishlatilmaydi.

## Qoidalar

1. **AI kadr yo'q.** AI ko'rinishidagi kadr (g'ayritabiiy qo'llar, "suzuvchi" teksturalar, haddan tashqari silliq yuzlar) bo'lsa — tashla.
2. **Har bir B-roll gapni kuchaytiradi.** Transkriptdan gapni ol, so'zma-so'z emas, *ma'noni* ko'rsatadigan kadr izla.
   - "Pul topish / daromad" → `counting money`, `money falling`, `cash`
   - "Vaqt / kech qolish" → `clock`, `city timelapse`, `hourglass`
   - "Charchoq / qiyinchilik" → `tired man`, `walking alone`, `rain window`
   - "Muvaffaqiyat / biznes" → `businessman`, `office meeting`, `city skyline`
   - "Kitob / o'qish" → `reading book`, `library`
   - "Erta turish / intizom" → `alarm clock`, `morning run`, `sunrise`
3. **So'rovlar inglizcha, 1–3 so'z** (Mixkit kategoriya sahifalari bo'yicha qidiradi). Natija kam bo'lsa, sinonim bilan qayta qidir yoki `--page 2`.
4. **Uslub:** referenslardagi kabi qorong'iroq, iliq, kontrastli, sayoz fokusli (shallow DOF), sekin harakatli kadrlarni afzal ko'r.
5. **Orientatsiya:** Mixkit ko'pincha 16:9. `--vertical` 9:16 ga markazdan kesadi (1080x1920). Muhim obyekt chetda bo'lsa, crop o'rnini qo'lda moslashtir yoki referensdagidek qora polosali "letterbox" qil (V1 uslubi).
6. **Davomiyligi:** bitta B-roll 1.5–4 soniya. Uzun klipdan eng kuchli bo'lagini kes.
7. **Kinofilm parchalari** (Hollywood va h.k.) internetdan yuklab olinmaydi (mualliflik huquqi). Foydalanuvchi o'zi yuborsa — ishlat.
8. **Ko'zdan kechir:** `get` `_sheet.jpg` kontakt-varaq yaratadi — Read bilan ko'rib, gapga mosligini va AI emasligini tekshir.
9. Har bir klip `credits.jsonl` ga yoziladi (manba, havola, litsenziya).

## Buyruqlar

```bash
PY=~/claude-video-kit/.venv/bin/python
SK=.claude/skills/broll-topish/broll.py

$PY $SK search "counting money" --n 10          # id + sarlavha + preview
$PY $SK search "city night" --page 2
$PY $SK get 18296 --out broll/ --vertical        # 1080p yuklab, 9:16 nusxa + kontakt-varaq
```

Kerakli tarmoq manzillari (muhitda ruxsat berilgan): `mixkit.co`, `assets.mixkit.co`.

## Ish tartibi (montajda)

1. Transkriptdan B-roll kerak bo'lgan har bir jumlani belgilab, montaj planidagi B-roll ustuniga yoz.
2. Har bir jumla uchun 2–3 xil so'rov bilan qidir, sarlavhalarga qarab 3–5 nomzodni yuklab, kontakt-varaqni ko'r.
3. Eng mosini tanla, kerakli 1.5–4 soniyalik bo'lagini kes, rangini asosiy videoga moslashtir.
4. Topilmasa yoki mos kelmasa — **taxmin qilib qo'ymagin**, foydalanuvchiga qaysi joyga qanday kadr kerakligini yoz.
