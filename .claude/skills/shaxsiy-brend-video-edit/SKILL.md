---
name: shaxsiy-brend-video-edit
description: Mustafo'ning shaxsiy brend vertikal (1080x1920) videolarini After Effects'da montaj qilish uslubi — so'zma-so'z kinetik sarlavhalar, minimal oq motion grafika, odam orqasidagi katta yozuv, to'liq ekranli ko'k infografika, Instagram obuna kartasi. "shaxsiy brend video edit", "shaxsiy brend montaj", "shu uslubda montaj qil" deyilganda HAR DOIM shu skillni ishlating.
---

# Shaxsiy brend video edit

Muloqot **o'zbek tilida**, qisqa va halol (nima tekshirilgan, nima taxmin ekanini ayting). Vertikal reels, odam kameraga gapiradi. 

## 0. Ish tartibi (foydalanuvchi qoidalari)
1. **Render faqat tasdiqdan keyin, bir marta.** Avval AE'da tayyorlang, kadrlarni `see-frame` bilan tekshiring, foydalanuvchi "yaxshi chiqdi" desa render qiling.
2. Render: `render-aerender`, shablon `H.264 - Match Render Settings - 15 Mbps`, `Best Settings`, chiqish `~/Desktop/<nom>.mp4`; loyiha `~/Desktop/<nom>.aep` (avval `app.project.save(new File(...))`). Eski render ustiga yozish mumkin (foydalanuvchi "qayta render qil" degan bo'lsa). Renderdan keyin ffprobe + 4–6 kadr + ovoz darajasini tekshiring.
3. Ish papkasini (`<loyiha>/`) toza saqlang: vaqtinchalik hamma narsa scratchpad'da.
4. **Higgsfield / pullik generatsiya faqat ruxsat bilan** (kreditlar kam). Rasm kerak bo'lsa avval vektor (SVG), ffmpeg, kod bilan qiling.
5. Vositalar tugamasa ham xavfsizlik: parollarni kiritmang, sudo'ni foydalanuvchi o'zi bajaradi (yoki macOS `osascript ... with administrator privileges` oynasi orqali u o'zi kiritadi).

## 1. Instagram Reels SAFE ZONE (majburiy, boshidan)
1080x1920 da hamma element (sarlavha, grafika, karta) shu ichida: **x 64–960, y 270–1540**, markaz **x=512**. Tashqarisi Instagram UI ostida qoladi. Skriptlarda `CXS = 512`. Chegaralarni `sourceRectAtTime` bilan hisoblab tekshiring. Katta yozuv eni ≤ 860.

## 2. Takrorlanmaslik qoidalari
- Bir so'z/ma'no bir vaqtda faqat bitta joyda (sarlavhada yoki grafikada). Masalan: vosita nomlari faqat grafikada, sarlavhada "g'oyalarni", "tekstni" qoladi (`groups2.py` da `[qavs]` ichidagi so'zlar sarlavhadan chiqariladi).
- **Sarlavhalarga SFX qo'ymang** (foydalanuvchiga yoqmagan). SFX faqat grafikaga mos va past ovozda (pop −16…−20 dB, whoosh −12…−16 dB); zoomlarda tovush yo'q.
- Sarlavhaga **drop shadow qo'ymang**. O'qilishi uchun pastki qoraytirish (solid, mask y>900, feather 700, opacity 55) ishlating.

## 3. Pipeline
1. **Material**: `ffprobe`, kontakt-sheet (`ffmpeg ... tile`), audio (`-vn -ac 1 -ar 16000`). Nutq deyarli uzluksiz bo'lsa kesmang.
2. **Matn**: `faster-whisper` o'zbekchani yomon yozadi (turkcha aralashadi) — `scripts/transcribe.py` faqat **so'z vaqtlari** uchun. Foydalanuvchiga mantiqan tuzatilgan matnni tasdiqlating, so'ng so'zlarni gap oralig'iga belgi uzunligi bo'yicha taqsimlang (`groups2.py`). Venv: `python3 -m venv` + `pip install faster-whisper` (model `medium`, `language="uz"`).
3. **AE ulanish** (qo'shimcha pastda), kompozitsiya `Reel_PR` 1080x1920, fps = manba fps, davomiylik = manba.
4. **Sarlavhalar** → **zoom** → **grafikalar** → **maxsus sahnalar** → **oxirgi karta** → tekshiruv → tasdiq → render.

## 4. Uslub spetsifikatsiyasi
**Sarlavhalar** (`build_tpl.jsx`): `HelveticaNeue-Bold`, oq. Har gapda: katta "hero" so'z (150px, tracking −35, eni ≤ 860) markazda y≈1090; oldida kichik "pre" (54px) chap-tepada, keyin kichik "post" (50px) o'ng-pastda. Kirish: 0,1 s opacity, pastdan +34px ko'tarilish 0,16 s (ease), hero scale 80→106→100. Chiqish: keyingi guruh boshlanganda. Guruhlar `|pre|hero|post` formatida (`groups2.py`).

**Zoom** (`fx_tpl.jsx`): ta'kid joylarida 100→111% (0,3 s kirish, 0,35 s chiqish), tovushsiz.

**Minimal oq grafika** (`gfx2_tpl.jsx`): oq doira/kapsula + qora belgi, gradientsiz va soyasiz; sakrab chiqish (scale 60→108→100, ~0,25 s). Misollar: 5 odam belgisi birlashib bitta + "AI" kapsulasi; vosita logolari oq doirada (ChatGPT=OpenAI qora, Claude to'q sariq #D97757, Gemini ko'k; Simple Icons CDN `cdn.jsdelivr.net/npm/simple-icons@14.15.0/icons/<nom>.svg`, foydalanuvchi bergan logo PNG'ni kesib qo'ying) chiziq bilan bog'langan, nomlari tagida; 4 ikonka (yulduz/play/karnay/sumka) markazga qo'shilib "odam" ikonkasi. 3D ikonkalar (`make.py` 3D rejimi) foydalanuvchiga **yoqmadi** — toza yassi uslub (`flat_*.svg`) ishlating.

**Odam orqasidagi katta yozuv** (`seg.swift`, `million.jsx`): ffmpeg bilan kerakli oraliqni kadrlarga ajrating (`fps=manba`), Apple Vision `VNGeneratePersonSegmentationRequest(.accurate)` bilan maska PNG ketma-ketligi (`swiftc -O seg.swift`), AE'ga `asSequence` import; qatlamlar tartibi: maska → odam dublikati (luma matte) → matn → asosiy video. Matn `DINCondensed-Bold`, vertikal 130% cho'zilgan, eni 860, markaz y≈500, faqat bitta so'z (masalan MILLION). Odam yozuvning bir qismini yopishi normal.

**To'liq ekranli infografika** (`fullscreen.jsx`): to'q ko'k fon = navy solid + 3 ta `ADBE Ramp` (radial) solid, blend Screen, sekin siljiydi (Gaussian Blur shape'lar chetidan kesiladi — ishlatmang). Shishasimon qatorlar (rounded rect #0D2673 ~66% + och ko'k kontur 45%), har birida nom, o'sib boruvchi raqam va nisbat chizig'i; oxirida yorqin "Jami" kartasi. Qatorlar 0,3 s oraliqda, raqamlar ~0,8 s. Hisoblagich: Slider Control + expression; **slider ±1 000 000 bilan cheklangan — mingliklarda saqlab ×1000 qiling**.

**Oxirgi karta** (`end2.jsx`): oxirgi ~3,4 s da. Foydalanuvchi bergan ikki holatli karta rasmi (Obuna bo'ling + / Rahmat! ✓) PNG qilib kesiladi (burchaklar yumaloq alpha bilan), pastdan sakrab chiqadi, + tugmasida to'lqin halqa, karta pulse, matn almashinuvi (yangi karta eski ustiga tez fade — karta o'zi shaffof bo'lib qolmasin). Karta ~612x333, markaz (512, 1360).

## 5. After Effects / MCP bog'lanish
- Panel `mcp-bridge-auto.jsx` AE'ning `Scripts/ScriptUI Panels` papkasida bo'lishi kerak (o'rnatilgan), AE sozlamasi "Allow Scripts to Write Files and Access Network" yoqiq. Panel yopilib qolsa: `app_menu` → `["Window","mcp-bridge-auto.jsx"]`, so'ng `check-bridge`.
- Skriptlarni `execute-script` ichida `File.read()` + `eval` bilan ishga tushiring (JSX fayllar scratchpad'da, ma'lumot `__GROUPS__`/`__T__` almashtirish bilan).
- ExtendScript tuzoqlari: kalit-kadrli xossada `setValue` xato beradi; `parent` ni transformlardan OLDIN qo'ying; shape guruhlarida glyph guruhini fon guruhidan OLDIN qo'shing (yuqorida turadi); `collapseTransformation` oldin `canSetCollapseTransformation` bilan tekshiring; matn rangi/shrift `TextDocument` orqali; `Position` expression bilan `pointOnPath` ishlaydi.
- Fayl tanlash oynasi (tizim jarayoni) boshqarib bo'lmaydi — foydalanuvchi o'zi tanlaydi.

## 6. Tekshiruv ro'yxati (render oldidan)
- [ ] Hamma element safe zone ichida (hisoblangan).
- [ ] Matn takrori yo'q; sarlavhalarda SFX/soya yo'q.
- [ ] Har ko'rinish uchun kamida 3–4 kadr `see-frame` bilan ko'rilgan.
- [ ] Loyiha saqlangan; foydalanuvchi tasdiqlagan.
- Hisobotda: so'z vaqtlari taxminiy ekani, qo'lda qo'shilgan raqam/matnlar (foydalanuvchi bermagan) aniq aytiladi.

## 7. Fayllar (`scripts/`) — shablon, qo'lda moslang
`transcribe.py` (so'z vaqtlari), `groups2.py` (guruhlash), `build_tpl.jsx` (sarlavhalar), `fx_tpl.jsx` (zoom), `gfx2_tpl.jsx` (minimal grafika, logolar, ikonkalar), `million.jsx` + `seg.swift` (odam orqasidagi yozuv), `fullscreen.jsx` (ko'k infografika), `end2.jsx` (obuna kartasi), `make.py` (SVG ikonkalar). Ularda vaqtlar va yo'llar shu videoga yozilgan — yangi videoda vaqt/yo'llarni almashtiring.
