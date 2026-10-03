#!/usr/bin/env python3
"""Recompute md5, word count and modified time for every VERSION_REGISTER.md row whose file changed.

Usage: python3 handoff_tools/register_sync.py
Only rows whose md5 no longer matches are touched; descriptions are never rewritten here.
Run after a patch is applied and its trail row written, immediately before the commit.
"""
import datetime, hashlib, pathlib, re, os
os.chdir(pathlib.Path(__file__).resolve().parent.parent)
R = pathlib.Path("VERSION_REGISTER.md"); s = R.read_text(encoding="utf-8"); changed = []


def md5(p): return hashlib.md5(pathlib.Path(p).read_bytes()).hexdigest()[:12]


def fix(m):
    t, p, h, w, mod, c = [x.strip() for x in m.groups()]
    P = pathlib.Path(p)
    if not P.is_file() or md5(p) == h:
        return m.group(0)
    changed.append(p)
    if re.fullmatch(r"[\d,]+", w):
        w = format(len(P.read_text(encoding="utf-8", errors="ignore").split()), ",")
    when = datetime.datetime.fromtimestamp(P.stat().st_mtime).strftime("%-d %b %H:%M")
    return f"| {t} | {p} | {md5(p)} | {w} | {when} | {c} |"


s = re.sub(r"^\| ([A-Z]+) \| ([^|]+?) \| ([0-9a-f]{12}) \| ([^|]*) \| ([^|]*) \| (.*) \|$", fix, s, flags=re.M)
R.write_text(s, encoding="utf-8")
print(f"register: {len(changed)} rows updated", *changed, sep="\n  ")
