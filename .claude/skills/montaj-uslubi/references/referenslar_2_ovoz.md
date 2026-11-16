# Referenslar 2-to'plam (N1–N8) — ovoz (earshot bilan "eshitilgan")

Usul: `earshot timeline --detail high` + `earshot critique` har bir videoga. Teglar — modelning taxmini (hint), raqamlar — o'lchov.

## Umumiy o'lchovlar
| | N1 | N2 | N3 | N4 | N5 | N6 | N7 | N8 |
|---|---|---|---|---|---|---|---|---|
| Verdict (launch profili) | launch-grade | launch-grade | close | launch-grade | launch-grade | launch-grade | close | launch-grade |
| LUFS / LRA | −14.1 / 1.7 | −14.1 / 1.8 | −16.3 / 3.7 | −13.8 / 2.0 | −14.2 / 3.0 | −14.4 / 2.7 | −14.3 / 3.0 | −14.1 / 1.6 |
| Musiqa bo'limlari | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 4 |
| Kesishda ovoz (±100 ms) | 93% | 91% | 94% | 85% | 65% | 84% | 89% | 80% |
| Salient hit /s | 1.42 | 1.68 | 1.75 | 1.82 | 1.76 | 1.92 | 1.96 | 1.47 |
| Stereo (side/mid) | −9 dB | −44 dB | −26 dB | −31 dB | −21 dB | −23 dB | −29 dB | −24 dB |
| "Chat pop" UI effektlar | 10 | 12 | 14 | 31 | 16 | 27 | 36 | 13 |
| Sub bass drop | 1 | 10 | 2 | 5 | 12 | 2 | 4 | 5 |
| Punchy impact hit | 2 | 9 | 3 | 10 | — | — | — | 3 |
| Whip/air whoosh | 1 | 7 | 3 | 1 | 1 | 4 | 2 | 2 |
| Boshqa | glockenspiel, celesta, reverse cymbal, water drop | kick, pluck | pluck, reverse cymbal ×3, riser ×3 | pluck, glockenspiel | orchestral stab, riser, pluck | orchestral stab ×2, reverse cymbal | pluck, glockenspiel, cork pop, ding | pluck |

## Musiqa
- Har bir videoda musiqa **3–5 bo'limga** bo'linadi, bo'lim har **6–15 s** da almashadi (trek, janr yoki aranjirovka) — odatda mavzu/bo'lim almashganda.
- Janrlar (earshot teglari): **inspirational corporate** (ko'pincha boshida), **trap beat**, **hip-hop heavy bass**, **techno**, **funk**, **glitch hop**. Deyarli hammasida "**vocal chop**" va "confident and cool" kayfiyat.
- Barqaror beat grid yo'q (pulse clarity < 0.15) — musiqa nutq ostida fon, ritm ustunlik qilmaydi.
- **Stop-down**: 0.3–0.5 s qisqa "tushish" (N7 da 5 ta, N6 da 2 ta) — dramatik pauza, keyin kuchli qaytish.
- Oxirgi qism (CTA) asosiy qismdan **past emas** (median −0.7 LU).

## SFX qonuniyatlari
- **Eng ko'p — UI "pop" (chat message pop / bubble pop)**: har bir matn bloki, karta, ikonka, avatar, pill paydo bo'lganda. 10–36 ta / video.
- **Ko'p SFX kesishga emas — grafika paydo bo'lishiga** joylashgan (kesishgacha 0.3–2.5 s). Kesishlarda: whip whoosh, impact.
- **Sub bass drop** — muhim fakt/raqam/sarlavha ostida (N5 da 12 ta).
- **Punchy impact** — bo'lim boshi, katta matn kirishi.
- **Pluck / glockenspiel / celesta** notalari — ijobiy "ding" urg'u, ro'yxat elementlari.
- **Reverse cymbal / riser** — reveal oldidan (kam: 1–3 ta).
- Salient hit zichligi reels'da **1.4–2.0 / s** (launch filmlardan zichroq — bu me'yor).

## earshot bank mosligi (bizning SFX)
| Referensdagi | earshot bank ID |
|---|---|
| chat message pop / bubble pop | `ui_pop/soft`, `ui_pop/boop`, `ui_pop/blip`, `ui_pop/wide`, `drip/bubble` |
| sub bass drop | `cut_hit/sub`, `cut_hit/kick` (--pitch F1/G1) |
| punchy impact hit | `cut_hit/punch`, `whoosh_big/thump` |
| whip pan whoosh | `whoosh_fast/whip`, `whoosh_fast/crisp`, `swish/bright` |
| fast air whoosh | `whoosh_fast/tight`, `swish/flick` |
| pluck / glockenspiel / celesta | `mallet/pluck`, `mallet/glock`, `mallet/celesta`, `mallet/flourish` |
| reverse cymbal swell | `reverse_swell/cymbal`, `reverse_swell/short` |
| riser | `riser/dark`, `riser/build` |
| notification ding | `notify/mid_tine`, `fit/bell/small_bell` |
| typing (typewriter) | `fit/key/*`, `typing` |
