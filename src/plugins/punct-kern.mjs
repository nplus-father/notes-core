const OPEN = "「『（《〈【〔";
const CLOSE = "」』）》〉】〕";
const MID = "，。、；：";
const STRAY =
  /(?<=[\p{Script=Han}A-Za-z0-9」』）》〉】〕])[ \t\n]+(?=[，。、；：？！」』）》〉】〕])/gu;

export function kernAmount(prev, ch) {
  if (prev === undefined) return "";
  const closing = CLOSE.includes(prev) || MID.includes(prev);
  if (closing && (MID.includes(ch) || OPEN.includes(ch))) {
    return MID.includes(prev) && MID.includes(ch) ? "" : "half";
  }
  if (CLOSE.includes(prev) && CLOSE.includes(ch)) return "quarter";
  if (OPEN.includes(prev) && OPEN.includes(ch)) return "quarter";
  return "";
}

export function collapseStraySpace(input) {
  return input.replace(STRAY, "");
}

export function kernPunct(input) {
  const chars = [...collapseStraySpace(input)];
  const parts = [];
  let buf = "";
  chars.forEach((ch, i) => {
    const kern = kernAmount(chars[i - 1], ch);
    if (kern) {
      if (buf) parts.push({ text: buf, kern: "" });
      parts.push({ text: ch, kern });
      buf = "";
    } else buf += ch;
  });
  if (buf) parts.push({ text: buf, kern: "" });
  return parts;
}

const kernSpan = (value, kern) => ({
  type: "emphasis",
  data: { hName: "span", hProperties: { className: ["pk", `is-${kern}`] } },
  children: [{ type: "text", value }],
});

export function kernTree(root) {
  let last;
  const visit = (node) => {
    if (node.type === "inlineCode") {
      last = undefined;
      return;
    }
    if (!node.children) return;
    const next = [];
    for (const child of node.children) {
      if (child.type !== "text") {
        visit(child);
        next.push(child);
        continue;
      }
      const chars = [...collapseStraySpace(child.value)];
      let buf = "";
      chars.forEach((ch, i) => {
        const kern = kernAmount(i === 0 ? last : chars[i - 1], ch);
        if (kern) {
          if (buf) next.push({ type: "text", value: buf });
          next.push(kernSpan(ch, kern));
          buf = "";
        } else buf += ch;
      });
      if (buf) next.push({ type: "text", value: buf });
      if (chars.length) last = chars[chars.length - 1];
    }
    node.children = next;
  };
  visit(root);
}
