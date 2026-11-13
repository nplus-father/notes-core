import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { visit, SKIP } from "unist-util-visit";

const FORBIDDEN = [
  [/<style[\s>]/i, "<style> (diagram colours come from notes-core tokens)"],
  [/\sstyle\s*=/i, "a style attribute"],
  [/<script[\s>]/i, "<script>"],
  [/<foreignObject[\s>]/i, "<foreignObject>"],
  [/<image[\s>]/i, "<image>"],
  [/\s(?:fill|stroke|color|stop-color)\s*=\s*"(?!none")[^"]*"/i, "a fill/stroke colour attribute"],
  [/\sfont-(?:family|size)\s*=/i, "a font attribute (use the d-* text classes)"],
];

const fail = (file, msg) => {
  throw new Error(`[notes-core figure] ${file}: ${msg}`);
};

export function prepareSvg(raw, prefix, where) {
  let svg = raw
    .replace(/<\?xml[^>]*\?>/g, "")
    .replace(/<!DOCTYPE[^>]*>/gi, "")
    .replace(/<!--[\s\S]*?-->/g, "")
    .trim();
  if (!svg.startsWith("<svg")) fail(where, "file must be a single <svg> element");
  for (const [re, what] of FORBIDDEN) if (re.test(svg)) fail(where, `contains ${what}`);
  const open = svg.match(/^<svg\b[^>]*>/)[0];
  const vb = open.match(/viewBox\s*=\s*"\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)\s*"/);
  if (!vb) fail(where, "<svg> needs a viewBox");
  if (!/<title>[^<]+<\/title>/.test(svg)) fail(where, "needs a non-empty <title>");
  if (!/<desc>[^<]+<\/desc>/.test(svg)) fail(where, "needs a non-empty <desc>");

  svg = svg
    .replace(/\sid="([^"]+)"/g, ` id="${prefix}-$1"`)
    .replace(/url\(#([^)]+)\)/g, `url(#${prefix}-$1)`)
    .replace(/href="#([^"]+)"/g, `href="#${prefix}-$1"`)
    .replace(/<title>/, `<title id="${prefix}-title">`)
    .replace(/<desc>/, `<desc id="${prefix}-desc">`);

  const attrs = open
    .replace(/^<svg\b/, "")
    .replace(/>$/, "")
    .replace(/\s(?:width|height|role|class|aria-[a-z]+|focusable)\s*=\s*"[^"]*"/g, "");
  const head =
    `<svg${attrs} class="diagram-svg" role="img" focusable="false"` +
    ` aria-labelledby="${prefix}-title" aria-describedby="${prefix}-desc">`;
  return {
    svg: svg.replace(/^<svg\b[^>]*>/, head),
    width: Number(vb[1]),
    height: Number(vb[2]),
  };
}

export default function remarkFigure() {
  return (tree, file) => {
    const from = String(file?.path || file?.history?.[0] || "");
    let n = 0;
    visit(tree, "leafDirective", (node, index, parent) => {
      if (node.name !== "figure" || !parent || index == null) return;
      const src = node.attributes?.src;
      if (!src) fail(from, "::figure needs a src attribute");
      if (!(node.children || []).length)
        fail(from, `::figure{src="${src}"} needs a caption in [brackets]`);
      const at = resolve(dirname(from), src);
      let raw;
      try {
        raw = readFileSync(at, "utf8");
      } catch {
        fail(from, `cannot read ${src} (resolved to ${at})`);
      }
      n += 1;
      const prefix = `fig${n}`;
      const { svg, width, height } = prepareSvg(raw, prefix, at);
      parent.children[index] = {
        type: "diagramFigure",
        data: {
          hName: "figure",
          hProperties: {
            className: ["diagram"],
            style: `--fig-w:${width};--fig-ratio:${width} / ${height}`,
          },
        },
        children: [
          {
            type: "html",
            value:
              `<div class="diagram-scroll" data-pagefind-ignore tabindex="0" role="group" aria-labelledby="${prefix}-cap">` +
              `${svg}</div>`,
          },
          {
            type: "paragraph",
            data: {
              hName: "figcaption",
              hProperties: { id: `${prefix}-cap`, className: ["diagram-cap"] },
            },
            children: [
              {
                type: "emphasis",
                data: { hName: "span", hProperties: { className: ["diagram-no"], lang: "en" } },
                children: [],
              },
              {
                type: "emphasis",
                data: { hName: "span", hProperties: { className: ["diagram-text"] } },
                children: node.children,
              },
              {
                type: "emphasis",
                data: {
                  hName: "span",
                  hProperties: {
                    className: ["diagram-scroll-hint"],
                    ariaHidden: "true",
                    lang: "en",
                  },
                },
                children: [{ type: "text", value: "Scroll →" }],
              },
            ],
          },
        ],
      };
      return SKIP;
    });
  };
}
