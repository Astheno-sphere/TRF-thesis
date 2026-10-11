# TRIM DOCTRINE — the contract for the length cut (Round 5, point 1)

**Written 12 October 2026. This governs every trimming edit and both instruments that police it. It can undo months of work, so nothing here is optional.**

---

## 0. The one line

> **Cut what repeats and what decorates. Keep what claims, qualifies, and proves. Density is the goal; brevity and readability are its by-products; precision is never traded for either.**

The target is 30–35k words (João [4]), but the number is a *consequence*, never the instruction. We do not cut a sentence to hit a count; we remove redundancy and decoration, and the count falls out.

---

## 1. The dynamic virtual barrier (no hard floor)

There is no fixed floor and no uniform percentage. Each section earns its allowed cut in proportion to the redundancy and decoration it actually carries:

- A dense, already-tight section (the proofs, §4.7, §6.2, §6.3, Ch7) earns ≈ 0 — it is left almost untouched.
- A padded section (Ch1 background, Ch2 overlaps, the collision restated across 11 sites) earns a large budget.

`trim_inspector.py` computes, per section, a **redundancy headroom** in words = removable slop + scaffolding + restatement beyond the home-section statement. The **barrier** is: *actual word-reduction may not exceed headroom × 1.3.* If a cut goes past that, it is presumed to be eating substance, and the preservation agent must justify every excess sentence as genuinely redundant before the cut stands. The barrier rises and falls with each section's measured quality — that is what "proportional to the quality of improvements" means in code.

---

## 2. KEEP — protected, the checker defends these

- Every claim, number, date, citation, Article reference, and **hedge/qualifier**.
- The **first, home-section** statement of each argument (only later restatements are cut).
- All legal-interpretive reasoning: §4.2 necessity analysis, §4.6 two readings, the Article 9 patient link, the ITI-55 payload, the Article 68(12) scope.
- Every Proposition, proof, Corollary, the mechanism specification, Table 4.1, the residue analysis.
- The honest self-limiting passages: the §4.7 "what kind of result this is" note, §6.2 authority problem, §6.3 assurance limit, the "what is not claimed" list. These are A-register and cost few words — cutting them lowers the grade.
- **Proposition 3 (the drafting test) and the invalidation-entry takeaway (§6.8)** — the reusable assets. WHIPLASHER GATE: a cut that weakens or removes either is rejected outright.
- Every defined term, verbatim (§4).

## 3. CUT — what the barrier's headroom is made of

- Restatements of an argument already made in its home section → replace with a cross-reference ("as §4.6 establishes"), never a re-explanation.
- Chapter/section re-recaps ("As established in Chapter 2 …" followed by the thing re-established).
- Structural signposting that narrates the document ("Having shown X, this section now turns to Y").
- Doubled examples where one carries the point.
- Emphasis-not-information padding (slop, §5).
- Enumerations a single sentence could carry.

---

## 4. Defined-term freeze (synonym substitution = rejection)

These carry the formal spine; trimming must never paraphrase them into a near-synonym. The inspector holds a floor count for each and rejects a drop.

`Semantics I`, `Semantics II`, `plaintext verifiability`, `accountability-preserving`, `accessor fields`, `subject fields`, `payload`, `commitment`, `hiding`, `binding`, `invalidation`, `Crypto-Erasure by Invalidation`, `retention floor`, `deletion ceiling`, `erasure right`, `Tri-Lateral Retention Feasibility`, `TRF`, `payload key`, `terminal transition`, `Merkle`, `necessity`, `Proposition 1/2/3/4`, `Corollary 1.1/1.2/2.1/2.2/2.3`, `Secure Processing Environment`, `National Contact Point`.

"verifiable" never becomes "checkable"; "accessor fields" never becomes "access data"; "invalidation" never becomes "deletion".

---

## 5. The AI-slop taxonomy (removal targets — their DECREASE is the win)

Detected and reported by the inspector; removed by the trim. Their replacement is **deletion, not flourish**:
- Filler openers: "it is important/worth noting (that)", "it should be emphasised/noted", "it is crucial/essential to", "the fact that", "it is interesting that".
- Inflated verbs/nouns: "delve", "underscore", "navigate the complexities", "play a crucial/key/vital/pivotal/significant role", "a myriad of", "a plethora of", "shed light on", "pave the way".
- Wordy connectives: "in order to" → "to"; "due to the fact that" → "because"; "in the context of" → "in/for"; "with regard to" → "on"; "a number of" → "several".
- Structural tics: reflexive tricolons (everything in threes), "not only … but also", "firstly/secondly/…" chains, "moreover/furthermore/additionally" stacks, paragraph-final sentences that restate the paragraph.

**The integrity whip (Tiger's rule):** readability is pursued *only* by removing clutter. The agent must NEVER add colour, rhetoric, informality, a conversational aside, a vivid metaphor, or a "compelling" flourish to make reading pleasant. Academic stimulation here means clarity, density and precision — the pleasure of a reader who meets no wasted word. Any edit that adds expressive decoration to "engage" is penalised exactly like a lost hedge.

---

## 6. INSTRUMENT A — `trim_inspector.py` (the mechanical whip)

Run on every trim edit, in addition to the existing `inspector.py` gate (which stays the hard floor: no undeclared loss of a claim, number, citation, Article ref, or hedge). `trim_inspector` adds, per changed file/section:

1. **Redundancy headroom + barrier** — words of slop + scaffolding + restatement; flags if actual reduction exceeds headroom × 1.3 (§1).
2. **Defined-term floor** — each frozen term's count may not fall below its pre-trim count (§4). A drop is a FAIL.
3. **Cross-reference resolver** — every `§N.N` / `Section N.N` / `Chapter N` / `Table N.N` / `Figure N.N` / `Proposition N` / `Corollary N.N` / `Appendix X` pointer in the trimmed text resolves to a heading or label that still exists in the assembled submission. A dangling pointer is a FAIL.
4. **Slop delta** — counts the §5 phrases; reports the decrease (good) and FAILS on any *increase* (slop introduced).
5. **Line-safety scan** on changed lines — comma splices, doubled words ("the the"), doubled clauses, broken en/em-dash pairs (the em-dash scar). Any hit is a FAIL to re-read.
6. **Equation guard** — the native-equation markers and `$`-free state are unchanged (run against the built docx when code/math-adjacent prose is touched).
7. **Word-count delta** — per file and running total toward the 30–35k band.

It prints a per-section verdict: ADMIT only if the floor passes, no defined term dropped, no dangling xref, no slop increase, no line-safety hit, and the reduction is within the earned barrier.

## 7. INSTRUMENT B — the preservation agent (the live, vigilant reader)

A fresh, read-only agent run **per chapter immediately after that chapter's trim patch, before it is committed** — the live parallel watchdog. It does what no counter can: it reads every changed sentence beside its original and judges meaning, not tokens. Its brief, verbatim, is:

> You are the preservation agent for an MSc thesis undergoing a length cut. You are read-only and adversarial in defence of substance. You are given, per edit, the ORIGINAL sentence(s) and the TRIMMED version, plus `TRIM_RATIONALE.md`. For each edit, return ADMIT or REJECT with the rule and a one-line reason. REJECT if the trimmed version does ANY of:
> 1. changes a claim's strength, scope, or truth-conditions (overclaim or underclaim);
> 2. drops or detaches a hedge/qualifier from the claim it governed ("reported", "illustrative", "on the broad reading", "specified but not implemented", "attested not proven", "presumptive", "contestable", "conditional");
> 3. removes or weakens a protected passage (§2 of the rationale), above all Proposition 3 or the invalidation-entry takeaway;
> 4. paraphrases a frozen defined term into a synonym (§4);
> 5. introduces a new claim, result, citation, or emphasis not present in the original;
> 6. adds colour, rhetoric, informality, metaphor, or a "compelling" flourish (§5 integrity whip) — readability must come only from removing clutter;
> 7. breaks a cross-reference, an equation, or a table/figure pointer;
> 8. removes content that is NOT redundant or decorative — i.e., the cut exceeds the section's earned redundancy, eating substance.
> Also return, per section: does the trimmed text still read as dense academic plain English, and is anything the argument depends on now missing? Report MUST-FIX (with file/line and the exact original wording to restore) separately from NICE-TO-HAVE. Judge only what changed; do not propose new cuts.

Its MUST-FIX list is actioned before the chapter's patch is committed. A chapter is not done until both instruments return clean.

---

## 8. Workflow per section (never one giant rewrite)

1. Measure the section with `trim_inspector.py` → read its redundancy headroom and barrier.
2. Draft the trim as a `patch.py` edit set (deletions and cross-references first; sentence-tightening only if still over the earned budget). De-duplicate before tightening.
3. `patch.py --dry` (floor gate) + `trim_inspector.py` (trim gate). Fix until both ADMIT.
4. Run the **preservation agent** on the section's before/after; action every MUST-FIX.
5. Apply, add the CHANGE_TRAIL row, re-assemble, `trail_check`, commit (its own patch — reversible), push.
6. Re-measure the running total. Stop when the band is reached with every protected element intact; do not cut further to chase a lower number.

Order across the thesis, by earned budget (most padded first): Ch1 §1.1–1.2 and the collision restatements → Ch2 overlaps and the programme-fit duplication → the abstract/Sammendrag to 250–300 → light touches elsewhere. The proofs, §4.7, §6.2–6.3 and Ch7 are near-frozen.
