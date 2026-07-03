import { visit } from "unist-util-visit";

/**
 * 把標準區塊 leaf directive 轉成「模板控制的英文小標」，正文照常由 markdown 提供。
 * 各概念頁反覆出現的三個 section（核心概念 / 案例 / 總整理）不再各自手寫中文 heading，
 * 改由此外掛統一產生英文標題——改字、改 emoji 一處生效。
 *
 * 語法（remark-directive 的 leaf directive，`::` 開頭、獨立一行）：
 *   ::core                 → 🧠 Core Ideas
 *   ::case[補述文字]        → ⚖️ Case Study（補述搬到標題下方，進入內容區）
 *   ::takeaways            → 🔑 Takeaways
 * 之後的 markdown（清單 / :::details / 段落）照常是「兄弟節點」，不需巢狀包裹。
 */
const SECTIONS = {
  core: { emoji: "🧠", label: "Core Ideas" },
  case: { emoji: "⚖️", label: "Case Study" },
  takeaways: { emoji: "🔑", label: "Takeaways" },
};

export default function remarkSections() {
  return (tree) => {
    visit(tree, (node) => {
      if (node.type !== "leafDirective") return;
      const spec = SECTIONS[node.name];
      if (!spec) return;

      // 補述：case 的 `[ ... ]` 內容，搬到標題下方當副標（留在內容區、非標題）。
      const sub = (node.children || []).length ? node.children : null;

      const heading = {
        type: "heading",
        depth: 2,
        children: [{ type: "text", value: `${spec.emoji} ${spec.label}` }],
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
    });
  };
}
