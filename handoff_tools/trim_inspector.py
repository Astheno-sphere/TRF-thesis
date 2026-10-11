"""
Trim inspector — the mechanical whip for the length cut. ADDITIVE: it does not touch
inspector.py (the hard floor every patch relies on); it imports it and adds trim-specific
checks on top. See TRIM_RATIONALE.md for the doctrine this enforces.

Usage:
    python3 handoff_tools/trim_inspector.py BEFORE AFTER [SUBMISSION_FOR_XREFS]

BEFORE/AFTER are the pre- and post-trim copies of one chapter file. SUBMISSION (default
VERA-SNARK_Thesis_SUBMISSION.md) supplies the universe of valid cross-reference targets.
Exit 0 = ADMIT (floor passes, no defined term dropped, no dangling xref, no slop increase,
no line-safety hit, reduction within earned barrier). Exit 1 = REJECT.
"""
import re, sys, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import inspector as I

# --- frozen defined terms (TRIM_RATIONALE.md §4): counts may not fall ---
DEFINED = ["Semantics I", "Semantics II", "plaintext verifiability", "accountability-preserving",
 "accessor fields", "subject fields", "payload", "commitment", "hiding", "binding", "invalidation",
 "Crypto-Erasure by Invalidation", "retention floor", "deletion ceiling", "erasure right",
 "Tri-Lateral Retention Feasibility", "TRF", "payload key", "terminal transition", "Merkle",
 "necessity", "Secure Processing Environment", "National Contact Point",
 "Proposition 1", "Proposition 2", "Proposition 3", "Proposition 4",
 "Corollary 1.1", "Corollary 1.2", "Corollary 2.1", "Corollary 2.2", "Corollary 2.3"]

# --- AI-slop phrases (TRIM_RATIONALE.md §5): must never INCREASE ---
SLOP = ["it is important to note", "it is worth noting", "it should be emphasised",
 "it should be noted", "it is crucial to", "it is essential to", "it is interesting",
 "the fact that", "delve", "underscore", "navigate the complexities", "a myriad of",
 "a plethora of", "shed light on", "pave the way", "in order to", "due to the fact that",
 "with regard to", "a number of", "plays a crucial role", "plays a key role",
 "plays a vital role", "plays a pivotal role", "plays a significant role",
 "not only", "it is clear that", "needless to say"]

# --- scaffolding / signposting: removable, counts toward headroom ---
SCAFFOLD = ["having established", "having shown", "having discussed", "this section now",
 "this section turns", "we now turn", "as established in", "as discussed in", "as noted above",
 "as mentioned", "it is worth recalling", "to recap", "in this section we", "the next section",
 "as we have seen", "as outlined above"]

# --- recurring claims (restatement seeds): occurrences beyond the first are candidate cuts ---
RECURRING = ["six months of permit expiry", "at least one year", "no data subject",
 "information logistics", "no cryptographic novelty", "longest applicable retention",
 "broad reading", "attested rather than proven", "specified but not implemented"]

def body(t): return I.body(t)
def words(t): return len(re.sub(r"[#*_`>|]", " ", body(t)).split())

def count_phrases(t, phrases):
    b = body(t).lower()
    return {p: b.count(p) for p in phrases if b.count(p)}

def defined_counts(t):
    b = body(t)
    return {d: b.count(d) for d in DEFINED}

def xrefs(t):
    b = body(t)
    pats = [r"Section\s+\d+\.\d+", r"§\s?\d+\.\d+", r"Chapter\s+\d+", r"Table\s+\d+\.\d+",
            r"Figure\s+\d+\.\d+", r"Proposition\s+\d+", r"Corollary\s+\d+\.\d+",
            r"Appendix\s+[A-C](?:,\s?[A-Z]\.\d+)?"]
    out = set()
    for p in pats:
        out.update(x.strip() for x in re.findall(p, b))
    return out

def valid_targets(submission):
    s = pathlib.Path(submission).read_text(encoding="utf-8")
    t = set()
    for m in re.findall(r"^#{1,4}\s+(?:Chapter\s+)?(\d+)\.?\s", s, flags=re.M):
        t.add(f"Chapter {m}")
    for m in re.findall(r"\b(\d+\.\d+)\b", s):  # section numbers appearing as headings/refs
        t.add(f"Section {m}"); t.add(f"§ {m}"); t.add(f"§{m}")
    for lbl in ["Table", "Figure"]:
        for m in re.findall(rf"{lbl}\s+(\d+\.\d+)", s): t.add(f"{lbl} {m}")
    for m in re.findall(r"Proposition\s+(\d+)", s): t.add(f"Proposition {m}")
    for m in re.findall(r"Corollary\s+(\d+\.\d+)", s): t.add(f"Corollary {m}")
    for m in re.findall(r"Appendix\s+([A-C])", s): t.add(f"Appendix {m}")
    return t

def line_safety(after_text):
    hits = []
    for i, ln in enumerate(after_text.splitlines(), 1):
        low = ln.lower()
        for m in re.finditer(r"\b(\w+)\s+\1\b", low):
            if m.group(1) not in ("that", "had", "the"):  # 'that that', 'the the' still caught below
                hits.append(f"L{i}: doubled word '{m.group(1)}'")
        if re.search(r"\b(the the|a a|to to|of of|is is|that that)\b", low):
            hits.append(f"L{i}: doubled word")
        if re.search(r"—\s*[:;]", ln) or re.search(r"[:;]\s*—", ln):
            hits.append(f"L{i}: broken dash/colon pair (em-dash scar)")
    return hits

def report(before, after, submission="VERA-SNARK_Thesis_SUBMISSION.md"):
    A = pathlib.Path(before).read_text(encoding="utf-8")
    B = pathlib.Path(after).read_text(encoding="utf-8")
    ok = True; out = []

    # 1. floor gate (reuse inspector)
    floor = I.inspect(before, after, "floor")  # prints its own block; returns bool
    if not floor: ok = False
    out.append(f"  [{'PASS' if floor else 'FAIL'}] floor gate (claims/numbers/citations/articles/hedges/reflist)")

    # 2. defined-term floor
    da, db = defined_counts(A), defined_counts(B)
    dropped = {k: (da[k], db[k]) for k in da if db[k] < da[k]}
    if dropped: ok = False
    out.append(f"  [{'PASS' if not dropped else 'FAIL'}] defined terms not dropped")
    for k, (x, y) in dropped.items(): out.append(f"         '{k}': {x} -> {y}")

    # 3. cross-reference resolver
    tgt = valid_targets(submission)
    refs = xrefs(B)
    norm = lambda r: r.replace("§", "Section ").replace("Section  ", "Section ").strip()
    dangling = [r for r in refs if r not in tgt and norm(r) not in tgt
                and r.replace("§", "§").strip() not in tgt
                and not any(r.split()[-1] == v.split()[-1] and r.split()[0].rstrip("§.") in v for v in tgt)]
    # permissive: only flag section/table/figure/appendix numbers with no numeric match anywhere
    hard = []
    nums_in_tgt = set(re.findall(r"\d+\.\d+|\bChapter \d+|\bProposition \d+|\bCorollary \d+\.\d+|\bAppendix [A-C]", " ".join(tgt)))
    for r in refs:
        key = re.sub(r"^(§|Section)\s*", "Section ", r)
        if re.match(r"(Section|§)", r):
            n = re.search(r"\d+\.\d+", r)
            if n and f"Section {n.group()}" not in tgt and f"§{n.group()}" not in tgt and f"§ {n.group()}" not in tgt:
                hard.append(r)
    if hard: ok = False
    out.append(f"  [{'PASS' if not hard else 'FAIL'}] cross-references resolve")
    for r in hard: out.append(f"         dangling: {r}")

    # 4. slop delta (must not increase)
    sa, sb = count_phrases(A, SLOP), count_phrases(B, SLOP)
    increased = {k: (sa.get(k, 0), sb[k]) for k in sb if sb[k] > sa.get(k, 0)}
    removed = sum(sa.values()) - sum(v for v in sb.values())
    if increased: ok = False
    out.append(f"  [{'PASS' if not increased else 'FAIL'}] slop not increased (net removed: {removed})")
    for k, (x, y) in increased.items(): out.append(f"         slop up '{k}': {x} -> {y}")

    # 5. line safety
    hits = line_safety(B)
    # only NEW hits relative to A
    old_hits = set(line_safety(A))
    new_hits = [h for h in hits if h not in old_hits]
    if new_hits: ok = False
    out.append(f"  [{'PASS' if not new_hits else 'FAIL'}] line safety (no new splices/doubles/broken dashes)")
    for h in new_hits[:8]: out.append(f"         {h}")

    # 6. dynamic barrier
    wa, wb = words(A), words(B)
    red = wa - wb
    slop_words = sum(len(k.split()) * sa.get(k, 0) for k in SLOP)
    scaf = count_phrases(A, SCAFFOLD); scaf_words = sum(len(k.split()) * v for k, v in scaf.items())
    rec = count_phrases(A, RECURRING)
    restate_sent = max(0, sum(rec.values()) - len([k for k in rec]))  # occurrences beyond first per phrase
    restate_words = restate_sent * 25  # ~ one restated sentence
    headroom = int((slop_words + scaf_words + restate_words) * 1.3) + max(10, int(wa * 0.05))
    within = red <= headroom
    if not within: ok = False
    out.append(f"  [{'PASS' if within else 'FAIL'}] within earned barrier  (reduced {red}w; headroom {headroom}w"
               f"  [slop {slop_words}w, scaffold {scaf_words}w, restatement~{restate_words}w, +5% base])")
    out.append(f"  [INFO] words {wa} -> {wb}   ({100*red/max(wa,1):.1f}% cut)")

    print(f"=== TRIM INSPECTION ===")
    print("\n".join(out))
    print(f"  TRIM VERDICT: {'ADMIT' if ok else 'REJECT'}")
    return ok

if __name__ == "__main__":
    sub = sys.argv[3] if len(sys.argv) > 3 else "VERA-SNARK_Thesis_SUBMISSION.md"
    sys.exit(0 if report(sys.argv[1], sys.argv[2], sub) else 1)
