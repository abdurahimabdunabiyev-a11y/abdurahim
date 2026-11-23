#!/usr/bin/env python3
"""Brend logotipini qora fonli rangli PNG qiladi (yumaloq kvadrat kartaga joylash uchun).

Ishlatish:
  python3 logo_png.py meta "#2D8CFF" --out logos/k            # Simple Icons CDN (foydalanuvchi skilli ruxsat bergan manba)
  python3 logo_png.py claude "#D97757" --out logos/k
  python3 logo_png.py --svg higgs.svg "#FFFFFF" --out logos/k  # o'z SVG'ingiz (bitta <path>)
Natija: out/<nom>_k.svg.png (1024x1024, fon #0B0B0B). macOS 'qlmanage' bilan rasterlanadi.
Rasmiy sayt SVG'si kerak bo'lsa (masalan Higgsfield): brauzerda sahifani oching, JS bilan `svg.hf-logo__glyph`.outerHTML ni oling.
"""
import argparse, os, re, subprocess, sys, tempfile, urllib.request
ap = argparse.ArgumentParser(); ap.add_argument("name", nargs="?"); ap.add_argument("color")
ap.add_argument("--svg"); ap.add_argument("--out", default="logos/k"); ap.add_argument("--bg", default="#0B0B0B"); ap.add_argument("--pad", type=float, default=7)
a = ap.parse_args()
if a.svg: src = open(a.svg).read(); nm = os.path.splitext(os.path.basename(a.svg))[0]
else:
    nm = a.name; src = urllib.request.urlopen(f"https://cdn.jsdelivr.net/npm/simple-icons@14.15.0/icons/{nm}.svg").read().decode()
m = re.search(r'viewBox="([\d.\- ]+)"', src); vb = [float(v) for v in m.group(1).split()] if m else [0, 0, 24, 24]
paths = "".join(re.findall(r'<path[^>]*/>', src, re.S))
paths = re.sub(r'fill="[^"]*"', "", paths)
x0, y0, w, h = vb[0] - a.pad, vb[1] - a.pad, vb[2] + 2 * a.pad, vb[3] + 2 * a.pad
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {w} {h}" width="1024" height="1024"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="{a.bg}"/><g fill="{a.color}">{paths}</g></svg>'
os.makedirs(a.out, exist_ok=True)
tmp = os.path.join(tempfile.mkdtemp(), f"{nm}_k.svg"); open(tmp, "w").write(svg)
subprocess.run(["qlmanage", "-t", "-s", "1024", "-o", a.out, tmp], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(os.path.join(a.out, f"{nm}_k.svg.png"))
