"""Ronma SKYMAX paneli teksturasi: hujayralar + showroom yorlig'idagi bosma yozuvlar (rasmdagidek joylashuv).
Raqamlar foydalanuvchi yuborgan paneldagi yozuvdan aynan olingan."""
import math, os
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__))
W, H = 2000, 4200                       # 1134 x 2382 mm nisbati (~1:2.1)
im = Image.new('RGB', (W, H), (150, 152, 158)); d = ImageDraw.Draw(im)
cols, rows, mid = 6, 22, 18; ch = (H - mid) / rows; cw = W / cols
for i in range(cols):
    for j in range(rows):
        y0 = j * ch + (mid if j >= rows // 2 else 0) + 4; x0 = i * cw + 5; x1 = x0 + cw - 10; y1 = y0 + ch - 7
        d.rectangle([x0, y0, x1, y1], fill=(9, 11, 15))
        for k in range(1, 17): xx = x0 + k * (x1 - x0) / 17; d.line([xx, y0, xx, y1], fill=(66, 68, 74), width=2)
        for k in range(1, 6): yy = y0 + k * (y1 - y0) / 6; d.line([x0, yy, x1, yy], fill=(14, 16, 20), width=1)

# --- bosma qatlam ---
pr = Image.new('RGBA', (W, H), (0, 0, 0, 0)); p = ImageDraw.Draw(pr)
B = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'; XB = '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
def F(path, s): return ImageFont.truetype(path, s)
GR = (196, 202, 208, 235); RED = (196, 58, 44, 240); LG = (150, 154, 160, 235)
X = int(W * .11)
# logo (uslublashtirilgan so'z belgisi): "Ro" qizil, "NMA" kulrang, ustida kichik "solar"
lx, ly = int(W * .50), int(H * .235)
p.text((lx, ly + 40), 'Ro', font=F(XB, 190), fill=RED)
rw = p.textlength('Ro', font=F(XB, 190))
p.text((lx + rw - 10, ly + 40), 'NMA', font=F(XB, 190), fill=LG)
p.text((lx + rw + 20, ly - 20), 's  o  l  a  r', font=F(B, 64), fill=LG)
p.line([(lx + rw - 40, ly + 205), (lx + rw + 520, ly + 150)], fill=RED, width=14)
# matnlar
p.text((X, int(H * .33)), 'RONMA SOLAR', font=F(XB, 150), fill=GR)
p.text((X, int(H * .377)), '585~625W  |  23.32% KPD', font=F(B, 104), fill=GR)
p.text((X, int(H * .42)), '2382 x 1134 x 30 mm | 33 kg', font=F(B, 66), fill=GR)
ix, tx = X + 70, X + 210
def gear(cx, cy, r):
    for a in range(8):
        t = a * math.pi / 4; p.rectangle([cx + (r + 6) * math.cos(t) - 12, cy + (r + 6) * math.sin(t) - 12, cx + (r + 6) * math.cos(t) + 12, cy + (r + 6) * math.sin(t) + 12], outline=GR, width=7)
    p.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GR, width=9); p.ellipse([cx - r * .4, cy - r * .4, cx + r * .4, cy + r * .4], outline=GR, width=7)
def target(cx, cy, r):
    for k in (1, .65, .3): p.ellipse([cx - r * k, cy - r * k, cx + r * k, cy + r * k], outline=GR, width=9)
    p.line([(cx, cy), (cx + r * 1.1, cy - r * 1.1)], fill=GR, width=8)
def doc(cx, cy, r):
    p.rounded_rectangle([cx - r * .7, cy - r, cx + r * .6, cy + r], radius=10, outline=GR, width=8)
    for k in (-.5, -.2): p.line([(cx - r * .3, cy + r * k), (cx + r * .3, cy + r * k)], fill=GR, width=7)
    p.ellipse([cx - r * .1, cy + r * .05, cx + r * .6, cy + r * .75], outline=GR, width=8); p.line([(cx + r * .5, cy + r * .65), (cx + r * .95, cy + r * 1.1)], fill=GR, width=9)
y = int(H * .483); gear(ix, y + 40, 46); p.text((tx, y), '1% (Year 1), 0.4% / year', font=F(B, 70), fill=GR)
y = int(H * .532); target(ix, y + 60, 55); p.text((tx, y), '-40 C ~ +85 C', font=F(B, 70), fill=GR); p.text((tx, y + 95), 'IEC 61215', font=F(B, 70), fill=GR)
y = int(H * .60); doc(ix, y + 50, 60); p.text((tx, y + 10), 'SKYMAX Series', font=F(B, 70), fill=GR)
# kafolat nishoni
bx, by, br = X + 110, int(H * .685), 120
pts = [(bx + (br if k % 2 == 0 else br * .88) * math.cos(k * math.pi / 12), by + (br if k % 2 == 0 else br * .88) * math.sin(k * math.pi / 12)) for k in range(24)]
p.polygon(pts, fill=(120, 124, 130, 220)); p.ellipse([bx - 78, by - 78, bx + 78, by + 78], outline=(210, 214, 220, 240), width=6)
p.text((bx, by - 30), '30', font=F(XB, 70), fill=(235, 238, 240, 255), anchor='mm'); p.text((bx, by + 18), 'YEARS', font=F(B, 26), fill=(235, 238, 240, 255), anchor='mm')
p.rectangle([bx - 150, by + 50, bx + 150, by + 102], fill=(150, 154, 160, 235)); p.text((bx, by + 76), 'WARRANTY', font=F(XB, 40), fill=(40, 42, 46, 255), anchor='mm')
im = Image.alpha_composite(im.convert('RGBA'), pr).convert('RGB')
im.save(os.path.join(D, 'ronma_hujayra.png')); im.resize((500, 1050)).save(os.path.join(D, 'ronma_tekstura_preview.png')); print('ok')
