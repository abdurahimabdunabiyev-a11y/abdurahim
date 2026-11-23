# Palitra va geometriya (qisqa jadval)

AE float -> hex: BG #0B0908 | ACC #ED6B38 | ACC2 #FF944D | tugma oxiri #CC4F24 | DEEP #66210B | panel boshi #571D0A | CARDF #151210 | CARDF2 #1D1917 | TXT #F9F6F4 | MUTE #A89E96.
Claude logo rangi #D97757 (faqat logoda). Chegara: oq 14-26%, 2 px.

Geometriya (1080x1920): panel y 245-835, video y 965-1555 (ikkalasi 940x590), subtitr y=900 (60 px), kartalar x 70-1010, radius 54/48.
Instagram safe zona: x 64-960, y 270-1540.

Konstantalar `lib/mustafo_lib.jsx` boshida: `BG ACC ACC2 DEEP CARDF CARDF2 TXT MUTE`, `TOP_CY TOP_H BOT_CY BOT_H CAP_Y CW`. Maketni o'zgartirish kerak bo'lsa, scenes.jsx boshida qayta belgilang (masalan `TOP_CY = 540; TOP_H = 590; BOT_CY = 1260; BOT_H = 590; CAP_Y = 900;`).

Tarix: v1 maketda panel 940x680 va video 940x480 edi, subtitr y=1540 (pastda). Foydalanuvchi videoni kichik topdi, shuning uchun teng o'lcham va o'rtada subtitrga o'tildi.
