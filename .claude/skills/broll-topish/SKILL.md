---
name: broll-topish
description: Montaj uchun haqiqiy (AI emas) kinematografik B-roll videolarni Pexels'dan qidirib, tanlab, yuklab olish. Xom videoga B-roll kerak bo'lganda, "B-roll top", "qo'shimcha kadr qo'y", "stok video" deyilganda yoki montaj planida B-roll ustuni to'ldirilayotganda ishlat.
---

# B-roll topish (haqiqiy kino kadrlar)

Foydalanuvchi talabi: **B-roll faqat haqiqiy, jonli suratga olingan kinematografik kadrlardan bo'ladi. AI yaratgan kadr ishlatilmaydi.**

## Qoidalar

1. **AI kadr yo'q.** Pexels natijalarida AI yaratilgan ko'rinadigan kadr (g'ayritabiiy qo'llar, "suzuvchi" teksturalar, haddan tashqari silliq yuzlar) bo'lsa, tashla.
2. **Har bir B-roll gapni kuchaytiradi.** Avval transkriptdan gapni ol, keyin so'zma-so'z emas, *ma'noni* ko'rsatadigan kadr izla.
   - "Pul topish" → `counting money hands close up`, `cash dollars slow motion`
   - "Kech qolish / vaqt" → `clock ticking close up`, `city timelapse night`
   - "Charchoq / qiyinchilik" → `man tired desk night`, `walking alone foggy forest`
   - "Muvaffaqiyat" → `businessman walking city sunset`, `man looking at skyline`
3. **Uslub so'zlari:** so'rovga kerak bo'lsa `cinematic`, `moody`, `slow motion`, `close up`, `shallow depth of field`, `golden hour`, `night` qo'sh. Referenslardagi kabi qorong'iroq, iliq, kontrastli kadrlarni afzal ko'r.
4. **Orientatsiya:** avval `portrait` (9:16). Yetarli bo'lmasa `landscape` olib, 9:16 ga markazdan kes (crop) yoki referensdagidek qora polosali "letterbox" qil.
5. **Davomiyligi:** referenslarda bitta B-roll 1.5–4 soniya turadi. Uzun klipdan eng yaxshi bo'lagini kes.
6. **So'rovlar inglizcha** yoziladi (Pexels inglizchani yaxshi tushunadi).
7. **Kinofilm parchalari** (Hollywood va boshqalar) — internetdan yuklab olinmaydi (mualliflik huquqi). Agar foydalanuvchi o'zi film parchasini yuborsa, uni ishlat.
8. **Ko'zdan kechir:** `get` buyrug'i `_sheet.jpg` kontakt-varaq yaratadi — uni Read bilan ko'rib, kadr gapga mosligini va AI emasligini tekshir.
9. Har bir yuklab olingan klip `credits.jsonl` ga yoziladi (muallif, havola, litsenziya).

## Buyruqlar

```bash
PY=~/claude-video-kit/.venv/bin/python
SK=.claude/skills/broll-topish/broll.py

# qidirish (natija: id, davomiylik, o'lcham, muallif)
$PY $SK search "man counting money cinematic" --n 8
$PY $SK search "city night timelapse" --orientation landscape --min 4 --max 20

# yuklab olish (1080x1920 ga yaqin sifat) + kontakt-varaq
$PY $SK get 1234567 --out broll/
```

## Ish tartibi (montajda)

1. Transkriptdan B-roll kerak bo'lgan har bir jumlani belgilab, montaj planidagi B-roll ustuniga yoz.
2. Har bir jumla uchun 2–3 xil inglizcha so'rov bilan qidir, 3–5 nomzodni yuklab, kontakt-varaqni ko'r.
3. Eng mosini tanla, kerakli 1.5–4 soniyalik bo'lagini kes, rangini asosiy videoga moslashtir.
4. Topilmasa yoki mos kelmasa — **taxmin qilib qo'ymagin**, foydalanuvchiga qaysi joyga qanday kadr kerakligini yoz.

## Kalit (API key)

Pexels bepul API kaliti kerak (https://www.pexels.com/api). U muhitning tarmoq sirlarida (network secret) `api.pexels.com` uchun saqlanadi va proksi avtomatik qo'shadi. Kalit hech qachon chatga yoki faylga yozilmaydi.
