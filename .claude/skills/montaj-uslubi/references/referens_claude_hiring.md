# Referens: "Hiring editors" reels (Claude'da qilingan deb ko'rsatilgan, 9 s)

Foydalanuvchi: "shu montaj claudeda qilingan ekan sen ham huda shundan qilishni organ".
Manba: ekran yozuvi (720x1280) ichida 9 s lik reels. Kadrlar 6 fps da ko'rib chiqildi + `earshot timeline --detail high`.

## Vizual uslub
1. **Ikki rang:** zumrad yashil + oq (va mayda qora matn). Footage iliq-och (bej devor, yog'och pol). Boshqa rang yo'q.
2. **Matn odamning ORQASIDA** (text-behind-subject): ulkan qalin *italic* so'z (Edita / Editing Studio / Claude)
   odam niqobi bilan kesiladi — boshi matn ustida turadi. Bizda: `kadr_ai.py niqob` + qatlamlar: fon → orqa matn → odam → old grafika.
3. **Kicker + katta so'z:** tepada kichik ingichka italic ("My name is", "The AI", "Who can edit with"),
   ostida katta so'z **harfma-harf yoziladi** (typewriter, ~0.08 s/harf). Yonida mitti yorliqlar ("of", "lab", "video").
4. **Piksel kvadratchalar:** so'z paydo bo'lganda 3–6 ta mayda yashil kvadrat "sochilib" chiqadi (glitch aksent).
5. **PIP karta:** yumaloq burchakli, yashil chiziqli ramka ichida boshqa kadr; paydo bo'lganda konsentrik halqa to'lqini.
   Chap tomonda kichik foto-kartalar to'plami, pastda keyingi sahnaning "shisha" kartasi (preview).
6. **O'tishlar (zoom yo'q, kamera statik):**
   - yashil **nur chizig'i** (to'lqinsimon yorug' chiziq) kadrni kesib o'tadi → keyingi sahna;
   - **radial blur + halqa to'lqini** (defokus bilan almashish);
   - **gologramma**: odamning ko'k-yorqin silueti qora fonda (bosh va oxirgi qismdan oldin) — 0.15–0.3 s.
7. **B-roll sahnasi:** yumshoq yalpiz-yashil fon, ustida UI elementlar: chiziqli karta, yashil play tugmasi, qog'oz samolyot ikonkasi,
   nuqtali halqa; karta ichida matn harfma-harf: kichik → KATTA QALIN → kichik "and" → KATTA QALIN.
8. **Ijtimoiy kartalar** oxirida: portret foto-karta + "@ism" pill + yashil audio-to'lqin chip — pop bilan.
9. **So'zma-so'z subtitr YO'Q** — faqat kalit so'z sarlavhalari (chatda "captions ham kerakmi?" deb so'ralgan).

## Tovush (earshot)
- −14 LUFS, beat grid yo'q (fon musiqa yengil), **zich SFX: 6.1 hodisa/s**.
- Har harf/element: **bubble pop / water drop / klaviatura bosish** (mayda, yuqori).
- O'tishlarda: **whip whoosh**, "swoosh passing by" (+12 dB aksent), katta o'tishda **deep cinematic boom** (3.84 s).
- Boshida bubble pop + kick, oxiri chat pop.
- Kesimlarning 100% i ±100 ms ichida tovush bilan.

## Bizning qo'llash qoidalari (Premium Solar)
- Ranglar: #22674D / yorqinroq #1E8A5A + oq; aksent sariq (#F6B52F) faqat juda kam.
- Har 1.5–3 s da bitta "katta so'z" sahnasi; so'z — gapning kaliti (OMBORDA, XITOYDAN, BEPUL, B2B).
- Zoom o'rniga: statik kadr + qatlamli grafika + nur/halqa/gologramma o'tishlari.
- Subtitrni foydalanuvchi so'rasa qo'shiladi; standart — kalit so'zlar.
- SFX: harf/element = pop/drop (−20…−24 dB), o'tish = whoosh (−16…−18 dB), katta o'tish = boom (−14 dB).
