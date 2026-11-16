#!/usr/bin/env python3
"""Haqiqiy (AI emas) kinematografik B-roll qidirish va yuklab olish.

Asosiy manba: Mixkit (bepul, kalitsiz, Mixkit Free License — videolarda tijorat
maqsadida ham ishlatish mumkin). Pexels ixtiyoriy (API kalit kerak).

Ishlatish:
  broll.py search "<inglizcha so'rov>" [--n 10] [--page 1]
  broll.py get <id> [--out papka] [--vertical]
  broll.py search "<so'rov>" --source pexels   (faqat Pexels kaliti bo'lsa)
"""
import argparse, json, os, re, subprocess, sys, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (broll-topish)"}


def _get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as f:
        return f.read()


def _exists(url):
    try:
        req = urllib.request.Request(url, headers=UA, method="HEAD")
        with urllib.request.urlopen(req, timeout=20) as f:
            return f.status == 200
    except Exception:
        return False


# ---------------- Mixkit ----------------
def mixkit_search(q, n, page):
    slug = re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")
    url = f"https://mixkit.co/free-stock-video/{slug}/"
    if page > 1:
        url += f"?page={page}"
    try:
        html = _get(url).decode("utf-8", "ignore")
    except Exception as e:
        sys.exit(f"Qidiruv ishlamadi: {e}")
    seen, out = set(), []
    for m in re.finditer(r'/free-stock-video/([a-z0-9-]+)-(\d+)/', html):
        title, vid = m.group(1), m.group(2)
        if vid in seen:
            continue
        seen.add(vid)
        out.append({"id": vid, "title": title.replace("-", " "),
                    "page": f"https://mixkit.co/free-stock-video/{title}-{vid}/",
                    "preview": f"https://assets.mixkit.co/videos/{vid}/{vid}-360.mp4"})
        if len(out) >= n:
            break
    print(json.dumps(out, ensure_ascii=False, indent=1))


def mixkit_get(vid, out, vertical):
    os.makedirs(out, exist_ok=True)
    src = None
    for q in ("2160", "1080", "720", "360"):
        u = f"https://assets.mixkit.co/videos/{vid}/{vid}-{q}.mp4"
        if _exists(u):
            src = u
            break
    if not src:
        sys.exit("Video fayl topilmadi")
    path = os.path.join(out, f"mixkit_{vid}.mp4")
    with open(path, "wb") as f:
        f.write(_get(src))
    _finish(path, {"id": vid, "source": "mixkit", "url": src,
                   "license": "Mixkit Free License (bepul, tijorat uchun ruxsat)"}, out, vertical)


# ---------------- Pexels (ixtiyoriy) ----------------
def pexels_search(q, n, page):
    key = os.environ.get("PEXELS_API_KEY", "proxy-injected")
    url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": q, "per_page": n, "page": page, "orientation": "portrait"})
    req = urllib.request.Request(url, headers={**UA, "Authorization": key})
    with urllib.request.urlopen(req, timeout=30) as f:
        data = json.load(f)
    print(json.dumps([{"id": v["id"], "duration": v["duration"], "w": v["width"], "h": v["height"],
                       "page": v["url"]} for v in data.get("videos", [])], indent=1))


# ---------------- umumiy ----------------
def _probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height:format=duration", "-of", "json", path],
                       capture_output=True, text=True)
    d = json.loads(r.stdout)
    s = d["streams"][0]
    return s["width"], s["height"], float(d["format"]["duration"])


def _finish(path, meta, out, vertical):
    w, h, dur = _probe(path)
    meta.update({"file": path, "w": w, "h": h, "duration": round(dur, 1)})
    if vertical and w > h:
        vpath = path.replace(".mp4", "_9x16.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vf",
                        "crop=ih*9/16:ih,scale=1080:1920", "-an", "-c:v", "libx264", "-crf", "18",
                        "-preset", "fast", vpath], check=True)
        meta["file_9x16"] = vpath
    sheet = path.replace(".mp4", "_sheet.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vf",
                    f"fps=6/{max(1.0, dur)},scale=240:-1,tile=6x1", "-frames:v", "1", sheet])
    meta["sheet"] = sheet
    with open(os.path.join(out, "credits.jsonl"), "a") as c:
        c.write(json.dumps(meta, ensure_ascii=False) + "\n")
    print(json.dumps(meta, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search"); s.add_argument("q"); s.add_argument("--n", type=int, default=10)
    s.add_argument("--page", type=int, default=1); s.add_argument("--source", default="mixkit")
    g = sp.add_parser("get"); g.add_argument("id"); g.add_argument("--out", default="broll")
    g.add_argument("--vertical", action="store_true"); g.add_argument("--source", default="mixkit")
    a = ap.parse_args()
    if a.cmd == "search":
        (pexels_search if a.source == "pexels" else mixkit_search)(a.q, a.n, a.page)
    else:
        if a.source == "pexels":
            sys.exit("Pexels yuklab olish hozircha o'chirilgan (kalit yo'q)")
        mixkit_get(a.id, a.out, a.vertical)
