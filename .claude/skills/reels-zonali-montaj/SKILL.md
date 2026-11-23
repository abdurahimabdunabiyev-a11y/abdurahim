---
name: reels-zonali-montaj
description: Mustafoning vertikal reels (1080x1920) montaji After Effects'da ZONALI tartib bilan — Instagram safe zona, sarlavha/vizual/caption zonalari, sahna kompozitsiyalari, avtomatik maket tekshiruvi, brend ranglar (sariq, to'q sariq, qora, oq) va SF Pro Display. "reels montaj qil", "zonali montaj", "grid bilan montaj", "ovoz va b-roll bor, video qil" deyilganda ishlating.
---

# Reels zonali montaj (AE)

Foydalanuvchi bergan: ovoz (ElevenLabs mp3) + ssenariy + b-roll (video/rasm) + musiqa + (ixtiyoriy) uslub referensi.
Natija: `00 MAIN` + har sahna alohida kompozitsiya + `CAPTIONS`, guide qatlamlar, avtomatik tekshiruv, render (ovoz+musiqa bilan).

## QAT'IY QOIDALAR (foydalanuvchi fikrlaridan)
1. **Ranglar — shaxsiy brend:** sariq `#FFB81C`, to'q sariq `#F05A1A`, qora `#0B0B0B`, oq. Urg'u so'z = sariq→to'q sariq GRADIENT (Ramp + alpha matte, `gradText`). Fon oq (yumshoq deraza soyasi). **Grid/referens "tartib"ni olishni so'rasa, RANGNI O'ZGARTIRMA** — faqat joylashuv tizimini ol (bir marta shu xato bo'lgan: namunadagi ko'k ranglarni qo'yib yuborgandim).
2. **Shrift:** faqat SF Pro Display (`SFProDisplay-Bold` sarlavha, `-Semibold` kicker/kichik). Heavy faqat italic bor. UPPERCASE emas — gap kabi katta-kichik harf. Bitta oila.
3. **Zonalar** (pastda) — matn/kartalar o'z zonasidan chiqmasin, bir-birining ustiga tushmasin. Builder `runChecks()` 0 muammo bergunicha ko'rsatma.
4. **Faqat grid:** namunaviy grid tizimi: chap hoshiya x=70, tepa o'ngda logo zonasi, kicker→sarlavha chapga tekislangan, vizual markazda, caption y≈1500 qalin qora oddiy matn.
5. Foydalanuvchi aytmasa render qilishdan oldin ko'rsatma — har safar so'ra yoki loyiha kontekstidan bil.
6. Tarjima/matn: ssenariyni foydalanuvchi bergan holda ishlat; o'zbek lotin, apostrof `'` (ASCII).

## Zonalar (1080x1920) — `reference/zonalar.md` ga qarang
- Umumiy xavfsiz (qizil guide): x 70–1010, y 250–1560
- Kontent (yashil): y 250–1380
- KICKER y=330 (kulrang 50%, chapda x=70, kenglik ≤740 — logo zonasi bilan to'qnashmasin)
- TITLE A y≈460 (qora, 128 px) / B y≈605 (gradient) — sarlavha zonasi y 250–690
- VIZUAL zona y 700–1380: kartalar 880x680 (markaz y=1040), qatorlar, doiralar
- CAPTION y=1500 (Bold 56, qora, kengligi ≤700, markazda)
- LOGO zonasi x 820–1010, y 260–360 — BO'SH (foydalanuvchi logosi kerak bo'lsa shu yerga)
- Instagram tugmalari: x>890 va y>956 — MATN kirmasin (rasm/klip bleed bo'lishi mumkin)
- Profil grid 3:4 → markazdan 1080x1440 (y 240–1680) kesadi — muhim narsa shu ichida.

## Ish tartibi
1. **Ovoz vaqtlari:** `ffmpeg` bilan 16 kHz wav, faster-whisper (`small`, `language=uz`, `word_timestamps=True`) — matn buzuq chiqadi, lekin SO'Z VAQTLARI yaxshi. Ssenariy jumlalari bo'yicha `scripts/gen_timing.py` (jumla boshlanishi = whisper vaqti, kenglik = belgilar soniga proporsional) → `timing.js` (`SENTS`, `SUBS`). **venv'ni exFAT diskda (tashqi fleshka) YARATMA** (`._*.pth` buzadi) — scratchpad/ichki diskda yarat.
2. **B-roll tahlili:** har bir fayldan `ffmpeg fps=1/3,tile` kontakt varaq → ko'rib chiq. Fayl nomi ko'pincha ishonchsiz (Klickpin nomlari mazmunga mos kelmaydi) — mazmunni ko'rib aniqla.
3. **Sahna rejasi:** jumla/bo'lak → sahna (kicker + A + B + vizual). Har sahnada bitta g'oya. Qorong'i klip ham KARTA ichida (vizual zonada), butun ekran emas.
4. **Builder:** `templates/build_template.jsx` ni nusxalab o'zgartir (`$.evalFile` bilan `lib/lib_zonali.jsx` ni ulaydi). Avval `runScene(nom, t0, t1, fn)` — absolyut vaqtlar. Yordamchilar: `kicker/lineA/lineB/titleBlock`, `gradText`, `clipCard(item,cx,cy,w,h,r,t0,t1,scale,sx,sy)` (manba nuqtasi kartaning markaziga), `chip`, `pill`, `strike`, `plane`, `ellipseShape`, `shapeRect`, `shadow`, `popIn/slamIn/riseIn/kf`.
5. **Ovoz:** `scripts/mix_audio.sh` → `audio_mix.wav` (ovoz + musiqa -14 dB, ducking). MAIN ichiga qo'sh — aerender AAC bilan chiqaradi.
6. **Ishga tushirish:** `scripts/run_ae.sh <builder.jsx> <log>` (bridge paneli shart emas). Log oxirida `TEKSHIRUV: N element, 0 muammo` bo'lishi kerak.
7. **Render:** `scripts/render.sh <aep> "00 MAIN" <mp4>` (~1 daqiqa). Keyin `scripts/review_sheet.py` bilan 32 kadrli varaq → ko'zda tekshir (zonalar, ustma-ust, gradient, kartalar).
8. Foydalanuvchiga: faylni yubor + nima tekshirilmaganini ayt (quloq bilan eshitilmagan, subtitr sinxroni ±0.2 s).

## Texnik tuzoqlar
- AE bridge panel ulanmasa ham `osascript ... DoScriptFile` va `aerender` ishlaydi; `check-bridge` muvaffaqiyatsiz bo'lsa vahima qilma.
- Eski `aerendercore` jarayoni osilib qolsa AE sekinlashadi — `pkill -f aerendercore`.
- ExtendScript'da ternary ikkala shoxni ham bajaradi (yon ta'sirli ternary ishlatma). Shape layer default position (0,0) emas — doim `position.setValue`. `layer.parent=` dan keyin child `position`ni qayta o'rnat. Text uchun anchor = `sourceRectAtTime` markazi/chap-markazi; matn kengligi `maxW` bilan avtomatik kichraytiriladi (SF Bold ≈0.55 em/belgi).
- `clipCard` — null ctrl + mask + parent: pop animatsiya oynani siljitmaydi. Oynaning kengligi/balandligi ekran pikselida beriladi.
- `gradText` — Ramp qattiq solid + alpha track matte; child'larning opacity'si ctrl'dan meros olinmaydi → fadeIn/Out'ni ikkalasiga ber.
- Mosseri kabi manba videolarda yoqilgan subtitr bo'ladi — karta oynasini subtitrdan yuqorida kesib ol (y 100–624 / 720x1280).
- Render AE'dan to'g'ri chiqadi; ffmpeg faqat audio mix uchun.

## Fayllar
- `lib/lib_zonali.jsx` — kutubxona (zonalar, helperlar, guide qatlamlar, REG tekshiruv)
- `templates/build_template.jsx` — Instagram algoritm reels uchun to'liq namuna (15 sahna)
- `scripts/` — `gen_timing.py`, `run_ae.sh`, `render.sh`, `mix_audio.sh`, `review_sheet.py`
- `reference/zonalar.md` — Instagram safe zona sxemasi raqamlari va namunaviy grid o'lchamlari; `white_bg.png` — fon
