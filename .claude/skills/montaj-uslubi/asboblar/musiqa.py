#!/usr/bin/env python3
"""Mixkit musiqa (Mixkit Stock Music Free License — tijoratda bepul, atribusiya shart emas).
  python3 musiqa.py qidir "cinematic"          (yoki teg: --teg corporate)
  python3 musiqa.py ol 623 musiqa/             (mp3 yuklab oladi + credits.jsonl)
Foydali so'zlar: cinematic, epic, corporate, inspiring, dark, suspense, tension, ambient, upbeat, emotional, technology, hip hop."""
import sys, re, json, urllib.request, os
UA = {'User-Agent': 'Mozilla/5.0'}
def page(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode('utf-8', 'ignore')
def items(h):
    out = []
    for m in re.finditer(r'\{"@id":"[^"]*","@type":"MusicRecording".*?"encodingFormat"', h):
        d = m.group(0)
        g = lambda k: (re.search(rf'"{k}":"([^"]*)"', d) or [None, ''])[1]
        u = g('url'); out.append({'id': re.search(r'/music/(\d+)/', u).group(1) if u else '', 'nom': g('name'), 'janr': g('genre'), 'muallif': g('byArtist'), 'davom': g('duration'), 'url': u})
    return out
if sys.argv[1] == 'qidir':
    q = sys.argv[2]
    u = f'https://mixkit.co/free-stock-music/tag/{q}/' if '--teg' in sys.argv else f'https://mixkit.co/free-stock-music/discover/{urllib.parse.quote(q)}/' if False else f'https://mixkit.co/free-stock-music/discover/{q.replace(" ", "-")}/'
    try: h = page(u)
    except Exception: h = page(f'https://mixkit.co/free-stock-music/tag/{q.replace(" ", "-")}/')
    for it in items(h): print(f"{it['id']:>5}  {it['davom']:>9}  {it['janr']:<14} {it['nom']} — {it['muallif']}")
elif sys.argv[1] == 'ol':
    i, d = sys.argv[2], sys.argv[3]; os.makedirs(d, exist_ok=True)
    u = f'https://assets.mixkit.co/music/{i}/{i}.mp3'; p = os.path.join(d, f'mixkit_music_{i}.mp3')
    open(p, 'wb').write(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read())
    open(os.path.join(d, 'credits.jsonl'), 'a').write(json.dumps({'id': i, 'url': u, 'license': 'Mixkit Stock Music Free License'}) + '\n'); print('OK', p)
