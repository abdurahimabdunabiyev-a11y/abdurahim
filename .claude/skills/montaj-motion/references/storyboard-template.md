# Storyboard formati

Storyboard yagona haqiqat manbai. Har sahna uchun: ekranda nima, harakat, kamera, vaqt va kadr oralig'i. Kadrlar yig'indisi umumiy davomiylikka teng bo'lishi shart (60 fps da 1 s = 60 kadr).

```
[NOMI] — storyboard
[davomiylik] s · [kenglik × balandlik] · [fps] fps · [jami kadr] kadr

Sahna 1 · [nomi] (hook) — 0:00–0:0X, kadr 0–XXX
Ekranda: ...
Harakat: ...
Kamera: ...

Sahna 2 · [nomi] (muammo) — ...
Sahna 3 · [nomi] (yechim) — ...
Sahna 4 · [nomi] (natija) — ...
Sahna 5 · Brend + CTA — ...
```

---

## Namuna A — ofis kreslosi brendi, lid reklama, 15 s, 9:16

15 s · 1080×1920 · 60 fps · 900 kadr

**Sahna 1 · Og'riq (hook) — 0:00–0:02.5, kadr 0–150**
Ekranda: qora fon. Katta matn so'zma-so'z: "Kun oxirida belingiz og'riydimi?" Pastda soat ikonkasi 9:00 → 18:00 ga tez aylanadi.
Harakat: so'zlar overshoot bilan, 4 kadr stagger. Soat strelkasi ~1 s da aylanadi.
Kamera: sekin push-in 100% → 105%.

**Sahna 2 · Muammo — 0:02.5–0:05.5, kadr 150–330**
Ekranda: oddiy stul siluet ikonkasi, umurtqa chizig'i egilib qoladi (vektor). Matn: "8 soat noto'g'ri o'tirish."
Harakat: umurtqa chizig'i 0.6 s da egiladi, qizil yumshoq glow paydo bo'ladi.
Kamera: statik, 2% drift.

**Sahna 3 · Yechim — 0:05.5–0:10, kadr 330–600**
Ekranda: Kreslo (fonsiz PNG) markazga ko'tariladi. Atrofida 3 ta xususiyat kartasi birma-bir: "Bel tayanchi", "Sozlanadigan balandlik", "Nafas oluvchi to'r".
Harakat: kreslo enter() bilan pastdan. Kartalar 6 kadr stagger, har biri chiziq bilan kreslodagi nuqtaga ulanadi.
Kamera: kreslo kirganda 110% zoom, kartalar chiqqanda 100% ga qaytadi.

**Sahna 4 · Natija — 0:10–0:12.5, kadr 600–750**
Ekranda: umurtqa chizig'i to'g'rilanadi, rang qizildan yashilga. Matn: "Kun oxirigacha yengil."
Harakat: to'g'rilanish 0.5 s, rang o'tishi bilan bir vaqtda. Kadr kamida 1.5 s turadi.
Kamera: yumshoq pull-back.

**Sahna 5 · Brend + CTA — 0:12.5–0:15, kadr 750–900**
Ekranda: Brend logosi, narx yoki aksiya, tugma: "Ariza qoldiring →".
Harakat: logo build, tugma press() bilan "bosiladi", 2 marta yengil pulse.
Kamera: sekin push-in oxirigacha.

---

## Namuna B — Infografika (agro-texnika tipidagi B2B), 20 s, 16:9

**Sahna 1 · Hook (0–3 s):** katta raqam sanaladi 0 → [natija raqami], ostida birlik ("tonna / gektar").
**Sahna 2 · Muammo (3–8 s):** an'anaviy usul: 3 ta xarajat kartasi birma-bir, har biri qizil minus bilan.
**Sahna 3 · Yechim (8–14 s):** tizim sxemasi — komponentlar chiziq bilan ulanadi, oqim strelkalari harakatlanadi.
**Sahna 4 · Natija (14–17 s):** ikki ustunli grafik: "oldin / keyin", ustunlar ~1 s da o'sadi.
**Sahna 5 · CTA (17–20 s):** logo, telefon/Telegram, "Konsultatsiya oling".

---

## Namuna C — Logo sting, 4 s, 1:1 va 16:9

**0–1.2 s:** logo elementlari bo'laklarda markazga yig'iladi (stagger, overshoot).
**1.2–2.5 s:** brend nomi harfma-harf, offset bilan.
**2.5–4 s:** shior pastdan, hammasi sekin drift bilan turadi. Oxirgi kadr toza, reels yakuniga qo'shish mumkin.

---

## Namuna D — B2B jarayon (qadoq ishlab chiqarish tipidagi), 30 s, 16:9

**Sahna 1 (0–4 s):** savol: "Brendingiz flakoni hali ham katalogdanmi?"
**Sahna 2 (4–10 s):** muammo: bir xil flakonlar qatori, sizniki ajralib turmaydi.
**Sahna 3 (10–22 s):** jarayon 4 qadami — brif → 3D maket → namuna → partiya. Har qadam ikonka + qisqa matn, chiziq bo'ylab progress.
**Sahna 4 (22–26 s):** natija: sizning flakoningiz qator ichidan ko'tarilib ajralib chiqadi.
**Sahna 5 (26–30 s):** logo + "Namuna buyurtma qiling".
