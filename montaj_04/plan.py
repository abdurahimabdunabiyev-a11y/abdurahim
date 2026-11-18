"""Montaj 04 — '3 sabab' reels: yagona reja (base.py va kompozitsiya uchun)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(D, 'sozlar.json')))
WORDS, PARTS, TALK = S['words'], S['parts'], S['total']
H = 2.8                      # hook (B-roll + katta matn) davomiyligi
TOTAL = round(H + TALK, 4)
FPS = 30

def w(i): return WORDS[i][1]   # i-so'z boshlanishi (talk vaqti)

# B-roll oynalari (talk vaqti): (boshi, oxiri, fayl, manbadagi boshlanish)
BR = 'broll/mixkit_%s_9x16.mp4'
BROLL = [
    (w(1), w(4), BR % 45848, 4.0),          # "hammasi omborda bor" -> ombor, yuklagich
    (w(27), w(29), BR % 39462, 1.0),        # "Panelni Xitoydan" -> port
    (w(29), w(32), BR % 4011, 10.0),        # "o'zimiz olib kelamiz" -> kema
    (w(65), w(70), BR % 28000, 2.5),        # "LONGi, Deye, ERA zavodlariga olib" -> samolyot
    (w(70), w(72), BR % 11303, 3.0),        # "ketamiz. Yo'l" -> bulutlar ustida
    (w(72), w(73), BR % 4196, 2.0),         # "mehmonxona" -> mehmonxona xonasi
    (w(73), w(75), BR % 46789, 3.0),        # "ovqat" -> taom
]
HOOK = [(0.0, 0.95, BR % 20806, 1.0), (0.95, 1.9, BR % 31089, 4.0), (1.9, H, BR % 4011, 20.0)]

# Zoom kalitlari har bo'lak ichida: (talk vaqti, zoom, ease) ; bo'laklar orasida keskin kesim (jump-cut punch)
E = 'io'  # easeInOutCubic
ZOOM = {
    'p1a': [(0, 1.10), (w(12) - 0.1, 1.17), (w(12) + 0.45, 1.36), (PARTS[0][2], 1.40)],
    'p1b': [(PARTS[1][1], 1.62), (PARTS[1][1] + PARTS[1][2], 1.68)],
    'p2a': [(PARTS[2][1], 1.28), (PARTS[2][1] + PARTS[2][2], 1.30)],
    'p2b': [(PARTS[3][1], 1.10), (w(32) - 0.05, 1.15), (w(32) + 0.45, 1.34), (w(39), 1.36), (w(39) + 0.4, 1.46), (PARTS[3][1] + PARTS[3][2], 1.48)],
    'p2c': [(PARTS[4][1], 1.42), (w(43) - 0.1, 1.36), (w(43) + 0.5, 1.18), (PARTS[4][1] + PARTS[4][2], 1.16)],
    'p3a': [(PARTS[5][1], 1.12), (w(53) - 0.1, 1.18), (w(53) + 0.6, 1.50), (PARTS[5][1] + PARTS[5][2], 1.54)],
    'p3b': [(PARTS[6][1], 1.20), (w(65), 1.26), (w(75), 1.32), (w(75) + 0.4, 1.56), (PARTS[6][1] + PARTS[6][2], 1.58)],
    'p4':  [(PARTS[7][1], 1.12), (w(80) - 0.05, 1.17), (w(80) + 0.5, 1.38), (PARTS[7][1] + PARTS[7][2], 1.42)],
    'p5':  [(PARTS[8][1], 1.32), (w(93) - 0.2, 1.24), (w(93) + 0.8, 1.06), (PARTS[8][1] + PARTS[8][2], 1.03)],
}
