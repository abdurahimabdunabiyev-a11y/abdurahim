---
name: montaj-motion
description: Kod orqali (Remotion) motion graphics video yaratish — reklama roliklari, mahsulot taqdimoti, infografika, logo animatsiyasi. Brif → storyboard → sahnalar → render → tuzatish tartibida ishlaydi. Animatsiya, motion, launch video, reklama roligi yoki "video qil" so'ralganda ishlat.
---

# Montaj Motion — kod orqali motion graphics

Bu skill senga tajribali motion dizaynerning qoidalarini beradi. Video tayyor kadrlardan emas, noldan kodda yasaladi: har bir element (matn, karta, tugma, kursor, logo) vektor sifatida chiziladi va harakati kodda yoziladi.

## Qachon to'g'ri vosita, qachon emas

To'g'ri: kinetik tipografiya, interfeys animatsiyasi, raqam/grafik infografika, logo intro/outro, narx va CTA kadrlari, jarayon sxemalari.

Noto'g'ri: real odam, real mahsulot tasviri, fotorealistik muhit. Bunday kadr kerak bo'lsa, foydalanuvchiga ayt: bu video generator (Higgsfield, Kling) yoki haqiqiy suratga olish ishi. Real kadr tayyor bo'lsa, uni Remotion ichiga `<OffthreadVideo>` sifatida qo'yib, ustiga motion qatlam qilish mumkin.

## Ish tartibi (buzilmaydi)

1. **Brif.** `references/brief-template.md` ni to'ldir. Mahsulot noma'lum bo'lsa, avval 3 ta qisqa savol ber: kim uchun, asosiy xabar, qayerda ko'rsatiladi.
2. **Storyboard.** `references/storyboard-template.md` formatida yoz. Storyboard yagona haqiqat manbai: sahnalar tartibini o'zgartirma, sahna qo'shma yoki olib tashlama. Foydalanuvchi tasdiqlamaguncha animatsiyaga o'tma.
3. **Aktivlar.** Brend ranglari (hex), shrift, logo SVG, UI ekranlari SVG. Hech qachon skrinshot ishlatma: kamera zoom qilganda skrinshot xiralashadi, SVG o'tkirligicha qoladi. Mahsulot fotosi kerak bo'lsa, foni olib tashlangan yuqori sifatli PNG ishlat.
4. **Qurish.** Har sahna alohida komponent (`src/scenes/Scene1Hook.tsx` va h.k.), hammasi `<Sequence>` bilan bitta kompozitsiyaga ulanadi. Harakat uchun `assets/motion.ts` dagi yordamchilardan foydalan (loyihada `src/lib/motion.ts` ga ko'chir).
5. **Tekshirish.** Har sahnadan bittadan kadr (still) render qil va `references/pre-render-checklist.md` bo'yicha tekshir. Xatoni topib tuzat, keyin to'liq render.
6. **Render.** Asosiy versiya, keyin kerakli formatlar (9:16, 1:1, 4:5).

## Hikoya qoidasi

Har video shu zanjirga xizmat qiladi: **e'tibor (hook) → muammo → yechim (mahsulot) → natija → brend + CTA.** Shu zanjirga xizmat qilmaydigan sahna olib tashlanadi. Qisqa formatlarda (6–15 s) muammo va hook birlashishi mumkin, lekin natija va CTA hech qachon tushib qolmaydi.

## Vaqt qoidalari

- Muhim narsa ekranda kamida ~1.5 soniya turadi (o'qilishi uchun).
- Raqam sanalishi ~1 soniya davom etadi. Bir kadrda sakrash taqiqlanadi.
- Natija (payoff) kadri kamida 1.5 soniya ushlab turiladi.
- Matn: bir ekranda ko'pi bilan 6–7 so'z. Ko'p bo'lsa, bo'lib chiqar.
- Ijtimoiy tarmoq uchun: birinchi 1.5 soniyada hook ko'rinishi shart.

## Harakat qoidalari

- **Chiziqli harakat yo'q.** Har doim easing ishlat.
- **Kirish:** ~0.5 s, biroz o'tib ketib qaytadi (overshoot) — `enter()`.
- **Chiqish:** kirishdan tezroq (~0.3 s) — `exit()`.
- **Ketma-ketlik (stagger):** guruh elementlari birdaniga emas, 3–6 kadr oraliq bilan chiqadi — `stagger()`.
- **Bosish:** har bir klikda tugma kichik "press" qiladi — `press()`.
- **Kursor:** to'g'ri chiziqda emas, yoy bo'ylab yuradi — `arcPoint()`. Bosishdan oldin bir lahza to'xtaydi.
- **Kamera:** surish va zoom easy-ease bilan, yumshoq boshlanib yumshoq to'xtaydi — `EASE.inOut`.

## Oltin qoida: hech narsa to'liq to'xtamaydi

After Effects mantiqi bilan ishla:
- Bog'liq elementlar bitta ota-konteyner (null) ostida turadi. Kamera harakati shu konteynerga beriladi.
- Kalit kadrlar bir-biridan 2–4 kadr siljigan bo'ladi.
- Keyingi harakat oldingisi to'liq tinchlanmasdan boshlanadi.
- Statik kadrlarda ham sekin "drift" (1–3% zoom yoki surilish) bo'ladi — `drift()`.

## Texnik standart

- Asosiy kanvas: 1920×1080, 60 fps (agar brif boshqacha demasa). Barcha joylashuv **markazdan** hisoblanadi, chetlardan emas.
- Xavfsiz zona: muhim kontent markaziy 1080×1080 kvadrat ichida, shunda 9:16 va 1:1 kesimlarda ham ko'rinadi.
- Shriftlar birinchi kadrdan oldin yuklanadi (`@remotion/google-fonts` yoki `delayRender` / `continueRender`). Aks holda dastlabki kadrlarda standart shrift chiqadi.
- Barcha o'zgaruvchan qiymatlar (raqamlar, matnlar, ranglar, vaqtlar) fayl boshida konstanta sifatida turadi. Mijoz tuzatishi bitta qatorni o'zgartirish bilan hal bo'lishi kerak.
- Musiqa va tovush effektlari `<Audio>` bilan, ovoz balandligi musiqa uchun ~0.4, klik uchun ~0.6.

## Mahalliy kontekst

- Matnlar o'zbek (lotin) yoki rus tilida bo'lishi mumkin. Tanlangan shrift kirill va oʻ, gʻ harflarini to'g'ri ko'rsatishini tekshir.
- Instagram/Telegram uchun 9:16 va 4:5 ko'pincha asosiy format. Brifda qaysi biri asosiy ekanini aniqlab ol.
- Reklama roligi lid yig'ishga qaratilgan bo'lsa, CTA aniq harakatni aytadi ("Ariza qoldiring", "Telegram'da yozing"), shunchaki logo bilan tugamaydi.

## Fayllar

- `references/brief-template.md` — brif shabloni
- `references/storyboard-template.md` — storyboard formati va namunalar
- `references/prompt-library.md` — qurish, tuzatish, sayqal va reviziya promptlari
- `references/pre-render-checklist.md` — render oldidan tekshiruv
- `assets/motion.ts` — harakat yordamchilari
