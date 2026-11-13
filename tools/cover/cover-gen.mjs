import { writeFileSync } from "node:fs";
import { sites } from "../../src/lib/sites.ts";
import { siteCovers } from "../../src/lib/site-covers.ts";
import { motifBodies, motifLegends, motifSvg } from "../../src/lib/motifs.ts";
import { coverPlateFor } from "../../src/lib/cover-plate.ts";

const siteBySlug = new Map(sites.map((s) => [s.slug, s]));
const topicSlugs = sites.filter((s) => s.axis === "topic").map((s) => s.slug);

const problems = [];
for (const slug of topicSlugs) {
  if (!siteCovers[slug]) problems.push(`${slug}: 是主題站但 site-covers.ts 沒有它`);
}
for (const slug of Object.keys(siteCovers)) {
  const s = siteBySlug.get(slug);
  if (!s) problems.push(`${slug}: site-covers.ts 有它但 sites.ts 沒有`);
  else if (s.axis !== "topic") problems.push(`${slug}: 是人物站，不該有封面參數（人物站用肖像照）`);
}
const seen = new Map();
for (const [slug, c] of Object.entries(siteCovers)) {
  if (!motifBodies[c.motif]) problems.push(`${slug}: 符號 '${c.motif}' 不在 src/lib/motifs.ts 裡`);
  else if (!motifLegends[c.motif])
    problems.push(`${slug}: 符號 '${c.motif}' 沒有 motifLegends 圖說`);
  if (seen.has(c.motif))
    problems.push(`符號撞圖：'${c.motif}' 同時被 ${seen.get(c.motif)} 與 ${slug} 使用`);
  seen.set(c.motif, slug);
}
if (problems.length) {
  console.error("registry 對帳失敗：\n  " + problems.join("\n  "));
  process.exit(1);
}

const slug = process.argv[2];
const out = process.argv[3];
const site = siteBySlug.get(slug);
if (!site) {
  console.error("unknown slug", slug);
  process.exit(1);
}
if (site.axis !== "topic") {
  console.error(`${slug} 是人物站，封面請用傳主肖像照，不由生成器產出`);
  process.exit(1);
}
const plate = coverPlateFor(slug);

const n = [...plate.title].length;
const titleSize = n <= 3 ? 104 : n <= 4 ? 96 : n <= 5 ? 84 : n <= 6 ? 72 : 62;

const PAPER = "#fbf9f4";
const INK = "#1b1b1e";
const RULE = "#bdb5a5";
const MUTED = "#6c665b";
const SEAL = "#c23b22";
const SERIF_TC = "'Noto Serif TC','Noto Serif CJK TC','Source Han Serif TC',serif";
const LATIN = "Newsreader,Georgia,serif";
const SANS = "Inter,'Noto Sans TC','Noto Sans CJK TC',sans-serif";
const MONO = "'JetBrains Mono',ui-monospace,monospace";

const html = `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@600&family=JetBrains+Mono:wght@600&family=Newsreader:ital,opsz,wght@1,6..72,400&family=Noto+Serif+TC:wght@700&display=block">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:900px;height:1200px;overflow:hidden}
body{background:${PAPER};color:${INK};position:relative}
.mark{position:absolute;left:63px;right:63px;top:63px;height:700px;border:2px solid ${RULE};display:grid;place-items:center}
.mark::before{content:"";position:absolute;inset:16px;border:2px solid ${RULE}}
.mark svg{width:660px;height:auto;overflow:visible}
.legend{position:absolute;left:0;right:0;top:790px;text-align:center;font:italic 400 34px/1.2 ${LATIN};letter-spacing:.01em}
.title{position:absolute;left:63px;right:63px;top:880px;text-align:center;font:700 ${titleSize}px/1.15 ${SERIF_TC};letter-spacing:.06em;margin-right:-.06em}
.foot{position:absolute;left:63px;right:63px;bottom:68px;display:flex;justify-content:center;align-items:center;gap:22px;
  font:600 22px/1 ${SANS};letter-spacing:.3em;text-transform:uppercase;color:${MUTED}}
.foot .n{font-family:${MONO};letter-spacing:.06em;color:${INK}}
.foot i{width:40px;height:2px;background:${RULE}}
.seal{position:absolute;right:63px;bottom:63px;width:30px;height:30px;background:${SEAL}}
</style></head><body>
  <div class="mark">${motifSvg(plate.motif)}</div>
  <p class="legend">${plate.legend}</p>
  <h1 class="title">${plate.title}</h1>
  <div class="foot"><span>${plate.en}</span><i></i><span class="n">N°${plate.serial}</span></div>
  <span class="seal"></span>
</body></html>`;

writeFileSync(out, html);
console.log(
  "ok",
  slug,
  `"${plate.title}" / "${plate.en}"`,
  "N°" + plate.serial,
  plate.motif,
  "titleSize",
  titleSize
);
