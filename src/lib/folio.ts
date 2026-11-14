import { splitBookLabel } from "./links";
import { coverPlateFor } from "./cover-plate";
import { motifSvg } from "./motifs";
import { pad2 } from "./toc";

export interface Folio {
  unit: string;
  num: number;
  name: string;
  href: string;
  page: number;
  pages: number;
  leaf: number;
  leaves: number;
}

export function folioFor<E extends { id: string }>(opts: {
  entry: E;
  unit: string;
  num: number;
  name: string;
  href: string;
  siblings: E[];
  volume: E[];
}): Folio {
  const { entry, siblings, volume } = opts;
  return {
    unit: opts.unit,
    num: opts.num,
    name: opts.name,
    href: opts.href,
    page: siblings.findIndex((e) => e.id === entry.id) + 1,
    pages: siblings.length,
    leaf: volume.findIndex((e) => e.id === entry.id) + 1,
    leaves: volume.length,
  };
}

export const chapterPrefix = (f: Folio): string | undefined =>
  f.num > 0 ? `--ch: "${pad2(f.num)}."` : undefined;

export function sourceBooks(items: { label: string }[]): string[] {
  const out: string[] = [];
  for (const it of items) {
    const book = splitBookLabel(it.label).book || it.label.trim();
    if (book && !out.includes(book)) out.push(book);
  }
  return out;
}

export function endpaperPattern(slug: string): string | undefined {
  const plate = coverPlateFor(slug);
  if (!plate) return undefined;
  const svg = motifSvg(plate.motif, { stroke: 10, fit: true }).replace(/currentColor/g, "#000");
  return `--ep-motif: url("data:image/svg+xml,${encodeURIComponent(svg)}")`;
}
