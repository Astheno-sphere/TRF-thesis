#!/usr/bin/env python3
"""Trail inspector. Run after every patch and before every commit, handoff or package.

Usage: python3 handoff_tools/trail_check.py [--full] [--remote]
  --full    also re-run the five recorded program runs (repro_package/run_all.sh)
  --remote  also compare the public repository (Astheno-sphere/TRF) with CHECKSUMS.md

It answers one question: is every change to the thesis on the record, and has nothing slid back?
Exit 0 only if no check FAILs. WARN does not block; read it anyway.

Checks
  1  git          on branch joao-base; uncommitted files listed
  2  md5 chain    every watched file's current md5 equals the last "after" md5 in patches/APPLIED.log,
                  the chain of before/after md5s has no gap, and a file with no log entry is
                  unchanged since tag joao-base-v1. A gap or mismatch is an edit nobody logged.
  3  trail        every edit ID in APPLIED.log has a row in CHANGE_TRAIL.md
  4  commits      every applied patch file has a commit whose message starts "<ID>:"
  5  code copies  repro_package/ and code_artefacts/ copies equal the demo_app/ originals
  6  assembly     rebuilding in a scratch copy reproduces the submission and bibliography exactly
  7  register     every md5 in VERSION_REGISTER.md matches its file
  8  base diff    every wording difference from the reviewed draft is explained by a logged patch
  9  guards       regression patterns stay at 0; review targets never rise (handoff_tools/guards.json)
 10  tracker      REVIEW_TRACKER.md: closed items name applied patches and meet their guard goals
 11  full/remote  optional, see above
 13  appendix     every source listing and console output in Appendix A equals its file
"""
import hashlib, json, os, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / "handoff_tools"))
TAG, BRANCH = "joao-base-v1", "joao-base"
COPIES = {"demo_app/trf_checker.py": ["repro_package/trf_checker.py", "code_artefacts/trf_checker.py"],
          "demo_app/synthea_layer.py": ["repro_package/synthea_layer.py", "code_artefacts/synthea_layer.py"],
          "demo_app/norwegian_layer.py": ["repro_package/norwegian_layer.py", "code_artefacts/norwegian/norwegian_layer.py"],
          "demo_app/cross_sector_check.py": ["repro_package/cross_sector_check.py", "code_artefacts/norwegian/cross_sector_check.py"]}
results = []


def md5(b):
    return hashlib.md5(b if isinstance(b, bytes) else b.encode()).hexdigest()[:12]


def fmd5(p):
    return md5(pathlib.Path(p).read_bytes())


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True).stdout


def report(n, name, status, lines=()):
    results.append(status)
    print(f"[{status:4}] {n:>2} {name}")
    for l in list(lines)[:25]:
        print(f"         {l}")
    if len(list(lines)) > 25:
        print(f"         ... {len(list(lines)) - 25} more")


def log_entries():
    rows = []
    p = pathlib.Path("patches/APPLIED.log")
    if not p.exists():
        return rows
    for ln in p.read_text(encoding="utf-8").splitlines():
        parts = [x.strip() for x in ln.split(" | ")]
        if len(parts) >= 6:
            ts, pf, eid, f, ba = parts[:5]
            b, a = [x.strip() for x in ba.split("->")]
            rows.append(dict(ts=ts, patch=pf, id=eid, file=f, before=b, after=a, why=" | ".join(parts[5:])))
    return rows


def main():
    full, remote = "--full" in sys.argv, "--remote" in sys.argv
    G = json.loads(pathlib.Path("handoff_tools/guards.json").read_text(encoding="utf-8"))
    watched = G["prose_files"] + G["code_files"] + [c for v in COPIES.values() for c in v]
    log = log_entries()

    # 1 git
    br = sh("git", "rev-parse", "--abbrev-ref", "HEAD").strip()
    dirty = [l for l in sh("git", "status", "--short").splitlines() if l.strip()]
    report(1, f"git: branch {br}, {len(dirty)} uncommitted", "FAIL" if br != BRANCH else ("WARN" if dirty else "PASS"), dirty)

    # 2 md5 chain
    probs = []
    runs = {}
    for r in log:
        runs.setdefault((r["ts"], r["patch"], r["file"]), (r["before"], r["after"]))
    chains = {}
    for (ts, pf, f), (b, a) in runs.items():
        chains.setdefault(f, []).append((ts, pf, b, a))
    for f, ch in chains.items():
        for (t1, p1, b1, a1), (t2, p2, b2, a2) in zip(ch, ch[1:]):
            if a1 != b2:
                probs.append(f"{f}: gap between {p1} (after {a1}) and {p2} (before {b2}): unlogged edit in between")
        if pathlib.Path(f).exists() and fmd5(f) != ch[-1][3]:
            probs.append(f"{f}: now {fmd5(f)}, last logged {ch[-1][3]} by {ch[-1][1]}: unlogged edit")
    for f in watched:
        if f in chains or not pathlib.Path(f).exists():
            continue
        tagged = subprocess.run(["git", "show", f"{TAG}:{f}"], capture_output=True).stdout
        if tagged and md5(tagged) != fmd5(f):
            probs.append(f"{f}: changed since {TAG} with no entry in APPLIED.log")
    report(2, f"md5 chain over {len(watched)} watched files, {len(runs)} logged file-runs", "FAIL" if probs else "PASS", probs)

    # 3 trail rows
    trail = pathlib.Path("CHANGE_TRAIL.md").read_text(encoding="utf-8")
    covered = set()
    for m in re.finditer(r"^\| (\S+?)(\d+) to \1(\d+) \|", trail, re.M):  # "| D0-01 to D0-29 |", "| P09-F09 to P09-F23 |"
        w = len(m.group(2))
        covered |= {f"{m.group(1)}{i:0{w}d}" for i in range(int(m.group(2)), int(m.group(3)) + 1)}
    for m in re.finditer(r"^\| ([A-Za-z0-9]+-\d+(?:, [A-Za-z0-9]+-\d+)+) \|", trail, re.M):  # "| P03-01, P03-02 |"
        covered |= set(m.group(1).split(", "))
    missing = sorted({r["id"] for r in log if r["id"] not in covered
                      and not re.search(rf"\|\s*{re.escape(r['id'])}\s*\|", trail)})
    report(3, f"every logged edit has a CHANGE_TRAIL row ({len({r['id'] for r in log})} IDs)", "FAIL" if missing else "PASS", missing)

    # 4 commits
    msgs = sh("git", "log", "--format=%B", BRANCH)  # full message: one commit may carry two patch lines
    nocommit = []
    for pf in sorted({r["patch"] for r in log}):
        pid = pf.split("_")[0]
        if not re.search(rf"^{re.escape(pid)}:", msgs, re.M):
            nocommit.append(f"{pf}: no commit message starting '{pid}:'")
    report(4, "every applied patch has its own commit", "WARN" if nocommit else "PASS", nocommit)

    # 5 code copies
    bad = [f"{c} {fmd5(c)} != {o} {fmd5(o)}" for o, cs in COPIES.items() for c in cs
           if pathlib.Path(c).exists() and fmd5(c) != fmd5(o)]
    report(5, "code copies identical to demo_app/", "FAIL" if bad else "PASS", bad)

    # 6 assembly reproducible
    with tempfile.TemporaryDirectory() as d:
        for f in list(pathlib.Path(".").glob("*.md")) + [pathlib.Path("Consolidated_Bibliography.Rmd")]:
            shutil.copy(f, d)
        os.makedirs(f"{d}/code_artefacts")
        shutil.copy("code_artefacts/README_Appendix_A.md", f"{d}/code_artefacts/")
        subprocess.run([sys.executable, str(ROOT / "handoff_tools/assemble.py")], cwd=d, capture_output=True)
        stale = [f for f in ("VERA-SNARK_Thesis_SUBMISSION.md", "Consolidated_Bibliography.md", "Consolidated_Bibliography.Rmd")
                 if fmd5(f"{d}/{f}") != fmd5(f)]
    report(6, "submission and bibliography equal a fresh assembly", "FAIL" if stale else "PASS",
           [f"{f} is stale: run handoff_tools/assemble.py" for f in stale])

    # 7 register
    s = pathlib.Path("VERSION_REGISTER.md").read_text(encoding="utf-8")
    rows = list(re.finditer(r"^\| [A-Z]+ \| ([^|]+?) \| ([0-9a-f]{12}) \|", s, re.M))
    badr = [m.group(1).strip() for m in rows
            if not pathlib.Path(m.group(1).strip()).exists() or fmd5(m.group(1).strip()) != m.group(2)]
    report(7, f"register: {len(rows)} rows", "WARN" if badr else "PASS",
           [f"{b}: register md5 out of date (expected while a patch is uncommitted; must be 0 before packaging)" for b in badr])

    # 8 base diff explained by patches
    import verify_base
    _, diffs, _ = verify_base.collect()
    pairs = []
    for pf in sorted({r["patch"] for r in log}):
        p = pathlib.Path("patches") / pf
        if p.exists():
            import importlib.util
            spec = importlib.util.spec_from_file_location(pf, p); m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            pairs += [(e["old"], e["new"]) for e in m.EDITS]
    SEP = "QQSEPQQ"
    rendered = sh_in(f"\n\n{SEP}\n\n".join(x for pr in pairs for x in pr)).split(SEP)
    rendered = [verify_base.norm(x) for x in rendered]
    plain_pairs = [(rendered[2 * i], rendered[2 * i + 1]) for i in range(len(pairs))] if len(rendered) == 2 * len(pairs) else []
    plain = " ".join(b for _, b in plain_pairs)
    unexplained = []
    for f, ours, draft in diffs:
        replayed = draft or ""
        for a, b in plain_pairs:  # replay every logged edit on the closest draft line
            if a and a in replayed:
                replayed = replayed.replace(a, b)
        if replayed == ours:
            continue
        w = ours.split()  # fallback: a new sentence that has no draft counterpart
        shingles = [" ".join(w[i:i + 6]) for i in range(0, max(1, len(w) - 5))]
        if not any(x in plain for x in shingles):
            unexplained.append(f"[{f}] {ours[:160]}")
    report(8, f"base diff: {len(diffs)} wording differences from the reviewed draft, {len(unexplained)} unexplained",
           "FAIL" if unexplained else "PASS", unexplained)

    # 9 guards
    out, fail = [], False
    for g in G["guards"]:
        files = G["prose_files"] if g["scope"] == "prose" else G["code_files"]
        n = sum(len(re.findall(g["pattern"], pathlib.Path(f).read_text(encoding="utf-8"))) for f in files if pathlib.Path(f).exists())
        g["now"] = n
        if n > g["baseline"]:
            fail = True; out.append(f"RISE  {g['name']}: {g['baseline']} -> {n}  ({g['kind']})")
        elif g["kind"] == "target" and n > g["goal"]:
            out.append(f"open  [{g['item']}] {g['name']}: {n} (goal {g['goal']})")
    tgt = [g for g in G["guards"] if g["kind"] == "target"]
    met = sum(1 for g in tgt if g["now"] <= g["goal"])
    report(9, f"guards: {sum(g['kind'] == 'regression' for g in G['guards'])} regression at 0; targets met {met}/{len(tgt)}",
           "FAIL" if fail else "PASS", out)

    # 10 tracker
    tr = pathlib.Path("REVIEW_TRACKER.md").read_text(encoding="utf-8")
    ids = {r["id"] for r in log} | {r["id"].split("-")[0] for r in log}
    tp, counts = [], {}
    for m in re.finditer(r"^\| ([A-Z0-9]+-?[0-9a-z]*) \| (.+?) \| (OPEN|BLOCKED|PARTIAL|CLOSED|DECLINED) \| ([^|]*) \| ([^|]*) \|$", tr, re.M):
        item, _, st, pids, ev = [x.strip() for x in m.groups()]
        counts[st] = counts.get(st, 0) + 1
        pl = [x.strip() for x in re.split(r"[,\s]+", pids) if x.strip()]
        if st in ("CLOSED", "PARTIAL"):
            if not pl:
                tp.append(f"{item}: {st} but names no patch")
            tp += [f"{item}: patch {x} not in APPLIED.log" for x in pl if x not in ids]
        if st == "CLOSED":
            tp += [f"{item}: CLOSED but guard '{g['name']}' at {g['now']} (goal {g['goal']})"
                   for g in G["guards"] if g.get("item") and item.startswith(g["item"]) and g["now"] > g["goal"]]
        if st == "DECLINED" and not ev:
            tp.append(f"{item}: DECLINED without evidence")
    report(10, "tracker: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())), "FAIL" if tp else "PASS", tp)

    # 11 optional
    if full:
        subprocess.run(["bash", "repro_package/run_all.sh"], capture_output=True)
        pairs = [("trf_output_rerun.txt", "trf_output.txt"), ("delta_witness_rerun.txt", "expected_delta_witness_output.txt"),
                 ("synthea_comparison_rerun.txt", "synthea_comparison_subset_output.txt"),
                 ("norwegian_layer_rerun.txt", "expected_norwegian_output.txt"), ("cross_sector_rerun.txt", "expected_cross_sector_output.txt")]
        R = pathlib.Path("repro_package/results")
        bad = [a for a, b in pairs if fmd5(R / a) != fmd5(R / b)]
        report(11, f"recorded runs: {5 - len(bad)}/5 match", "FAIL" if bad else "PASS", bad)
    if remote:
        clone = pathlib.Path("/home/claude/trf") if pathlib.Path("/home/claude/trf/.git").exists() else pathlib.Path("/home/claude/astheno-sphere/trf")
        if not (clone / ".git").exists():
            subprocess.run(["git", "clone", "-q", "--depth", "1", "https://github.com/Astheno-sphere/trf", str(clone)],
                           env={**os.environ, "GIT_LFS_SKIP_SMUDGE": "1"}, capture_output=True)
        else:
            subprocess.run(["git", "-C", str(clone), "pull", "-q", "--ff-only"], capture_output=True)
        head = sh("git", "-C", str(clone), "log", "--format=%h %s", "-1").strip()
        cs = pathlib.Path("CHECKSUMS.md").read_text(encoding="utf-8")
        bad = [f"{f}: repo {fmd5(clone / f) if (clone / f).exists() else 'missing'} != CHECKSUMS {h}"
               for f, h in re.findall(r"^\| `([^`]+)` \| ([0-9a-f]{12}) \|", cs, re.M)
               if not (clone / f).exists() or fmd5(clone / f) != h]
        bad += [f"{c} (canonical {o}) != repo {pathlib.Path(o).name}" for o in COPIES
                if (clone / pathlib.Path(o).name).exists() and fmd5(o) != fmd5(clone / pathlib.Path(o).name)]
        report(12, f"public repository at {head} vs CHECKSUMS.md and demo_app/", "FAIL" if bad else "PASS", bad)

    # 13 Appendix A listings equal the files they reproduce
    import appendix_sync
    A = pathlib.Path(appendix_sync.APPENDIX).read_text(encoding="utf-8")
    bad = [f"{h[3:]} differs from {f}" for h, f in appendix_sync.BLOCKS.items()
           if appendix_sync.block(A, h).strip() != pathlib.Path(f).read_text(encoding="utf-8").strip()]
    report(13, f"Appendix A: {len(appendix_sync.BLOCKS) - len(bad)}/{len(appendix_sync.BLOCKS)} listings equal their files",
           "FAIL" if bad else "PASS", bad)

    n_fail = results.count("FAIL")
    print(f"\nTRAIL {'BROKEN' if n_fail else 'INTACT'}: {n_fail} fail, {results.count('WARN')} warn")
    sys.exit(1 if n_fail else 0)


def sh_in(text):
    return subprocess.run(["pandoc", "-f", "markdown", "-t", "plain", "--wrap=none"], input=text,
                          capture_output=True, text=True).stdout.replace("\n", " ")


if __name__ == "__main__":
    main()
