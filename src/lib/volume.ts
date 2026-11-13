import { siteBySlug, topicSites, personSites } from "./sites";
import { coverPlateFor } from "./cover-plate";
import { motifSvg } from "./motifs";

export interface Volume {
  serial: string;
  label: string;
  emblem: string | null;
}

export function currentVolume(fallbackLabel: string): Volume {
  const slug = import.meta.env.BASE_URL.replace(/^\/|\/$/g, "");
  const station = siteBySlug.get(slug);
  const pool = station?.axis === "person" ? personSites : topicSites;
  const idx = pool.findIndex((s) => s.slug === slug);
  const plate = coverPlateFor(slug);
  return {
    serial: idx >= 0 ? `N°${String(idx + 1).padStart(2, "0")}` : "",
    label: station?.label ?? fallbackLabel,
    emblem: plate
      ? motifSvg(plate.motif, { className: "volume-emblem", stroke: 9, fit: true })
      : null,
  };
}
