import { siteBySlug, topicSites, personSites } from "./sites";
import { clothFor, coverPlateFor, sealFor } from "./cover-plate";
import { motifSvg } from "./motifs";

const PAPER = "#f6f3ec";
const NIGHT = "#111013";

function luminance(hex: string): number {
  const m = hex.replace("#", "").match(/^([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
  if (!m) return 0;
  const [r, g, b] = m.slice(1).map((h) => {
    const c = parseInt(h, 16) / 255;
    return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

export function contrast(a: string, b: string): number {
  const [x, y] = [luminance(a), luminance(b)].sort((p, q) => q - p);
  return (x + 0.05) / (y + 0.05);
}

export interface Volume {
  serial: string;
  label: string;
  emblem: string | null;
  style: string | undefined;
}

export function currentVolume(fallbackLabel: string): Volume {
  const slug = import.meta.env.BASE_URL.replace(/^\/|\/$/g, "");
  const station = siteBySlug.get(slug);
  const pool = station?.axis === "person" ? personSites : topicSites;
  const idx = pool.findIndex((s) => s.slug === slug);
  const plate = coverPlateFor(slug);
  const cloth = clothFor(slug);
  const vars: string[] = [];
  const seal = sealFor(slug);
  if (cloth) {
    const light = [cloth.light, seal?.light].find((c) => c && contrast(c, PAPER) >= 3);
    const dark = [cloth.dark, cloth.light, seal?.dark].find((c) => c && contrast(c, NIGHT) >= 3);
    if (light) vars.push(`--vol-l: ${light}`);
    if (dark) vars.push(`--vol-d: ${dark}`);
  }
  return {
    serial: idx >= 0 ? `N°${String(idx + 1).padStart(2, "0")}` : "",
    label: station?.label ?? fallbackLabel,
    emblem: plate
      ? motifSvg(plate.motif, { className: "volume-emblem", stroke: 9, fit: true })
      : null,
    style: vars.length ? vars.join("; ") : undefined,
  };
}
