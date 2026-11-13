import { visit, SKIP } from "unist-util-visit";

const PAIR = /^(前|後)\s*[—–-]+\s*/;
const FITS = [32, 40, 48, 56];

const span = (className, value, extra = {}) => ({
  type: "emphasis",
  data: { hName: "span", hProperties: { className, ...extra } },
  children: value == null ? [] : [{ type: "text", value }],
});

const isDetails = (node) => node?.type === "containerDirective" && node.name === "details";

const sideOf = (node) => {
  const title = node.attributes?.title || "";
  const m = title.match(PAIR);
  if (!m) return null;
  return { side: m[1] === "前" ? "before" : "after", text: title.slice(m[0].length) };
};

const cols = (line) => [...line].reduce((n, ch) => n + (/[ᄀ-￯]/u.test(ch) ? 2 : 1), 0);

const widest = (node) => {
  let max = 0;
  visit(node, "code", (c) => {
    for (const line of (c.value || "").split("\n")) {
      max = Math.max(max, cols(line.replace(/\t/g, "  ")));
    }
  });
  return max;
};

function pane(node, info) {
  const label = info.side === "before" ? "Before" : "After";
  return {
    type: "comparePane",
    data: { hName: "div", hProperties: { className: ["compare-pane", `is-${info.side}`] } },
    children: [
      {
        type: "paragraph",
        data: { hName: "p", hProperties: { className: ["compare-head"] } },
        children: [span(["compare-side"], label, { lang: "en" })],
      },
      ...node.children,
    ],
  };
}

function compare(before, after, b, a, open) {
  const need = Math.max(widest(before), widest(after));
  const fit = FITS.find((n) => need <= n);
  return {
    type: "compare",
    data: {
      hName: "details",
      hProperties: {
        className: ["lc-details", "compare", ...(fit ? [`fit-${fit}`] : [])],
        ...(open ? { open: true } : {}),
      },
    },
    children: [
      {
        type: "paragraph",
        data: { hName: "summary" },
        children: [
          {
            type: "emphasis",
            data: { hName: "span", hProperties: { className: ["details-side"], lang: "en" } },
            children: [span(["details-side-text"], "Before / After")],
          },
          {
            type: "emphasis",
            data: { hName: "span", hProperties: { className: ["details-title"] } },
            children: [
              span(["compare-from"], b.text),
              span(["compare-arrow"], " → ", { ariaHidden: "true" }),
              span(["visually-hidden"], "；"),
              span(["compare-to"], a.text),
            ],
          },
          span(["details-mark"], null, { ariaHidden: "true" }),
        ],
      },
      {
        type: "compareGrid",
        data: { hName: "div", hProperties: { className: ["compare-grid"] } },
        children: [pane(before, b), pane(after, a)],
      },
    ],
  };
}

function pairUp(tree) {
  let first = true;
  visit(tree, (parent) => {
    if (!parent.children) return;
    for (let i = 0; i < parent.children.length - 1; i++) {
      const x = parent.children[i];
      const y = parent.children[i + 1];
      if (!isDetails(x) || !isDetails(y)) continue;
      const b = sideOf(x);
      const a = sideOf(y);
      if (b?.side !== "before" || a?.side !== "after") continue;
      const open = first || x.attributes?.open !== undefined || y.attributes?.open !== undefined;
      parent.children.splice(i, 2, compare(x, y, b, a, open));
      first = false;
    }
  });
}

function openFirstDesign(tree, file) {
  const where = String(file?.path || file?.history?.[0] || "");
  if (!/[\\/]problems[\\/]/.test(where)) return;
  const top = tree.children || [];
  const ref = top.findIndex((n) => n.type === "leafDirective" && n.name === "reference");
  const from = ref >= 0 ? ref + 1 : 0;
  let target = null;
  for (const node of top.slice(from)) {
    visit(node, (n) => {
      if (target) return SKIP;
      if (isDetails(n)) {
        target = n;
        return SKIP;
      }
    });
    if (target) break;
  }
  if (target) target.attributes = { ...(target.attributes || {}), open: "" };
}

export default function remarkDetails() {
  return (tree, file) => {
    openFirstDesign(tree, file);
    pairUp(tree);

    visit(tree, (node) => {
      if (!isDetails(node)) return;

      const attrs = node.attributes || {};
      const title = attrs.title || "Details";
      const open = attrs.open !== undefined && attrs.open !== null;
      const pair = sideOf(node);

      const className = ["lc-details"];
      if (pair) className.push(`is-${pair.side}`);

      const data = node.data || (node.data = {});
      data.hName = "details";
      data.hProperties = { className, ...(open ? { open: true } : {}) };

      const summaryKids = [];
      if (pair) {
        const label = pair.side === "before" ? "Before" : "After";
        summaryKids.push(span(["details-side"], label, { lang: "en" }));
      }
      summaryKids.push(span(["details-title"], pair ? pair.text : title));
      summaryKids.push(span(["details-mark"], null, { ariaHidden: "true" }));

      node.children.unshift({
        type: "paragraph",
        data: { hName: "summary" },
        children: summaryKids,
      });
    });
  };
}
