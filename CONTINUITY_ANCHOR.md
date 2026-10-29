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
- Branch **joao-base**, HEAD **d63ab94** (P87), origin == local (0/0 divergence), clean tree.
- Tags: `joao-base-v1` → 184c91d (reviewed-draft base); `joao-base-v2` exists (later anchor).
- Chapter body: raw `wc -w` of Front+Ch1–7 = **56,118**; project-tracked "body" figure was ~48k at P84
  (the tracked counter strips reference lists/front — re-run the project counter if an exact figure is needed for João).
- `concordance.py --check` → all cross-references resolve (711→716 after red-team additions); current content sound.
- REVIEW_TRACKER ~90% CLOSED; R3-F10 closed (Helsedirektoratet 19 Oct reply, floor primary-sourced).
- **Red team COMPLETE and committed:** P85 (EDPB 02/2026 anonymisation → §4.9, R4 residue), P86 (§6.1 overclaim
  aligned to §4.7/§5.5 concessions), P87 (R3b narrow-reading honesty §4.6, R3c/R3d necessity hedges §4.2,
  R5 energy framing §2.7, Parallel AI named in AI declaration). RED_TEAM.md holds the 7-persona panel + defence doctrine.
- **zk-product question answered (29 Oct, text-only):** thesis mechanism does NOT need a zk-SNARK (§1.5 excl. #1);
  a market product would help but not "solve" (provable key-destruction is an open problem); worth is highest as a
  reference design + open implementation timed to the Art 73(5) implementing acts (due 26 Mar 2027), not a zk startup.
- **PENDING (first next-session action):** statement-of-contribution paragraph — see NEXT_SESSION.md §A. Drafted,
  NOT yet applied; must be checked against existing §1.4/§6.7/§7 to tighten-or-merge, not duplicate. Gated patch.

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
