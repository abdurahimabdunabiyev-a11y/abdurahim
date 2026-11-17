// Premium qatlam: umumiy gradientlar + chizmalarni boyitish (ART ustidan)
(function () {
  const defs = `<svg width="0" height="0" style="position:absolute"><defs>
  <linearGradient id="gGlass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3f6fb8"/><stop offset=".45" stop-color="#1a3a72"/><stop offset="1" stop-color="#0c1d3d"/></linearGradient>
  <linearGradient id="gAlu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f6f8"/><stop offset=".5" stop-color="#b9c0c7"/><stop offset="1" stop-color="#7d868f"/></linearGradient>
  <linearGradient id="gMetal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3f8db3"/><stop offset=".6" stop-color="#2a6684"/><stop offset="1" stop-color="#1b4458"/></linearGradient>
  <linearGradient id="gPlastic" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d9d3c6"/></linearGradient>
  <linearGradient id="gBox" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7f4ec"/><stop offset=".7" stop-color="#d8d2c4"/><stop offset="1" stop-color="#b8b0a0"/></linearGradient>
  <radialGradient id="gSun" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#fff3b8"/><stop offset=".45" stop-color="#ffc53d"/><stop offset="1" stop-color="#e98a12"/></radialGradient>
  <radialGradient id="gSkin" cx=".42" cy=".38" r=".75"><stop offset="0" stop-color="#f5d3b2"/><stop offset=".7" stop-color="#e0ad84"/><stop offset="1" stop-color="#c48d63"/></radialGradient>
  <linearGradient id="gHair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3b322d"/><stop offset=".5" stop-color="#16120f"/><stop offset="1" stop-color="#0a0807"/></linearGradient>
  <linearGradient id="gSuit" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3c3c46"/><stop offset="1" stop-color="#16161b"/></linearGradient>
  <linearGradient id="gLeather" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d8ab6c"/><stop offset=".6" stop-color="#a87634"/><stop offset="1" stop-color="#7a5020"/></linearGradient>
  <linearGradient id="gWood" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6f5a40"/><stop offset=".5" stop-color="#a68a62"/><stop offset="1" stop-color="#5c4a33"/></linearGradient>
  <linearGradient id="gDome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9c8a8"/><stop offset="1" stop-color="#8f7b5c"/></linearGradient>
  <linearGradient id="gWafer" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4b6fb0"/><stop offset=".35" stop-color="#6f5aa8"/><stop offset=".6" stop-color="#2a5a8a"/><stop offset="1" stop-color="#1b2f5c"/></linearGradient>
  <linearGradient id="gSand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1d9a6"/><stop offset="1" stop-color="#c79d5a"/></linearGradient>
  <radialGradient id="gBulb" cx=".45" cy=".4" r=".6"><stop offset="0" stop-color="#ffffff" stop-opacity=".95"/><stop offset="1" stop-color="#e7e2d6" stop-opacity=".85"/></radialGradient>
  <linearGradient id="gPaper" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbf6e8"/><stop offset="1" stop-color="#e6dcc3"/></linearGradient>
  <linearGradient id="gWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#efe3cb"/><stop offset="1" stop-color="#cdbb98"/></linearGradient>
  <linearGradient id="gWin" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#cfe6f2"/><stop offset="1" stop-color="#6f9fbd"/></linearGradient>
  <linearGradient id="gRed" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e05a45"/><stop offset="1" stop-color="#9c2a1f"/></linearGradient>
  <linearGradient id="gPigeon" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c3c8d2"/><stop offset="1" stop-color="#7d8592"/></linearGradient>
  <linearGradient id="gGold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffe08a"/><stop offset=".5" stop-color="#f6b52f"/><stop offset="1" stop-color="#c98612"/></linearGradient>
  <linearGradient id="gShine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".5" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  </defs></svg>`;
  document.addEventListener('DOMContentLoaded', () => document.body.insertAdjacentHTML('afterbegin', defs));
  if (document.body) document.body.insertAdjacentHTML('afterbegin', defs);
  // rang -> gradient almashtirish xaritasi (har chizma uchun)
  const MAP = {
    panel: [['#1F3F73', 'url(#gGlass)']], wafer: [['#2a3f6e', 'url(#gWafer)']], sun: [['#F6B52F', 'url(#gSun)']],
    inverter: [['#E8E4D8', 'url(#gBox)'], ['#16374a', '#0e2230']], stanok: [['#2F6F8F', 'url(#gMetal)'], ['#F6B52F', 'url(#gGold)']],
    rozetka: [['#FBF8F1', 'url(#gPlastic)'], ['#efe8da', 'url(#gBox)']], bag: [['#C99A5B', 'url(#gLeather)']],
    tower: [['#8d7a5e', 'url(#gWood)'], ['#B9A587', 'url(#gDome)']], sand: [['#E2C48A', 'url(#gSand)']], bulb: [['#efe8da', 'url(#gBulb)'], ['#9aa7ad', 'url(#gAlu)']],
    patent: [['#FBF8F1', 'url(#gPaper)']], pigeon: [['#9aa1ad', 'url(#gPigeon)']],
    factory: [['#E4D6BC', 'url(#gWall)'], ['#9FC3D6', 'url(#gWin)'], ['#1F3F73', 'url(#gGlass)'], ['#8d7a5e', 'url(#gWood)']],
    house: [['#C8372D', 'url(#gRed)'], ['#C99A5B', 'url(#gLeather)']], city: [['#3E5C76', 'url(#gMetal)'], ['#C99A5B', 'url(#gLeather)'], ['#8DAA6B', '#7fa060']],
    tesla: [['#EBC39C', 'url(#gSkin)'], ['#E3B58E', 'url(#gSkin)'], ['#2a2a30', 'url(#gSuit)'], ['#1c1816', 'url(#gHair)']],
    teslaOld: [['#2a2a30', 'url(#gSuit)']],
    edison: [['#EBC39C', 'url(#gSkin)'], ['#E3B58E', 'url(#gSkin)']],
  };
  // qo'shimcha yaltirash qatlami (shisha / metall / qog'oz)
  const SHINE = {
    panel: '<path d="M90 30 L250 30 L140 290 L30 290 Z" fill="url(#gShine)" opacity=".7"/><path d="M30 290 L380 290" stroke="#c9d2db" stroke-width="10"/>',
    wafer: '<rect x="20" y="20" width="220" height="220" rx="20" fill="url(#gShine)" opacity=".6"/>',
    inverter: '<rect x="20" y="20" width="140" height="340" rx="24" fill="url(#gShine)" opacity=".5"/><rect x="60" y="60" width="200" height="110" rx="12" fill="#5BE3C8" opacity=".08"/>',
    stanok: '<rect x="20" y="80" width="200" height="280" rx="26" fill="url(#gShine)" opacity=".45"/>',
    bulb: '<ellipse cx="72" cy="78" rx="18" ry="34" fill="#fff" opacity=".7" transform="rotate(20 72 78)"/>',
    sun: '<circle cx="150" cy="150" r="140" fill="#ffd36b" opacity=".18"/>',
    rozetka: '<rect x="20" y="20" width="130" height="260" rx="40" fill="url(#gShine)" opacity=".6"/>',
    bag: '<ellipse cx="110" cy="190" rx="40" ry="60" fill="#fff" opacity=".15"/>',
  };
  const raw = window.ART;
  const scaleStroke = s => s.replace(/stroke-width="([\d.]+)"/g, (m, w) => `stroke-width="${(+w * 0.62).toFixed(1)}"`).replace(/#1d1a16/g, '#2b221b');
  window.ART = {};
  Object.keys(raw).forEach(k => window.ART[k] = (...a) => {
    let s = raw[k](...a);
    (MAP[k] || []).forEach(([c, g]) => { s = s.split(`fill="${c}"`).join(`fill="${g}"`); });
    if (SHINE[k]) s = s.replace(/<\/svg>\s*$/, SHINE[k] + '</svg>');
    return scaleStroke(s);
  });
})();
