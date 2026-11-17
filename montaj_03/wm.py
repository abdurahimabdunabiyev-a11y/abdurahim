#!/usr/bin/env python3
"""Wikimedia Commons: qidirish (litsenziya bilan) va yuklash. python3 wm.py search "query" | get "File:..." out.jpg"""
import sys, json, urllib.request, urllib.parse, re
UA = {'User-Agent': 'montaj-bot/1.0 (educational video editing)'}
API = 'https://commons.wikimedia.org/w/api.php'
def q(params):
    u = API + '?' + urllib.parse.urlencode({**params, 'format': 'json'})
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
def clean(h): return re.sub('<[^>]+>', '', h or '').strip()[:60]
if sys.argv[1] == 'search':
    d = q({'action': 'query', 'generator': 'search', 'gsrnamespace': 6, 'gsrsearch': sys.argv[2], 'gsrlimit': int(sys.argv[3]) if len(sys.argv) > 3 else 8,
           'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata'})
    for p in sorted(d.get('query', {}).get('pages', {}).values(), key=lambda p: p.get('index', 0)):
        ii = p['imageinfo'][0]; m = ii.get('extmetadata', {})
        print(f"{p['title'][:70]:70s} {ii['width']}x{ii['height']}  {m.get('LicenseShortName', {}).get('value', '?')}  | {clean(m.get('Artist', {}).get('value'))}")
elif sys.argv[1] == 'get':
    d = q({'action': 'query', 'titles': sys.argv[2], 'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'iiurlwidth': 1400})
    ii = list(d['query']['pages'].values())[0]['imageinfo'][0]; m = ii.get('extmetadata', {})
    url = ii.get('thumburl') or ii['url']
    open(sys.argv[3], 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
    rec = {'file': sys.argv[2], 'url': ii['descriptionurl'], 'license': m.get('LicenseShortName', {}).get('value'), 'artist': clean(m.get('Artist', {}).get('value'))}
    open('foto/wm/credits.jsonl', 'a').write(json.dumps(rec, ensure_ascii=False) + '\n'); print('OK', rec)
