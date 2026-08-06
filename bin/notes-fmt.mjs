#!/usr/bin/env node
// 星系共用格式化入口：把 prettier 的 config / ignore / 目標集中在 notes-core，
// 各站 package.json 只需：
//   "format":       "notes-fmt write"
//   "format:check": "notes-fmt check"
// 於是各站不必再放 .prettierignore、也不必重複 prettier 參數。
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { existsSync } from "node:fs";
import { spawnSync } from "node:child_process";

const here = dirname(fileURLToPath(import.meta.url));
const pkgRoot = join(here, "..");
const config = join(pkgRoot, "prettier.config.json");
const ignore = join(pkgRoot, "prettierignore");

const sub = process.argv[2];
const mode = sub === "check" ? "--check" : sub === "write" ? "--write" : null;
if (!mode) {
  console.error("usage: notes-fmt <write|check> [extra prettier args/globs]");
  process.exit(2);
}

const extra = process.argv.slice(3);
const targets = extra.length ? extra : ["."];

// prettier 執行檔：優先用消費端 repo 的 node_modules/.bin，開發時退回 PATH。
const localBin = join(
  pkgRoot,
  "..",
  "..",
  ".bin",
  process.platform === "win32" ? "prettier.cmd" : "prettier",
);
const bin = existsSync(localBin) ? localBin : "prettier";

const r = spawnSync(
  bin,
  [mode, "--config", config, "--ignore-path", ignore, ...targets],
  { stdio: "inherit" },
);
process.exit(r.status ?? 1);
