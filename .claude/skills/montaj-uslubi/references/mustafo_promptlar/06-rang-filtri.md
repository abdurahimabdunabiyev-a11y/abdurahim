# Iliq rang filtri ("C" varianti)

Kamera videosiga yumshoq iliq tus beradi: kontrast deyarli o'zgarmaydi, umumiy to'yinganlik biroz pastda, yashil va sariq-yashil qahrabo tomonga suriladi, teri rangi deyarli o'zgarmaydi. Ikki variantni rad etib, shunga kelganmiz: kuchli "kuzgi" grade terini kuydirdi, juda yumshoq kremsimon variant esa xira chiqdi.

```bash
ffmpeg -i cut.mp4 -vf "curves=all='0/0.015 0.2/0.17 0.5/0.5 0.8/0.81 1/0.95',huesaturation=hue=-22:saturation=-0.35:colors=g,huesaturation=hue=-8:saturation=-0.15:colors=y,colorbalance=rs=0.02:bs=-0.01:rm=0.035:gm=0.005:bm=-0.03:rh=0.02:bh=-0.03,eq=saturation=0.92" -c:a copy cut_grade.mp4
```

Claude'ga ayting: *"Avval bitta kadrda asl va filtrli variantni yonma-yon ko'rsat, keyin butun videoga qo'lla."* Sahna boshqacha bo'lsa ta'siri ham boshqacha bo'ladi.

(`huesaturation` filtri FFmpeg 6+ da bor. Filtr `skills/mustafo-montaj-usuli/grade/` ichida ham bor.)
