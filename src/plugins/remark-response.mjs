import { visit } from "unist-util-visit";

/**
 * 把 `:::response` 容器（remark-directive 解析）轉成
 * <section class="my-response"> … </section>，並在最前面插入
 * 「✍️ 我的回應」標頭。內部 Markdown 照常被 remark 解析。
 *
 * 用途：每個主題頁的「兩區塊」中，屬於「我的回應／心得／Q&A」的那一塊。
 * 與書本位正文分開呈現。空內容時顯示低調 placeholder。
 */
export default function remarkResponse() {
  return (tree) => {
    visit(tree, (node) => {
      if (node.type !== "containerDirective" || node.name !== "response") return;

      const data = node.data || (node.data = {});
      data.hName = "section";
      data.hProperties = { className: ["my-response"] };

      // 空內容 → 低調 placeholder
      const hasContent = (node.children || []).some(
        (c) => !(c.type === "paragraph" && (!c.children || c.children.length === 0))
      );
      if (!hasContent) {
        node.children = [
          {
            type: "paragraph",
            data: { hProperties: { className: ["response-empty"] } },
            children: [
              {
                type: "text",
                value: "No notes yet — jot your takeaways or Q&A here.",
              },
            ],
          },
        ];
      }

      // 標頭
      node.children.unshift({
        type: "paragraph",
        data: { hName: "header", hProperties: { className: ["my-response-head"] } },
        children: [{ type: "text", value: "✍️ My Notes" }],
      });
    });
  };
}
