import { visit, SKIP } from "unist-util-visit";
import remarkReading, { emojiSpan } from "./remark-reading.mjs";

const SECTIONS = {
  core: { emoji: "🧠", label: "Core Ideas" },
  case: { emoji: "⚖️", label: "Case Study" },
  takeaways: { emoji: "🔑", label: "Takeaways" },
  intuition: { emoji: "🧠", label: "Intuition" },
  tradeoffs: { emoji: "⚖️", label: "Tradeoffs" },
  whentouse: { emoji: "🧠", label: "When to Use" },
  structure: { emoji: "⚖️", label: "Structure & Variants" },
  antipatterns: { emoji: "⚠️", label: "Misuse & Anti-patterns" },
  approaches: { emoji: "🪜", label: "Approaches" },
  whyproblem: { emoji: "🧠", label: "Why It's a Problem" },
  whymatters: { emoji: "🧠", label: "Why It Matters" },
  refactor: { emoji: "⚖️", label: "Refactoring" },
  discussion: { emoji: "🗣️", label: "Discussion Log" },
  signals: { emoji: "🧠", label: "Signals" },
  pitfalls: { emoji: "⚠️", label: "Pitfalls" },
  questions: { emoji: "❓", label: "Common Questions" },
  star: { emoji: "⭐", label: "STAR Example" },
  scenario: { emoji: "🎯", label: "Scenario" },
  requirements: { emoji: "📋", label: "Requirements" },
  reference: { emoji: "⚖️", label: "Reference Design" },
};

export default function remarkSections() {
  const reading = remarkReading();
  return (tree, file) => {
    visit(tree, (node) => {
      if (node.type !== "leafDirective") return;
      const spec = SECTIONS[node.name];
      if (!spec) return;

      const sub = (node.children || []).length ? node.children : null;

      const heading = {
        type: "heading",
        depth: 2,
        data: { hProperties: { lang: "en" } },
        children: [emojiSpan(spec.emoji), { type: "text", value: ` ${spec.label}` }],
      };
      const kids = [heading];
      if (sub) {
        kids.push({
          type: "paragraph",
          data: { hProperties: { className: ["section-sub"] } },
          children: sub,
        });
      }

      const data = node.data || (node.data = {});
      data.hName = "header";
      data.hProperties = { className: ["section-head", `section-${node.name}`] };
      node.children = kids;
      return SKIP;
    });
    reading(tree, file);
  };
}
