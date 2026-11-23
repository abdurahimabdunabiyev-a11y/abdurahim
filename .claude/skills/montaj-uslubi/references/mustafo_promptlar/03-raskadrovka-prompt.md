# Raskadrovka (storyboard) prompti

> `video-storyboard` skilli bilan birga ishlaydi (havola `GITHUB-SKILLAR.md` da). Buni raskadrovka papkangizga `CLAUDE.md` qilib qo'ying yoki chatga shu holicha tashlang.

## Ishlatish
Claude'ga yozing: **"Mana referens: <Instagram havola>. Mening g'oyam: <1–2 gap>. Raskadrovka qilib ber."**

## Qoidalar
1. **Referensni ko'r:** havolani brauzerda och (`instagram.com/reels/<ID>/` shakli login'siz ochiladi), `video.currentTime` + pauza bilan kadrma-kadr ko'r. Har kesimni yoz: soniya, kadr o'lchami (umumiy/o'rta/yaqin/detal), kamera harakati (panorama, dolly, qo'lda), nima bo'layapti, o'tish turi. Referensdan faqat tuzilma va kamera tili olinadi, matn so'zma-so'z ko'chirilmaydi.
2. **G'oya bilan birlashtir:** referens ritmi + mening mavzum → kadrlar jadvali. Rasm chizishdan OLDIN jadvalni ko'rsat va tasdiq ol.
3. **Uslub:** qora-oq qalam/marker eskiz (klassik kino raskadrovkasi), kulrang soya; kadr ustida kamera strelkalari va qisqa yozuvlar ("PAN", "ZOOM IN"). Fotorealistik emas.
4. **Format:** reels uchun har panel **9:16 vertikal**, YouTube uchun 16:9. Panel soni: ≤9 s → 9, ≤12 s → 12, ko'p bo'lsa 16; uzun video bir nechta varaqqa bo'linadi.
5. **Rasm generatsiyasi faqat ruxsat bilan:** avval model va narxni ayt.
6. **Men kadrda bo'lsam:** fotoimni qahramon referensi sifatida ber (yuz, soch, kiyim hamma panelda bir xil).
7. **Natija:** `raskadrovka-01.png` + `raskadrovka-01.md` (kadr, soniya, kamera, harakat, ovoz/matn) + `referens-tahlil.md`.

## G'oya fayli shabloni
```
# <Sarlavha>
Holat: xom | tanlangan | ssenariyda | olindi | montajda | chiqdi
Hook (birinchi 2 soniya):
Asosiy fikr (1 gap):
Nega ko'rishadi:
Format: talking-head | ekran yozuvi | AI-generatsiya | aralash
Referens:

## Raskadrovka
| # | Soniya | Kadr (yaqin/o'rta/umumiy) | Ekranda nima | Ovoz / matn | Manba (kamera / AI / ekran) |

## Syomka ro'yxati
Joy, vaqt, jihozlar, kiyim/rekvizit, dublar ✓
```
