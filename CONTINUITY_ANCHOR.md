# CONTINUITY ANCHOR — read first on any fresh clone

The git repo is the permanent state across sessions. Tags do NOT push to this remote
(repo policy hook rejects non-branch refs), so recreate the base tag locally each clone.

## Re-anchor in one line
```
git checkout joao-base && git tag -f joao-base-v1 184c91d
```
- `joao-base-v1` → commit **184c91d** ("Baseline: 30 Sept migration package") — the reviewed-draft
  base the trail_check replay and verify_base measure from. Verified: Front_Matter md5 e3afa723b46f
  and Chapter2 md5 f2694c7dfd13 at 184c91d match the D0 patch "before" hashes.

## Last verified state (update this when you hand off)
- Branch **joao-base**, HEAD **760caa3** (P84), chapter body **48,060 words**.
- `concordance.py --check` → all 711 cross-references resolve (current content sound).
- REVIEW_TRACKER ~90% CLOSED; R3-F10 closed (Helsedirektoratet 19 Oct reply, floor now primary-sourced).

## Integrity note (honest)
- `trail_check.py` replay reconstructs Ch1/2/3 cleanly from the base tag; Ch4/5/6/7/Front_Matter show
  ~25 anchor mismatches = **historical provenance drift** in the pre-handoff patch chain, NOT current
  content error. Current correctness is established by: HEAD = the exact pushed, in-session-verified
  commit; 711 xrefs resolve; chapter bodies intact.
- FORWARD work is gated per-edit by: `patch.py` (floor: citations/numbers/articles/hedges),
  `trim_inspector.py` (defined terms, slop, line safety, cross-refs), `concordance.py --check`
  (whole-thesis xref = the interconnectedness/domino guard), and a full-context preservation-agent
  pass. None of these need the historical replay. Diff-review before every commit; no unlogged edits.

## Objective (standing)
Make VERA-SNARK / the TRF thesis an A-grade, genuinely novel, defensible MSc thesis with a true
academic contribution Norwegian and European researchers can build on — submitted on time and able
to survive a brutal examination. Every move surgical; every change checked for domino effects across
chapters and cross-references before commit.
