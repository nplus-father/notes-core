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
