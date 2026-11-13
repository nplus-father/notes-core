export type ChartTier = "basic" | "advanced" | null;

export interface ChartPageInput {
  slug: string;
  title: string;
  href: string | null;
  tier: ChartTier;
  importance: number;
  written: boolean;
  related: string[];
}

export interface ChartCategoryInput {
  slug: string;
  name: string;
  num: number;
  pages: ChartPageInput[];
}

export interface ChartInput {
  seed: string;
  categories: ChartCategoryInput[];
}

export interface ChartStar {
  i: number;
  k: number;
  slug: string;
  title: string;
  href: string | null;
  x: number;
  y: number;
  r: number;
  mag: number;
  written: boolean;
  hit: number;
  alpha: boolean;
}

export interface ChartSegment {
  k: number;
  a: number;
  b: number;
  d: string;
  order: number;
}

export interface ChartLink {
  a: number;
  b: number;
  d: string;
}

export interface ChartLabel {
  k: number;
  mobile: { id: string; d: string } | null;
  slug: string;
  num: number;
  text: string;
  latin: boolean;
  lines: { id: string; d: string; text: string }[];
  fits: boolean;
  start: number;
  end: number;
  numX: number;
  numY: number;
}

export interface ChartTag {
  k: number;
  i: number;
  lines: string[];
  latin: boolean;
  size: number;
  x: number;
  y: number;
  anchor: "start" | "middle" | "end";
  leader: string | null;
}

export interface ChartFurniture {
  size: number;
  c: number;
  rOuter: number;
  rTick: number;
  rLabel: number;
  rField: number;
  declination: number[];
  boundaries: string;
  dividers: string;
  hours: string;
  fieldSmall: string;
  fieldLarge: string;
  rays: { mag: number; d: string }[];
}

export interface ChartLayout {
  stars: ChartStar[];
  segments: ChartSegment[];
  links: ChartLink[];
  labels: ChartLabel[];
  furniture: ChartFurniture;
  counts: { stars: number; written: number; planned: number; constellations: number };
  abbreviated: boolean;
  sparse: boolean;
  labelScale: number;
  bayer: { i: number; letter: string; x: number; y: number }[];
  tags: ChartTag[];
  mobileTags: ChartTag[];
  sectors: { k: number; d: string }[];
}

const SIZE = 1000;
const C = SIZE / 2;
const R_OUTER = 494;
const R_TICK = 476;
const R_LABEL = 455;
const R_FIELD = 434;
const R_IN = 62;
const R_OUT = 404;
const LABEL_SIZE = 17;
const CJK_SIZE = 19;
const NUM_SIZE = 13;
const MAG_R = [0, 2.3, 3.2, 4.3, 5.7, 7.4];
const PLANNED_R = 3.4;
const SPACING = 30;
const TAG_CJK = 19;
const TAG_LATIN = 17.5;
const TAG_CAP = 12;
const MOBILE_RING = 28;

const r1 = (n: number) => Math.round(n * 10) / 10;
const rad = (deg: number) => (deg * Math.PI) / 180;
const clamp = (v: number, lo: number, hi: number) => Math.min(hi, Math.max(lo, v));

function hash(s: string): number {
  let h = 0x811c9dc5;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return h >>> 0;
}

function rng(seed: string) {
  let a = hash(seed) || 1;
  return () => {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const polar = (r: number, deg: number): [number, number] => [
  C + r * Math.cos(rad(deg)),
  C + r * Math.sin(rad(deg)),
];

function splitLabel(text: string, latin: boolean): [string, string] | null {
  if (latin) {
    const words = text.split(" ");
    if (words.length < 2) return null;
    let best: [string, string] | null = null;
    let bestScore = Infinity;
    for (let i = 1; i < words.length; i++) {
      const a = words.slice(0, i).join(" ");
      const b = words.slice(i).join(" ");
      const score = Math.abs(a.length - b.length) - (a.endsWith("&") ? 3 : 0);
      if (score < bestScore) {
        bestScore = score;
        best = [a, b];
      }
    }
    return best;
  }
  const chars = [...text];
  if (chars.length < 6) return null;
  const mid = Math.round(chars.length / 2);
  for (const d of [0, -1, 1, -2, 2]) {
    const i = mid + d;
    if (/[與和及、・·]/.test(chars[i - 1] ?? ""))
      return [chars.slice(0, i).join(""), chars.slice(i).join("")];
  }
  return [chars.slice(0, mid).join(""), chars.slice(mid).join("")];
}

const CJK = /[⺀-鿿豈-﫿＀-￯　-〿]/;

export const isLatin = (text: string) => !CJK.test(text);

export function labelWidth(text: string, base: number, latin: boolean): number {
  const size = latin ? base : (base * CJK_SIZE) / LABEL_SIZE;
  let w = 0;
  for (const ch of text) {
    if (CJK.test(ch)) w += size * 1.06;
    else if (ch === " ") w += size * 0.4;
    else if (latin) w += size * (/[MW]/.test(ch) ? 0.98 : /[IJ1]/.test(ch) ? 0.46 : 0.76);
    else w += size * 0.66;
  }
  return w;
}

function arcPath(r: number, from: number, to: number, reverse: boolean): string {
  const [a, b] = reverse ? [to, from] : [from, to];
  const [x0, y0] = polar(r, a);
  const [x1, y1] = polar(r, b);
  const large = Math.abs(to - from) > 180 ? 1 : 0;
  return `M${r1(x0)} ${r1(y0)}A${r} ${r} 0 ${large} ${reverse ? 0 : 1} ${r1(x1)} ${r1(y1)}`;
}

function allocate(weights: number[], floors: number[], total: number): number[] {
  const sumFloors = floors.reduce((s, f) => s + f, 0);
  if (sumFloors >= total) return floors.map((f) => (f / sumFloors) * total);
  let lo = 0;
  let hi = total / Math.max(1e-6, Math.min(...weights));
  for (let it = 0; it < 60; it++) {
    const k = (lo + hi) / 2;
    const s = weights.reduce((acc, w, i) => acc + Math.max(floors[i], k * w), 0);
    if (s > total) hi = k;
    else lo = k;
  }
  return weights.map((w, i) => Math.max(floors[i], lo * w));
}

function segCross(
  a: [number, number],
  b: [number, number],
  c: [number, number],
  d: [number, number]
): boolean {
  const o = (p: [number, number], q: [number, number], s: [number, number]) =>
    (q[0] - p[0]) * (s[1] - p[1]) - (q[1] - p[1]) * (s[0] - p[0]);
  const d1 = o(c, d, a);
  const d2 = o(c, d, b);
  const d3 = o(a, b, c);
  const d4 = o(a, b, d);
  return d1 * d2 < 0 && d3 * d4 < 0;
}

function pointSegDist(p: [number, number], a: [number, number], b: [number, number]): number {
  const vx = b[0] - a[0];
  const vy = b[1] - a[1];
  const len2 = vx * vx + vy * vy || 1;
  const t = clamp(((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / len2, 0, 1);
  return Math.hypot(p[0] - (a[0] + t * vx), p[1] - (a[1] + t * vy));
}

function rayPath(x: number, y: number, r: number, mag: number): string {
  if (mag < 4) return "";
  const parts: string[] = [];
  const dirs = mag >= 5 ? 8 : 4;
  for (let j = 0; j < dirs; j++) {
    const deg = j * (360 / dirs) - 90;
    const long = j % 2 === 0 || dirs === 4;
    const r0 = r + 2.2;
    const rEnd = r + (long ? (mag >= 5 ? 9 : 6) : 4.2);
    const [x0, y0] = [x + r0 * Math.cos(rad(deg)), y + r0 * Math.sin(rad(deg))];
    const [xe, ye] = [x + rEnd * Math.cos(rad(deg)), y + rEnd * Math.sin(rad(deg))];
    parts.push(`M${r1(x0)} ${r1(y0)}L${r1(xe)} ${r1(ye)}`);
  }
  return parts.join("");
}

type Box = { x0: number; y0: number; x1: number; y1: number };

const TITLE_EN_TAIL = /^(.*?[^\s])\s*[（(][^()（）]*[)）]\s*$/;

const FUNCTION_TAIL = /[的之與和及或在]+$/;

const WORDS =
  "新耶路撒冷 耶路撒冷 程式碼 一致性 系統化 方法論 心理學 神學 程式 系統 設計 實務 函式 介面 物件 測試 重構 架構 資料 管理 創新 目的 聖經 心理 教會 福音 情緒 饒恕 羞恥 概念 審查 註解 模組 領域 事件 驅動 快取 分散 一致 共識 歷史 時代 世俗 治療 傳統 知識 生產 決策 責任 組織 社會 未來 典範 模式 原則 取代 主義 資本 條件 時間 渴望 道德 多型 面試 框架 實作 演算法".split(
    " "
  );

function balance(tokens: { t: string; w: number; brk: number }[], cap: number): string[] | null {
  const total = tokens.reduce((n, x) => n + x.w, 0);
  const joined = tokens.map((x) => x.t);
  const inside = new Set<number>();
  for (const word of WORDS) {
    const wl = [...word].length;
    for (let i = 0; i + wl <= joined.length; i++) {
      if (joined.slice(i, i + wl).join("") === word)
        for (let j = i + 1; j < i + wl; j++) inside.add(j);
    }
  }
  if (total <= cap * 0.86)
    return [
      tokens
        .map((x) => x.t)
        .join("")
        .trim(),
    ];
  let best: string[] | null = null;
  let bestScore = Infinity;
  let left = 0;
  for (let i = 1; i < tokens.length; i++) {
    left += tokens[i - 1].w;
    const right = total - left;
    if (left > cap || right > cap) continue;
    const before = /^(?:[與和及或]|vs\.?)$/i.test(tokens[i].t.trim()) ? 2.2 : 0;
    const after = /[的之與和及或]$/.test(tokens[i - 1].t) ? 1.5 : 0;
    const score =
      Math.abs(left - right) -
      Math.max(before, after, tokens[i - 1].brk) -
      (left > right ? 0.1 : 0) +
      (inside.has(i) ? 3 : 0);
    if (score < bestScore) {
      bestScore = score;
      best = [
        tokens
          .slice(0, i)
          .map((x) => x.t)
          .join("")
          .trim(),
        tokens
          .slice(i)
          .map((x) => x.t)
          .join("")
          .trim(),
      ];
    }
  }
  return best;
}

function tokenize(text: string): { t: string; w: number; brk: number }[] {
  const out: { t: string; w: number; brk: number }[] = [];
  for (const m of text.matchAll(/[A-Za-z0-9][\w.+#'’-]*|\s+|./gu)) {
    const t = m[0];
    if (/^\s+$/.test(t)) {
      if (out.length)
        out[out.length - 1] = { ...out[out.length - 1], t: out[out.length - 1].t + " ", brk: 2 };
      continue;
    }
    const cjk = CJK.test(t);
    out.push({ t, w: cjk ? 1 : t.length * 0.5, brk: 0 });
  }
  return out;
}

export function tagText(title: string): { lines: string[]; latin: boolean } | null {
  let main = title.replace(TITLE_EN_TAIL, "$1");
  const cut = main.search(/[：:，、；;。！？!?（(「『]|, |——|—/);
  if (cut > 0) main = main.slice(0, cut);
  main = main.trim();
  if (!main) return null;
  const latin = !CJK.test(main);
  if (latin) {
    const fit = (text: string): string[] | null => {
      if (text.length <= 16) return [text];
      const words = text.split(/\s+/);
      let best: string[] | null = null;
      let bestScore = Infinity;
      for (let i = 1; i < words.length; i++) {
        const a = words.slice(0, i).join(" ");
        const b = words.slice(i).join(" ");
        if (a.length > 15 || b.length > 15) continue;
        const score = Math.abs(a.length - b.length) + (/[/&+:,-]$/.test(a) ? 8 : 0);
        if (score < bestScore) {
          bestScore = score;
          best = [a, b];
        }
      }
      return best;
    };
    const first = main.split(/\s+(?:and|&|vs\.?|or)\s+|:\s*/i)[0].trim();
    const lines = fit(main) ?? fit(first);
    return lines ? { lines, latin } : null;
  }
  const tries = [main, main.replace(FUNCTION_TAIL, "")];
  const clause = main.split(/\s*vs\.?\s*|與|和|及|或|\s+/)[0];
  if (clause && clause !== main) tries.push(clause);
  for (const text of tries) {
    if ([...text].filter((ch) => CJK.test(ch)).length < 2 && tokenize(text).length < 2) continue;
    const lines = balance(tokenize(text), 7);
    if (lines) return { lines, latin };
  }
  return null;
}

function tagWidth(text: string, size: number): number {
  let w = 0;
  for (const ch of text) {
    if (CJK.test(ch)) w += size;
    else if (ch === " ") w += size * 0.28;
    else if (ch === "…") w += size * 0.9;
    else if (/[MWmw]/.test(ch)) w += size * 0.82;
    else if (/[A-Z]/.test(ch)) w += size * 0.66;
    else if (/[il.,'’|]/.test(ch)) w += size * 0.26;
    else w += size * 0.54;
  }
  return w;
}

const boxHitsCircle = (b: Box, x: number, y: number, r: number) =>
  Math.hypot(x - clamp(x, b.x0, b.x1), y - clamp(y, b.y0, b.y1)) < r;

const boxesOverlap = (a: Box, b: Box) => a.x0 < b.x1 && b.x0 < a.x1 && a.y0 < b.y1 && b.y0 < a.y1;

function boxHitsSeg(b: Box, p: [number, number], q: [number, number]): boolean {
  const inside = (v: [number, number]) => v[0] > b.x0 && v[0] < b.x1 && v[1] > b.y0 && v[1] < b.y1;
  if (inside(p) || inside(q)) return true;
  const c: [number, number][] = [
    [b.x0, b.y0],
    [b.x1, b.y0],
    [b.x1, b.y1],
    [b.x0, b.y1],
  ];
  for (let j = 0; j < 4; j++) if (segCross(p, q, c[j], c[(j + 1) % 4])) return true;
  return false;
}

function annularSector(r0: number, r1o: number, from: number, to: number): string {
  if (to - from >= 359.9) {
    const ring = (r: number) =>
      `M${C - r} ${C}A${r} ${r} 0 1 1 ${C + r} ${C}A${r} ${r} 0 1 1 ${C - r} ${C}Z`;
    return ring(r1o) + ring(r0);
  }
  const [ax, ay] = polar(r1o, from);
  const [bx, by] = polar(r1o, to);
  const [cx, cy] = polar(r0, to);
  const [dx, dy] = polar(r0, from);
  const large = to - from > 180 ? 1 : 0;
  return (
    `M${r1(ax)} ${r1(ay)}A${r1o} ${r1o} 0 ${large} 1 ${r1(bx)} ${r1(by)}` +
    `L${r1(cx)} ${r1(cy)}A${r0} ${r0} 0 ${large} 0 ${r1(dx)} ${r1(dy)}Z`
  );
}

export function layoutStarChart(input: ChartInput): ChartLayout | null {
  const cats = input.categories.filter((c) => c.pages.length > 0);
  if (cats.length === 0) return null;
  const K = cats.length;
  const starTotal = cats.reduce((a, c) => a + c.pages.length, 0);
  const sparse = starTotal < 15;
  const rOut = sparse ? 340 : R_OUT;
  const mScale = sparse ? 1.4 : 1;
  const magR = (m: number) => r1(MAG_R[m] * mScale);
  const gap = K > 1 ? clamp(16 / K, 1.2, 2.6) : 0;
  const avail = 360 - gap * K;

  const texts = cats.map((c) => {
    const latin = isLatin(c.name);
    return { latin, text: latin ? c.name.toUpperCase() : c.name };
  });
  const toDeg = (w: number) => (w / R_LABEL) * (180 / Math.PI);
  const numW = NUM_SIZE * 0.62 * 2 + LABEL_SIZE * 0.6;
  const splits = texts.map((t) => splitLabel(t.text, t.latin));
  const need1 = texts.map((t) => toDeg(numW + labelWidth(t.text, LABEL_SIZE, t.latin) + 30));
  const need2 = texts.map((t, k) => {
    const sp = splits[k];
    if (!sp) return need1[k];
    return toDeg(
      Math.max(
        numW + labelWidth(sp[0], LABEL_SIZE, t.latin),
        labelWidth(sp[1], LABEL_SIZE, t.latin)
      ) + 30
    );
  });
  const twoLine = texts.map(() => false);
  const need = need1.slice();
  const order = texts.map((_, k) => k).sort((a, b) => need1[b] - need2[b] - (need1[a] - need2[a]));
  for (const k of order) {
    if (need.reduce((a, b) => a + b, 0) <= avail * 0.88) break;
    if (need2[k] < need1[k] - 0.5) {
      need[k] = need2[k];
      twoLine[k] = true;
    }
  }
  const needSum = need.reduce((a, b) => a + b, 0);
  const labelScale = needSum > avail * 0.94 ? Math.max(0.8, (avail * 0.94) / needSum) : 1;
  for (let k = 0; k < need.length; k++) need[k] *= labelScale;
  const numNeed = ((NUM_SIZE * 2 + 20) / R_LABEL) * (180 / Math.PI);
  const weights = cats.map((c) => c.pages.length + 1.2);
  let floors = need.slice();
  if (floors.reduce((s, f) => s + f, 0) > avail * 0.94) {
    const cap = (avail * 0.94) / K;
    floors = need.map((n) => Math.max(numNeed, Math.min(n, cap)));
  }
  const spans = allocate(weights, floors, avail);

  const sectors: { s0: number; s1: number }[] = [];
  let cursor = -90 + gap / 2;
  for (const span of spans) {
    sectors.push({ s0: cursor, s1: cursor + span });
    cursor += span + gap;
  }

  const total = cats.reduce((a, c) => a + c.pages.length, 0);
  const spacing = clamp(Math.sqrt((Math.PI * (rOut * rOut - R_IN * R_IN) * 0.3) / total), 50, 128);
  const stars: ChartStar[] = [];
  const bySlug = new Map<string, number>();
  const chains: number[][][] = [];

  cats.forEach((cat, k) => {
    const rand = rng(`${input.seed}/${cat.slug}`);
    const { s0, s1 } = sectors[k];
    const n = cat.pages.length;
    const ordered = [
      ...cat.pages.filter((p) => p.tier === "basic"),
      ...cat.pages.filter((p) => p.tier === "advanced"),
      ...cat.pages.filter((p) => p.tier !== "basic" && p.tier !== "advanced"),
    ];
    const padDeg = (r: number) => ((14 / r) * 180) / Math.PI;
    const target = n * spacing * spacing * 1.8;
    let dR = clamp(Math.sqrt(target) * (0.9 + rand() * 0.5), 70, rOut - R_IN);
    let rc = R_IN + dR / 2 + rand() * (rOut - R_IN - dR);
    let dTheta = 0;
    for (let it = 0; it < 3; it++) {
      const maxTheta = rad(s1 - s0) - 2 * rad(padDeg(rc));
      dTheta = Math.max(0, Math.min(maxTheta, target / dR / rc));
      if (dTheta >= maxTheta - 1e-6 && dR < rOut - R_IN) {
        dR = Math.min(rOut - R_IN, target / Math.max(1e-6, maxTheta) / rc);
        rc = clamp(rc, R_IN + dR / 2, rOut - dR / 2);
      }
    }
    if (n === 1) {
      dR = 0;
      dTheta = 0;
      rc = R_IN + 90 + rand() * (rOut - R_IN - 140);
    }
    const thetaDeg = (dTheta * 180) / Math.PI;
    const room = s1 - s0 - 2 * padDeg(rc) - thetaDeg;
    const mid = s0 + padDeg(rc) + thetaDeg / 2 + Math.max(0, room) * (0.2 + rand() * 0.6);
    const r0b = Math.max(R_IN, rc - dR / 2);
    const r1b = Math.min(rOut, rc + dR / 2);
    const f = 0.35 + Math.sqrt(n) * 0.3;
    const phase = [rand(), rand(), rand()];
    const tiers = [
      ordered.filter((p) => p.tier === "basic"),
      ordered.filter((p) => p.tier === "advanced"),
      ordered.filter((p) => p.tier !== "basic" && p.tier !== "advanced"),
    ];
    const outward = rand() < 0.78;
    let idx = 0;
    const catChains: number[][] = [];
    tiers.forEach((list, ti) => {
      const chain: number[] = [];
      for (const page of list) {
        const t = n === 1 ? 0.5 : (idx + 0.5) / n;
        const v = clamp((outward ? t : 1 - t) + (rand() - 0.5) * (0.7 / n), 0, 1);
        const u = clamp(
          0.78 * Math.sin(2 * Math.PI * (f * t + phase[ti])) +
            0.2 * Math.sin(2 * Math.PI * (2.7 * f * t + phase[2])) +
            (rand() - 0.5) * 0.28,
          -1,
          1
        );
        const r = Math.sqrt(r0b * r0b + v * (r1b * r1b - r0b * r0b));
        const deg = mid + (u * thetaDeg) / 2;
        const [x, y] = polar(r, deg);
        const mag = clamp(Math.round(page.importance || 3), 1, 5);
        const i = stars.length;
        stars.push({
          i,
          k,
          slug: page.slug,
          title: page.title,
          href: page.href,
          x,
          y,
          r: page.written ? magR(mag) : r1(PLANNED_R * mScale),
          mag: page.written ? mag : 0,
          written: page.written,
          hit: 0,
          alpha: false,
        });
        if (!bySlug.has(page.slug)) bySlug.set(page.slug, i);
        chain.push(i);
        idx++;
      }
      if (chain.length) catChains.push(chain);
    });
    chains.push(catChains);
  });

  const bounds = (s: ChartStar) => sectors[s.k];
  for (let it = 0; it < 90; it++) {
    for (let a = 0; a < stars.length; a++) {
      for (let b = a + 1; b < stars.length; b++) {
        const A = stars[a];
        const B = stars[b];
        const need = A.r + B.r + SPACING + (A.k === B.k ? 0 : 10);
        let dx = B.x - A.x;
        let dy = B.y - A.y;
        let d = Math.hypot(dx, dy);
        if (d >= need) continue;
        if (d < 1e-6) {
          const ang = rad((hash(A.slug + B.slug) % 360) + 0.5);
          dx = Math.cos(ang);
          dy = Math.sin(ang);
          d = 1;
        }
        const push = ((need - d) / 2) * 0.6;
        A.x -= (dx / d) * push;
        A.y -= (dy / d) * push;
        B.x += (dx / d) * push;
        B.y += (dy / d) * push;
      }
    }
    for (const s of stars) {
      const { s0, s1 } = bounds(s);
      const mid = (s0 + s1) / 2;
      let r = Math.hypot(s.x - C, s.y - C);
      let deg = (Math.atan2(s.y - C, s.x - C) * 180) / Math.PI;
      while (deg < mid - 180) deg += 360;
      while (deg >= mid + 180) deg -= 360;
      r = clamp(r, R_IN - 16, rOut + 12);
      const pad = ((14 + s.r) / r) * (180 / Math.PI);
      deg = s1 - s0 > 2 * pad ? clamp(deg, s0 + pad, s1 - pad) : mid;
      [s.x, s.y] = polar(r, deg);
    }
  }

  for (const s of stars) {
    s.x = r1(s.x);
    s.y = r1(s.y);
    let nn = Infinity;
    for (const o of stars) if (o !== s) nn = Math.min(nn, Math.hypot(o.x - s.x, o.y - s.y));
    s.hit = r1(clamp(nn / 2 - 0.5, s.r + 4, 34));
  }

  const written = stars.filter((s) => s.written);
  const brightest: number[] = [];
  if (written.length) {
    const degree = new Map<number, number>();
    cats.forEach((cat) =>
      cat.pages.forEach((p) => {
        const i = bySlug.get(p.slug);
        if (i == null) return;
        degree.set(i, (degree.get(i) ?? 0) + p.related.length);
        for (const r of p.related) {
          const j = bySlug.get(r);
          if (j != null) degree.set(j, (degree.get(j) ?? 0) + 1);
        }
      })
    );
    const ranked = [...written].sort(
      (a, b) =>
        b.mag - a.mag ||
        (degree.get(b.i) ?? 0) - (degree.get(a.i) ?? 0) ||
        hash(input.seed + a.slug) - hash(input.seed + b.slug)
    );
    ranked[0].alpha = true;
    brightest.push(...ranked.slice(0, 3).map((s) => s.i));
  }
  const bayer = brightest.map((i, j) => {
    const s = stars[i];
    const dx = s.x - C;
    const dy = s.y - C;
    const d = Math.hypot(dx, dy) || 1;
    const px = -dy / d;
    const py = dx / d;
    const off = s.r + (s.mag >= 5 ? 17 : s.mag >= 4 ? 14 : 10);
    return {
      i,
      letter: "αβγ"[j],
      x: r1(s.x + (px * 0.7 + (dx / d) * 0.7) * off),
      y: r1(s.y + (py * 0.7 + (dy / d) * 0.7) * off),
    };
  });

  const pt = (i: number): [number, number] => [stars[i].x, stars[i].y];
  const key = (a: number, b: number) => (a < b ? `${a}-${b}` : `${b}-${a}`);
  const edges: { k: number; a: number; b: number; order: number }[] = [];
  const have = new Set<string>();
  const valence = new Map<number, number>();
  const addEdge = (k: number, a: number, b: number) => {
    have.add(key(a, b));
    valence.set(a, (valence.get(a) ?? 0) + 1);
    valence.set(b, (valence.get(b) ?? 0) + 1);
    edges.push({ k, a, b, order: edges.filter((e) => e.k === k).length });
  };

  for (const catChains of chains) {
    for (const chain of catChains) {
      for (let pass = 0; pass < 12; pass++) {
        let changed = false;
        for (let i = 0; i < chain.length - 3; i++) {
          for (let j = i + 2; j < chain.length - 1; j++) {
            const P = (x: number): [number, number] => [stars[chain[x]].x, stars[chain[x]].y];
            if (segCross(P(i), P(i + 1), P(j), P(j + 1))) {
              const mid = chain.slice(i + 1, j + 1).reverse();
              chain.splice(i + 1, mid.length, ...mid);
              changed = true;
            }
          }
        }
        if (!changed) break;
      }
    }
  }

  chains.forEach((catChains, k) => {
    const placed: number[] = [];
    for (const chain of catChains) {
      if (placed.length) {
        const head = chain[0];
        let best = placed[0];
        let bestD = Infinity;
        for (const p of placed) {
          const d = Math.hypot(stars[p].x - stars[head].x, stars[p].y - stars[head].y);
          if (d < bestD) {
            bestD = d;
            best = p;
          }
        }
        addEdge(k, best, head);
      }
      for (let j = 1; j < chain.length; j++) addEdge(k, chain[j - 1], chain[j]);
      placed.push(...chain);
    }
  });

  const spineLens = edges.map((e) =>
    Math.hypot(stars[e.a].x - stars[e.b].x, stars[e.a].y - stars[e.b].y)
  );
  const median = spineLens.length
    ? [...spineLens].sort((a, b) => a - b)[Math.floor(spineLens.length / 2)]
    : 80;

  const intra: { k: number; a: number; b: number; len: number }[] = [];
  const cross: { a: number; b: number; score: number }[] = [];
  const seenPair = new Set<string>();
  cats.forEach((cat) =>
    cat.pages.forEach((p) => {
      const a = bySlug.get(p.slug);
      if (a == null || !stars[a].written) return;
      for (const r of p.related) {
        const b = bySlug.get(r);
        if (b == null || b === a || !stars[b].written) continue;
        const kk = key(a, b);
        if (seenPair.has(kk) || have.has(kk)) continue;
        seenPair.add(kk);
        if (stars[a].k === stars[b].k) {
          intra.push({
            k: stars[a].k,
            a,
            b,
            len: Math.hypot(stars[a].x - stars[b].x, stars[a].y - stars[b].y),
          });
        } else {
          cross.push({
            a,
            b,
            score: stars[a].mag + stars[b].mag + (hash(input.seed + kk) % 1000) / 1000,
          });
        }
      }
    })
  );

  intra.sort((x, y) => x.len - y.len);
  const intraCap = new Map<number, number>();
  for (const cand of intra) {
    const n = cats[cand.k].pages.length;
    const cap = Math.max(1, Math.round(n * 0.4));
    if ((intraCap.get(cand.k) ?? 0) >= cap) continue;
    if (cand.len > median * 1.9) continue;
    if ((valence.get(cand.a) ?? 0) >= 4 || (valence.get(cand.b) ?? 0) >= 4) continue;
    const A = pt(cand.a);
    const B = pt(cand.b);
    let blocked = false;
    for (const e of edges) {
      if (e.a === cand.a || e.a === cand.b || e.b === cand.a || e.b === cand.b) continue;
      if (segCross(A, B, pt(e.a), pt(e.b))) {
        blocked = true;
        break;
      }
    }
    if (!blocked) {
      for (const s of stars) {
        if (s.i === cand.a || s.i === cand.b) continue;
        if (pointSegDist([s.x, s.y], A, B) < s.r + 7) {
          blocked = true;
          break;
        }
      }
    }
    if (blocked) continue;
    addEdge(cand.k, cand.a, cand.b);
    intraCap.set(cand.k, (intraCap.get(cand.k) ?? 0) + 1);
  }

  const segments: ChartSegment[] = [];
  for (const e of edges) {
    const A = stars[e.a];
    const B = stars[e.b];
    const d = Math.hypot(B.x - A.x, B.y - A.y);
    const ga = A.r + (A.mag >= 4 ? 5 : 4);
    const gb = B.r + (B.mag >= 4 ? 5 : 4);
    if (d <= ga + gb + 2) continue;
    const ux = (B.x - A.x) / d;
    const uy = (B.y - A.y) / d;
    segments.push({
      k: e.k,
      a: e.a,
      b: e.b,
      order: e.order,
      d: `M${r1(A.x + ux * ga)} ${r1(A.y + uy * ga)}L${r1(B.x - ux * gb)} ${r1(B.y - uy * gb)}`,
    });
  }

  const linkCap = Math.min(16, Math.max(3, Math.round(stars.length * 0.12)));
  cross.sort((x, y) => y.score - x.score);
  const links: ChartLink[] = [];
  const perStar = new Map<number, number>();
  for (const cand of cross) {
    if (links.length >= linkCap) break;
    if ((perStar.get(cand.a) ?? 0) >= 2 || (perStar.get(cand.b) ?? 0) >= 2) continue;
    const A = stars[cand.a];
    const B = stars[cand.b];
    const mx = (A.x + B.x) / 2;
    const my = (A.y + B.y) / 2;
    const pull = 0.42;
    const cx = C + (mx - C) * pull;
    const cy = C + (my - C) * pull;
    const off = (s: ChartStar, tx: number, ty: number, g: number): [number, number] => {
      const d = Math.hypot(tx - s.x, ty - s.y) || 1;
      return [s.x + ((tx - s.x) / d) * g, s.y + ((ty - s.y) / d) * g];
    };
    const [ax, ay] = off(A, cx, cy, A.r + 6);
    const [bx, by] = off(B, cx, cy, B.r + 6);
    links.push({
      a: cand.a,
      b: cand.b,
      d: `M${r1(ax)} ${r1(ay)}Q${r1(cx)} ${r1(cy)} ${r1(bx)} ${r1(by)}`,
    });
    perStar.set(cand.a, (perStar.get(cand.a) ?? 0) + 1);
    perStar.set(cand.b, (perStar.get(cand.b) ?? 0) + 1);
  }

  const labels: ChartLabel[] = cats.map((cat, k) => {
    const { s0, s1 } = sectors[k];
    const mid = (s0 + s1) / 2;
    const norm = ((mid % 360) + 360) % 360;
    const reverse = norm > 2 && norm < 178;
    const [nx, ny] = polar(R_LABEL, mid);
    const parts = twoLine[k] && splits[k] ? splits[k]! : [texts[k].text];
    const step = parts.length > 1 ? 10 : 0;
    const lines = parts.map((text, j) => {
      const r = R_LABEL + (j === 0 ? step : -step) * (reverse ? -1 : 1);
      return { id: `sc-arc-${k}-${j}`, d: arcPath(r, s0, s1, reverse), text };
    });
    const mNeed = toDeg(
      MOBILE_RING * 1.4 + labelWidth(texts[k].text, MOBILE_RING, texts[k].latin) + 36
    );
    return {
      mobile:
        s1 - s0 >= mNeed ? { id: `sc-arc-${k}-m`, d: arcPath(R_LABEL, s0, s1, reverse) } : null,
      k,
      slug: cat.slug,
      num: cat.num,
      text: texts[k].text,
      latin: texts[k].latin,
      lines,
      fits: s1 - s0 >= need[k] - 0.01,
      start: s0,
      end: s1,
      numX: r1(nx),
      numY: r1(ny),
    };
  });

  const boundaries: string[] = [];
  const dividers: string[] = [];
  if (K > 1) {
    for (const { s0 } of sectors) {
      const b = s0 - gap / 2;
      const [x0, y0] = polar(140, b);
      const [x1, y1] = polar(R_FIELD, b);
      boundaries.push(`M${r1(x0)} ${r1(y0)}L${r1(x1)} ${r1(y1)}`);
      const [x2, y2] = polar(R_FIELD, b);
      const [x3, y3] = polar(R_TICK, b);
      dividers.push(`M${r1(x2)} ${r1(y2)}L${r1(x3)} ${r1(y3)}`);
    }
  }

  const hours: string[] = [];
  for (let h = 0; h < 360; h += 90) {
    const [x0, y0] = polar(14, h - 90);
    const [x1, y1] = polar(R_FIELD, h - 90);
    hours.push(`M${r1(x0)} ${r1(y0)}L${r1(x1)} ${r1(y1)}`);
  }

  const frand = rng(`${input.seed}/field`);
  const small: string[] = [];
  const large: string[] = [];
  const field: [number, number][] = [];
  const fieldCount = clamp(150 - stars.length, 60, 130);
  let tries = 0;
  while (field.length < fieldCount && tries < fieldCount * 30) {
    tries++;
    const r = Math.sqrt(frand()) * (R_FIELD - 10);
    const [x, y] = polar(r, frand() * 360);
    if (stars.some((s) => Math.hypot(s.x - x, s.y - y) < s.r + 12)) continue;
    if (field.some(([fx, fy]) => Math.hypot(fx - x, fy - y) < 9)) continue;
    field.push([x, y]);
    (frand() < 0.22 ? large : small).push(`M${r1(x)} ${r1(y)}h0`);
  }

  const pts: [number, number][][] = segments.map((sg) => [
    [stars[sg.a].x, stars[sg.a].y],
    [stars[sg.b].x, stars[sg.b].y],
  ]);
  for (const ln of links) {
    const A = stars[ln.a];
    const B = stars[ln.b];
    const m = ln.d.match(/Q([\d.-]+) ([\d.-]+)/);
    if (!m) continue;
    const qx = +m[1];
    const qy = +m[2];
    let prev: [number, number] = [A.x, A.y];
    for (let j = 1; j <= 8; j++) {
      const t = j / 8;
      const u = 1 - t;
      const nxt: [number, number] = [
        u * u * A.x + 2 * u * t * qx + t * t * B.x,
        u * u * A.y + 2 * u * t * qy + t * t * B.y,
      ];
      pts.push([prev, nxt]);
      prev = nxt;
    }
  }
  const glyphBoxes: Box[] = bayer.map((b) => ({
    x0: b.x - 8,
    y0: b.y - 10,
    x1: b.x + 8,
    y1: b.y + 10,
  }));
  glyphBoxes.push({ x0: C - 14, y0: C - 14, x1: C + 14, y1: C + 14 });
  const rules: [number, number][][] = [];
  if (K > 1) {
    for (const { s0 } of sectors)
      rules.push([polar(140, s0 - gap / 2), polar(R_FIELD, s0 - gap / 2)]);
  }
  for (let hh = 0; hh < 360; hh += 90) rules.push([polar(14, hh - 90), polar(R_FIELD, hh - 90)]);
  const reach = (s: ChartStar) => s.r + (s.mag >= 5 ? 10 : s.mag >= 4 ? 8 : 5);
  const lead: ChartStar[][] = [];
  cats.forEach((_, k) => {
    const own = stars.filter((s) => s.k === k && s.written);
    if (!own.length) return;
    own.sort(
      (a, b) =>
        Number(b.alpha) - Number(a.alpha) ||
        b.mag - a.mag ||
        hash(input.seed + a.slug) - hash(input.seed + b.slug)
    );
    lead.push(own.slice(0, 3));
  });
  const sizeOf = (k: number) => cats[k].pages.length;

  const placeTags = (groups: ChartStar[][], scale: number, cap: number): ChartTag[] => {
    const tagBoxes: Box[] = [];
    const leaders: [number, number][][] = [];
    const out: ChartTag[] = [];
    const tryTag = (s: ChartStar, strict: boolean): boolean => {
      const t = tagText(s.title);
      if (!t) return false;
      const size = (t.latin ? TAG_LATIN : TAG_CJK) * scale;
      const lh = size * 1.22;
      const w = Math.max(...t.lines.map((ln) => tagWidth(ln, size)));
      const h = lh * t.lines.length + size * 0.08;
      const g = reach(s) + 3;
      const outX = s.x >= C ? 1 : -1;
      const dirs = [0, 180, -30, 30, 150, 210, -60, 60, 120, 240, -90, 90];
      for (const extra of [0, 24 * scale, 50 * scale]) {
        for (const base of dirs) {
          const deg = outX > 0 ? base : 180 - base;
          const ux = Math.cos(rad(deg));
          const uy = Math.sin(rad(deg));
          const d = g + extra;
          const px = s.x + ux * d;
          const py = s.y + uy * d;
          let anchor: ChartTag["anchor"];
          let x0: number;
          if (ux > 0.3) {
            anchor = "start";
            x0 = px;
          } else if (ux < -0.3) {
            anchor = "end";
            x0 = px - w;
          } else {
            anchor = "middle";
            x0 = px - w / 2;
          }
          const y0 =
            Math.abs(uy) < 0.3
              ? py - h / 2
              : uy < 0
                ? py - h * (Math.abs(ux) > 0.3 ? 0.75 : 1)
                : py - h * (Math.abs(ux) > 0.3 ? 0.25 : 0);
          const box = { x0, y0, x1: x0 + w, y1: y0 + h };
          const pad: Box = { x0: box.x0 - 5, y0: box.y0 - 3, x1: box.x1 + 5, y1: box.y1 + 3 };
          const corners: [number, number][] = [
            [pad.x0, pad.y0],
            [pad.x1, pad.y0],
            [pad.x1, pad.y1],
            [pad.x0, pad.y1],
          ];
          if (corners.some(([x, y]) => Math.hypot(x - C, y - C) > R_FIELD - 8)) continue;
          if (stars.some((o) => boxHitsCircle(pad, o.x, o.y, reach(o)))) continue;
          if (pts.some(([p, q]) => boxHitsSeg(pad, p, q))) continue;
          if (strict && rules.some(([p, q]) => boxHitsSeg(pad, p, q))) continue;
          if (glyphBoxes.some((o) => boxesOverlap(pad, o))) continue;
          if (tagBoxes.some((o) => boxesOverlap(pad, o))) continue;
          if (leaders.some(([p, q]) => boxHitsSeg(pad, p, q))) continue;
          let leader: string | null = null;
          if (extra > 0) {
            const cx = clamp(s.x, box.x0, box.x1);
            const cy = clamp(s.y, box.y0, box.y1);
            const dist = Math.hypot(cx - s.x, cy - s.y) || 1;
            const lx = (cx - s.x) / dist;
            const ly = (cy - s.y) / dist;
            const p: [number, number] = [s.x + lx * (reach(s) + 1), s.y + ly * (reach(s) + 1)];
            const q: [number, number] = [cx - lx * 4, cy - ly * 4];
            if (stars.some((o) => o !== s && pointSegDist([o.x, o.y], p, q) < reach(o))) continue;
            if (tagBoxes.some((o) => boxHitsSeg(o, p, q))) continue;
            leaders.push([p, q]);
            leader = `M${r1(p[0])} ${r1(p[1])}L${r1(q[0])} ${r1(q[1])}`;
          }
          tagBoxes.push(pad);
          out.push({
            k: s.k,
            i: s.i,
            lines: t.lines,
            latin: t.latin,
            size: r1(size),
            x: r1(anchor === "start" ? box.x0 : anchor === "end" ? box.x1 : (box.x0 + box.x1) / 2),
            y: r1((box.y0 + box.y1) / 2),
            anchor,
            leader,
          });
          return true;
        }
      }
      return false;
    };
    for (const group of groups) {
      if (out.length >= cap) break;
      let done = false;
      for (const strict of [true, false]) {
        for (const st of group) {
          if (tryTag(st, strict)) {
            done = true;
            break;
          }
        }
        if (done) break;
      }
    }
    return out;
  };

  const tagScale = sparse ? 1.18 : 1;
  const tags = placeTags(
    lead.slice().sort((a, b) => sizeOf(b[0].k) - sizeOf(a[0].k) || b[0].mag - a[0].mag),
    tagScale,
    TAG_CAP
  );
  const mobileTags = placeTags(
    lead
      .slice()
      .sort(
        (a, b) =>
          Number(b[0].alpha) - Number(a[0].alpha) ||
          b[0].mag - a[0].mag ||
          sizeOf(b[0].k) - sizeOf(a[0].k)
      ),
    1.75,
    5
  );

  const sectorPaths = sectors.map((sc, k) => ({
    k,
    d: annularSector(
      R_IN - 30,
      R_TICK,
      sc.s0 - (K > 1 ? gap / 2 : 0),
      sc.s1 + (K > 1 ? gap / 2 : 0)
    ),
  }));

  const plannedCount = stars.filter((s) => !s.written).length;
  return {
    stars,
    segments,
    links,
    labels,
    furniture: {
      size: SIZE,
      c: C,
      rOuter: R_OUTER,
      rTick: R_TICK,
      rLabel: R_LABEL,
      rField: R_FIELD,
      declination: sparse ? [180, 320] : [140, 250, 360],
      boundaries: boundaries.join(""),
      dividers: dividers.join(""),
      hours: hours.join(""),
      fieldSmall: small.join(""),
      fieldLarge: large.join(""),
      rays: [4, 5].map((mag) => ({ mag, d: rayPath(0, 0, magR(mag), mag) })),
    },
    counts: {
      stars: stars.length,
      written: stars.length - plannedCount,
      planned: plannedCount,
      constellations: K,
    },
    abbreviated: labels.some((l) => !l.fits),
    sparse,
    labelScale: Math.round(labelScale * 100) / 100,
    bayer,
    tags,
    mobileTags,
    sectors: sectorPaths,
  };
}
