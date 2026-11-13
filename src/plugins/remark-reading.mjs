import { visit, SKIP } from "unist-util-visit";

const LEADING_EMOJI =
  /^((?:\p{Extended_Pictographic}|\p{Regional_Indicator})(?:️|⃣|‍\p{Extended_Pictographic}|\p{Emoji_Modifier}|\p{Regional_Indicator})*)\s*/u;

const CJK_BEFORE = /[\p{Script=Han}　-〿＀-･—…「」『』（）《》〈〉]/u;
const CJK_PUNCT = /[\u3000-\u303F\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u2014\u2026」』）》〉]/u;

const LANGS = {
  js: "JavaScript",
  javascript: "JavaScript",
  jsx: "JSX",
  ts: "TypeScript",
  typescript: "TypeScript",
  tsx: "TSX",
  kt: "Kotlin",
  kotlin: "Kotlin",
  java: "Java",
  py: "Python",
  python: "Python",
  go: "Go",
  rust: "Rust",
  rs: "Rust",
  rb: "Ruby",
  ruby: "Ruby",
  c: "C",
  cpp: "C++",
  "c++": "C++",
  cs: "C#",
  csharp: "C#",
  swift: "Swift",
  scala: "Scala",
  php: "PHP",
  sql: "SQL",
  sh: "Shell",
  bash: "Shell",
  zsh: "Shell",
  shell: "Shell",
  console: "Console",
  yaml: "YAML",
  yml: "YAML",
  json: "JSON",
  toml: "TOML",
  xml: "XML",
  html: "HTML",
  css: "CSS",
  scss: "SCSS",
  diff: "Diff",
  dockerfile: "Dockerfile",
  hcl: "HCL",
  terraform: "Terraform",
  graphql: "GraphQL",
  http: "HTTP",
  proto: "Protobuf",
  text: "Text",
  txt: "Text",
  plaintext: "Text",
  md: "Markdown",
  markdown: "Markdown",
};

const toText = (node) =>
  node.type === "text" || node.type === "inlineCode"
    ? node.value
    : (node.children || []).map(toText).join("");

export const emojiSpan = (value) => ({
  type: "emphasis",
  data: {
    hName: "span",
    hProperties: { className: ["sec-emoji"], ariaHidden: "true" },
  },
  children: [{ type: "text", value }],
});

const isPlainQuote = (node) => node && node.type === "blockquote" && !node.data?.hName;

function wrapHeadingEmoji(node) {
  const first = node.children?.[0];
  if (!first) return;
  if (first.type === "emphasis" && first.data?.hProperties?.className?.includes("sec-emoji"))
    return;
  if (first.type !== "text") return;
  const m = first.value.match(LEADING_EMOJI);
  if (!m) return;
  const rest = first.value.slice(m[0].length);
  const after = rest + node.children.slice(1).map(toText).join("");
  if (/\p{Extended_Pictographic}/u.test(after)) return;
  node.children.splice(0, 1, emojiSpan(m[1]), { type: "text", value: first.value.slice(m[1].length) });
}

const TRAILING_LATIN = /\s*[(（]\s*([^()（）]*[A-Za-z][^()（）]*?)\s*[)）]\s*$/;
const HAN = /\p{Script=Han}/u;

const hidden = (value) => ({
  type: "emphasis",
  data: { hName: "span", hProperties: { className: ["visually-hidden"] } },
  children: [{ type: "text", value }],
});

function splitHeadingLatin(node) {
  const last = node.children?.[node.children.length - 1];
  if (!last || last.type !== "text") return;
  const m = last.value.match(TRAILING_LATIN);
  if (!m || HAN.test(m[1])) return;
  const head = last.value.slice(0, m.index);
  const before = node.children.slice(0, -1).map(toText).join("") + head;
  if (!HAN.test(before)) return;
  node.children.splice(node.children.length - 1, 1, { type: "text", value: head }, {
    type: "emphasis",
    data: { hName: "span", hProperties: { className: ["h-latin"], lang: "en" } },
    children: [hidden(" ("), { type: "text", value: m[1] }, hidden(")")],
  });
}

function joinCjkLines(node, index, parent) {
  if (!node.value.includes("\n")) return;
  const prev = index > 0 ? toText(parent.children[index - 1]) : "";
  const next = index < parent.children.length - 1 ? toText(parent.children[index + 1]) : "";
  node.value = node.value.replace(/\n/g, (_, offset, s) => {
    const before = offset > 0 ? s[offset - 1] : prev.slice(-1);
    const after = offset < s.length - 1 ? s[offset + 1] : next.charAt(0);
    if (!before || !after) return "\n";
    if (CJK_PUNCT.test(before)) return "";
    return CJK_BEFORE.test(before) && CJK_BEFORE.test(after) ? "" : "\n";
  });
}

const LONG_LEAD = 90;
const WIDE_CODE = 72;

const charCols = (ch) => (/[\u1100-\uFFEF]/u.test(ch) ? 2 : 1);
const lineCols = (line) => [...line.replace(/\t/g, "  ")].reduce((n, ch) => n + charCols(ch), 0);
const codeCols = (value = "") => Math.max(0, ...value.split("\n").map(lineCols));
const INTRO_MAX = 120;

const textLength = (node) => [...toText(node).replace(/\s+/g, "")].length;

const addClass = (node, ...names) => {
  const data = node.data || (node.data = {});
  const props = (data.hProperties = { ...(data.hProperties || {}) });
  const prev = props.className ? [].concat(props.className) : [];
  props.className = [...prev, ...names];
};

const isSectionHead = (node) =>
  (node?.type === "heading" && node.depth === 2) ||
  (node?.type === "leafDirective" &&
    [].concat(node.data?.hProperties?.className || []).includes("section-head"));

function markIntros(tree) {
  const top = tree.children || [];
  const first = top[0];
  if (first?.type === "paragraph") {
    addClass(first, "opening", ...(textLength(first) > LONG_LEAD ? ["is-long"] : []));
  }
  for (let i = 1; i < top.length; i++) {
    const node = top[i];
    if (node.type !== "paragraph" || !isSectionHead(top[i - 1])) continue;
    if (textLength(node) <= INTRO_MAX) addClass(node, "intro");
  }
}

export default function remarkReading() {
  return (tree, file) => {
    const lead = tree.children?.[0];
    if (isPlainQuote(lead)) {
      const data = lead.data || (lead.data = {});
      data.hProperties = {
        ...(data.hProperties || {}),
        className: ["standfirst", ...(textLength(lead) > LONG_LEAD ? ["is-long"] : [])],
      };
      const astro = file?.data?.astro;
      if (astro) {
        astro.frontmatter = astro.frontmatter || {};
        astro.frontmatter.standfirst = toText(lead).replace(/\s+/g, " ").trim();
      }
    }
    markIntros(tree);

    visit(tree, (node, index, parent) => {
      if (node.type === "heading" && (node.depth === 2 || node.depth === 3)) {
        wrapHeadingEmoji(node);
        splitHeadingLatin(node);
        return;
      }
      if (node.type === "textDirective" && !node.data?.hName && parent && index != null) {
        const label = (node.children || []).length ? `[${toText(node)}]` : "";
        parent.children[index] = { type: "text", value: `:${node.name}${label}` };
        return [SKIP, index];
      }
      if (node.type === "text" && parent) {
        joinCjkLines(node, index, parent);
        return;
      }
      if (node.type === "code" && parent && index != null) {
        const lang = (node.lang || "").toLowerCase();
        const name = LANGS[lang] ?? (lang ? lang.toUpperCase() : "");
        const caption = {
          type: "paragraph",
          data: { hName: "figcaption", hProperties: { className: ["code-head"] } },
          children: name
            ? [
                {
                  type: "emphasis",
                  data: { hName: "span", hProperties: { className: ["code-lang"] } },
                  children: [{ type: "text", value: name }],
                },
              ]
            : [],
        };
        parent.children[index] = {
          type: "codeFigure",
          data: {
            hName: "figure",
            hProperties: {
              className: ["code-block", ...(codeCols(node.value) > WIDE_CODE ? ["is-wide"] : [])],
              dataLang: lang || "text",
            },
          },
          children: [caption, node],
        };
        return SKIP;
      }
      if (node.type === "table" && parent && index != null) {
        parent.children[index] = {
          type: "tableScroll",
          data: {
            hName: "div",
            hProperties: { className: ["table-scroll"], tabIndex: 0 },
          },
          children: [node],
        };
        return SKIP;
      }
    });
  };
}
