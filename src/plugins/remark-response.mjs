import { visit } from "unist-util-visit";

/**
 * 把 `:::response` 容器（remark-directive 解析）轉成
 * <section class="my-response"> … </section>，並在最前面插入
 * 「✍️ 我的回應」標頭。內部 Markdown 照常被 remark 解析。
 *
 * 用途：每個主題頁的「兩區塊」中，屬於「我的回應／心得／Q&A」的那一塊。
 * 與書本位正文分開呈現。
 *
 * 空內容**不渲染**（v0.44.0）：來源檔仍保留 `:::response` 空區塊當兩層模型的標記，但頁面上
 * 不出現任何東西。與 ✅ Check、📖 Guide 的 tab 同一原則：有資料才出現。v0.43 以前這裡會畫一個
 * 「No notes yet」的空框，2026-11-06 盤點時 2233 個概念頁有 2197 頁都是那個空框。
 */
export default function remarkResponse() {
  return (tree) => {
    visit(tree, (node, index, parent) => {
      if (node.type !== "containerDirective" || node.name !== "response") return;

      const hasContent = (node.children || []).some(
        (c) => !(c.type === "paragraph" && (!c.children || c.children.length === 0))
      );
      if (!hasContent) {
        parent.children.splice(index, 1);
        return index;
      }

      const data = node.data || (node.data = {});
      data.hName = "section";
      data.hProperties = { className: ["my-response"] };

      // 標頭
      node.children.unshift({
        type: "paragraph",
        data: { hName: "header", hProperties: { className: ["my-response-head"] } },
        children: [{ type: "text", value: "✍️ My Notes" }],
      });
    });
  };
}
