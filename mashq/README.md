# Mashq kutubxonasi — o'tish va animatsiya shablonlari

HyperFrames tamoyili (pauzadagi GSAP timeline'ni kadrma-kadr seek qilish) bo'yicha o'z rendererimiz:
`node render.mjs scenes/<sahna>.html out/<sahna>.mp4 <sekund>` (Playwright + ffmpeg, 1080x1920, 30 fps).
Yig'ish + SFX (earshot bank) + musiqa + −14 LUFS: `python assemble.py`.

| # | Sahna | Referens | Nima |
|---|---|---|---|
| 1 | `s1_whip.html` | N1 7.2 s | Whip-slide: gorizontal SVG blur (feGaussianBlur "90 0"), 0.28 s, power3 |
| 2 | `s2_card.html` | N3 12 s, N4 2 s | Kartaga kichrayish: scale 0.62 + radius 60 + soya, 0.65 s, power3.inOut; ostida raqam pop |
| 3 | `s3_push.html` | N7 10.8 s | Karta push: kichik karta chetdan kiradi → to'liq ekran |
| 4 | `s4_zoom.html` | N3 19.3 s | Zoom-blur: 5 ta "arvoh" nusxa (radial blur) + oq flash |
| 5 | `s5_arc.html` | N1 1.5–7 s | Bosh atrofida yoy matn (SVG textPath), so'zma-so'z; iyak ostida sariq yoy |
| 6 | `s6_type.html` | N5, N7 | Typewriter oq quti + deterministik miltillovchi kursor |
| 7 | `s7_count.html` | N1 38–49 s | Rolling sanagich (raqam ustunlari) + orqada ulkan xira raqam + sariq lower bar + uchqunlar |
| 8 | `s8_chat.html` | N3, N4 | Chat dialog: chap/o'ng pufakchalar, avatar, back.out pop |

Kadrlar: `assets/frames/<seq>_%04d.jpg` (ffmpeg bilan 1080x1920 ga ajratiladi; gitga kirmaydi).
Eslatma: hyperframes plagini CLI 0.9.57 ni so'raydi, npm'da yo'q (2026-11-16) — shuning uchun o'z renderer.
