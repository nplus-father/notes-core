const FULL = /[，。、：；！？「」『』（）《》〈〉【】〔〕]/;

export function tightenPunct(html: string): string {
  let prevPunct = false;
  return html
    .split(/(<[^>]+>)/)
    .map((part) => {
      if (part.startsWith("<")) return part;
      let out = "";
      for (const ch of part) {
        const punct = FULL.test(ch);
        if (punct && prevPunct) out += `<span class="pt">${ch}</span>`;
        else out += ch;
        prevPunct = punct;
      }
      return out;
    })
    .join("");
}
