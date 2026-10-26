#!/usr/bin/env python3
import argparse
import glob
import os
import re
import subprocess
import sys

GALAXY = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

AIISMS = [
    r"不是[^。，；\n]{1,25}，而是",
    "正是",
    "真正的",
    "不只是",
    "恰恰",
    "本質上",
    "換句話說",
    "換言之",
    "也就是說",
    "這就是為什麼",
    "值得注意",
    "某種程度",
]

FM = re.compile(r"\A---\n.*?\n---\n", re.S)
RESPONSE = re.compile(r"^:::response\n.*?^:::\s*$", re.S | re.M)
DIRECTIVE = re.compile(r"^(::+)([a-z]+)", re.M)
HEADING = re.compile(r"^(#{2,6})\s+(.*)$", re.M)
LINK = re.compile(r"\]\(([^)\s]+)\)")
YEAR = re.compile(r"(?<!\d)(1[0-9]{3}|20[0-9]{2})(?!\d)")
QUOTE = re.compile(r"「([^」]{8,})」")
HEADNUM = re.compile(r"^(主線|第)?[一二三四五六七八九十0-9]+[、：:.．]\s*|^(主線|場景|階段)[一二三四五六七八九十]+[：:]\s*")


def prose_files(site):
    pats = ["src/content/**/*.md", "src/data/overview.ts", "src/data/profile.ts", "src/site.config.ts"]
    out = []
    for p in pats:
        out += glob.glob(os.path.join(site, p), recursive=True)
    return sorted(out)


def body_of(text):
    return FM.sub("", text, count=1)


def metrics(text):
    body = body_of(text)
    n = len(body) or 1
    dash = body.count("——")
    ai = sum(len(re.findall(p, body)) for p in AIISMS)
    long_lines = sum(
        1 for l in body.splitlines() if len(l) > 150 and not l.startswith(("-", "|", "#", ":"))
    )
    return n, dash, ai, long_lines


def site_metrics(site):
    n = dash = ai = ll = 0
    files = prose_files(site)
    for f in files:
        with open(f, encoding="utf-8") as fh:
            a, b, c, d = metrics(fh.read())
        n, dash, ai, ll = n + a, dash + b, ai + c, ll + d
    k = (n or 1) / 1000
    return len(files), n, dash / k, ll / k, ai / k


def rank(sites):
    rows = [(os.path.basename(s), *site_metrics(s)) for s in sites]
    rows.sort(key=lambda r: -(r[3] + 3 * r[5]))
    print(f"{'repo':28}{'files':>6}{'chars':>9}{'dash/k':>8}{'long/k':>8}{'aiism/k':>9}")
    for r in rows:
        print(f"{r[0]:28}{r[1]:>6}{r[2]:>9}{r[3]:>8.2f}{r[4]:>8.2f}{r[5]:>9.2f}")


def git_show(site, base, rel):
    r = subprocess.run(
        ["git", "-C", site, "show", f"{base}:{rel}"], capture_output=True, text=True
    )
    return r.stdout if r.returncode == 0 else None


def changed(site, base):
    r = subprocess.run(
        ["git", "-C", site, "-c", "core.quotePath=false", "diff", "--name-only", base, "--", "src"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [l for l in r.stdout.splitlines() if l]


def fm_key(m):
    if not m:
        return None
    return re.sub(r"^intro:.*$", "", m.group(0), flags=re.M)


def norm_heading(h):
    return HEADNUM.sub("", h.strip()).replace("——", "：")


def line_of(text, needle):
    i = text.find(needle)
    return text.count("\n", 0, i) + 1 if i >= 0 else 0


def gate_file(rel, old, new, lo, hi):
    fails, warns = [], []
    if old is None:
        return fails, [f"{rel}: new file"]
    if rel.endswith(".md"):
        fo, fn = FM.match(old), FM.match(new)
        if fm_key(fo) != fm_key(fn):
            fails.append(f"{rel}:1 frontmatter changed")
        if RESPONSE.findall(old) != RESPONSE.findall(new):
            fails.append(f"{rel}: :::response block changed")
        do = [m.group(2) for m in DIRECTIVE.finditer(body_of(old))]
        dn = [m.group(2) for m in DIRECTIVE.finditer(body_of(new))]
        if do != dn:
            fails.append(f"{rel}: directives {do} -> {dn}")
        ho = sorted(norm_heading(m.group(2)) for m in HEADING.finditer(body_of(old)))
        hn = sorted(norm_heading(m.group(2)) for m in HEADING.finditer(body_of(new)))
        if ho != hn:
            for h in sorted(set(ho) - set(hn)):
                warns.append(f"{rel}: heading gone or renamed: {h}")
    bo, bn = body_of(old), body_of(new)
    lo_set, ln_set = set(LINK.findall(bo)), set(LINK.findall(bn))
    for l in sorted(lo_set - ln_set):
        fails.append(f"{rel}: link dropped {l}")
    for l in sorted(ln_set - lo_set):
        fails.append(f"{rel}:{line_of(new, l)} link added {l}")
    yo, yn = set(YEAR.findall(bo)), set(YEAR.findall(bn))
    for y in sorted(yo - yn):
        fails.append(f"{rel}: year dropped {y}")
    for y in sorted(yn - yo):
        fails.append(f"{rel}:{line_of(new, y)} year added {y}")
    qo, qn = set(QUOTE.findall(bo)), set(QUOTE.findall(bn))
    for q in sorted(qo - qn):
        warns.append(f"{rel}: quote gone or edited 「{q[:30]}」")
    a, b = len(re.sub(r"\s", "", bo)), len(re.sub(r"\s", "", bn))
    shrink = 1 - b / a if a else 0
    if shrink > hi:
        warns.append(f"{rel}: shrank {shrink:.0%} (> {hi:.0%}), read it")
    elif shrink < lo:
        warns.append(f"{rel}: shrank {shrink:.0%} (< {lo:.0%})")
    return fails, warns


def gate(site, base, lo, hi):
    fails, warns = [], []
    rels = changed(site, base)
    tot_old = tot_new = 0
    for rel in rels:
        path = os.path.join(site, rel)
        if not os.path.exists(path):
            fails.append(f"{rel}: deleted")
            continue
        with open(path, encoding="utf-8") as fh:
            new = fh.read()
        old = git_show(site, base, rel)
        f, w = gate_file(rel, old, new, lo, hi)
        fails += f
        warns += w
        if old:
            tot_old += len(re.sub(r"\s", "", body_of(old)))
            tot_new += len(re.sub(r"\s", "", body_of(new)))
    for w in warns:
        print("WARN", w)
    for f in fails:
        print("FAIL", f)
    if tot_old:
        print(f"{len(rels)} files, {tot_old} -> {tot_new} chars ({1 - tot_new / tot_old:.0%} shorter)")
    _, _, d, l, ai = site_metrics(site)
    print(f"now dash/k {d:.2f}  long/k {l:.2f}  aiism/k {ai:.2f}")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rank", action="store_true")
    ap.add_argument("--gate", metavar="SITE")
    ap.add_argument("--base", default="HEAD")
    ap.add_argument("--min-shrink", type=float, default=0.0)
    ap.add_argument("--max-shrink", type=float, default=0.4)
    ap.add_argument("--root", default=GALAXY)
    a = ap.parse_args()
    if a.gate:
        site = a.gate if os.path.isdir(a.gate) else os.path.join(a.root, a.gate)
        sys.exit(gate(site, a.base, a.min_shrink, a.max_shrink))
    sites = sorted(d for d in glob.glob(os.path.join(a.root, "*-note")) if os.path.isdir(d))
    rank(sites)


if __name__ == "__main__":
    main()
