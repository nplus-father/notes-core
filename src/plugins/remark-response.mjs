import { visit } from "unist-util-visit";

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

      node.children.unshift({
        type: "paragraph",
        data: { hName: "header", hProperties: { className: ["my-response-head"], lang: "en" } },
        children: [{ type: "text", value: "My Notes" }],
      });
    });
  };
}
