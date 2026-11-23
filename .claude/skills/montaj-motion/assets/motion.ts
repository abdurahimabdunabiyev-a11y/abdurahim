// Montaj Motion — harakat yordamchilari (Remotion)
// Loyihada src/lib/motion.ts ga ko'chiring.

import {Easing, interpolate, spring} from 'remotion';

// ---- Asosiy sozlamalar -------------------------------------------------
export const FPS = 60;
export const W = 1920;
export const H = 1080;
export const CX = W / 2;
export const CY = H / 2;

/** Soniyani kadrga aylantiradi: s(0.5) -> 30 */
export const s = (sec: number, fps: number = FPS) => Math.round(sec * fps);

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

// ---- Easing to'plami ---------------------------------------------------
export const EASE = {
  /** Tez boshlanib yumshoq to'xtaydi — kirishlar uchun */
  out: Easing.bezier(0.16, 1, 0.3, 1),
  /** Yumshoq boshlanib yumshoq to'xtaydi — kamera uchun */
  inOut: Easing.bezier(0.65, 0, 0.35, 1),
  /** Sekin boshlanib tezlashadi — chiqishlar uchun */
  in: Easing.bezier(0.7, 0, 0.84, 0),
};

// ---- Kirish / chiqish --------------------------------------------------
/**
 * Overshoot bilan kirish. 0 -> ~1.05 -> 1 qiymat qaytaradi.
 * scale, opacity yoki translate uchun ko'paytiruvchi sifatida ishlating.
 */
export function enter(frame: number, start: number, fps: number = FPS, durSec = 0.5) {
  return spring({
    frame: frame - start,
    fps,
    durationInFrames: s(durSec, fps),
    config: {damping: 12, stiffness: 150, mass: 0.8},
  });
}

/** Kirishdan tezroq chiqish: 1 -> 0 */
export function exit(frame: number, start: number, fps: number = FPS, durSec = 0.3) {
  return interpolate(frame, [start, start + s(durSec, fps)], [1, 0], {
    ...clamp,
    easing: EASE.in,
  });
}

/** Opacity uchun yumshoq paydo bo'lish: 0 -> 1 */
export function fadeIn(frame: number, start: number, fps: number = FPS, durSec = 0.35) {
  return interpolate(frame, [start, start + s(durSec, fps)], [0, 1], {
    ...clamp,
    easing: EASE.out,
  });
}

// ---- Ketma-ketlik va raqamlar ------------------------------------------
/** i-element uchun boshlanish kadri: base + i * gap */
export const stagger = (i: number, base: number, gap = 5) => base + i * gap;

/** Raqam sanalishi (~1 s). Butun son qaytaradi. */
export function countUp(
  frame: number,
  start: number,
  from: number,
  to: number,
  fps: number = FPS,
  durSec = 1,
) {
  return Math.round(
    interpolate(frame, [start, start + s(durSec, fps)], [from, to], {
      ...clamp,
      easing: EASE.out,
    }),
  );
}

/** Raqamni bo'shliq bilan formatlash: 2490000 -> "2 490 000" */
export const fmt = (n: number) => n.toLocaleString('ru-RU').replace(/ /g, ' ');

// ---- Interaksiya -------------------------------------------------------
/** Tugma bosilishi: klik kadrida 1 -> 0.94 -> 1 scale */
export function press(frame: number, clickFrame: number) {
  return interpolate(frame, [clickFrame - 3, clickFrame, clickFrame + 8], [1, 0.94, 1], {
    ...clamp,
    easing: EASE.inOut,
  });
}

/** Yengil pulse: start dan boshlab `times` marta, har biri ~0.4 s */
export function pulse(frame: number, start: number, times = 1, fps: number = FPS, amount = 0.05) {
  const period = s(0.4, fps);
  const local = frame - start;
  if (local < 0 || local > period * times) return 1;
  const phase = (local % period) / period;
  return 1 + Math.sin(phase * Math.PI) * amount;
}

type Pt = {x: number; y: number};

/**
 * Kursor uchun yoy bo'ylab nuqta (kvadratik Bezier).
 * t: 0..1 (odatda EASE.inOut bilan interpolate qilingan), lift: yoy balandligi (px).
 */
export function arcPoint(t: number, from: Pt, to: Pt, lift = 120): Pt {
  const mid = {x: (from.x + to.x) / 2, y: Math.min(from.y, to.y) - lift};
  const u = 1 - t;
  return {
    x: u * u * from.x + 2 * u * t * mid.x + t * t * to.x,
    y: u * u * from.y + 2 * u * t * mid.y + t * t * to.y,
  };
}

/** start..end oralig'ida 0..1 progress, easing bilan */
export function progress(frame: number, start: number, end: number, easing = EASE.inOut) {
  return interpolate(frame, [start, end], [0, 1], {...clamp, easing});
}

// ---- Kamera ------------------------------------------------------------
/** Sahna davomida sekin drift (zoom): 1 -> 1 + amount */
export function drift(frame: number, total: number, amount = 0.02) {
  return interpolate(frame, [0, total], [1, 1 + amount], clamp);
}

/** Kamera zoom'i: [kadrlar] -> [masshtablar], easy-ease bilan */
export function camera(frame: number, frames: number[], scales: number[]) {
  return interpolate(frame, frames, scales, {...clamp, easing: EASE.inOut});
}
