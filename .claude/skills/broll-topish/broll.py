#!/usr/bin/env python3
"""Pexels'dan haqiqiy (AI emas) kinematografik B-roll qidirish va yuklab olish.

Ishlatish:
  broll.py search "<inglizcha so'rov>" [--n 8] [--orientation portrait|landscape|square] [--min 4] [--max 30]
  broll.py get <video_id> [--out papka] [--height 1920]

API kalit tarmoq proksisi orqali avtomatik qo'shiladi (Authorization sarlavhasi).
Agar PEXELS_API_KEY muhit o'zgaruvchisi bo'lsa, o'shani ishlatadi.
"""
import argparse, json, os, subprocess, sys, urllib.parse, urllib.request

API = "https://api.pexels.com/videos"
HERE = os.path.dirname(os.path.abspath(__file__))


def _req(url):
    key = os.environ.get("PEXELS_API_KEY", "proxy-injects-key")
    r = urllib.request.Request(url, headers={"Authorization": key, "User-Agent": "broll-topish/1.0"})
    with urllib.request.urlopen(r, timeout=30) as f:
        return json.load(f)


def _best_file(v, want_h):
    files = [f for f in v.get("video_files", []) if f.get("file_type") == "video/mp4" and f.get("height")]
    if not files:
        return None
    # eng yaqin, lekin want_h dan past bo'lmagan; bo'lmasa eng kattasi
    ok = sorted([f for f in files if max(f["width"], f["height"]) >= want_h], key=lambda f: f["width"] * f["height"])
    return ok[0] if ok else max(files, key=lambda f: f["width"] * f["height"])


def search(q, n, orientation, dmin, dmax):
    params = {"query": q, "per_page": min(80, n * 3), "size": "medium"}
    if orientation:
        params["orientation"] = orientation
    data = _req(f"{API}/search?" + urllib.parse.urlencode(params))
    out = []
    for v in data.get("videos", []):
        if not (dmin <= v.get("duration", 0) <= dmax):
            continue
        out.append({
            "id": v["id"], "duration": v["duration"], "w": v["width"], "h": v["height"],
            "author": v.get("user", {}).get("name"), "page": v.get("url"),
            "thumb": v.get("image"),
        })
        if len(out) >= n:
            break
    print(json.dumps(out, ensure_ascii=False, indent=1))


def get(vid, out, want_h):
    v = _req(f"{API}/videos/{vid}")
    f = _best_file(v, want_h)
    if not f:
        sys.exit("mp4 fayl topilmadi")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, f"pexels_{vid}.mp4")
    urllib.request.urlretrieve(f["link"], path)
    meta = {"id": vid, "file": path, "w": f["width"], "h": f["height"], "fps": f.get("fps"),
            "duration": v["duration"], "author": v.get("user", {}).get("name"), "page": v.get("url"),
            "license": "Pexels License (bepul, tijorat uchun ruxsat, manba ko'rsatish ixtiyoriy)"}
    with open(os.path.join(out, "credits.jsonl"), "a") as c:
        c.write(json.dumps(meta, ensure_ascii=False) + "\n")
    # ko'zdan kechirish uchun 6 kadrli kontakt-varaq
    sheet = path.replace(".mp4", "_sheet.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vf",
                    f"fps=6/{max(1, v['duration'])},scale=240:-1,tile=6x1", "-frames:v", "1", sheet])
    meta["sheet"] = sheet
    print(json.dumps(meta, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search"); s.add_argument("q"); s.add_argument("--n", type=int, default=8)
    s.add_argument("--orientation", default="portrait"); s.add_argument("--min", type=int, default=3)
    s.add_argument("--max", type=int, default=40)
    g = sp.add_parser("get"); g.add_argument("id"); g.add_argument("--out", default="broll")
    g.add_argument("--height", type=int, default=1920)
    a = ap.parse_args()
    if a.cmd == "search":
        search(a.q, a.n, a.orientation if a.orientation != "any" else None, a.min, a.max)
    else:
        get(a.id, a.out, a.height)
