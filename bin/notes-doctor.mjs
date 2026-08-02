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
import { basename, dirname, join } from "node:path";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
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

/**
 * 星系入列健檢（結構性，`fix` 修不了——要人去改 sites.ts）：
 *   1. 本站有沒有登記進 notes-core 的 registry（沒登記 → 跨站連結／portal 分區都看不到它）
 *   2. 知識軸對不對：`src/data/profile.ts` 存在 ⟺ axis === "person"
 *      （主題站可以沒有 schools.ts——如 behaviour-interview-note——故只用 profile.ts 當不變式）
 *
 * 以正則讀 sites.ts 原始碼：該檔按慣例「一站一行」，故 slug 與 axis 必同行。
 * 若哪天改成多行排版，這裡要跟著改（.mjs 無法 import .ts，不想為此多生一份 JSON
 * 而讓 registry 有兩個正本）。
 */
function registryCheck() {
  const slug = basename(process.cwd());
  // 只查真正的站台：core 本身與 note-template 不入列，不該被判為漏登記。
  if (!slug.endsWith("-note") || slug === "note-template") return null;
  let src;
  try {
    src = readFileSync(join(here, "..", "src", "lib", "sites.ts"), "utf8");
  } catch {
    return null; // 讀不到 registry 就不擋（例如被裁切安裝）
  }
  const line = src
    .split("\n")
    .find(
      (l) => l.includes(`slug: "${slug}"`) && l.trimStart().startsWith("{"),
    );
  if (!line) return { slug, problem: "unlisted" };
  // 站上釘的 core 早於 v0.12.0（registry 還沒有 axis 欄位）→ 只做入列檢查，
  // 不然每個還沒升版的站都會被誤判成軸錯。
  if (!src.includes('axis: "')) return null;
  const axis = /axis: "(topic|person)"/.exec(line)?.[1] ?? null;
  const hasProfile = existsSync(
    join(process.cwd(), "src", "data", "profile.ts"),
  );
  if (hasProfile && axis !== "person")
    return { slug, problem: "should-be-person", axis };
  if (!hasProfile && axis === "person")
    return { slug, problem: "should-be-topic", axis };
  return null;
}

const registry = registryCheck();
if (registry) {
  const msg = {
    unlisted: `未登記進 notes-core registry（src/lib/sites.ts）——跨站連結與 nplus.wiki 分區都看不到本站`,
    "should-be-person": `有 src/data/profile.ts 卻登記成 axis: "${registry.axis}"——人物站請改成 "person" 並補 subject`,
    "should-be-topic": `登記成 axis: "person" 卻沒有 src/data/profile.ts——主題站請改成 "topic"`,
  }[registry.problem];
  console.log(`  registry  ${registry.slug}: ${msg}`);
}

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

if (!drift.length && !core?.stale && !registry) {
  console.log(
    "notes-doctor: 依賴版本與 notes-core versions.json 一致，星系入列正確。",
  );
  process.exit(0);
}

if (mode === "fix" && !registry) {
  console.log(
    "notes-doctor: 已改寫 package.json——記得跑 npm install 並重新 build 驗證。",
  );
  process.exit(0);
}

// registry 問題 fix 修不了（要人去改 sites.ts），故即使 fix 模式也回非零。
const drifts = drift.length + (core?.stale ? 1 : 0);
if (drifts) {
  console.log(`notes-doctor: ${drifts} 項漂移，跑 \`notes-doctor fix\` 修正。`);
}
if (registry) {
  console.log(
    "notes-doctor: 星系入列有問題——請改 notes-core 的 src/lib/sites.ts。",
  );
}
process.exit(1);
