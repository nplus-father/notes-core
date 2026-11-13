import { visit } from "unist-util-visit";

const PAIR = /^(前|後)\s*[—–-]+\s*/;

export default function remarkDetails() {
  return (tree) => {
    visit(tree, (node) => {
      if (node.type !== "containerDirective" || node.name !== "details") return;

      const attrs = node.attributes || {};
      const title = attrs.title || "Details";
      const open = attrs.open !== undefined;
      const pair = title.match(PAIR);
      const side = pair ? (pair[1] === "前" ? "before" : "after") : null;
      const text = pair ? title.slice(pair[0].length) : title;

      const className = ["lc-details"];
      if (side) className.push(`is-${side}`);

      const data = node.data || (node.data = {});
      data.hName = "details";
      data.hProperties = { className, ...(open ? { open: true } : {}) };

      const summaryKids = [];
      if (side) {
        summaryKids.push({
          type: "emphasis",
          data: {
            hName: "span",
            hProperties: { className: ["details-side"], lang: "en" },
          },
          children: [{ type: "text", value: side === "before" ? "Before" : "After" }],
        });
      }
      summaryKids.push({
        type: "emphasis",
        data: { hName: "span", hProperties: { className: ["details-title"] } },
        children: [{ type: "text", value: text }],
      });
      summaryKids.push({
        type: "emphasis",
        data: {
          hName: "span",
          hProperties: { className: ["details-mark"], ariaHidden: "true" },
        },
        children: [],
      });

      node.children.unshift({
        type: "paragraph",
        data: { hName: "summary" },
        children: summaryKids,
      });
    });
  };
}
