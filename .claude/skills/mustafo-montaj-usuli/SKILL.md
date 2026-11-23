---
name: mustafo-montaj-usuli
description: Mustafoning shaxsiy After Effects montaj uslubi (qora fon + to'q sariq nur, Helvetica Neue, yupqa chegarali kartalar, tepada grafik panel va pastda BIR XIL o'lchamdagi yuzni kuzatuvchi video karta, subtitr o'rtada) - brend ranglar, shriftlar, maket, animatsiya lug'ati, tayyor AE kutubxonasi va pipeline. "Mustafoning montaj usulida", "mening stilimda", "mening dizaynimda", "shu uslubda montaj qil", "men yuborgan animatsiyadan ideya ol, mening stilimga moslab ber" deyilganda HAR DOIM shu skillni ishlating.
---

# Mustafoning montaj usuli (AE)

Muloqot **o'zbek tilida**, qisqa va halol (nima tekshirilgan, nima taxmin ekanini ayting). Vertikal 1080x1920 reels, odam kameraga gapiradi va/yoki ekran yozuvi (b-roll) bor.

**Asosiy qoida:** yangi montaj so'ralganda ("professionalroq qil" desa ham) AVVAL shu uslubni ishlating. Uslubni faqat u **aniq yangi referens** bersa va "shunday qil" desa o'zgartiring, u ham faqat joylashuv/harakat g'oyasi bo'yicha, **ranglar va shriftlarni almashtirmang**. 

## 1. Ranglar (AE float [r,g,b] 0-1 va hex)
| Nom | AE | Hex | Qayerda |
|---|---|---|---|
| BG | [0.043,0.035,0.032] | #0B0908 | asosiy fon |
| ACC (to'q sariq) | [0.93,0.42,0.22] | #ED6B38 | asosiy urg'u: chiziq, raqam doirasi, halqa, tugma |
| ACC2 (och to'q sariq) | [1.0,0.58,0.30] | #FF944D | tugma gradienti boshi, plyus, ikonka, "hot" tugun |
| tugma gradient oxiri | [0.80,0.31,0.14] | #CC4F24 | ACC2 -> shu |
| DEEP | [0.40,0.13,0.045] | #66210B | chuqur to'q sariq |
| panel gradient boshi | [0.34,0.115,0.04] | #571D0A | tepa panel: shundan CARDF ga |
| CARDF | [0.082,0.07,0.064] | #151210 | karta fon |
| CARDF2 | [0.115,0.098,0.09] | #1D1917 | ichki karta/qator |
| TXT | [0.975,0.965,0.955] | #F9F6F4 | asosiy matn (iliq oq) |
| MUTE | [0.66,0.62,0.59] | #A89E96 | ikkilamchi matn, teg |
| nur 1 / nur 2 | [0.80,0.30,0.09] / [0.62,0.22,0.07] | #CC4D17 / #9E3812 | radial nur (darkBg) |
| chegara | oq 14-26% | | hamma kartada 2 px yupqa chegara |
| Claude brend | #D97757 | | FAQAT Claude logotipida |
| shaxsiy brend sariq | #FFB81C | | zonali oq-fon uslubida (reels-zonali-montaj); bu uslubda kamdan-kam |

Gradient faqat ikki joyda: tugma/panel (gradPanel) va fon nuri (radial Ramp + Screen). Boshqa hamma narsa tekis.

## 2. Shriftlar
- **HelveticaNeue-Medium**: sarlavha, UI matni, subtitr (60 px).
- **HelveticaNeue-Light**: ikkilamchi matn, "1-QADAM" tegi (26 px), kichik yozuvlar.
- **HelveticaNeue-Bold**: urg'u, raqamlar, tugma matni.
- **DINCondensed-Bold**: faqat odam orqasidagi katta yozuv uchun (shaxsiy-brend skill'idagi usul).
- Eski oq-fon zonali uslub: SFProDisplay-Bold/Semibold (alohida skill: reels-zonali-montaj).
O'lchamlar: panel sarlavhasi 52, katta raqam 150-200, belgi yozuvi 28-36, tugma 50-54.

## 3. Maket (standart "split")
- Tepada **grafik panel** 940x590 (y 245-835, radius 54, gradient + yupqa chegara), pastda **video karta** 940x590 (y 965-1555, radius 48, chegara). **Ikkalasi BIR XIL o'lchamda** (video kichik bo'lib qolgani uchun shikoyat bo'lgan).
- **Subtitr ikkalasining O'RTASIDA**: markaz y=900, 60 px Medium, iliq oq, bir qatorli chunk (2-4 so'z).
- Panel ichida: yuqori chapda qadam tegi (206x58 kapsula "N-QADAM"), markazda sarlavha (y 378), ostida grafika (y 480-800).
- Video karta rejimlari: **face** (yuzni kuzatadi, k=1.05) va **broll** (monitor yozuvi, 108->118% sekin yaqinlashish, fy = e'tibor nuqtasi). Rejim kesish chegarasida almashadi.
- Fon: qora + ikki radial nur (pastda chap, tepada o'ng). Sahnalar orasida yumshoq crossfade: 0.32 s opacity + 96->100% masshtab.
- Instagram safe zona: x 64-960 (markaz 512) va y 270-1540 hisobga olinadi; kartalar kengligi 940 (x 70-1010).

## 4. Animatsiya lug'ati (blok funksiyalar: lib/)
| G'oya | Funksiya |
|---|---|
| fon + nur | `darkBg`, `radial` |
| panel / karta | `gradPanel`, `flatCard`, `rr`, `oval` |
| yuzni kuzatuvchi video | `faceCard`; b-roll: `brollCard`; ikkalasi: `base2(t0,t1,[[a,b,"face"],[b,c,"broll",fy]])` |
| qadam tegi + sarlavha | `stepTag(n)`, `panelTitle(str)` |
| logotip kartasi | `tileLogo(kind,...)` (qora yumaloq kvadrat + haqiqiy belgi), `plus2` |
| Claude belgisi | `claudeMark`, oq uchqun `sparkW` |
| oqim diagrammasi | `node(icon,label,x,y,t0,t1,hot)`, `flowPath` (punktir yo'l + yugurib o'tuvchi nur) |
| aylanuvchi teglar | `orbitChip` |
| hisoblagich | `money(cx,cy,size,tS,dur,tE,target,prefix)` |
| ro'yxat qatorlari | `flatCard` + `iCheck` (S05/S09 namunasi) |
| ustunlar o'sishi | scenes_example.jsx S06 |
| ikonkalar (vektor) | `iCheck iDown iUp iSearch iX iClock iPlus`, `strokeLines` |
| tugma bosilishi | `pressAnim`, oq "Obuna bo'ldingiz ✓" holati (S10) |
Kirish qoidalari: pop 80->106->100 (0.2-0.34 s), matn pastdan 36 px ko'tarilib 0.2 s fade, kartalar 95->100%, chiqish 0.2-0.3 s fade. Zoom zarbasi faqat ta'kid so'zda (100->109%, 0.3 s kirish, 0.35 s chiqish).

## 5. QAT'IY QOIDALAR (foydalanuvchi fikrlaridan)
1. **Soya va blur yo'q**: shape layer'dagi blur/drop shadow qatlam chegarasida kesilib qoladi. Nur kerak bo'lsa: butun kadrli solid + radial Ramp + Screen.
2. **Rang tabiiy**: kamera videosini ffmpeg'da yumshoq tuzat (contrast 1.05, saturation 1.12, yengil highlight siqish). Kuchli grade terini "kuydiradi".
3. **O'tishlar yumshoq**: sahna qatlamlarini ikki yonga uzaytiring (+0.7 s / -0.25 s), aks holda ostidagi xom video "xira kadr" bo'lib ko'rinadi; chiquvchi sahna faqat keyingisi shaffof bo'lsa so'nadi.
4. **Natijada hamma narsa kadr ichida**: hech narsa kesilib qolmasin, matn eni <= 860.
5. **Pastdagi video kichik bo'lmasin** (panel bilan teng).
6. **Faktlarni uydirma**: panelga qo'yilgan yozuv/raqam gapdan chiqsin; o'zim qo'shgan so'z/raqam bo'lsa, hisobotda ayt.
7. AE'ni foydalanuvchidan so'ramay yopma; yangi loyiha oldidan `app.project.close(DO_NOT_SAVE_CHANGES)` (lib shuni qiladi). `layer.scale` foizda (135, 1.35 emas); `parent=` dan keyin bola qiymatlarini yoz, ota animatsiyasini oxirida qo'sh.
8. Subtitr matnini men gapdan tozalab yozaman: Whisper o'zbekchani yomon o'qiydi, shuning uchun "taxminiy joylar"ni hisobotda ko'rsat.

## 6. Pipeline
1. **Material**: `ffprobe`, kontakt-sheet, ovoz (`-vn -ac 1 -ar 16000`). iPhone MOV 4K aylantirilgan bo'ladi, ffmpeg o'zi to'g'rilaydi.
2. **Matn va vaqt**: `HF_HUB_OFFLINE=1 uvx --quiet --with faster-whisper python ...` (large-v3, uz + tr, `initial_prompt` bilan muhim so'zlarni bering, audio numpy massiv). **Whisper vaqtlari ~0.4 s oldinda**: kesish va subtitr vaqtini ovoz energiyasi (RMS, 25 ms) bo'laklaridan toping.
3. **Kesish**: `scripts/prep_cut.py INPUT --out PAPKA --segments "a-b,..."` (to'xtashlarni olib tashlaydi, yumshoq rang, ovoz tozalash, `cuts.json`).
4. **Yuz kuzatuvi**: `scripts/face_track.py` (uvx + opencv), faqat gapiradigan oraliqlarda.
5. **Logotiplar**: `scripts/logo_png.py nom "#rang"` (Simple Icons) yoki sayt SVG'si.
6. **Ma'lumot fayllari**: `data.js` (`DATA.CAPS=[[t0,t1,matn,aksent],...]` chiqish vaqtida), `data2.js` (`D2.KB` kesish vaqtlari, `D2.Z` zoom).
7. **Qurish**: loyiha papkasida `cfg.jsx` (templates/cfg_example.jsx) va `scenes.jsx` (templates/scenes_example.jsx dan boshlang), keyin `scripts/build.sh PAPKA`.
8. **Render**: `~/.claude/skills/reels-zonali-montaj/scripts/render.sh <aep> "00 MAIN" <mp4>` (H.264 15 Mbps). Kadrlarni `ffmpeg -ss` bilan ajratib tekshiring (kontakt-sheet + 3-4 ta yuqori sifatli kadr).
9. **Ovoz**: `real-sfx` skilli. `events.json` -> `from_cues.py --ui library --no-stems` -> `mix.py --voice-safe --voice-depth light --base-audio voice.wav music.wav:-17 --duck-music --target-lufs -14 --no-match-layer`. SFX faqat grafikaga (pop g~0.5, kesishda whoosh g~0.4), sarlavha/subtitrga yo'q. Musiqa ovoz tagida pasayadi.
10. **Yetkazish**: tayyor mp4 ni loyiha papkasidagi `render/` ga qo'yib `SendUserFile` bilan yuboring; hisobotda: nima tekshirilgan, nima taxmin, ovoz tinglanmagani.

## 7. Foydalanuvchi animatsiya/video yuborsa: ideyani olib, MENING stilimga moslash
Batafsil: `reference/adapt_references.md`. Qisqasi:
1. Referensni ko'ring (Instagram: `https://www.instagram.com/reels/ID/` shakli brauzer panelida login'siz ochiladi; `video.currentTime` + play/pause 250 ms + zoom skrinshot bilan kadrma-kadr).
2. "G'oya kartasi" yozing: u nimani tushuntiradi, tuzilma, ritm/vaqt, harakat turi, matn bilan ishlash.
3. Har elementni shu skillning lug'atiga o'giring (jadval adapt_references.md da) va **referensning rang/shrift/logosini QO'YMANG**; faqat harakat mantig'i va kompozitsiyani oling.
4. Prototipni qurib, nimasi ideya, nimasi mening talqinim ekanini aniq ayting.

## 8. Fayllar
- `lib/mustafo_lib.jsx` (asosiy helperlar, konstantalar), `lib/mustafo_blocks.jsx` (logotip, tugun, hisoblagich, base2...), kerak bo'lsa `reels-zonali-montaj/lib/lib_zonali.jsx` (mkText, kf, popIn...) avtomatik ulanadi.
- `templates/cfg_example.jsx`, `templates/scenes_example.jsx` ("1 soatda 100$" montaji, 10 sahna + subtitr + crossfade).
- `scripts/`: `prep_cut.py`, `face_track.py`, `logo_png.py`, `build.sh`.
- `reference/palette.md` (ranglar va maket jadvali), `reference/adapt_references.md`.
- Bog'liq skilllar: `reels-zonali-montaj` (oq fon, zonalar), `shaxsiy-brend-video-edit` (oq minimal motion, odam orqasidagi yozuv), `real-sfx` (tovush), `viral-reels-scriptwriter` (ssenariy).
