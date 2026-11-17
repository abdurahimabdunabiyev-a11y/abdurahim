window.PB_LOGO = '../../.claude/skills/montaj-uslubi/assets/logo_premium_solar_shaffof.png';
// Bir nechta yuz holatli Panelbek: el ichiga har holat uchun svg; show(tl, t, face) bilan almashtiriladi
window.makeBot = (el, faces, wave = true) => {
  faces.forEach((f, k) => el.insertAdjacentHTML('beforeend', `<svg viewBox="0 0 400 440" data-f="${f}" style="opacity:${k ? 0 : 1}">${bot(f, wave)}</svg>`));
};
window.face = (tl, el, f, t) => {
  el.querySelectorAll('svg').forEach(s => tl.set(s, { opacity: s.dataset.f === f ? 1 : 0 }, t));
};
