"""fontsource woff2 -> TTF, aniq oila nomi bilan (har qalinlik alohida oila: "<Family> <Weight>")."""
import glob, json, os, re, sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

S = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
DEST = os.path.expanduser("~/.fonts/montaj")
os.makedirs(DEST, exist_ok=True)
WN = {100: "Thin", 200: "ExtraLight", 300: "Light", 400: "Regular", 500: "Medium", 600: "SemiBold",
      700: "Bold", 800: "ExtraBold", 900: "Black"}

def rename(font, family):
    name = font["name"]
    for rec in list(name.names):
        if rec.nameID in (1, 2, 4, 6, 16, 17, 21, 22):
            name.removeNames(nameID=rec.nameID)
    ps = re.sub(r"[^A-Za-z0-9-]", "", family.replace(" ", "-"))
    for nid, val in ((1, family), (2, "Regular"), (4, family), (6, ps), (16, family), (17, "Regular")):
        name.setName(val, nid, 3, 1, 0x409)
        name.setName(val, nid, 1, 0, 0)
    if "OS/2" in font:
        font["OS/2"].fsSelection = (font["OS/2"].fsSelection & ~0b1100001) | 0b1000000  # REGULAR bit

made = []
for pkg in sorted(glob.glob(f"{S}/x/fontsource-*")):
    meta = json.load(open(glob.glob(f"{pkg}/package/package.json")[0]))
    fam = meta.get("description", "")
    m = re.search(r'"?([A-Z][\w ]+?)"? (?:font|typeface)', meta.get("description", ""))
    family = None
    mpath = glob.glob(f"{pkg}/package/metadata.json")
    if mpath:
        family = json.load(open(mpath[0])).get("family")
    if not family:
        family = m.group(1) if m else os.path.basename(pkg)
    if "variable" in pkg:
        continue
    for f in glob.glob(f"{pkg}/package/files/*-latin-*-*.woff2"):
        b = os.path.basename(f)
        if "-ext-" in b:
            continue
        mm = re.search(r"-latin-(\d+)-(normal|italic)\.woff2$", b)
        if not mm:
            continue
        w, st = int(mm.group(1)), mm.group(2)
        fullfam = f"{family} {WN.get(w, w)}" + (" Italic" if st == "italic" else "")
        t = TTFont(f); t.flavor = None; rename(t, fullfam)
        out = f"{DEST}/{fullfam.replace(' ', '')}.ttf"; t.save(out); made.append(fullfam)

# Druk Wide muqobili: Archivo variable -> wdth 125 (Expanded) instansiyalari
for f in glob.glob(f"{S}/x/fontsource-variable-archivo*/package/files/*latin-wdth-normal.woff2") + \
         glob.glob(f"{S}/x/fontsource-variable-archivo*/package/files/*latin-full-normal.woff2"):
    if "-ext-" in os.path.basename(f):
        continue
    base = TTFont(f); base.flavor = None
    axes = {a.axisTag: (a.minValue, a.maxValue) for a in base["fvar"].axes}
    if "wdth" not in axes:
        continue
    for w in (700, 800, 900):
        inst = instancer.instantiateVariableFont(TTFont(f), {"wght": min(w, axes["wght"][1]), "wdth": axes["wdth"][1]})
        inst.flavor = None
        fullfam = f"Archivo Expanded {WN[w]}"
        rename(inst, fullfam); inst.save(f"{DEST}/{fullfam.replace(' ', '')}.ttf"); made.append(fullfam)
    break
print(len(made), "shrift"); print(sorted(set(m.rsplit(' ', 1)[0] if m.split()[-1] in WN.values() else m for m in made)))
