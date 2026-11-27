#!/usr/bin/env python3
"""Concordance gate: every reported number in manuscript.md must match the code archive.

Sources: docs/expected_trf_output.txt, docs/expected_sensitivity_output.txt,
docs/expected_delta_witness_output.txt (recorded runs), trf_checker.py constants, and a direct
recomputation by importing trf_checker. Exit 1 on any mismatch or on any missing anchor phrase.
Usage: python3 concordance_gate.py [--review-code PATH]
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RC = os.environ.get("REVIEW_CODE", os.path.join(HERE, "..", "review_code"))
if "--review-code" in sys.argv:
    RC = sys.argv[sys.argv.index("--review-code") + 1]
RC = os.path.abspath(RC)

def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()

MS_RAW = read(os.path.join(HERE, "manuscript.md"))
MS = re.sub(r"\s+", " ", MS_RAW)
TRF = read(os.path.join(RC, "docs", "expected_trf_output.txt"))
SENS = read(os.path.join(RC, "docs", "expected_sensitivity_output.txt"))
DELTA = read(os.path.join(RC, "docs", "expected_delta_witness_output.txt"))
SEC = read(os.path.join(RC, "docs", "expected_secondary_output.txt"))
SRC = read(os.path.join(RC, "trf_checker.py"))

UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve "
         "thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}

def num(tok):
    t = tok.strip().lower()
    if re.fullmatch(r"\d+(\.\d+)?", t):
        return float(t) if "." in t else int(t)
    if t in UNITS:
        return UNITS[t]
    if "-" in t:
        a, b = t.split("-", 1)
        return TENS[a] + UNITS[b]
    if t in TENS:
        return TENS[t]
    raise ValueError(tok)

def grab(pattern, text, label):
    m = re.search(pattern, text)
    if not m:
        raise LookupError(f"{label}: pattern not found: {pattern}")
    return [num(g) for g in m.groups()]

FAIL, ROWS = [], []
def check(label, ms_pattern, expected, source, text=MS):
    try:
        got = grab(ms_pattern, text, label)
    except LookupError as e:
        FAIL.append(str(e)); ROWS.append((label, "MISSING", expected, source)); return
    exp = list(expected) if isinstance(expected, (list, tuple)) else [expected]
    ok = got == exp
    ROWS.append((label, got, exp, source + ("" if ok else "  <-- MISMATCH")))
    if not ok:
        FAIL.append(f"{label}: manuscript {got} != source {exp} ({source})")

def p(pattern, text=TRF):
    m = re.search(pattern, text, re.M)
    if not m:
        FAIL.append(f"source pattern not found: {pattern}"); return [None]
    return [num(g) for g in m.groups()]

W = r"([A-Za-z]+(?:-[a-z]+)?|\d+)"   # a number written in digits or words

# ---- recorded-run values ------------------------------------------------------------
seed, = p(r"seed=(\d+)")
n_all, n_x, n_s = p(r"Generated (\d+) records \((\d+) cross-border, (\d+) SPE")
recs, = p(r"records with >=1 violation : (\d+)/200")
xb, = p(r"cross-border \(F=120\)\s+: (\d+)/100")
spe, = p(r"SPE access-log \(F=12\)\s+: (\d+)/100")
viol, = p(r"total constraint violations: (\d+)")
cor12, = p(r"Corollary 1\.2 witnesses .*?: (\d+)")
inv, = p(r"records invalidated\s+: (\d+)/200")
g17, = p(r"ground = GDPR Art 17\(1\)\s+: (\d+)")
g68, = p(r"ground = EHDS Art 68\(12\) : (\d+)")
sem2, = p(r"RESULT  Semantics II: (\d+) violations")
verif, = p(r"records verifying\s+: (\d+)/200")
ta, tpi, c3, c1end = p(r"rid=100: t_a=(\d+) permit expires t_pi=(\d+) -> C3 from t=(\d+), C1 to t=(\d+)")
fspe, = p(r"SPE=(\d+)")
fxb, = p(r"cross-border=(\d+)")
ceil, = p(r"ceiling=(\d+)")
n_false = len(re.findall(r"feasible=False", TRF)); n_true = len(re.findall(r"feasible=True", TRF))
sens_rows = [(int(a), b, int(c), int(d), int(e), int(f)) for a, b, c, d, e, f in
             re.findall(r"^\s*(\d+)\s+(applies|excluded)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$", SENS, re.M)]
s3 = p(r"response period 3 months, floor 120, ceiling applies: (\d+) records, (\d+) violations, accountability (\d+)", SENS)
d3 = p(r"^\s+3\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$", DELTA)
sens = {(r[0], r[1]): r[2:] for r in sens_rows}
excl120 = sens[(120, "excluded")]

# ---- direct recomputation --------------------------------------------------------
sys.path.insert(0, RC)
import trf_checker as t  # noqa: E402
recs_ = t.generate()
v1 = {r.rid: t.check_semantics_I(r) for r in recs_}
cons = {rid: {v["constraint"] for v in vs} for rid, vs in v1.items() if vs}
req_only = sum(1 for c in cons.values() if c == {"C2"})
ceil_only = sum(1 for c in cons.values() if c == {"C3"})
both = sum(1 for c in cons.values() if c == {"C2", "C3"})
by_id = {r.rid: r for r in recs_}
noreq = [rid for rid, c in cons.items() if "C3" in c and by_id[rid].t_r == t.INF]
noreq_subset_ceil_only = all(cons[rid] == {"C3"} for rid in noreq)
ceil_viol = sum(1 for c in cons.values() if "C3" in c)
if not noreq_subset_ceil_only:
    FAIL.append("no-request ceiling collisions are not a subset of ceiling-only records")

# ---- abstract and Sections 1 to 5 ------------------------------------------------
m = re.search(r"\[1\] Secondary-use subset, 12-month floor\s+ceiling applies : n=(\d+) request-related=(\d+) ceiling=(\d+) both=(\d+) affected_records=(\d+) record_constraint_pairs=(\d+)\s+ceiling excluded: n=\d+ request-related=\d+ ceiling=\d+ both=\d+ affected_records=(\d+) record_constraint_pairs=(\d+)", SEC)
sec = [int(x) for x in m.groups()] if m else None
if not sec: FAIL.append("expected_secondary_output: section [1] not parsed")
m = re.search(r"\[2\].*?ceiling applies : affected_records=(\d+) record_constraint_pairs=(\d+).*?ceiling excluded: affected_records=(\d+) record_constraint_pairs=(\d+)", SEC, re.S)
s60 = [int(x) for x in m.groups()] if m else None
m = re.search(r"strict  : pairs=(\d+) records=(\d+) SPE ceiling\(C3\) pairs=(\d+)", SEC)
strict = [int(x) for x in m.groups()] if m else None
m = re.search(r"distinct labels=(\d+) reused \(>1 record\)=(\d+).*?distinct expiry months per label: (\{.*?\})", SEC, re.S)
labels = [int(m.group(1)), int(m.group(2))] if m else None
lab_months = sorted(set(eval(m.group(3)).values())) if m else []
check("abstract: secondary-use records", r"plaintext verification produced conflicts for (\d+) of (\d+) secondary-use records", [sec[4], sec[0]], "expected_secondary_output [1]")
check("abstract: ceiling excluded", r"and (nine) when the permit ceiling excluded log fields", sec[6], "expected_secondary_output [1]")
check("5.2 secondary split", r"Of (\d+) records, (nine) had a request-related conflict and (\d+) had a permit-ceiling conflict\. (Five) had both, giving (\d+) affected records and (\d+) record", [sec[0], sec[1], sec[2], sec[3], sec[4], sec[5]], "expected_secondary_output [1]")
check("5.2 secondary excluded", r"only the (nine) request-related conflicts remained", sec[7], "expected_secondary_output [1]")
check("5.2 sixty-month", r"made all (\d+) events conflict under the broad reading, with (\d+) record.constraint pairs, and left (\d+) conflicts", [s60[0], s60[1], s60[3]], "expected_secondary_output [2]")
check("5.2 pooled remainder", r"The (\d+) affected records outside the secondary-use subset", recs - sec[4], "expected_trf_output minus secondary [1]")
check("5.2 strict endpoint", r"gives (\d+) pairs across (\d+) records.*?falls from \d+ to (\d+)", strict, "expected_secondary_output [3]")
check("5.1 permit labels", r"to (\d+) permit labels by record identifier", labels[0] if labels else None, "expected_secondary_output [5]")
check("5.1 expiry months per label", r"between (four) and (six) different expiry months", [lab_months[0], lab_months[-1]] if lab_months else None, "expected_secondary_output [5]")
if labels and labels[0] != labels[1]: FAIL.append("not every permit label is reused")
check("3.2 example: s, e, s+F, d", r"created at month (\d+), with a one-year floor and permit expiry at month (\d+), is retained through model month (\d+) and reaches the ceiling at month (\d+)",
      [ta, tpi, c1end, c3], "expected_trf_output: rid=100 witness line")
check("3.2 example: collision month", r"the collision occurs at month (\d+) without", c3, "expected_trf_output: rid=100 collision")
check("3.1 ceiling d_C = e + L", r"d_\{C\} = e \+ (\d+)", ceil, "trf_checker.CEILING")
check("5.1 records per class", r"generates (\d+) cross-border records and (\d+) SPE access-log records at seed (\d+)", [n_x, n_s, seed], "expected_trf_output header / trf_checker.SEED")
check("5.1 primary creation month range", r"creation month uniformly from (\d+) through (\d+)", [int(x) for x in re.search(r"t_a = rng\.randint\((\d+), (\d+)\)", SRC).groups()], "trf_checker.generate: rng.randint(0, 11)")
check("5.1 primary request probability", r"request with probability (0\.\d+) and", float(re.search(r"if rng\.random\(\) < (0\.\d+) else INF\n", SRC).group(1)), "trf_checker.generate (class 1)")
check("5.1 primary request offset", r"offset of (\d+) to (\d+) months", [int(x) for x in re.search(r"t_r = t_a \+ rng\.randint\((\d+), (\d+)\) if rng\.random\(\) < 0\.40", SRC).groups()], "trf_checker.generate (class 1)")
check("5.1 primary floor", r"reference run uses a (\d+)-month primary-use", fxb, "trf_checker.FLOOR_XBORDER / output header")
check("5.1 SPE floor", r"same creation range, a (\d+)-month floor", fspe, "trf_checker.FLOOR_SPE / output header")
check("5.1 SPE expiry offset", r"expiry offset from (\d+) through (\d+) months", [int(x) for x in re.search(r"permit_len = rng\.randint\((\d+), (\d+)\)", SRC).groups()], "trf_checker.generate: permit_len")
check("5.1 SPE request probability/offset", r"request with probability (0\.\d+), with an offset from (\d+) to (\d+) months",
      [float(re.search(r"rng\.randint\(1, 18\) if rng\.random\(\) < (0\.\d+)", SRC).group(1))] + [int(x) for x in re.search(r"t_r = t_a \+ rng\.randint\((\d+), (\d+)\) if rng\.random\(\) < 0\.25", SRC).groups()],
      "trf_checker.generate (class 2)")
check("5.1 ceiling length", r"applies the six-month ceiling", [], "trf_checker.CEILING = 6") if ceil == 6 else FAIL.append("ceiling != 6")
check("5.1 sensitivity floors", r"primary-use floor to (\d+), (\d+) or (\d+) months", sorted({r[0] for r in sens_rows}, reverse=True), "expected_sensitivity_output rows")
check("5.1 brute-force cases", r"plaintext result for (three) small conflict cases and (one) control", [n_false, n_true], "expected_trf_output: INDEPENDENT CROSS-CHECK")
check("5.2 reference violations/records", r"reproduced (\d+) plaintext violations across (\d+) records", [viol, recs], "expected_trf_output")
check("5.2 cross-border / SPE records", W + r" cross-border and (\d+) SPE records incurred", [xb, spe], "expected_trf_output: per-class lines")
check("5.2 request-only / ceiling-only / both", W + r" records incurred a request-related violation alone, (\d+) incurred a ceiling violation alone and " + W + r" incurred both",
      [excl120[0] - (viol - recs), recs - excl120[0], viol - recs], "derived: 46-5, 90-46, 95-90")
check("5.2 request-only etc (direct)", W + r" records incurred a request-related violation alone, (\d+) incurred a ceiling violation alone and " + W + r" incurred both",
      [req_only, ceil_only, both], "direct: trf_checker.check_semantics_I per record")
check("5.2 no-request ceiling collisions", W + r" SPE records had a ceiling collision in the absence of a request", [cor12], "expected_trf_output: Corollary 1.2 witnesses")
check("5.2 no-request (direct)", W + r" SPE records had a ceiling collision in the absence of a request", [len(noreq)], "direct recomputation")
check("5.2 subset claim", r"Those (\d+) are a subset of the (\d+) ceiling-only", [len(noreq), ceil_only], "direct recomputation (subset verified)")
check("5.2 verified records", r"verified all (\d+) records against its log", verif, "expected_trf_output: records verifying")
check("5.2 invalidations", r"scheduled (\d+) payload invalidations, attributing (\d+) to erasure requests and (\d+) to the permit ceiling", [inv, g17, g68], "expected_trf_output: SEMANTICS II")
check("5.2 sem II zero", r"the checker reported (zero) violations", sem2, "expected_trf_output")
check("5.2 ceiling removal reduces violations", r"reduces the baseline by (\d+) violations", viol - excl120[1], "derived: 95-46 (sensitivity rows)")
check("5.2 ceiling violations (direct)", r"reduces the baseline by (\d+) violations", ceil_viol, "direct: records with a C3 violation")
check("5.2 records keeping a request violation", r"For " + W + r" of the affected records", both, "direct: records with C2 and C3")
check("5.2 violating records drop", r"violating records drops by (\d+)", recs - excl120[0], "derived: 90-46")
check("5.2 ceiling violations persist", r"all (\d+) ceiling violations remain",
      [sens[(f, "applies")][1] - sens[(f, "excluded")][1] for f in (120,)], "derived: applies-excluded")
for f in (72, 36):
    if sens[(f, "applies")][1] - sens[(f, "excluded")][1] != viol - excl120[1]:
        FAIL.append(f"ceiling violations at floor {f} differ from 49")
check("5.2 delta=3 result", r"changes the plaintext result to (\d+) violations across (\d+) records", [s3[1], s3[0]], "expected_sensitivity_output: response period 3 months")
check("5.2 delta=3 (delta witness)", r"changes the plaintext result to (\d+) violations across (\d+) records", [d3[1], d3[0]], "expected_delta_witness_output: delta 3 row")
check("5.2 delta=3 witnesses persist", r"The (\d+) no-request witnesses persist", d3[2], "expected_delta_witness_output: Cor1.2 at delta 3")
check("5.2 delta=3 sem II zero", r"second semantics again produces (zero) violations", s3[2], "expected_sensitivity_output")

# ---- Table 3 ---------------------------------------------------------------------
t2 = re.findall(r"^\| (\d+) months \| (Applies|Excluded) \| (\d+) \| (\d+) \| (\d+) \|$", MS_RAW, re.M)
if len(t2) != 6:
    FAIL.append(f"Table 3: expected 6 rows, found {len(t2)}")
for f, c, a, b, d in t2:
    src = sens.get((int(f), c.lower()))
    got = [int(a), int(b), int(d)]
    exp = list(src[:3]) if src else None
    ROWS.append((f"Table 3 {f} {c}", got, exp, "expected_sensitivity_output"))
    if got != exp:
        FAIL.append(f"Table 3 row {f} {c}: {got} != {exp}")
check("Table 3 caption: cohort / SPE floor", r"Fixed cohort of (\d+) records with a (\d+)-month SPE floor", [n_all, fspe], "expected_sensitivity_output header")

# ---- figure captions and floor values in 2.3 -----------------------------------------
check("Fig. 1 caption: s, F, window, e, d", r"created at month \$s = (\d+)\$ with a one-year floor, \$F = (\d+)\$, so the retention window is \$W = \\\{s, \\ldots, s \+ F\\\} = \\\{(\d+), \\ldots, (\d+)\\\}\$. The permit expires at month \$e = (\d+)\$ and the ceiling deadline is \$d = d_\{C\} = e \+ (\d+) = (\d+)\$",
      [ta, fspe, ta, c1end, tpi, ceil, c3], "expected_trf_output: rid=100 line and header")
check("Fig. 1 caption: t*", r"from \$t\^\{\*\} = \\max\(s, d\) = (\d+)\$", max(ta, c3), "derived from rid=100 line")
check("Fig. 3 caption: floors", r"primary-use floor \((\d+), (\d+) or (\d+) months\)", sorted({r[0] for r in sens_rows}, reverse=True), "expected_sensitivity_output rows")
check("2.3 ten-year sandbox floor", r"The (ten)-year value used in the supplied sandbox", fxb // 12, "trf_checker.FLOOR_XBORDER / 12")
check("2.3 six-year and 72-month", r"kept as part of the log for (six) years.*?The (\d+)-month value applied", [72 // 12, 72], "sensitivity row 72 months / [25]")
check("2.3 36-month scenario", r"and by a (\d+)-month scenario", 36, "sensitivity row 36 months")
if not {72, 36} <= {r[0] for r in sens_rows}:
    FAIL.append("sensitivity output lacks the 72 or 36 month floors")

# ---- Algorithm 1: line-by-line mapping to trf_checker.py lines 305-318 ---------------------
# Each algorithm line carries its source line(s) in manuscript.md. The gate checks that (a) the code
# lines 305-318 start at "def V_II" and end at the final return, (b) every executable code line
# (not the docstring, not blank) is covered by exactly one algorithm line, (c) each algorithm line
# has the code construct it claims (anchor), (d) every quoted string in the algorithm occurs in the
# mapped code line, and (e) the algorithm has no executable line without a code line.
# It writes ALGORITHM_MAPPING.md from the manuscript, so the table cannot drift.
CODE = SRC.splitlines()
if not CODE[304].startswith("def V_II(") or CODE[317].strip() != 'return True, ""':
    FAIL.append("trf_checker.py lines 305-318 are no longer V_II; update Algorithm 1")
alg = re.search(r"```\{\.alg\}\n(.*?)```", MS_RAW, re.S)
ANCHOR = {
    "309": "integrity_result if integrity_result is not None else integrity(rec)",
    "310": "if not ok:", "311": "return False, why",
    "312": "if not rec.c:", "313": 'return False, "commitment missing"',
    "314": "if alpha(rec, t) == 0 and t >= rec.t_a and rec.iota is None:",
    "315": 'return False, "payload inaccessible but no invalidation entry"',
    "316": "if not any(f in rec.m for f in SUBJECT_FIELDS) and rec.iota_subj is None:",
    "317": 'return False, "subject fields removed without a logged entry"',
    "318": 'return True, ""',
    "305-308": "def V_II(rec, t, integrity_result=None):",
}
if not alg:
    FAIL.append("Algorithm 1 block missing from manuscript.md")
else:
    covered, table, n = [], [], 0
    for line in alg.group(1).strip().splitlines():
        f = [x.strip() for x in line.split(" | ")]
        kind, text, src = f[0], f[1], f[2]
        if kind != "H":
            n += 1
        label = "-" if kind == "H" else str(n)
        lo, hi = (src.split("-") + [src])[:2] if "-" in src else (src, src)
        lo, hi = int(lo), int(hi)
        txt = "\n".join(CODE[lo - 1:hi])
        if src not in ANCHOR:
            FAIL.append(f"Algorithm 1 line {label}: unmapped source {src}")
        elif ANCHOR[src] not in txt:
            FAIL.append(f"Algorithm 1 line {label}: code lines {src} lack `{ANCHOR[src]}`")
        for q in re.findall(r'"([^"]*)"', text):
            if q and f'"{q}"' not in txt:
                FAIL.append(f"Algorithm 1 line {label}: string \"{q}\" not in code lines {src}")
        if kind != "H":
            covered += list(range(lo, hi + 1))
        else:
            if not (lo == 305 and hi == 308):
                FAIL.append("Algorithm 1 header must map to lines 305-308")
        table.append((label, text, src))
    must = {309, 310, 311, 312, 313, 314, 315, 316, 317, 318}
    if sorted(covered) != sorted(must):
        FAIL.append(f"Algorithm 1 covers code lines {sorted(covered)}, expected {sorted(must)}")
    if len(set(covered)) != len(covered):
        FAIL.append("Algorithm 1 maps a code line twice")
    md = ["# Algorithm 1: algorithm line to code line", "",
          "Generated by `concordance_gate.py` from `manuscript.md`; do not edit by hand.",
          "Source: `review_code/trf_checker.py`, function `V_II`, lines 305 to 318 (lines 306 to 308 are the docstring and are summarised by the Input and Output lines).", "",
          "| Algorithm line | Algorithm text | trf_checker.py line | Code |", "|---|---|---|---|"]
    for label, text, src in table:
        lo, hi = (src.split("-") + [src])[:2] if "-" in src else (src, src)
        code = " ".join(CODE[int(lo) - 1].split()) if label != "-" else "def V_II(rec, t, integrity_result=None):"
        t = text.replace("|", "/")
        md.append(f"| {label} | {t} | {src} | `{code}` |")
    open(os.path.join(HERE, "ALGORITHM_MAPPING.md"), "w").write("\n".join(md) + "\n")
    if not any("Algorithm 1" in x for x in FAIL):
        ROWS.append(("Algorithm 1", f"{n} lines", "maps to lines 305-318", "trf_checker.py"))

# ---- report ------------------------------------------------------------------------
w = max(len(r[0]) for r in ROWS)
for label, got, exp, src in ROWS:
    print(f"{label:<{w}}  ms={got}  src={exp}  [{src}]")
print(f"\nreview_code: {RC}")
if FAIL:
    print("\nGATE FAILED:")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print(f"\nGATE PASSED: {len(ROWS)} checks, 0 mismatches")
