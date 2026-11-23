# Ish papkasi tizimi (CLAUDE.md)

> Asosiy ish papkangizga (masalan `ISHLAR/`) `CLAUDE.md` qilib qo'ying. `<Kimniki>` o'rniga o'z brend/mijoz nomlaringizni yozing.

| Papka | Vazifa |
|---|---|
| `01-Loyihalar` | Mijoz/brend loyihalari: har brend o'z papkasida (brend.md, materiallar/, strategiya) |
| `02-Shaxsiy-brend` | O'z videolarim, strategiya va natijalar. `videolar/` ga faqat yakuniy versiya |
| `03-Montaj` | Barcha montaj ishlari |
| `04-Ssenariylar` | Barcha ssenariylar va ovoz matnlari |
| `05-Goyalar-raskadrovka` | G'oyalar, raskadrovka, syomka ro'yxati |
| `06-Resurslar` | `sfx/`, `musiqa/`, `shriftlar/` |

## Bir xil nom qoidasi
`03`, `04`, `05` ichida birinchi daraja: **kimniki** (`Shaxsiy-brend/`, `<Brend-1>/`, `<Brend-2>/`).
Ikkinchi daraja: **video**. Bitta video hamma joyda bir xil qisqa nom bilan yuradi:

```
05-Goyalar-raskadrovka/Shaxsiy-brend/video-nomi.md
04-Ssenariylar/Shaxsiy-brend/video-nomi.md
03-Montaj/Shaxsiy-brend/video-nomi/
02-Shaxsiy-brend/videolar/video-nomi.mp4   ← tayyor video
```

Oqim: **G'oya/raskadrovka → Ssenariy → Syomka → Montaj → Tayyor video**

## Montaj papkasi ichida
```
03-Montaj/<Kimniki>/<video-nomi>/
  manba/    — kamera fayllari, ekran yozuvlari, referens kadrlar
  ovoz/     — ovoz yozuvi, musiqa, SFX
  loyiha/   — AE / Premiere / Remotion / HyperFrames loyihasi
  render/   — chiqqan videolar: v1, v2 ... (eskisi o'chirilmaydi)
```

## Qaysi skill qachon
- "montaj usulida", "mening stilimda" → `mustafo-montaj-usuli` (yoki o'zingizga moslagan nusxasi)
- "zonali montaj", "reels montaj qil" → `reels-zonali-montaj`
- "shaxsiy brend montaj" → `shaxsiy-brend-video-edit`
- Kod orqali motion / reklama → `montaj-motion` yoki `hyperframes`
- SFX qo'shish → `real-sfx`
- Ovozni tekshirish → `earshot`
- Ssenariy → `viral-reels-scriptwriter`
- Raskadrovka → `video-storyboard`

## Umumiy qoidalar
- Sessiya qaysi papkada ochilgan bo'lsa, faqat shu papkaning ishi qilinadi. Boshqa bosqich kerak bo'lsa, aytiladi.
- Boshqa papkalardagi fayllarni o'qish mumkin, o'zgartirish faqat o'z papkasida.
- Ruxsatsiz hech narsa sotib olinmaydi, joylanmaydi, yuborilmaydi. Pullik generatsiyadan oldin narx aytiladi.
- Fayl o'chirish yoki ko'chirishdan oldin ro'yxat ko'rsatiladi va ruxsat so'raladi.
- Remotion/Node loyihalarini exFAT fleshkada qurmang (node_modules buziladi): ichki diskda quring, tayyor mp4 ni `render/` ga ko'chiring.
