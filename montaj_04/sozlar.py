import json, subprocess, numpy as np, soundfile as sf
from faster_whisper import WhisperModel
P = [('p1a',8.28,"Birinchisi, hammasi omborda bor: LONGi, Jinko, ERA, Ronma panellari hamda Deye invertorlari. 10 ta kerakmi, ya 500 tami?"),
 ('p1b',0.88,"Hammasi bor!"),
 ('p2a',0.68,"Ikkinchisi —"),
 ('p2b',6.48,"birinchi qo'ldan va kafolati bilan. Panelni Xitoydan o'zimiz olib kelamiz. O'rtada hech kim yo'q, shuning uchun narxlar ulgurji."),
 ('p2c',1.86,"Chek ham beramiz, kafolat ham."),
 ('p3a',5.08,"Va nihoyat, uchinchisi: bizdan quyosh paneli xarid qilsangiz, Xitoyga mutlaqo bepul ketishingiz mumkin."),
 ('p3b',8.06,"Dekabr oyida 5 ta mijozimizni 7 kunga LONGi, Deye, ERA zavodlariga olib ketamiz. Yo'l, mehmonxona, ovqat — hammasi bizdan."),
 ('p4',4.54,"Biz uyga o'rnatmaymiz. Biz faqat ustanovkachilar, do'konlar va dilerlar bilan ishlaymiz."),
 ('p5',4.64,"Agar sizga taklifimiz qiziq bo'lsa, pastdagi tugmani bosing, biz siz bilan o'zimiz bog'lanamiz.")]
y16, sr = sf.read('talk16.wav', dtype='float32')


m = WhisperModel('large-v3', device='cpu', compute_type='int8')
out, off, parts = [], 0.0, []
for name, d, txt in P:
    seg = y16[int(off*16000):int((off+d)*16000)]
    ss, _ = m.transcribe(seg, language='uz', word_timestamps=True, vad_filter=False)
    W = [(w.word.strip(), w.start, w.end) for s in ss for w in (s.words or []) if w.word.strip()]
    tw = txt.split()
    if W:
        wc = np.cumsum([0] + [len(w[0]) for w in W]); wc = wc / wc[-1]
        ws = np.array([w[1] for w in W] + [W[-1][2]])
        tc = np.cumsum([0] + [len(w) for w in tw]); tc = tc / tc[-1]
        ts = np.interp(tc, wc, ws)
    else:
        ts = np.linspace(0.05, d - 0.05, len(tw) + 1)
    for i, w in enumerate(tw):
        out.append([w, round(off + ts[i], 3), round(off + min(ts[i+1], d), 3)])
    parts.append([name, round(off, 3), d])
    off += d
json.dump({'words': out, 'parts': parts, 'total': off}, open('../sozlar.json', 'w'), ensure_ascii=False, indent=0)
print(off); [print(w) for w in out]
