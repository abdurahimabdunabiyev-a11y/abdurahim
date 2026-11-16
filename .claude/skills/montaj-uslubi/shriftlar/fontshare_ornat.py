"""Fontshare (ITF Free Font License) shriftlarini aniq nom bilan o'rnatish: <ish papkasi> argument."""
import glob, os, sys
from fontTools.ttLib import TTFont
W = sys.argv[1]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fontsource_ornat.py")).read().split("made = []")[0])
FAM = {"GeneralSans": "General Sans", "Satoshi": "Satoshi", "ClashDisplay": "Clash Display", "CabinetGrotesk": "Cabinet Grotesk"}
WM = {"Extralight": "ExtraLight", "Semibold": "SemiBold", "Extrabold": "ExtraBold", "": "Regular"}
n = 0
for f in glob.glob(f"{W}/fs/*/*_Complete/Fonts/WEB/fonts/*.ttf"):
    b = os.path.basename(f)[:-4]
    if "Variable" in b: continue
    pre, w = b.split("-", 1)
    it = w.endswith("Italic"); w = w[:-6] if it else w
    w = WM.get(w, w)
    fam = f"{FAM[pre]} {w}" + (" Italic" if it else "")
    t = TTFont(f); rename(t, fam); t.save(f"{DEST}/{fam.replace(' ', '')}.ttf"); n += 1
print(n, "Fontshare shrift")
