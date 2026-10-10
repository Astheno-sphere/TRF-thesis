# Audit status — 10 October 2026

How the work is checked, what the last audits found, and what is still open. Every claim here can be re-run.

## Automated checks (run these first in any new session)

| Check | Command | Last result (10 Oct) |
|---|---|---|
| Trail inspector, 14 checks incl. full replay of every patch from `joao-base-v1`, recorded runs, public repo | `python3 handoff_tools/trail_check.py --full --remote` | TRAIL INTACT; 11 recorded runs 6/6 match; 13 Appendix A 14/14; 14 replay of 79 patch runs; 12 public repo `169c99a` matches CHECKSUMS |
| Appendix A listings equal their files | `python3 handoff_tools/appendix_sync.py` | 14/14 |
| Checker reproduces Chapter 5 | `python3 demo_app/trf_checker.py` | 95/90, 39, 0, 138 (52/86), 200/200 verify, three tamper tests fail |
| All modules vs recorded outputs | `bash repro_package/run_all.sh` then trail_check check 11 | 6/6 identical |
| Bounded SMT check | `python3 demo_app/z3_check.py` (needs z3-solver) | 9/9 unsat; sanity and mutations sat |
| Viewer self-check | `streamlit run demo_app/app.py`, Thesis run | "Matches the thesis" locally; live app needs reboot |
| Figures | Archify `finalize … --quality showcase` on `.archify/*/candidate.json` | validate/deliver/check/browser-check pass |
| Word build | `python3 handoff_tools/build_docx.py --pages` | 9 captioned tables, 79 contents entries, 541 cross-links, contents page numbers cached |

## Independent audits this session (fresh agent each time, read-only)

| Date | Scope | Outcome |
|---|---|---|
| 3 Oct (B-38) | Tracker closures vs text | Over-claimed closures corrected |
| 4 Oct (P52) | Review 3 merge, Z3 | 38 fixes incl. Rival 4 restored verbatim; Z3 P2 tautology found and rewritten (B-45) |
| 5 Oct (P56) | P53–P55 (hooks, SPUHiN, SEL, figures) | 23 fixes (§4.1 hook put ten-year floor and ceiling on one record; P31 overstated; Elhub quote; counts) |
| 6 Oct (P59i) | Review 4 merge, 77 paragraphs, 17 comments | 53/64 verbatim; 4 must-fix (cut-off [39] tail, "two tamper tests", stray 1,006, stale contents) fixed; nice-to-haves partly done |
| 6 Oct (Rak / D6.3 / helsedata agents) | Source checks | Rak paywalled (abstract only); D6.3 claims (2),(3) unsupported → removed; Helsedataservice corrected |

**Audit prompt pattern** (reuse): "You are an independent auditor (read-only). [Context of files and patches]. Check: (1) every supervisor change present in the assembled md and reading cleanly; (2) every comment addressed; (3) consistency of numbers, citations, cross-references, line counts; (4) run the checker and trail_check. Report MUST FIX vs NICE TO HAVE with file/line and fix."

## Known open findings (not yet fixed)

| # | Finding | Severity | Owner |
|---|---|---|---|
| 1 | Live Streamlit app holds the pre-P58 `trf_checker` in memory → third tamper test "PASSES", mismatch banner | High (public demo) | Tiger: reboot |
| 2 | Global `AUDIT_LOG` shared across Streamlit sessions: concurrent runs can fail proofs spuriously; unbounded growth; O(n) proofs | Medium | Code fix proposed |
| 3 | App does not reload `trf_checker` per run | Medium | Code fix proposed |
| 4 | `repro_package/README.md` "deterministic and regenerable" full cohort; subset README "1,006" | Low | Text fix |
| 5 | No List of Figures; figure references not hyperlinked; two Ch2 tables uncaptioned | Low | Build/text |
| 6 | D6.3 v2.0 page for the six-month sentence unverified | Medium (citation precision) | Tiger opens PDF |
| 7 | Rak (2024) cited from abstract only | Medium | Tiger: library |
| 8 | Datatilsynet send date missing | Low | Tiger |
| 9 | Proactive invalidation not in code or Z3 | Low (stated as specified-only) | Optional |
| 10 | Abstract 421 words; length vs programme limits | Open by decision | End |
| 11 | Long sentences (>60 words) in Ch4/Ch6 | Low | Style pass |
| 12 | AI declaration not confirmed with coordinator; Archify not named | Medium (integrity) | Tiger |
