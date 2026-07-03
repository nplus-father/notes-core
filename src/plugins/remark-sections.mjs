import { visit } from "unist-util-visit";

/**
 * 把標準區塊 leaf directive 轉成「模板控制的英文小標」，正文照常由 markdown 提供。
 * 全星系各領域反覆出現的區塊（核心概念 / 心智模型 / 權衡 / 案例 / 總整理…）不再各自
 * 手寫中文 heading，改由此外掛統一產生英文標題——改字、改 emoji 一處生效。
 *
 * 語法（remark-directive 的 leaf directive，`::` 開頭、獨立一行）：
 *   ::core                 → 🧠 Core Ideas
 *   ::case[補述文字]        → ⚖️ Case Study（補述搬到標題下方，進入內容區）
 *   ::takeaways            → 🔑 Takeaways
 * 之後的 markdown（清單 / :::details / 段落）照常是「兄弟節點」，不需巢狀包裹。
 *
 * 詞彙表 = 全星系區塊的聯集；英文標籤取自各站原本「中文 (English)」括號內的英文。
 */
const SECTIONS = {
  // 通用（軟技能站：習慣 / 成長 / 投資 / 思考…）
  core: { emoji: "🧠", label: "Core Ideas" }, // 核心概念
  case: { emoji: "⚖️", label: "Case Study" }, // 案例 / 案例／對照 / 對照 / 前後對照
  takeaways: { emoji: "🔑", label: "Takeaways" }, // 總整理 (Takeaways)
  // 技術站（data-systems / cloud-infra / design-patterns…）
  intuition: { emoji: "🧠", label: "Intuition" }, // 心智模型 / 先想一下 (Intuition)
  tradeoffs: { emoji: "⚖️", label: "Tradeoffs" }, // 關鍵權衡 (Tradeoffs)
  whentouse: { emoji: "🧠", label: "When to Use" }, // 適用情境 (When to use)
  structure: { emoji: "⚖️", label: "Structure & Variants" }, // 結構與變體
  antipatterns: { emoji: "⚠️", label: "Misuse & Anti-patterns" }, // 誤用與反模式
  approaches: { emoji: "🪜", label: "Approaches" }, // Approaches（leetcode）
  // clean-code
  whyproblem: { emoji: "🧠", label: "Why It's a Problem" }, // 為什麼是問題
  whymatters: { emoji: "🧠", label: "Why It Matters" }, // 為什麼重要
  refactor: { emoji: "⚖️", label: "Refactoring" }, // 重構手法 / 前後對照
  // behaviour-interview
  discussion: { emoji: "🗣️", label: "Discussion Log" }, // 討論區 (Discussion Log)
  signals: { emoji: "🧠", label: "Signals" }, // 面試官想看的訊號 (Signals)
  pitfalls: { emoji: "⚠️", label: "Pitfalls" }, // 陷阱 (Pitfalls)
  questions: { emoji: "❓", label: "Common Questions" }, // 常見問法 (Questions)
  star: { emoji: "⭐", label: "STAR Example" }, // STAR 範例骨架 (Example)
  scenario: { emoji: "🎯", label: "Scenario" }, // 情境與壞味道 / 情境與需求 (Scenario)
  // system-design
  requirements: { emoji: "📋", label: "Requirements" }, // 需求與約束 (Requirements)
  reference: { emoji: "⚖️", label: "Reference Design" }, // 參考架構 / 對照解析 (Reference)
};

export default function remarkSections() {
  return (tree) => {
    visit(tree, (node) => {
      if (node.type !== "leafDirective") return;
      const spec = SECTIONS[node.name];
      if (!spec) return;

      // 補述：directive 的 `[ ... ]` 內容，搬到標題下方當副標（留在內容區、非標題）。
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
