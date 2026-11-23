import math
def star(cx, cy, ro, ri, n=5):
    pts = []
    for i in range(n * 2):
        r = ro if i % 2 == 0 else ri
        a = -math.pi / 2 + i * math.pi / n
        pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
    return " ".join(pts)

GLYPHS = {
 "brand": lambda fill, extra="": f'<polygon points="{star(256,238,142,62)}" fill="{fill}" stroke="{fill}" stroke-width="26" stroke-linejoin="round" {extra}/>',
 "content": lambda fill, extra="": f'<polygon points="214,152 214,328 358,240" fill="{fill}" stroke="{fill}" stroke-width="46" stroke-linejoin="round" {extra}/>',
 "ads": lambda fill, extra="": (
    f'<g {extra}><polygon points="158,214 306,144 306,336 158,266" fill="{fill}" stroke="{fill}" stroke-width="30" stroke-linejoin="round"/>'
    f'<rect x="134" y="206" width="44" height="68" rx="20" fill="{fill}"/>'
    f'<rect x="178" y="270" width="54" height="104" rx="22" fill="{fill}"/>'
    f'<path d="M 350 190 Q 396 240 350 290" fill="none" stroke="{fill}" stroke-width="24" stroke-linecap="round"/>'
    f'<path d="M 382 152 Q 462 240 382 328" fill="none" stroke="{fill}" stroke-width="24" stroke-linecap="round"/></g>'),
 "sales": lambda fill, extra="": (
    f'<g {extra}><path d="M 148 206 H 364 L 384 366 Q 387 394 358 394 H 154 Q 125 394 128 366 Z" fill="{fill}" stroke="{fill}" stroke-width="22" stroke-linejoin="round"/>'
    f'<path d="M 202 214 V 172 Q 202 116 256 116 Q 310 116 310 172 V 214" fill="none" stroke="{fill}" stroke-width="28" stroke-linecap="round"/></g>'),
 "one": lambda fill, extra="": (
    f'<g {extra}><circle cx="256" cy="168" r="66" fill="{fill}"/>'
    f'<path d="M 128 372 Q 128 262 256 262 Q 384 262 384 372 Z" fill="{fill}" stroke="{fill}" stroke-width="30" stroke-linejoin="round"/></g>'),
}
COLORS = {
 "brand":   ("#8fb4ff", "#2f5bff", "#1a2ea6"),
 "content": ("#ffc07a", "#ff5a36", "#a8260f"),
 "ads":     ("#dc9bff", "#8a3cff", "#44189e"),
 "one":     ("#7bf0c4", "#10b585", "#08664e"),
 "sales":   ("#ffe184", "#ffa51f", "#a5560a"),
}
def svg(name):
    lt, base, dk = COLORS[name]
    g = GLYPHS[name]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<defs>
<linearGradient id="top" x1="0.15" y1="0" x2="0.85" y2="1"><stop offset="0" stop-color="{lt}"/><stop offset="0.55" stop-color="{base}"/><stop offset="1" stop-color="{dk}" stop-opacity="0.9"/></linearGradient>
<linearGradient id="side" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{dk}"/><stop offset="1" stop-color="#000" stop-opacity="0.75"/></linearGradient>
<radialGradient id="gloss" cx="0.28" cy="0.1" r="0.75"><stop offset="0" stop-color="#fff" stop-opacity="0.75"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.12"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
<radialGradient id="sh" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#000" stop-opacity="0.45"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<linearGradient id="gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dfe6ff"/></linearGradient>
<clipPath id="face"><rect x="40" y="36" width="432" height="404" rx="116"/></clipPath>
</defs>
<ellipse cx="256" cy="486" rx="190" ry="22" fill="url(#sh)"/>
<rect x="40" y="62" width="432" height="404" rx="116" fill="url(#side)"/>
<rect x="40" y="36" width="432" height="404" rx="116" fill="url(#top)"/>
<g clip-path="url(#face)">
<ellipse cx="170" cy="70" rx="300" ry="190" fill="url(#gloss)"/>
<rect x="40" y="36" width="432" height="404" rx="116" fill="none" stroke="#fff" stroke-opacity="0.45" stroke-width="6"/>
<rect x="40" y="360" width="432" height="90" fill="#000" fill-opacity="0.10"/>
</g>
<g transform="translate(0,14)" opacity="0.9">{g(dk)}</g>
<g transform="translate(0,0)">{g("url(#gl)")}</g>
</svg>
'''
for n in COLORS:
    open(f"icons3d/icon_{n}.svg", "w").write(svg(n))
print("ok")

# ---- clean flat style: white circle + dark glyph (matches the logo nodes)
def flat(name):
    g = GLYPHS[name]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<circle cx="256" cy="256" r="240" fill="#ffffff" fill-opacity="0.96"/>
<g transform="translate(256,256) scale(0.72) translate(-256,-244)">{g("#121212")}</g>
</svg>
'''
for n in COLORS:
    open(f"icons3d/flat_{n}.svg", "w").write(flat(n))
print("flat ok")
