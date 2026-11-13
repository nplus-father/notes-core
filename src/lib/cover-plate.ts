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
  return cover.cloth?.hue ?? oklchHue(cover.accent2);
}

const gamma = (c: number) => (c <= 0.0031308 ? 12.92 * c : 1.055 * c ** (1 / 2.4) - 0.055);

function oklchToRgb(l: number, c: number, h: number): number[] {
  const a = c * Math.cos((h * Math.PI) / 180);
  const b = c * Math.sin((h * Math.PI) / 180);
  const l_ = (l + 0.3963377774 * a + 0.2158037573 * b) ** 3;
  const m_ = (l - 0.1055613458 * a - 0.0638541728 * b) ** 3;
  const s_ = (l - 0.0894841775 * a - 1.291485548 * b) ** 3;
  return [
    4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
    -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
    -0.0041960863 * l_ - 0.7034186147 * m_ + 1.707614701 * s_,
  ];
}

export function oklchHex(l: number, c: number, h: number): string {
  let chroma = c;
  let rgb = oklchToRgb(l, chroma, h);
  while (rgb.some((v) => v < 0 || v > 1) && chroma > 0) {
    chroma = Math.max(0, chroma - 0.002);
    rgb = oklchToRgb(l, chroma, h);
  }
  return (
    "#" +
    rgb
      .map((v) => Math.round(Math.min(1, Math.max(0, gamma(Math.min(1, Math.max(0, v))))) * 255))
      .map((v) => v.toString(16).padStart(2, "0"))
      .join("")
  );
}

export interface Cloth {
  light: string;
  dark: string;
}

const dye = (h: number) => {
  const warm = Math.max(0, Math.cos(((h - 75) * Math.PI) / 70));
  const blue = Math.max(0, Math.cos(((h - 255) * Math.PI) / 80));
  const green = Math.max(0, Math.cos(((h - 170) * Math.PI) / 100));
  const violet = Math.max(0, Math.cos(((h - 300) * Math.PI) / 60));
  return {
    l: 0.42 + 0.05 * warm - 0.02 * blue,
    c: 0.08 + 0.015 * warm - 0.008 * blue - 0.016 * green - 0.01 * violet,
  };
};

const clothOf = (h: number, tone = 0, chroma = 1): Cloth => {
  const { l, c } = dye(h);
  return {
    light: oklchHex(l + tone, c * chroma, h),
    dark: oklchHex(l - 0.1 + tone * 0.7, c * 0.8 * chroma, h),
  };
};

export const PERSON_CLOTH = clothOf(52, -0.02, 0.62);
export const AXIS_CLOTH = clothOf(235, -0.01, 0.5);

export function clothFor(slug: string): Cloth | undefined {
  const site = sites.find((s) => s.slug === slug);
  if (!site) return undefined;
  if (site.axis === "person") return PERSON_CLOTH;
  const cover = siteCovers[slug];
  if (!cover) return AXIS_CLOTH;
  return clothOf(cover.cloth?.hue ?? oklchHue(cover.accent2), cover.cloth?.tone ?? 0);
}
