#!/usr/bin/env python3
"""Montaj Yuklash sahifasidagi bo'laklarni asl videoga yig'ish.

Ishlatish: yigish.py <uploads hujjati .json> <bo'laklar papkasi> <chiqish.mp4>
Hujjat: ArtifactData list (collection "uploads", out_dir) natijasi.
Bo'laklar: Artifact read (path=<id>) bilan yuklab olingan <id>.txt fayllar.
"""
import base64, json, os, subprocess, sys

doc_path, chunk_dir, out = sys.argv[1:4]
d = json.load(open(doc_path))
d = d.get("data", d)
if d.get("status") != "done":
    sys.exit(f"Yuklama tugallanmagan: status={d.get('status')}")
chunks = sorted(d["chunks"], key=lambda c: c["start"])
pos = 0
with open(out, "wb") as f:
    for c in chunks:
        if c["start"] != pos:
            sys.exit(f"Bo'laklar orasida bo'shliq: {pos} != {c['start']}")
        p = os.path.join(chunk_dir, c["id"] + ".txt")
        raw = open(p, "rb").read()
        data = base64.b64decode(raw) if d.get("encoding") == "base64" else raw
        if len(data) != c["size"]:
            sys.exit(f"{c['id']}: hajm mos emas ({len(data)} != {c['size']})")
        f.write(data)
        pos += len(data)
if pos != d["size"]:
    sys.exit(f"Umumiy hajm mos emas: {pos} != {d['size']}")
probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration:stream=codec_name,width,height,r_frame_rate",
                        "-of", "compact", out], capture_output=True, text=True)
print(f"OK {out} {pos} bayt\n{probe.stdout.strip()}{probe.stderr.strip()}")
