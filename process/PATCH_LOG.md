# Patch Log — João's Review

Running record of what has actually been changed, in order, with the cascade each change
pulled with it. Written as work happens, not afterwards.

**This file records what was done. `PATCH_QUEUE.md` records what is left.** When they
disagree, grep the files — see `FAILURE_LEDGER.md` for why.

---

## Session opened 30 September 2026

Review received, verified and captured. Patch queue built with the cascade for each item
grepped rather than estimated.

**Nothing patched yet.** Work is gated on P-01 (which reading of Art. 68(12) the thesis
carries), which is Tiger's decision and determines what Chapter 4 proves.

### State at the start of patching

Recorded so any later drift is measurable against a known baseline.

- Submission: 62,888 words, 67 bibliography entries, 67 with a locator
- Register: 43 files, 0 stale
- Archive: 89 files, all byte-identical
- Figures in the thesis: 0
- Em-dashes: 111 total, 12 in prose and all deliberate
- Checker: 90/200 records, 95 violations, 39 Corollary 1.2 witnesses, 138 invalidations, 0
  under Semantics II, reference commitment `11087780fd192c8f`
- δ witness: 90/95 at δ=1, 89/94 at δ=3
- Synthea layer: 8 bundles, 891 bytes mean, six measures identical, 200/200 commitments
  differing
- Repository: `github.com/Astheno-sphere/TRF` at `dba9c56`, untagged
- Word build: 191 native OMML equations, 25 tables, 0 LaTeX leakage

**If any figure above changes as a result of a patch, it must change in all of:** the chapter
text, the app's Tab 1 self-assertion, `docs/expected_*.txt` in the repository,
`repro_package/results/`, and the fresh-clone verification must pass again.

---

## Entries

### 2 Oct 2026 — D0: base reset to the draft the supervisor reviewed (commit `0438daf`, tag `joao-base-v1`)

| ID | What | Verified by |
|---|---|---|
| D0-01 | Abstract replaced with the draft's version; Sammendrag and supervisor/artefact line added; "(Approx. 520 words.)" dropped | Paragraph comparison against `supervisor_review/draft_as_reviewed_tracked_rejected.txt` |
| D0-02 | Ch1 opening returned to the reviewed text; H-01 (Bodø) becomes proposal C-1 | Same |
| D0-03, 04 | Ch2: fifth-round sentence; accumulator caveat | Same |
| D0-05 to 13 | Ch4: Corollary 1.2 "sixth"; terminal transition outside C1; accumulator caveats ×3; F+1 window ×2; five rivals ×2 | Same |
| D0-14 to 19 | Ch5: witness count nine/four/five; "separately" ×2; two new paragraphs; chapter-level Appendix A stub removed | Same |
| D0-20 to 26 | Ch6: "separately"; terminal transition note; narrow-reading hedges ×2; addressee split ×2; first-version paragraph shortened | Same |
| D0-27 to 29 | Ch7: "separately"; accumulators not implemented; competent authorities | Same |

**Result.** After D0 every prose paragraph of the chapter files matches the reviewed draft. The
13 remaining line differences are template and rendering only, listed in `DECISION_RECORD.md`
D-14. Checker output byte-identical (`41b56742d35d`). Bibliography 67 entries, 67 linked.
Submission 63,126 words by `len(split())`.

**Not yet applied, deliberately.** The base keeps the draft's own defects, because the
supervisor's comments and tracked changes refer to them: "an separately" (3×), §4.8 saying the
salt is not destroyed while the code destroys it, the paraphrased Art 68(12), the EY dates in
§2.2, the four-round count in §2.1.4 against five rounds in Appendix B. Each is now a patch in
`PATCHES.md`.

---

## Cascade ledger

Each row is a change and every place it propagated. Filled in as patches land, so that a
future session can see not just what changed but what changing it forced.

*(Empty.)*
