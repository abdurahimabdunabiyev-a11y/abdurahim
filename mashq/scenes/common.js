// Umumiy: kadrlar ketma-ketligi (img[data-seq]) va timeline seek.
window.FPS = 30;
window.renderFrame = async (i) => {
  const t = i / window.FPS;
  document.querySelectorAll('img[data-seq]').forEach(img => {
    const st = +(img.dataset.start || 0), max = +(img.dataset.max || 150);
    const n = Math.min(max, Math.max(1, Math.floor((t - st) * window.FPS) + 1 + +(img.dataset.offset || 0)));
    const src = `../assets/frames/${img.dataset.seq}_${String(n).padStart(4, '0')}.jpg`;
    if (img.getAttribute('src') !== src) img.setAttribute('src', src);
  });
  await Promise.all([...document.images].map(im => im.decode().catch(() => {})));
  window.tl.seek(t, false);
};
// Mashq yorlig'i
window.addLabel = (txt) => {
  const d = document.createElement('div');
  d.className = 'mlabel'; d.textContent = txt; document.body.appendChild(d);
};
