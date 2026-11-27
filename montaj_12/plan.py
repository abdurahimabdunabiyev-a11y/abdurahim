"""Uy narxi reels — to'liq montaj rejasi (bitta manba haqiqat).
SEG: kesilgan bo'laklar (manba, boshi, oxiri). PH: iboralar (manba vaqtida) — subtitr. SHOT: kadr rejasi (chiqish vaqti, iboraga bog'langan)."""
X = '/tmp/claude-0/-home-user-abdurahim/95b55091-90bf-59e6-b39c-f98dfd0220b8/scratchpad/xom4/'
FACE = {'IMG_7007': (.591, .448), 'IMG_7008': (.553, .437), 'IMG_7010': (.514, .455), 'IMG_7011': (.501, .468)}
SEG = [('IMG_7007', 0.00, 7.60),
       ('IMG_7008', 3.00, 4.85), ('IMG_7008', 5.15, 11.95), ('IMG_7008', 12.25, 19.95),
       ('IMG_7010', 3.02, 9.95), ('IMG_7010', 10.18, 13.42), ('IMG_7010', 13.74, 17.05), ('IMG_7010', 17.36, 19.60), ('IMG_7010', 19.90, 23.56), ('IMG_7010', 23.82, 26.95),
       ('IMG_7011', 2.18, 5.50), ('IMG_7011', 5.80, 12.45), ('IMG_7011', 12.74, 15.73), ('IMG_7011', 16.25, 23.28), ('IMG_7011', 23.66, 28.44), ('IMG_7011', 28.71, 33.08),
       ('IMG_7011', 77.90, 86.42), ('IMG_7011', 86.82, 89.76),
       ('IMG_7011', 112.42, 127.18), ('IMG_7011', 127.47, 129.20)]
# iboralar: (manba, boshi, oxiri, matn, kadr, param)
#  kadr: close | wide | broll:<id>:<manba boshi> | card:<nomi>
PH = [
 ('IMG_7007', 0.00, 1.02, "2027-yilda", 'close', None),
 ('IMG_7007', 1.02, 2.76, "uylar narxi keskin oshib ketadimi?", 'broll', '32529:1.0'),
 ('IMG_7007', 3.24, 7.60, "Namanganliklar, sizlar uchun ajoyib bir statistikani birgalikda ko'rib chiqamiz.", 'wide', None),
 ('IMG_7008', 3.04, 4.79, "Oxirgi 10 yilda uylar", 'close', None),
 ('IMG_7008', 5.20, 8.60, "narxi taxminan 3–4 barobar,", 'broll', '5020:2.0'),
 ('IMG_7008', 8.60, 11.88, "hatto markazlarda 5 barobargacha oshgan.", 'broll', '10030:1.0'),
 ('IMG_7008', 12.29, 14.10, "Ya'ni 2016-yilda", 'wide', None),
 ('IMG_7008', 14.10, 19.80, "150–200 millionlik uylar hozirda 600–800 million so'mgacha sotilmoqda.", 'card', 'narx'),
 ('IMG_7010', 3.09, 9.88, "Oxirgi bir yilda esa uylarning tannarxi o'sishi 6,5–7% ni tashkil qilgan.", 'close', 'p67'),
 ('IMG_7010', 10.24, 13.36, "Ya'ni 2025-yildagi uylar 2026-yilga kelib 6,5–7% ga oshgan.", 'wide', None),
 ('IMG_7010', 13.80, 16.99, "Endi 2027-yil nima bo'ladi? Narx oshadimi, kamayadimi?", 'close', None),
 ('IMG_7010', 17.42, 19.54, "2027-yilda usta haqi oshishi,", 'broll', '20874:0.5'),
 ('IMG_7010', 19.95, 21.40, "qurilish materiallarining oshishi,", 'broll', '31455:1.0'),
 ('IMG_7010', 21.46, 24.30, "aholi sonining o'zgarishi, pul inflyatsiyasi —", 'broll', '18296:0.5'),
 ('IMG_7010', 24.30, 26.90, "hammasini hisoblab,", 'broll', '47416:1.0'),
 ('IMG_7011', 2.22, 5.45, "katta ehtimol bilan bu yil ham uylarning tannarxi yana oshadi.", 'close', None),
 ('IMG_7011', 5.84, 8.00, "Bundan tashqari, qurilishga yangilik kiritilyapti.", 'wide', None),
 ('IMG_7011', 8.00, 12.40, "Eskrou tizimi qo'llanilishi mumkin. Agar eskrou tizimi qo'llanilsa,", 'close', 'eskrou'),
 ('IMG_7011', 12.78, 15.68, "yana 7,5% dan 15% gacha o'zgarish bo'lishi mumkin.", 'broll', '25480:1.0'),
 ('IMG_7011', 16.29, 20.20, "Umumiy statistikani olsak, taxminan 15% gacha tannarx oshishi mumkin.", 'wide', None),
 ('IMG_7011', 20.20, 27.00, "Ya'ni siz 400 millionlik uyni olaman desangiz, 15% oshsa, 60 million ustiga qo'shiladi.", 'close', None),
 ('IMG_7011', 27.00, 33.04, "Ya'ni hozir 400 millionga olmoqchi bo'lgan uyingiz 2027-yilda 450–460 million bo'lishi mumkin.", 'card', 'uy400'),
 ('IMG_7011', 77.94, 83.22, "Shuning uchun uy olishni niyat qilgan bo'lsangiz, bu niyatingizga 2026-yilda erishishga harakat qiling,", 'close', None),
 ('IMG_7011', 83.24, 86.40, "chunki 2027-yilda yana uylar narxi oshadi", 'wide', None),
 ('IMG_7011', 86.84, 89.72, "va orzular kechga qolib ketishi mumkin.", 'broll', '12877:0.5'),
 ('IMG_7011', 112.47, 117.40, "Agar sizga Namangan markazida barcha qulayliklarga ega loyihadan xonadon kerak bo'lsa,", 'wide', None),
 ('IMG_7011', 117.48, 119.50, "Bunyodkor City loyihasi aynan siz uchun.", 'card', 'brand'),
 ('IMG_7011', 119.60, 121.70, "Hozirda juda katta aksiyalar ketyapti.", 'close', None),
 ('IMG_7011', 121.82, 125.60, "Mana shu raqamlarga aloqaga chiqib, savdo ofisimizga tashrif buyursangiz,", 'wide', None),
 ('IMG_7011', 125.72, 129.15, "o'zingizga mos xonadonni katta chegirmada xarid qilishingiz mumkin.", 'broll', '15064:0.5'),
]
FPS = 30
def out_time(src, t):
    """Manba vaqtini chiqish vaqtiga o'tkazish (kesilgan joyga tushsa — eng yaqin chegaraga)."""
    acc = 0.0; best = None
    for s, a, b in SEG:
        d = round((b - a) * FPS) / FPS
        if s == src:
            if a - 1e-6 <= t <= b + 1e-6: return acc + min(t - a, d)
            if best is None or abs(t - a) < best[0]: best = (abs(t - a), acc)
            if abs(t - b) < best[0]: best = (abs(t - b), acc + d)
        acc += d
    return best[1]
TOTAL = sum(round((b - a) * FPS) / FPS for _, a, b in SEG)
def phrases():
    """Iboralar chiqish vaqtida, so'zlar belgilar soniga proporsional taqsimlangan."""
    R = []
    for src, a, b, txt, kind, prm in PH:
        A, B = out_time(src, a), out_time(src, b)
        ws = txt.split(); L = [len(w) + 1 for w in ws]; tot = sum(L); acc = 0; W = []
        for w, l in zip(ws, L):
            W.append([w, round(A + (B - A) * acc / tot, 3)]); acc += l
        R.append(dict(t0=round(A, 3), t1=round(B, 3), txt=txt, words=W, kind=kind, prm=prm, src=src))
    return R
