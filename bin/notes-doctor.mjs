#!/usr/bin/env node
// 星系依賴健檢：把「哪些套件該釘哪個版本」集中在 notes-core 的 versions.json，
// 各站用它檢查自己的 package.json 有沒有漂掉。
//   "deps:check": "notes-doctor check"   ← 可接進 CI，擋住漂移
//   "deps:fix":   "notes-doctor fix"     ← 就地改齊，改完自己跑 npm install
//
// 另外檢查 @nplus-father/notes-core 這一釘本身是不是最新 tag（需要 gh CLI；
// 拿不到就跳過，不讓離線環境變成紅燈）。versions.json 沒列到的套件一律不碰
// ——站別特有的依賴（例如 leetcode-note 的 unist-util-visit）不歸這裡管。
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { readFileSync, writeFileSync } from "node:fs";
import { spawnSync } from "node:child_process";

const here = dirname(fileURLToPath(import.meta.url));
const canonical = JSON.parse(
  readFileSync(join(here, "..", "versions.json"), "utf8"),
);
const selfName = "@nplus-father/notes-core";

const mode = process.argv[2];
if (mode !== "check" && mode !== "fix") {
  console.error("usage: notes-doctor <check|fix>");
  process.exit(2);
}

const pkgPath = join(process.cwd(), "package.json");
let pkg;
try {
  pkg = JSON.parse(readFileSync(pkgPath, "utf8"));
} catch {
  console.error(
    `notes-doctor: 找不到或讀不了 ${pkgPath}——請在 -note 站根目錄執行。`,
  );
  process.exit(2);
}

/** 站上這個套件實際釘在哪個區塊（可能跟正本歸的區塊不同，不視為錯）。 */
function findBlock(name) {
  for (const b of ["dependencies", "devDependencies"]) {
    if (pkg[b] && name in pkg[b]) return b;
  }
  return null;
}

const drift = [];
for (const [block, entries] of Object.entries(canonical)) {
  if (block.startsWith("$")) continue;
  for (const [name, want] of Object.entries(entries)) {
    const at = findBlock(name);
    if (!at) continue; // 站上沒裝這個套件——不是漂移，是它不需要
    const got = pkg[at][name];
    if (got !== want) drift.push({ name, block: at, got, want });
  }
}

/** notes-core 這一釘是否落後最新 tag。拿不到 tag（離線／沒 gh）就回 null。 */
function coreCurrency() {
  const at = findBlock(selfName);
  if (!at) return null;
  const got = pkg[at][selfName];
  const pinned = /#(v[\d.]+)/.exec(got)?.[1];
  if (!pinned) return null;
  const r = spawnSync(
    "gh",
    ["api", "repos/nplus-father/notes-core/tags", "--jq", ".[0].name"],
    { encoding: "utf8" },
  );
  const latest = r.status === 0 ? r.stdout.trim() : null;
  if (!latest) return null;
  return { block: at, got, pinned, latest, stale: pinned !== latest };
}

const core = coreCurrency();

if (mode === "fix") {
  for (const d of drift) pkg[d.block][d.name] = d.want;
  if (core?.stale)
    pkg[core.block][selfName] = core.got.replace(/#v[\d.]+/, `#${core.latest}`);
  if (drift.length || core?.stale) {
    writeFileSync(pkgPath, JSON.stringify(pkg, null, 2) + "\n");
  }
}

const verb = mode === "fix" ? "已修正" : "漂移";
for (const d of drift) {
  console.log(`  ${verb}  ${d.name}: ${d.got} → ${d.want}`);
}
if (core?.stale) {
  console.log(`  ${verb}  ${selfName}: ${core.pinned} → ${core.latest}`);
}

if (!drift.length && !core?.stale) {
  console.log("notes-doctor: 依賴版本與 notes-core versions.json 一致。");
  process.exit(0);
}

if (mode === "fix") {
  console.log(
    "notes-doctor: 已改寫 package.json——記得跑 npm install 並重新 build 驗證。",
  );
  process.exit(0);
}

console.log(
  `notes-doctor: ${drift.length + (core?.stale ? 1 : 0)} 項漂移，跑 \`notes-doctor fix\` 修正。`,
);
process.exit(1);
