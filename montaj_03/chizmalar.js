// Montaj 03 — kodda chizilgan illyustratsiyalar (stiker uslubi, qora kontur #1d1a16)
const K = '#1d1a16';
window.ART = {
  tesla: (old = false) => `<svg viewBox="0 0 400 520">
    <path d="M60 520 C60 400 110 360 200 350 C290 360 340 400 340 520 Z" fill="${old ? '#4a4a52' : '#2b2b33'}" stroke="${K}" stroke-width="8"/>
    <path d="M160 350 L200 430 L240 350 Z" fill="#FBF8F1" stroke="${K}" stroke-width="6"/>
    <path d="M182 372 L200 392 L218 372 L200 412 Z" fill="${K}"/>
    <rect x="168" y="290" width="64" height="70" fill="#E3B58E" stroke="${K}" stroke-width="7"/>
    <path d="M118 170 C118 92 160 58 200 58 C240 58 282 92 282 170 C282 250 248 312 200 318 C152 312 118 250 118 170 Z" fill="#EBC39C" stroke="${K}" stroke-width="8"/>
    <path d="M112 168 C100 70 160 30 205 34 C262 36 300 80 288 168 C280 120 262 96 238 88 C226 112 212 118 200 118 C188 110 170 96 160 88 C138 98 120 122 112 168 Z" fill="${old ? '#9a9aa2' : '#1f1b1a'}" stroke="${K}" stroke-width="7"/>
    <path d="M200 40 L200 112" stroke="${old ? '#7a7a82' : '#3a3330'}" stroke-width="5"/>
    <path d="M150 178 Q168 168 186 178 M214 178 Q232 168 250 178" stroke="${K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <ellipse cx="168" cy="196" rx="7" ry="8" fill="${K}"/><ellipse cx="232" cy="196" rx="7" ry="8" fill="${K}"/>
    <path d="M200 205 L192 240 L206 242" stroke="#b9875f" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M168 262 Q200 248 232 262 Q214 256 200 258 Q186 256 168 262 Z" fill="${old ? '#8a8a92' : '#1f1b1a'}" stroke="${K}" stroke-width="4"/>
    <path d="M182 280 Q200 288 218 280" stroke="#a36f4c" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M140 230 Q150 250 160 252 M260 230 Q250 250 240 252" stroke="#c99b74" stroke-width="4" fill="none"/>
  </svg>`,
  edison: () => `<svg viewBox="0 0 400 520">
    <path d="M50 520 C50 400 110 360 200 350 C290 360 350 400 350 520 Z" fill="#3E5C76" stroke="${K}" stroke-width="8"/>
    <path d="M165 350 L200 420 L235 350 Z" fill="#FBF8F1" stroke="${K}" stroke-width="6"/>
    <path d="M178 368 L222 368 L210 384 L222 400 L178 400 L190 384 Z" fill="${K}"/>
    <rect x="165" y="290" width="70" height="70" fill="#E3B58E" stroke="${K}" stroke-width="7"/>
    <ellipse cx="200" cy="190" rx="100" ry="125" fill="#EBC39C" stroke="${K}" stroke-width="8"/>
    <path d="M98 170 C90 80 150 52 200 54 C258 56 312 84 302 170 C300 128 280 104 262 96 C240 84 160 84 138 96 C120 106 102 130 98 170 Z" fill="#F4F1EA" stroke="${K}" stroke-width="7"/>
    <path d="M150 180 Q168 172 186 182 M214 182 Q232 172 250 180" stroke="#8d8a83" stroke-width="7" fill="none" stroke-linecap="round"/>
    <ellipse cx="168" cy="200" rx="7" ry="8" fill="${K}"/><ellipse cx="232" cy="200" rx="7" ry="8" fill="${K}"/>
    <path d="M200 210 Q190 246 204 250" stroke="#b9875f" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M176 280 Q200 270 224 280" stroke="#a36f4c" stroke-width="6" fill="none" stroke-linecap="round"/>
  </svg>`,
  investor: () => `<svg viewBox="0 0 400 560">
    <path d="M40 560 C40 420 110 380 200 372 C290 380 360 420 360 560 Z" fill="${K}"/>
    <ellipse cx="200" cy="250" rx="95" ry="120" fill="${K}"/>
    <rect x="120" y="40" width="160" height="150" rx="10" fill="${K}"/><rect x="80" y="178" width="240" height="26" rx="13" fill="${K}"/>
    <rect x="120" y="150" width="160" height="22" fill="#C8372D"/>
    <path d="M290 300 L360 290" stroke="#8d5a2b" stroke-width="16" stroke-linecap="round"/><circle cx="364" cy="289" r="9" fill="#F6B52F"/>
    <path d="M370 280 Q380 250 360 230 Q350 210 372 190" stroke="#cfc8bb" stroke-width="6" fill="none" opacity=".8"/>
  </svg>`,
  bag: () => `<svg viewBox="0 0 300 320"><path d="M110 60 L190 60 L170 100 C260 130 280 210 260 260 C240 310 60 310 40 260 C20 210 40 130 130 100 Z" fill="#C99A5B" stroke="${K}" stroke-width="8"/>
    <path d="M100 60 L200 60" stroke="${K}" stroke-width="12" stroke-linecap="round"/>
    <text x="150" y="235" text-anchor="middle" font-family="Archivo Black Regular" font-size="110" fill="#22674D">$</text></svg>`,
  tower: () => `<svg viewBox="0 0 400 700">
    <path d="M150 700 L190 300 L210 300 L250 700 Z" fill="#8d7a5e" stroke="${K}" stroke-width="8"/>
    <g stroke="${K}" stroke-width="5"><path d="M160 640 L240 560 M240 640 L160 560 M168 560 L232 480 M232 560 L168 480 M175 480 L225 400 M225 480 L175 400 M182 400 L218 320 M218 400 L182 320"/></g>
    <path d="M70 300 C70 200 130 160 200 160 C270 160 330 200 330 300 Z" fill="#B9A587" stroke="${K}" stroke-width="8"/>
    <path d="M70 300 L330 300" stroke="${K}" stroke-width="10"/>
    <g stroke="${K}" stroke-width="4" fill="none"><path d="M110 220 Q200 180 290 220 M90 260 Q200 225 310 260"/><path d="M200 160 L200 300 M140 175 L130 300 M260 175 L270 300"/></g>
  </svg>`,
  rozetka: () => `<svg viewBox="0 0 300 300"><rect x="20" y="20" width="260" height="260" rx="40" fill="#FBF8F1" stroke="${K}" stroke-width="8"/>
    <circle cx="150" cy="150" r="90" fill="#efe8da" stroke="${K}" stroke-width="7"/><circle cx="115" cy="150" r="16" fill="${K}"/><circle cx="185" cy="150" r="16" fill="${K}"/></svg>`,
  house: (c = '#C99A5B') => `<svg viewBox="0 0 200 200"><path d="M20 90 L100 20 L180 90 Z" fill="#C8372D" stroke="${K}" stroke-width="7"/>
    <rect x="35" y="88" width="130" height="100" fill="${c}" stroke="${K}" stroke-width="7"/><rect class="win" x="60" y="110" width="35" height="35" fill="#5b5a63" stroke="${K}" stroke-width="5"/>
    <rect class="win" x="110" y="110" width="35" height="35" fill="#5b5a63" stroke="${K}" stroke-width="5"/></svg>`,
  city: () => `<svg viewBox="0 0 420 320"><g stroke="${K}" stroke-width="7">
    <rect x="20" y="120" width="90" height="190" fill="#8DAA6B"/><rect x="120" y="40" width="110" height="270" fill="#3E5C76"/><rect x="240" y="90" width="80" height="220" fill="#C99A5B"/><rect x="330" y="150" width="70" height="160" fill="#B9A587"/></g>
    <g class="cw" fill="#4a4a52">${[...Array(18)].map((_, i) => { const xs = [35, 70, 140, 185, 255, 290, 345, 375][i % 8], ys = [150, 190, 230, 270, 80, 120][i % 6]; return `<rect x="${xs}" y="${ys}" width="22" height="22"/>`; }).join('')}</g></svg>`,
  panel: () => `<svg viewBox="0 0 460 320"><path d="M30 290 L90 30 L440 30 L380 290 Z" fill="#1F3F73" stroke="${K}" stroke-width="9"/>
    <g stroke="#5B8BD0" stroke-width="4"><path d="M60 160 H410 M75 95 H425 M45 225 H395 M175 30 L150 290 M265 30 L240 290 M355 30 L330 290"/></g>
    <path d="M110 50 L200 50 L150 140 Z" fill="#fff" opacity=".18"/></svg>`,
  inverter: () => `<svg viewBox="0 0 320 380"><rect x="20" y="20" width="280" height="340" rx="24" fill="#E8E4D8" stroke="${K}" stroke-width="9"/>
    <rect x="60" y="60" width="200" height="110" rx="12" fill="#16374a" stroke="${K}" stroke-width="6"/>
    <path d="M80 115 Q105 75 130 115 T180 115 T230 115" stroke="#5BE3C8" stroke-width="8" fill="none"/>
    <circle cx="100" cy="230" r="14" fill="#5BE3C8" stroke="${K}" stroke-width="5"/><circle cx="150" cy="230" r="14" fill="#F6B52F" stroke="${K}" stroke-width="5"/>
    <g stroke="${K}" stroke-width="6"><path d="M70 290 H250 M70 320 H250"/></g></svg>`,
  stanok: () => `<svg viewBox="0 0 460 400"><rect x="20" y="80" width="420" height="280" rx="26" fill="#2F6F8F" stroke="${K}" stroke-width="8"/>
    <rect x="60" y="120" width="190" height="120" rx="14" fill="#16374a" stroke="${K}" stroke-width="6"/><rect class="scr" x="78" y="138" width="154" height="84" rx="8" fill="#22303a"/>
    <g class="gear" transform="translate(345 190)"><circle r="60" fill="#F6B52F" stroke="${K}" stroke-width="8"/><circle r="18" fill="${K}"/>
    ${[0, 45, 90, 135, 180, 225, 270, 315].map(a => `<rect x="-10" y="-78" width="20" height="22" fill="#F6B52F" stroke="${K}" stroke-width="5" transform="rotate(${a})"/>`).join('')}</g>
    <rect x="40" y="360" width="60" height="40" fill="${K}"/><rect x="360" y="360" width="60" height="40" fill="${K}"/></svg>`,
  sand: () => `<svg viewBox="0 0 300 200"><path d="M20 180 C60 60 240 60 280 180 Z" fill="#E2C48A" stroke="${K}" stroke-width="8"/>
    <g fill="#c9a866">${[...Array(25)].map((_, i) => `<circle cx="${60 + (i * 37) % 180}" cy="${110 + (i * 23) % 60}" r="4"/>`).join('')}</g></svg>`,
  wafer: () => `<svg viewBox="0 0 260 260"><rect x="20" y="20" width="220" height="220" rx="20" fill="#2a3f6e" stroke="${K}" stroke-width="8"/>
    <g stroke="#8fb4ea" stroke-width="4"><path d="M20 90 H240 M20 165 H240 M95 20 V240 M170 20 V240"/></g><path d="M40 40 L120 40 L60 120 Z" fill="#fff" opacity=".2"/></svg>`,
  bulb: () => `<svg viewBox="0 0 200 280"><circle class="glow" cx="100" cy="100" r="95" fill="#FFE38A" opacity="0"/>
    <path d="M100 20 C150 20 180 60 180 100 C180 140 150 160 140 190 L60 190 C50 160 20 140 20 100 C20 60 50 20 100 20 Z" class="glass" fill="#efe8da" stroke="${K}" stroke-width="8"/>
    <rect x="60" y="190" width="80" height="60" rx="10" fill="#9aa7ad" stroke="${K}" stroke-width="7"/><path d="M80 120 L100 150 L120 120" stroke="${K}" stroke-width="6" fill="none"/></svg>`,
  sun: () => `<svg viewBox="0 0 300 300"><g stroke="${K}" stroke-width="7" fill="#F6B52F">${[...Array(12)].map((_, i) => `<path d="M150 8 L166 52 L134 52 Z" transform="rotate(${i * 30} 150 150)"/>`).join('')}</g>
    <circle cx="150" cy="150" r="88" fill="#F6B52F" stroke="${K}" stroke-width="8"/><circle cx="125" cy="125" r="22" fill="#FFE38A"/></svg>`,
  patent: () => `<svg viewBox="0 0 420 560"><rect x="20" y="20" width="380" height="520" fill="#FBF8F1" stroke="${K}" stroke-width="7"/>
    <text x="210" y="80" text-anchor="middle" font-family="Archivo Black Regular" font-size="34" fill="${K}">N. TESLA · PATENT</text>
    <text x="210" y="118" text-anchor="middle" font-family="General Sans SemiBold" font-size="22" fill="#6b6152">1901 · No. 685,957</text>
    <g transform="translate(70 170)" stroke="${K}" stroke-width="5" fill="none"><circle cx="40" cy="40" r="30" fill="#F6B52F"/>
      <path d="M70 60 L150 140 M60 80 L130 160" stroke-dasharray="10 8"/><rect x="140" y="140" width="130" height="18" fill="#9aa7ad"/>
      <path d="M205 158 V230 M180 230 H230 M190 245 H220"/><rect x="170" y="260" width="70" height="70" fill="#d8cfbd"/></g>
    <g fill="#d8cfbd"><rect x="60" y="470" width="300" height="14"/><rect x="60" y="495" width="220" height="14"/></g></svg>`,
  pigeon: () => `<svg viewBox="0 0 160 120"><ellipse cx="80" cy="75" rx="55" ry="32" fill="#9aa1ad" stroke="${K}" stroke-width="6"/>
    <circle cx="120" cy="45" r="20" fill="#9aa1ad" stroke="${K}" stroke-width="6"/><path d="M138 45 L152 50 L138 54" fill="#C99A5B" stroke="${K}" stroke-width="4"/>
    <circle cx="124" cy="42" r="3.5" fill="${K}"/><path d="M40 80 Q70 60 100 82" stroke="#6f7480" stroke-width="6" fill="none"/>
    <path d="M70 105 L66 118 M90 105 L94 118" stroke="#C8372D" stroke-width="5"/></svg>`,
  factory: () => `<svg viewBox="0 0 940 560"><rect x="90" y="20" width="80" height="230" fill="#8d7a5e" stroke="${K}" stroke-width="8"/>
    <path d="M20 220 L920 220 L920 250 L20 250 Z" fill="#B7B2A8" stroke="${K}" stroke-width="8"/>
    <rect x="40" y="250" width="860" height="300" fill="#E4D6BC" stroke="${K}" stroke-width="8"/>
    <g fill="#9FC3D6" stroke="${K}" stroke-width="6"><rect x="90" y="300" width="150" height="90"/><rect x="290" y="300" width="150" height="90"/><rect x="490" y="300" width="150" height="90"/><rect x="690" y="300" width="150" height="90"/></g>
    <rect x="380" y="430" width="180" height="120" fill="#5b4a36" stroke="${K}" stroke-width="6"/>
    <g>${[...Array(6)].map((_, i) => `<g transform="translate(${230 + i * 110} 125)"><path d="M0 100 L30 0 L130 0 L100 100 Z" fill="#1F3F73" stroke="${K}" stroke-width="6"/><path d="M15 50 H115 M48 0 L35 100 M82 0 L68 100" stroke="#5B8BD0" stroke-width="3"/></g>`).join('')}</g></svg>`,
};
