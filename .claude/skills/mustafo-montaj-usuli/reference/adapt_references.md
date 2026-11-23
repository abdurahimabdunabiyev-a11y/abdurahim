# Referensdan ideya olib, Mustafoning uslubiga moslash

Foydalanuvchi animatsiya yoki video yuboradi ("shundan ideya ol"). Maqsad: **g'oyani** olish, **uslubni** o'zimizniki qilish.

## 1. Referensni ko'rish
- Instagram: `https://www.instagram.com/reels/<ID>/` (`/reel/<ID>/?srtk=...` shakli login so'raydi, `/reels/` shaklini ishlating). Brauzer panelida `javascript_tool` bilan:
  `var v=document.querySelector('video'); v.muted=true; v.currentTime=T; v.play(); await new Promise(r=>setTimeout(r,250)); v.pause();`
  keyin `computer zoom` bilan kerakli sohani oling. 1.5-2 s qadam bilan 8-12 kadr yetadi. Video uzunligi/o'lchami: `[v.duration, v.videoWidth, v.videoHeight]`.
- Pinterest pin: sahifa HTML'idan `v1.pinimg.com/...mp4` manzilini toping (qidiruv login so'raydi).
- Foydalanuvchi fayl bergan bo'lsa: `ffmpeg -vf fps=0.5,scale=270:-1,tile=11x2` kontakt-sheet.
- Ko'ra olmasangiz (login, yopiq), buni ochiq ayting va kover/tavsif bilan ishlang.

## 2. G'oya kartasi (yozib oling)
- Nima tushuntiriladi / qanday his beradi?
- Tuzilma: nechta bosqich, qanday ketma-ketlik.
- Ritm: bosqichlar vaqti, urg'u joylari, kesishlar.
- Harakat: nima chiqadi, qanday chiqadi (pop, slayd, chizilish, sanash, aylanish).
- Matn: qanday so'zlar, qanday ajratilgan (kinetik, bitta so'z, chip).
- Kompozitsiya: odam qayerda, grafika qayerda.

## 3. Moslashtirish jadvali (referens elementi -> mening lug'atim)
| Referensda | Menda |
|---|---|
| suzuvchi UI kartalar, telefon maketi | `gradPanel`/`flatCard` kartalar, yupqa chegara |
| logotiplar qatori "A + B + C" | `tileLogo` + `plus2` |
| oqim / zanjir diagrammasi | `node` + `flowPath` (punktir yo'l, yugurib o'tuvchi nur) |
| doira bo'ylab aylanuvchi elementlar | `orbitChip` |
| o'sib boruvchi raqam | `money(...)` yoki `counter` |
| reyting / tier list | `flatCard` qatorlari + `iCheck`, "hot" qator `gradPanel` |
| bar chart | ustunlar (S06 namunasi) |
| kinetik katta so'z | panel ichida HelveticaNeue-Bold katta so'z (pop 80->106->100) |
| odam orqasidagi yozuv | DINCondensed-Bold + Vision maskasi (shaxsiy-brend-video-edit/scripts/seg.swift) |
| tugma bosilishi, obuna | `pressAnim` + oq "Obuna bo'ldingiz" holati |
| yorqin neon/gradient fon (boshqa rangda) | `darkBg` radial nur, ACC/ACC2 ga qayta bo'yalgan |
| qora kontur/soya bilan subtitr | oq 60 px Medium, o'rtada, soyasiz |
| tez oq yaltirash o'tishlar | yumshoq crossfade (0.32 s) + zoom zarbasi |

## 4. Qoidalar
- Referensning ranglari, shrifti, logo/belgilarini KO'CHIRMANG. Faqat harakat va tuzilma.
- Referensdagi matn/raqamni o'z faktlaringiz bilan almashtiring; uydirma raqam bo'lsa ayting.
- Brend belgilar (Claude, Meta, Higgsfield) haqiqiy bo'lsin: `scripts/logo_png.py`.
- Prototipdan keyin hisobot: "bu ideya referensdan, bu mening talqinim", va qaysi qismi taxminiy.
