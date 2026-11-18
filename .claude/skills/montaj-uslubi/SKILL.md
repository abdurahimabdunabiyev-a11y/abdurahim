---
name: montaj-uslubi
description: Foydalanuvchining shaxsiy video montaj uslubi (Instagram reels, o'zbek tilida ekspert/podkast videolar) va xom videoni shu uslubda montaj qilish tartibi. Foydalanuvchi xom video yuborganda, "montaj qil", "reels qil", "subtitr qo'sh", "montaj plani tuz" deganda, yoki yangi referens video yuborib "o'rgan" deganda ALBATTA ishlat.
---

> **Foydalanuvchi tasdiqlagan YO'NALISH (2026-11-17):** uslub — **@birfoiz tushuntiruvchi illyustratsiya** (references/referens_birfoiz.md).
> **Real foto/video va real ko'rinishli AI rasm ISHLATILMAYDI** — faqat chizilgan illyustratsiya (qog'oz fon, yirtiq qog'oz, oq konturli stikerlar, yorliqlar, shtamplar).
> Mavzu B2B (zavod). Premium Solar'da **akkumulyator + invertor bor**. Namuna: `montaj_02/kompozitsiya.html` + `ovoz_mix.py`. Real B-roll'li montaj_01 rad etilgan.

# Montaj uslubi — doimiy qoidalar

Sen foydalanuvchining shaxsiy video editori, motion designeri va sound designerisan.
Foydalanuvchi bilan **o'zbekcha** gaplash. Montajni foydalanuvchi **"boshla"** demaguncha boshlama.

Bu qoidalar 6 ta referens video tahlilidan chiqarilgan (`references/referenslar.md` — soniyama-soniya tahlil).
Yangi referens kelganda: uni ham shu formatda tahlil qil, `referenslar.md` ga qo'sh, takrorlanayotgan elementlarni quyidagi qoidalarga kirit.

## 0. Qat'iy talablar (foydalanuvchidan)

- **B-roll faqat haqiqiy, jonli suratga olingan kinematografik kadrlar. AI kadr ishlatilmaydi.** → `broll-topish` skilini ishlat.
- Referens uslubiga maksimal yaqin bo'l, o'z boshingdan ortiqcha kreativ element qo'shma.
- Har bir effektning maqsadi bo'lsin; bir xil transitionni haddan tashqari ko'p ishlatma.
- Mavjud bo'lmagan B-roll, audio yoki effektni "bor" deb ko'rsatma. Aniqlay olmasang — ayt.
- Montajdan oldin **montaj plani** (6-bo'lim) tuzib, foydalanuvchiga ko'rsat.

## 1. Format

- 1080x1920 (9:16), 30 fps, H.264, AAC 48 kHz. Davomiylik odatda **35–45 s**.
- Yakuniy ovoz: **−14 LUFS integrated**, true peak ≤ −1 dBTP, LRA ≤ 4 LU.

## 2. Kesish (cutting) va ritm

- **Hamma pauzalar, "eee", takrorlar, xato jumlalar kesiladi.** Referenslarda 0.3 s dan uzun pauza deyarli yo'q (6 tadan 5 tasida 0 ta). So'zlar orasida 0.05–0.15 s havo qoldir — nafas kesilgandek eshitilmasin.
- Gap tezligi natijada ~2.5–3 so'z/s chiqadi.
- **Kadr har 1.8–3.5 s da almashadi** (kesish, burchak almashishi, B-roll yoki to'liq ekranli grafika).
- Bitta kamera bo'lsa: keng ↔ **punch-in** (raqamli zoom 115–135%) navbatlashadi; jump cut joyini punch-in bilan yashir. Ikki kamera bo'lsa: keng ↔ o'rta-yaqin.
- Ma'no bo'yicha urg'u jumlasida — yaqin plan; ro'yxat/tushuntirishda — keng plan.
- Kuchli imo-ishora bo'lgan qisqa joyda subtitrsiz yaqin plan qoldirish mumkin (V1 25 s).

## 3. Hook (birinchi 1–3 soniya)

Quyidagilardan biri (referenslarda hammasi bor):
- Katta **sarlavha qutisi** (mavzu nomi, masalan "INTIZOMLI INSONLARNI 4 ODATI") + kuchli kinematografik B-roll yoki uchayotgan pul overlay.
- Shok jumla + katta raqam: "keyingi **50 YILDA**", "**$20.000 dan** quruq qolasiz".
- Tomoshabinga murojaat: "**SIZ** ... bo'lishingiz mumkin".
Birinchi kadr hech qachon statik "salom" bilan boshlanmaydi.

## 4. Subtitrlar (eng muhim imzo)

**Ikki qavatli tizim:**
- **Kalit so'z** — katta, qalin (ekran kengligining ~70–85%, 1080 kenglikda ~90–120 px), ko'pincha 1–2 so'z.
- **Kontekst** — kichik, ingichka (~35–45 px), kalit so'z ostida yoki ustida.
- Har bir jumladan **ma'no urg'usi** bo'lgan so'z(lar) kalit so'z bo'ladi (sonlar, natija, his-tuyg'u).
- **So'zma-so'z sinxron paydo bo'ladi** (har so'z ovoz bilan birga, fade/blur-in 3–5 kadr yoki pastdan 10–20 px siljib).
- Kichik harflar asosiy; sarlavha va raqamli bo'limlar BOSH HARFLAR bilan.
- Bitta ekranda 2–3 qatordan, qatorda ~3–5 so'zdan oshma.
- Joylashuv: keng planda yuqori uchdan birda yoki spikerning ko'krak balandligida; yaqin planda markaz/pastroq; yuzni yopma.
- Matn rangi asosan **oq**, yumshoq soya bilan. Aksentlar:
  - Pul, raqam → **ko'k** (#2D8CFF atrofida) yoki uslub rangi
  - Salbiy so'z ("javob yo'q", "birinchi" urg'u) → **qizil** (#E53935)
  - Tech-uslubda → laym-yashil (#B6F23A) / sariq (#F5E642)
- **Bo'lim yorliqlari** (ro'yxatli videolarda): tepada keng/kengaytirilgan qalin BOSH HARFLAR — "BIRINCHISI", "IKKINCHISI"...
- Sanash/ro'yxat: yorliq-plitkalar ("1", "2" 3D aylanib), ✦ ikonkali ro'yxat, kvadrat qavsdagi almashuvchi so'zlar [ ... ].
- Shriftlar (aniq nomi tasdiqlanmagan — foydalanuvchi fayl bersa o'shani ishlat):
  - Asosiy: geometrik qalin sans (Poppins/Gilroy/SF Pro Display Bold uslubi)
  - Aksent: nafis italik serif (Playfair Display Italic / Instrument Serif uslubi) — "Ular ertaga", "Intizomli"
  - Raqam/sarlavha: tor bosh harflar (Bebas Neue / Oswald uslubi)
  - Bo'lim yorlig'i: keng ekstended (Druk Wide / Archivo Expanded uslubi)

## 4.5 Shriftlar (foydalanuvchining TOP-20 ro'yxati asosida, 2026-11-16)

O'rnatish: `bash .claude/skills/montaj-uslubi/shriftlar/ornat.sh` (setup skriptida avtomatik). Fayllar gitga kirmaydi.
**Nomlash:** har qalinlik alohida oila — `"<Oila> <Qalinlik>"`, masalan `General Sans SemiBold`, `Archivo Expanded Black`, `Anton Regular`, `Instrument Serif Regular Italic`. ASS (`Fontname`) va HTML (`font-family`) da aynan shu nom.
Namuna varag'i: `mashq/scenes/shriftlar.html`. Hammasi o'zbekcha (o', g', «») to'g'ri ko'rsatadi.

| Vazifa | Asosiy | Muqobil |
|---|---|---|
| **Premium subtitr** (kontekst + kalit so'z) | `General Sans SemiBold/Regular` | Satoshi, Manrope, Plus Jakarta Sans |
| **Kuchli hook** (keng, og'ir) | `Archivo Expanded Black` (Druk Wide o'rnida) | Unbounded Black, Clash Display SemiBold |
| **Professional montaj** (toza grotesk) | `Cabinet Grotesk` / `Inter Tight` (Neue Montreal / Neue Haas / Helvetica Now o'rnida) | Instrument Sans, Hanken Grotesk |
| **Katta sarlavha** (tor, baland) | `Anton Regular` | Bebas Neue, Oswald Bold |
| **Zamonaviy / kreativ** | `Space Grotesk Bold` | Syne ExtraBold, Bricolage Grotesque |
| **Editorial / nafis urg'u** (italik 2-qator) | `Instrument Serif Regular Italic` | — |
| **Raqamlar / sanagich** | `Bebas Neue` / `Anton` | Archivo Expanded |
| **Brend yorlig'i** (Premium Solar) | `Michroma` | Archivo Expanded |

Qoidalar: bitta videoda **2 (ko'pi bilan 3) oila** — bitta subtitr + bitta hook/sarlavha (+ ixtiyoriy editorial italik). Gotham o'rnida Montserrat.
**Pullik shriftlar** (Druk Wide, Neue Montreal, Helvetica Now, Gotham, Neue Haas Grotesk) — o'rnatilmagan, litsenziyasiz yuklab olinmaydi; foydalanuvchi sotib olgan faylni yuborsa, `~/.fonts/montaj/` ga shu nomlash bilan o'rnat.

## 5. B-roll

- Videoning **~30–55%** vaqti B-roll yoki to'liq ekranli grafika.
- **Har bir B-roll aytilayotgan gapni ko'rsatadi yoki kuchaytiradi** (pul → pul; "kitob o'qiyman" → kutubxona; "neft tugaydi" → zavod). Bo'sh joyni to'ldirish uchun qo'yilmaydi.
- B-roll odatda jumla boshida kiradi va jumla oxirida spikerga qaytadi; uzunligi 1.5–4 s, bitta jumla ichida 2–3 ta B-roll ketma-ket ham bo'lishi mumkin.
- 16:9 kinematografik klip: 9:16 ga markazdan kes **yoki** qora polosali letterbox (V1 uslubi) — matn polosaga tushadi.
- Uslub: qorong'iroq, iliq/teal-orange, sayoz fokus, sekin harakat, siluetlar, tuman, oltin soat.
- Subtitr B-roll ustida ham davom etadi.
- Spiker aytgan **predmetlar uchun PNG-kesmalar** (mashina, benzin to'pponchasi, quyosh paneli, pul sumkasi) subtitr yonida pop bo'lib chiqadi — kichik, 1–2 s.

## 6. Motion grafika

- Matn animatsiyasi: blur-in, scale 90→100%, pastdan siljish; overshoot (bounce) yengil.
- **Raqam sanagich** (100.000.000 → 200.000.000) — pul/statistika uchun.
- Foto-kartochkalar: yumaloq burchak, ingichka rangli ramka, biroz burilgan holda ustma-ust tushadi.
- Ikonkalar: odam ikonkalari, chat pufakchalari, ✦ yulduzchalar, HUD qavslar, progress chiziqlar.
- O'tishlar: oddiy cut asosiy; vaqti-vaqti bilan **doira wipe**, **flash kadr**, **xromatik aberratsiya glitch**, oq fonli grafik sahnaga o'tish. Bitta videoda 2–3 xil o'tishdan oshma.
- **CTA (oxirgi 3–5 s):** yumaloq avatar + @nik "pill" + "Obuna" tugmasi bosiladi (✓ / "Rahmat"), va/yoki "izohlarda **7** raqamini qoldiring" (ulkan raqam).

## 6.5 O'tishlar va animatsiya (2-to'plam, batafsil: `references/referenslar_2.md`)

**O'tishlar** — asosiysi toza kesish; "katta" o'tish faqat bo'lim almashganda (har 8–15 s), bitta videoda 2–3 xil:
- **Whip-slide** 0.2–0.3 s: yangi kadr yon tomondan, kuchli gorizontal motion-blur, ease-out (+ `whoosh_fast/whip`).
- **Kartaga kichrayish** 0.5–0.7 s: to'liq kadr yumaloq burchakli kartaga kichrayadi (oq/rangli fon), keyin grafik sahna.
- **Karta push/expand** 0.6–0.8 s: kichik video karta chetdan kirib to'liq ekranga kattalashadi.
- **Zoom-blur push-in** 0.3 s: obyektga tez zoom + radial blur → keyingi sahna.
- **Glitch/to'lqin** 0.4–0.5 s: displacement + RGB siljish (kamdan-kam).
- **Defokus → fokus** video boshida; matn chiqishi pastga siljib + blur.

**Animatsiya/grafika arsenali** (mavzuga mos tanla, hammasini birdan emas):
- Kinetik matn: **bosh atrofida yoy (arc) matn**, harf-harf rang to'ldirish, **typewriter + kursor** (oq quti), chizib tashlash, **qo'lda chizilgan doira**, qo'shtirnoqli ko'chirma.
- 3D: muz/shisha/xrom raqam va so'zlar, 3D ikonka kartalar (gradient kvadrat), mahsulot render + callout yorliqlar (01, 02, 03).
- UI: **chat pufakchalari** (2 spiker dialogi), iOS toggle, bildirishnoma stack, qidiruv paneli, tanlov tugmalari, AI/ilova kartalari, REC viewfinder.
- Editorial: Didone serif sarlavha, **tilla italik script** ikkinchi qator, halftone poster, piksel shrift.
- Raqamlar: **rolling sanagich** + orqada ulkan xira raqam, to'q sariq lower bar.
- Atmosfera: chang/uchqun zarralari, spotlight nur.
- Layout: pastki 30% qora gradient + chapga tekislangan matn (N2); 4:5 kadr 9:16 ichida (N8).
- Imo-ishora bilan bog'langan obyekt (qo'ldan uchib chiqadi) — trek qilinadi.
- Asbob: murakkab animatsiyalar **HyperFrames** (HTML→video, GSAP) bilan quriladi; oddiylari ffmpeg/ASS.

## 7. Ovoz dizayni

- **Musiqa foni hech qachon to'xtamaydi**, nutqdan ~12–18 dB past (nutq ~−20 dB, fon ~−30…−36 dB). Bass ko'p musiqada nutq diapazonini (1–4 kHz) EQ bilan bo'shat.
- Kayfiyat: motivatsion/kinematografik — yengil pianino yoki ambient beat; biznes/infografika — zamonaviy ritmik fon. (Janrni foydalanuvchi tasdiqlaydi.)
- **SFX** (taxminiy aniqlangan, kesishlar va grafikalar bilan bir vaqtda):
  - **Whoosh/swoosh** — B-rollga kirish, bo'lim almashishi, katta matn kirishi
  - **Pop/click** — kartochka, ikonka, chat pufakcha, checklist paydo bo'lishi
  - **Tick** — raqam sanagich
  - **Hit/impact** — hook sarlavhasi, flash kadr, katta raqam
  - **Riser** — katta raqam yoki xulosadan oldin
- SFX nutqni bosib ketmasin (nutqdan 6–10 dB past). Zichlik uslubga bog'liq: kino-podkast — kam; infografika/tech — har grafikada.

## 7.5 Ovozni "eshitib" tekshirish — earshot (MAJBURIY)

Men ovozni eshitmayman. Ovoz haqida hech qachon taxmin bilan gapirma — earshot raqamlari bilan gapir.
O'rnatilgan: `~/earshot-venv/bin/earshot` (skill: `.claude/skills/earshot`). `EARSHOT_THREADS=4`.

- **Har bir renderdan keyin:** `earshot critique video.mp4` → verdict (launch-grade / close / needs work) va tuzatishlar ro'yxati. Kamida **launch-grade** bo'lmaguncha foydalanuvchiga yuborma (yoki sababini ayt).
- Batafsil: `earshot timeline video.mp4` (har bir kesishda ovoz bormi), `earshot sheet video.mp4 -o sheet.png` (rasmni ko'r).
- **SFX manbai — earshot bank** (252 ta, mualliflik huquqisiz): `earshot sfx render ID -o x.wav --json` → `onset_s`/`peak_s` bo'yicha joylash: pop/hit onset kesishda (tap −10…−40 ms oldin), whoosh peak kesishdan +37 ms, reverse swell peak +42 ms. Shablon: `shablon_ovoz.py`.
- Musiqa/SFX tanlash: `earshot rank "<tavsif>" papka/`, `earshot describe fayl`.

**REELS PROFILI (asosiy!):** `earshot critique video.mp4 --profile .claude/skills/montaj-uslubi/reels_profile.json` — foydalanuvchining 14 ta referens reels'idan yasalgan (V1–V6, N1–N8). Standart (launch film) profilni emas, SHUNI ishlat. Yangi referens kelganda profilni qayta yasa: `earshot profile <papka> -o reels_profile.json`.
Reels me'yorlari: −14 LUFS, LRA 1.6–3.7, kesishda ovoz ≥ 85%, salient hit 1.4–2.0/s, stereo deyarli mono (normal), oxiri asosiy qismdan past emas.

**2-to'plamdan (N1–N8) ovoz qoidalari** (batafsil: `references/referenslar_2_ovoz.md`):
- Musiqa 3–5 bo'lim, har 6–15 s da trek/janr almashadi (bo'lim almashganda). Janrlar: corporate (boshida), trap, hip-hop bass, techno, funk, glitch hop; vocal chop'li.
- Har bir matn/karta/ikonka paydo bo'lishiga **UI pop** (`ui_pop/*`) — eng ko'p ishlatiladigan effekt.
- Muhim raqam/fakt ostiga **sub drop**; bo'lim boshiga **impact**; o'tishlarga **whip whoosh**; ijobiy urg'uga **pluck/glock**; reveal oldidan **reverse swell** (kam).
- 0.3–0.5 s **stop-down** dramatik pauza uchun; CTA'da musiqa pasaymaydi.

**earshot'dan o'rganilgan qoidalar (2026-11-16, birinchi qoralama):**
- Har bir kesish/B-roll kirishiga ovoz (whoosh, pop, shutter, hit) — ovozsiz kesish ≤ 1 ta.
- Musiqani gap ostida **qattiq sidechain qilma** (daqiqasiga 20+ "stop-down" — professional: 0–9). Statik past daraja; faqat katta hitdan oldin 0.3–0.4 s pasaytir (stop-down), hitda qaytar.
- Kichik effektlar (pop, shutter) −12…−14 dB; salient hit zichligi ≤ 1.7/s.
- SFX'ni chap/o'ngga taqsimla (pan ±0.3…0.8); musiqaga `extrastereo` (stereowiden basni o'ldiradi — ishlatma).
- Hook hiti ostiga `cut_hit/sub` bas qatlami; CTA'ga yakuniy sting (`mallet/flourish`) — oxiri sust bo'lmasin.
- Bassiz musiqa (M2) "thin bottom" beradi — infografika uchun ham bas bor trek afzal.

## 7.55 Azvuchka (o'zbekcha TTS) — OmniVoice (VoiceStudio dvigateli)

- Manba: foydalanuvchi yuborgan t.me/momedov_blog/128 → VoiceStudio (github.com/debpalash/VoiceStudio, AGPL) → dvigateli **k2-fsa/OmniVoice** (600+ til, **o'zbek `uz` — 115 soat o'quv nutqi**, "Northern Uzbek" `uzn` ham bor).
- O'rnatilgan: `~/tts-venv` (CPU torch + `pip install omnivoice`). Model HF'dan birinchi chaqiruvda yuklanadi.
- **Ovoz dizayni** (klonsiz, tavsif bilan):
  `~/tts-venv/bin/omnivoice-infer --text "<matn>" --language uz --instruct "female, young adult" --output out.wav --device cpu`
  (`--instruct` misollar: "male, middle-aged, low pitch", "female, young adult"; `--speed`, `--duration` bilan vaqtga moslash).
- **Klonlash**: `--ref_audio ref.wav --ref_text "<ref matni>"` (3–10 s toza yozuv). ⚠️ Faqat ovoz egasining **roziligi** bilan.
- Tezlik (4 CPU): ~9 s ovoz ≈ 85–100 s (model yuklanishi bilan). Uzun matnni jumlalarga bo'lib yarat.
- **Sifat tekshiruvi (majburiy):** (1) Whisper uz bilan qayta transkripsiya — so'zlar tanilishi kerak; (2) `earshot realness` ≥ 0.77. Sinov 2026-11-17: erkak 0.91, ayol 0.94; ayol ovozi Whisper'da deyarli to'liq tanildi.
- Chiqish 24 kHz mono → montajda `loudnorm` va musiqa ostida miks.

## 7.6 Videoni "ko'rish" — /watch (claude-video plagini)

- Plagin: `watch@claude-video` (github.com/bradautomates/claude-video). Skript: `/root/.claude/plugins/cache/claude-video/watch/*/skills/watch/scripts/watch.py`.
- **local** (sozlangan): `watch.py <video> --question "..." --detail balanced` → vaqt belgili kadrlar; nutq uchun o'zimizning faster-whisper large-v3 (uz) ishlatiladi (watch'ning ASR fallback'i o'chirilgan: `backend none`).
- **gemini** (kalit bo'lsa): Gemini videoni ovozi bilan to'liq ko'radi — referens tahlili va tayyor montajni "tomosha qilib" baholash uchun. Kalit muhit tarmoq sirida (`generativelanguage.googleapis.com`, header `x-goog-api-key`); `~/.config/watch/.env` da `GEMINI_API_KEY=proxy-injected`.
- Instagram/TikTok/YouTube havolalarini yuklab olish bu muhitda ishlamaydi (CDN manzillari dinamik) — videoni foydalanuvchi yuboradi.

## 8. Rang (color grading)

- Bitta videoda barcha kadrlar bir xil kayfiyatda; B-rollni spiker kadriga moslashtir.
- Spiker: iliq teri ohangi, yumshoq-o'rta kontrast, biroz past saturatsiya, chuqur soyalar (kinematografik).
- Kino-uslub: teal-orange, qorong'i; infografika-uslub: toza, oq-ko'k; tech-uslub: zaytun fon + neon aksent.

## 9. Uslub variantlari — **mavzuga qarab o'zing tanla** (foydalanuvchi qarori, 2026-11-16)

Tanlovni montaj planida qisqa asoslab yoz.

| Variant | Referens | Qachon |
|---|---|---|
| A. Kino-podkast | V1, V2, V3 | Motivatsiya, hayotiy maslahat, sotuv |
| B. Infografika | V4, V5 | Biznes, raqamlar, investitsiya |
| C. Tech-HUD | V6 | Shaxsiy brend, marketing, zamonaviy mavzular |

## 9.5 Katta videolarni qabul qilish (4K 60)

Claude ilovasi 30 MB dan katta faylni qabul qilmaydi. Foydalanuvchida App Store/Google Drive yo'q.
Yechim — **"Montaj Yuklash" sahifasi**: https://claude.ai/artifact/J1Emidie83yWqgp1qwL6rm
(manba: `artifacts/video-yuklash.html`, capabilities: assets + db + user).

- Sahifa videoni 15 MB bo'laklarga bo'lib, har birini **base64 matn (`text/plain`)** qilib `assets` ga yuklaydi. (Video bo'lakni `video/mp4` deb yuklab bo'lmaydi — platforma MP4 sarlavhasini tekshirib `unsupported_type` beradi; matnni tekshirmaydi.)
- Har bir video uchun `uploads` kolleksiyasida hujjat: `{name, size, mime, encoding: "base64", status: "uploading"|"done"|"failed", uploaded, chunks: [{id, start, size}]}`.
- **Yig'ish:** `ArtifactData list` (`collection: "uploads"`) → `status == "done"` hujjatni ol → har bir `chunks[i].id` ni `Artifact read` (`url` + `path: <id>`) bilan yuklab ol (`.txt` bo'lib tushadi) → `start` tartibida har birini `base64 -d` qilib birlashtir → hajm `size` ga tengligini va `ffprobe` ochishini tekshir.
- Ishlov berib bo'lgach, foydalanuvchi sahifadagi **"O'chirish"** tugmasi bilan tozalaydi (yoki so'rasa, Claude o'chiradi) — joy (quota) cheklangan.

## 10. Ish tartibi (xom video kelganda)

1. **Ko'rib chiq:** `ffprobe` (o'lcham, fps, ovoz), kontakt-varaqlar (`fps=2,tile`), transkripsiya:
   ```bash
   ~/claude-video-kit/.venv/bin/python  # faster-whisper large-v3, language="uz", word_timestamps=True
   ```
   ⚠️ Whisper o'zbekchani sust taniydi — vaqtlar to'g'ri, matnda xato ko'p. Subtitr matnini **qo'lda tuzat** va foydalanuvchiga tasdiqlatish uchun ko'rsat.
   (PyAV mos kelmaydi — audioni ffmpeg bilan numpy massivga o'qib uzat.)
2. **Eng yaxshi dublni tanla**, pauza/takror/xatolarni belgilab, kesish ro'yxatini tuz.
3. **Hook** tanla (eng kuchli jumla boshiga ko'chirilishi mumkin).
4. **Montaj plani** tuz va foydalanuvchiga ko'rsat:

   | Vaqt | Kadr | Subtitr (kalit / kontekst) | B-roll (so'rov) | SFX | Animatsiya |
   |---|---|---|---|---|---|
   | 00:00 | Yaqin | **50 YILDA** / keyingi | drift smoke | hit | scale-in |

5. Tasdiqdan keyin: B-roll topish (`broll-topish`), kesish (ffmpeg), grafika va subtitrlar (HyperFrames yoki Remotion), ovoz miksi (`loudnorm=I=-14:TP=-1:LRA=4`), rang.
6. Render → kontakt-varaq bilan o'zing tekshir → foydalanuvchiga yubor.
7. Musiqa/SFX fayllari: foydalanuvchi yuborgan kutubxonani ishlat; yo'q bo'lsa HyperFrames `media-use` ichidagi bepul SFX. Topilmasa — ayt.

## 10.5 Brend: Premium Solar

- Instagram: **@premiumsolar.uz** — "Quyosh paneli | Ta'minotchi", O'zbekiston bo'yicha quyosh energetikasi ta'minotchisi (B2B ham). Hamkor brendlar postlarda: LONGi, Deye.
- Logotip: `assets/logo_premium_solar.png` (1536x1024, to'q yashil fon; CTA va intro/outro uchun fonini kesib PNG qil).
- Ranglar (logotipdan o'lchangan):

  | Rol | HEX |
  |---|---|
  | Asosiy fon (to'q yashil) | `#041512` → gradient `#142E28` |
  | Brend yashil (panellar) | `#22674D` |
  | Aksent sariq (quyosh, "SOLAR") | `#F6B52F` / `#FAB42D` |
  | Oq matn | `#F2F1EF` |

- Shrift xarakteri: "PREMIUM" — keng, ekstended geometrik bosh harflar (Michroma / Syncopate / Eurostile Extended uslubi); "SOLAR" — ingichka, keng harf oralig'i bilan. Bo'lim yorliqlari va CTA da shu xarakterni ishlat.
- **Aksent qoidasi:** pul/raqam va urg'u so'zlar — **sariq `#F6B52F`**; ijobiy/eko so'zlar — **yashil `#22674D`** (to'q fonda yorqinroq `#2E8A63`); salbiy — qizil `#E53935`. Referenslardagi ko'k o'rniga brend sariq ishlatiladi.
- Grafik kartochkalar/qutilar: to'q yashil fon (`#041512`, 85–90% shaffoflik), ingichka sariq yoki yashil ramka.
- CTA: yumaloq avatar (logotip) + `@premiumsolar.uz` pill + "Obuna" tugmasi (sariq) va/yoki "Ariza qoldiring / izohga '+' yozing" — sotuv videolarida ariza (B2B katalog) chaqiruvi.
- **⚠️ ASOSIY AUDITORIYA — B2B** (foydalanuvchi talabi, 2026-11-17, UNUTMA): korxona, zavod, ombor, do'kon, fermer va biznes egalari. Ohang: professional-do'stona, raqamlar bilan (kVt, oylik tejash, qoplanish muddati, kafolat, ulgurji narx). Xonadon/bolalar ohangi — faqat ikkinchi darajali.
- **Personaj (maskot) — TANLANGAN: 02 PANELBEK** (2026-11-17). Asosiy fayl `mashq/scenes/panelbek.html` (bot(face) funksiyasi, 1080x1920 hero + ekran-yuz holatlari: salom / kozqisish / raqam / hayron). Quyosh panelidan yasalgan B2B muhandis-robot: yashil alyumin rama, ko'k kataklar, ekran-yuz (#5BE3C8), tilla qo'lqoplar, chaqmoq. Kepkada **faqat original logo** — `assets/logo_premium_solar_shaffof.png` (foni olingan); logoni qo'lda qayta chizma. Raqamlar ekran-yuzda chiqadi (−78%, kVt, qoplanish muddati). Boshqa konseptlar (`personaj.html`: Quyoshvoy, Nurchik; `personaj_odam.html`) zaxirada. Haqiqiy odam yoki AI rasm EMAS — personaj kodda chiziladi (foydalanuvchi talabi).
- **Personaj ovozi — TANLANGAN: ElevenLabs v4, "Liam" (voice_id TX3LPaxmHKxFdv7VOQHJ)** (2026-11-17). API: `POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128`, header `xi-api-key: proxy-injected` (kalit muhitda saqlangan, proksi qo'yadi), body `{"text", "model_id":"eleven_v4", "language_code":"uz"}`. eleven_v3 o'zbekchani QO'LLAMAYDI. Hissiyot teglari ishlaydi va o'qilmaydi: `[cheerful] [curious] [laughs] [confident]`. `voice_settings.speed` v4'da sezilmadi → tezlik postda: `silenceremove` (stop_duration 0.2, stop_silence 0.12, -45 dB) → `rubberband=tempo=1.12` → fx.sh tabiiy (EQ+kompressor). Panelbek robot-effekti QO'SHILMAYDI — foydalanuvchi Liamni asl holida tanlagan. Maqsad: 2.0–2.4 so'z/s, ohang ≥13 st (Liam 16 st). Bepul tarif: 10 000 belgi/oy — har generatsiyadan oldin `/v1/user/subscription` bilan limitni tekshir. OmniVoice va edge "Sardor" rad etilgan (bir tekis, cho'ziq).
- Mavzular: quyosh panellari, tejash, elektr narxi, biznes uchun SES, import, ombor, mijozlar → odatda **B. Infografika** yoki ekspert intervyu (V4 uslubi). B-roll: solar farm, rooftop solar, factory, electricity bill, city at night (Mixkit: `solar panels`, `solar energy`, `power lines`, `factory`).

## 11. Ochiq savollar (foydalanuvchidan hali javob kutilmoqda)

- ~~Asosiy uslub~~ → javob: mavzuga qarab tanla.
- Musiqa manbasi → foydalanuvchining Telegram kanali `t.me/dilshodkhamraevmuzika`. Telegram bu muhitda bloklangan va fayllarni yuklab bo'lmaydi — foydalanuvchi treklarni 📎 orqali yuboradi; ularni `music/` papkasiga saqlab, BPM va kayfiyat bo'yicha katalog qil.
- Aniq shrift nomlari / fayllari.
- O'z SFX kutubxonasi (yo'q bo'lsa HyperFrames `media-use` SFX).
- ~~Instagram nik, avatar, brend ranglari~~ → 10.5-bo'limga qarang.

## §11 Xom kadr (isxodnik) asboblari — 2026-11-17 o'rnatildi
Hammasi `asboblar/` da. Venv: `~/montaj-venv` (Python 3.12: mediapipe, opencv, torch-cpu, DeepFilterNet3). Modellar: `~/montaj-models/`, `~/.cache/DeepFilterNet/DeepFilterNet3`.

| Vazifa | Buyruq | Izoh |
|---|---|---|
| **Ovoz tozalash** (shovqin, shamol, aks-sado) | `~/montaj-venv/bin/python asboblar/ovoz_tozala.py xom.mp4 toza.wav [--kuch 0.85]` | DeepFilterNet3 + EQ/de-esser/kompressor. Sinov: shovqin −50 → −66 dB. `--kuch 0.6` tabiiyroq. |
| **Yuz kuzatish** | `~/montaj-venv/bin/python asboblar/kadr_ai.py yuz video.mp4 yuz.json` | har 0.2 s, silliqlangan |
| **16:9 → 9:16 aqlli kesish** | `... kadr_ai.py kes video.mp4 vert.mp4 [--zoom 1.15] [--yuz yuz.json]` | kadr yuzni kuzatadi; 4K kirishni avval 1920 ga tushirish tezroq |
| **Odam niqobi** | `... kadr_ai.py niqob video.mp4 niqob.mp4` | oq=odam. Matnni odam orqasiga: `[fon][matn]overlay[t];[t][asl][niqob]maskedmerge` (asl odam ustida). Fon blur: `[asl]boxblur[b];[b][asl][niqob]maskedmerge` |
| **Jump-cut** | `~/claude-video-kit/.venv/bin/python asboblar/jumpcut.py xom.mp4 kes.mp4 [--pauza 0.35]` | pauza va "ee/mmm" kesiladi; `kes.words.json` — subtitr uchun yangi so'z vaqtlari. Takroriy dublni (bir gap 2 marta) o'zing tanla. Sinov: 22.0 → 17.3 s |
| **Kino ranglar (LUT)** | `-vf lut3d=file=lut/NOM.cube` | `kino_teal`, `tungi_kok` (FERS kabi qorong'i ko'k-yashil), `iliq_premium`, `toza_tabiiy`, `brend_yashil`. Qayta yasash: `python3 asboblar/lut_yasa.py` |
| **Musiqa (Mixkit)** | `python3 asboblar/musiqa.py qidir cinematic` · `... ol 614 ~/montaj-musiqa` | tijoratda bepul. Tayyor: 614 Silent Descent, 184 Vastness, 871 Fright Night, 676 Epical Drums, 1167 Close Up, 175 Digital Clouds |

**Xom kadr ish tartibi:** ovoz_tozala → jumpcut → (kerak bo'lsa kes 9:16) → LUT + yengil push-in → subtitr (words.json) → B-roll/grafika → musiqa+SFX → loudnorm −14 → earshot critique.
**Yuklash:** 7 ta sahifa, har biri 1 GiB (jami 7 GB). Bitta fayl ≤ ~1 GB bo'lishi kerak. Har montajdan keyin bo'laklarni o'chir.
1 J1Emidie83yWqgp1qwL6rm · 2 XrtEdFcoEyhyz6f5jk3TYd · 3 4scFBJ54EwhPNyLFeGCbi8 · 4 3m8stXeZdzPYoyHuQXXE4Q · 5 AdDQgwjjCPL54QsJRSEimu · 6 FGxvXeYoTjVpbmDm98dRH8 · 7 NSxgrXruaRhw9E3kRrVeVp (https://claude.ai/artifact/<id>). DB: `uploads` kolleksiyasi (chunks[].id → /_blob/<id>, base64).
