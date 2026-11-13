import { sites } from "./sites.ts";
import { siteCovers } from "./site-covers.ts";
import { motifLegends } from "./motifs.ts";

export interface CoverPlateData {
  slug: string;
  title: string;
  en: string;
  serial: string;
  motif: string;
  legend: string;
}

const topicSlugs = sites.filter((s) => s.axis === "topic").map((s) => s.slug);

export function coverPlateFor(slug: string): CoverPlateData | undefined {
  const site = sites.find((s) => s.slug === slug);
  const cover = siteCovers[slug];
  if (!site || site.axis !== "topic" || !cover) return undefined;
  return {
    slug,
    title: site.label,
    en: site.brand.replace(/\s*Notes$/, ""),
    serial: String(topicSlugs.indexOf(slug) + 1).padStart(2, "0"),
    motif: cover.motif,
    legend: motifLegends[cover.motif] ?? "",
  };
}

const linear = (c: number) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);

export function oklchHue(hex: string): number {
  const [r, g, b] = [1, 3, 5].map((i) => linear(parseInt(hex.slice(i, i + 2), 16) / 255));
  const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
  const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
  const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
  const a = 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s;
  const bb = 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s;
  return Math.round(((Math.atan2(bb, a) * 180) / Math.PI + 360) % 360);
}

export function stationHue(slug: string): number | undefined {
  const cover = siteCovers[slug];
  const site = sites.find((s) => s.slug === slug);
  if (!cover || site?.axis !== "topic") return undefined;
  return oklchHue(cover.accent2);
}
