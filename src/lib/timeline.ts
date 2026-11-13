import type { BibliographyEntry } from "./library";

export type TimelineBar = {
  key: string;
  label: string;
  title: string;
  total: number;
  owned: number;
  gapAfter?: boolean;
};

const BUCKETS = [10, 20, 25, 50, 100, 200, 250, 500, 1000];
const MAX_BARS = 14;

export const yearLabel = (y: number): string => (y < 0 ? `${-y} BC` : `${y}`);

export function buildTimeline(entries: BibliographyEntry[]) {
  const years = entries
    .map((e) => e.year)
    .filter((y): y is number => typeof y === "number")
    .sort((a, b) => a - b);
  let bucket = BUCKETS[0];
  const lo = years.length ? years[0] : 0;
  const hi = years.length ? years[years.length - 1] : 0;
  const p5 = years.length ? years[Math.floor(years.length * 0.05)] : 0;
  const truncated = years.length >= 8 && p5 - lo > (hi - lo) * 0.5;
  const axisLo = truncated ? p5 : lo;
  const overflow = truncated
    ? entries.filter((e) => typeof e.year === "number" && e.year < axisLo)
    : [];

  const bars: TimelineBar[] = [];
  if (years.length >= 4) {
    bucket =
      BUCKETS.find((b) => Math.floor(hi / b) - Math.floor(axisLo / b) + 1 <= MAX_BARS) ??
      BUCKETS[BUCKETS.length - 1];
    if (overflow.length > 0) {
      const ownedN = overflow.filter((e) => e.status === "owned").length;
      bars.push({
        key: "earlier",
        label: "Earlier",
        title: `${yearLabel(lo)}–${yearLabel(axisLo - 1)} · ${overflow.length} · owned ${ownedN}`,
        total: overflow.length,
        owned: ownedN,
        gapAfter: true,
      });
    }
    const from = Math.floor(axisLo / bucket) * bucket;
    const to = Math.floor(hi / bucket) * bucket;
    for (let s = from; s <= to; s += bucket) {
      const inBucket = entries.filter(
        (e) => typeof e.year === "number" && e.year >= s && e.year < s + bucket
      );
      const ownedN = inBucket.filter((e) => e.status === "owned").length;
      bars.push({
        key: String(s),
        label: s >= 0 && bucket === 10 ? `${s}s` : yearLabel(s),
        title: `${yearLabel(s)}–${yearLabel(s + bucket - 1)} · ${inBucket.length} · owned ${ownedN}`,
        total: inBucket.length,
        owned: ownedN,
      });
    }
  }
  return {
    bars,
    years,
    lo,
    hi,
    show: bars.filter((b) => b.key !== "earlier").length >= 2,
    peak: Math.max(1, ...bars.map((b) => b.total)),
    labelEvery: bars.length > 10 ? 2 : 1,
    binWord: bucket === 10 ? "decade" : `${bucket}-year bin`,
  };
}
