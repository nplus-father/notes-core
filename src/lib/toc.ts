const EN_TAIL = /^(.*?[^\s])\s*[（(]([^()（）]*[A-Za-z][^()（）]*)[)）]\s*$/;
const CJK = /[㐀-鿿豈-﫿]/;

export function splitTitle(title: string): { main: string; sub: string; en: string } {
  const m = title.match(EN_TAIL);
  if (m && CJK.test(m[1]) && !CJK.test(m[2])) return { main: m[1], sub: "", en: m[2] };
  const i = title.indexOf("：");
  if (i > 0 && i < title.length - 1 && CJK.test(title)) {
    return { main: title.slice(0, i + 1), sub: title.slice(i + 1), en: "" };
  }
  return { main: title, sub: "", en: "" };
}

export function standfirst(body: string | undefined): string {
  if (!body) return "";
  for (const raw of body.split("\n")) {
    const line = raw.trim();
    if (!line) continue;
    if (!line.startsWith(">")) return "";
    const text = line.replace(/^>\s*/, "");
    if (text.startsWith("[!")) return "";
    return text
      .replace(/!?\[([^\]]*)\]\([^)]*\)/g, "$1")
      .replace(/(\*\*|__|\*|`)/g, "")
      .replace(/<[^>]+>/g, "")
      .trim();
  }
  return "";
}

export function chapterNumbers<C extends { slug: string; order: number; roadmap?: unknown[] }>(
  categories: C[],
  hasPages: (slug: string) => boolean
): Map<string, number> {
  const out = new Map<string, number>();
  let n = 0;
  for (const c of [...categories].sort((a, b) => a.order - b.order)) {
    if ((c.roadmap?.length ?? 0) > 0 || hasPages(c.slug)) out.set(c.slug, ++n);
  }
  return out;
}

export const pad2 = (n: number): string => String(n).padStart(2, "0");

export const STATUS_MARK: Record<string, string> = {
  studied: "Studied",
  reviewed: "Reviewed",
};

export const DIFFICULTY_LEVEL: Record<string, number> = { easy: 1, medium: 2, hard: 3 };

export const latinLang = (text: string): "en" | undefined =>
  /^[\x20-\x7e–—’]+$/.test(text) ? "en" : undefined;
