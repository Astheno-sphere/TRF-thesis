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

*(Nothing yet. First entry goes here once P-01 is answered or an unblocked item is started.)*

---

## Cascade ledger

Each row is a change and every place it propagated. Filled in as patches land, so that a
future session can see not just what changed but what changing it forced.

*(Empty.)*
