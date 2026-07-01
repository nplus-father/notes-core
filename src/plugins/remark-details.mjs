import { visit } from "unist-util-visit";

/**
 * 把 remark-directive 解析出的 `:::details{title="..."}` 容器
 * 轉成原生 <details><summary>title</summary>…</details>。
 *
 * 來源（Hugo）：{{% details "標題" %}} … {{% /details %}}
 * 遷移後：     :::details{title="標題"}  … :::
 *
 * 內部 Markdown（含 ```kotlin code fence）會照常被 remark 解析，
 * 這正是不用 MDX 也能保留摺疊解法的關鍵。
 */
export default function remarkDetails() {
  return (tree) => {
    visit(tree, (node) => {
      if (node.type !== "containerDirective" || node.name !== "details") return;

      const attrs = node.attributes || {};
      const title = attrs.title || "Details";
      const open = attrs.open !== undefined;

      const data = node.data || (node.data = {});
      data.hName = "details";
      data.hProperties = { className: ["lc-details"], ...(open ? { open: true } : {}) };

      // 在最前面插入 <summary>標題</summary>
      node.children.unshift({
        type: "paragraph",
        data: { hName: "summary" },
        children: [{ type: "text", value: title }],
      });
    });
  };
}
