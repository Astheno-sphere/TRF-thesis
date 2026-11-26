# Submission package: resume state

Read this first if a session ends mid-task. Updated as each step finishes.

## Decided (Tiger, 8 Nov)
- Supplement is a separate PDF, not a thesis appendix. Thesis goes on Zenodo only after grading.
- Scope now: submission core (thesis, app link, Zenodo DOI, deck) and four supplements bound as one PDF:
  submission index, reproduce card, verification dossier (red teams + code audit + novelty), evidence map,
  policy brief (English and Norwegian). Video skipped. App UX later ("feels basic, kiddish").
- Visual system (revised 9 Nov): charcoal cover with oxblood band, brass accent #A9863B, oxblood kickers, orange only for
  open items; IBM Plex Sans headings, Source Serif 4 body, IBM Plex Mono for code. No filled boxes, no em dashes.
- A whipper agent reviews every text before Tiger sees it.

## Files
- supplement_content.py: all text and figures (sourced from thesis, recorded runs, CODE_REVIEW.md)
- build_supplement.py: HTML template and PDF render (Playwright chromium)
- fonts/: Montserrat, Source Serif 4 (+ italic), IBM Plex Mono

## Steps
- [x] content drafted (supplement_content.py)
- [x] build_supplement.py, render, look at every page (10 pages, layout fits)
- [x] whipper review (accuracy, em dashes, slop, overclaims), 16 findings fixed: briefs legally corrected (C3 is SPE-only; 17(3)(b) includes public task; claims scoped to model), P2-M1 and P2-M5 (open) added, counts from CODE_REVIEW, AI reviewers named, asks as questions
- [x] code exhibits added (real before/after lines from git, with commit and guard), audit as compact table (9 Nov)
- [x] joao-base mirrors main via .github/workflows/mirror-joao-base.yml
- [x] app UX pass in the same type system (Plex Sans, Source Serif lede), restrained (TRF 7e70bfe, P123)
- [ ] link supplement from README
- [ ] deck (Slides type), same system
- [ ] thesis final assembly (9 Nov): HiMolde template uploaded (document_template-masters_thesis.dotx).
  - [x] build_docx.py: template title page transplanted (LOG953, logos), Calibri/TNR, oxblood accents, roman front
        matter + arabic from Ch1, contents after Sammendrag, list of figures, figure labels/bookmarks/links,
        TableText style for cells, wide tables 9 pt; Fig 5.2 re-rendered 4x from ui.life_strip (record 100)
  - [x] libreoffice-math installed in container (needed to see equations in renders)
  - [x] sync audit (6 blunders, 8 stale) -> P125, P127, B-57; TRF R-38 (Appendix A, provenance, .zenodo.json ORCID/keywords)
  - [x] citation audit -> P126 (agent-built, 97 edits), P128 Aikebaier follow-ups, B-58 apa_key
  - [x] whipper round 1 (8 MUST) -> B-59 build + P129 source; committed 21817eb
  - [x] whipper round 2 (3 MUST) -> P130, B-60; committed 9df2579. Open (minor): S6 figure label size needs Archify re-layout; S10 App D quote rule gaps; S13 check math in Word (t*, subscripts); uncaptioned appendix tables
  - [x] em dashes: none left outside cited titles and code
  - [ ] left for Tiger: citation I-2, I-9 (retrieval dates), I-11..I-14, M-2, M-3, M-7; Rak/TEHDAS pages; Springer check Martinez/Voss-Knude
  - [ ] Zenodo: decide 1.3.1 (needs Tiger's yes), discoverability metadata
  - [ ] deck

## 9 Nov evening: LaTeX PDF and one repository
- [x] thesis PDF via xelatex: handoff_tools/build_pdf.py + thesis_pdf/ (B-62); docx kept as secondary
- [x] links: TRF-thesis joao-base everywhere (P131, P132, README, supplement, BibTeX)
- [x] Streamlit: new app trf-thesis-himolde.streamlit.app from TRF-thesis/joao-base/demo_app/app.py (Python 3.12), deployed
- [ ] verify new app loads; ask Tiger: delete old trf app, rename new to trfhimolde (keeps thesis URL)
- [ ] whipper round 3 on PDF -> scratchpad/whipper_round3.md; fix
- [ ] send Tiger final PDF + package; package = thesis PDF, supplement PDF, Zenodo DOI, Streamlit link, GitHub link

## 19 Nov: pre-defence pass (session resumed)
- [x] three read-only reviews (opus/sonnet; Fable needs credits): scratchpad/review_thesis_gaps.md (G1-G21), review_audit_report.md (R1-R21), review_deck.md
- [ ] P139 thesis patch (agent, private copy scratchpad/p139copy) -> apply, assemble, PDF+docx, Appendix A copies, trail, commit
- [ ] audit report fixes (agent, scratchpad/auditcopy) -> copy supplement_content.py, build_supplement.py, CODE_REVIEW.md; chmod +x repro_package/run_all.sh
- [ ] deck fixes (agent, scratchpad/deckfix) -> publish to https://claude.ai/artifact/3fBxsBPWgwWQsMeh23YGm3
- [ ] viva notes rebuilt from the three reviews (process/Viva_Preparation_Notes.md is PUBLIC on joao-base: Tiger to decide G21)
- [ ] Tiger: submitted 14 Nov? G17-G19 citation items; G20 open app URL; G21 private or move viva notes

### 19 Nov, later
- DONE: P139 (35 edits), P140, P141 (viewer sync to TRF 854b2a6, Appendix A copy, checksums); PDF 183 pp, docx, supplement rebuilt; trail 0 fail. Commit 17088c7.
- DONE: B-65 audit report + supplement (R1-R21, G16). Commit cc9d4d5. run_all.sh now executable.
- RUNNING: deck fix agent (scratchpad/deckfix), viva notes agent (scratchpad/viva). Viva notes NOT committed until Tiger decides G21 (notes public on joao-base).
- WAITING ON TIGER: 14 Nov submitted? (errata note), G21 privacy, G17-G19 citations, open app, old Streamlit app delete/rename.
- 20 Nov: deck fixes published to Slides artifact (version 22): 31 slides, notes 14:40, 4 new backup slides. Viva notes agent resumed (scratchpad/viva).
- 20 Nov: TRF 1.3.2 released (524250a, DOI 10.5281/zenodo.24399784; Zenodo controlled subjects + Norwegian abstract not re-applied: needs Tiger logged in). B-66: code table, viva notes (public, Tiger's choice), cheat sheet, walkthrough. Deck notes v24. Tiger submits today.
- 21 Nov: R-45 deep links (TRF e2d342a), P142, B-67: deck links (v28), cheat sheet slide-by-slide. Tiger submits Monday 23 Nov.

## 22 Nov 2026 (evening)
- Impeccable v4.10.0 installed by hand (Skill tool does not load it). Critique of slides 1 to 16 delivered.
- Deck fixes applied and published (version 1795363641-70fe): timelines on slides 4, 5, 9 now static (no animation dependence); footers shortened on slides 4, 12, 13; fallback note moved off slide 13 (kept in notes); slide 2 duplicate section strip removed, list enlarged; slide 12 "39 / 78" condition reworded.
- Not done: slide 10 (mechanism) overload fix (optional, riskier); slide 12 dot grid is still animated.
- Zenodo R-46 edit (ef9fe70) and its description upgrade are in the code repo; Tiger still to close the open Zenodo edit page without publishing.
- Open for Tiger: three citation checks, live test of deep links, old Streamlit app rename decision.

## 24 to 26 Nov 2026
- 24 Nov: deck animations restored and extended (slides 4, 5, 9, 11, 12), slop stripes removed, footers shortened; deck version 1795364123-22cb. Supplement typography pass B-68 (1db4aa4), 12 pages. Delivered to Tiger: thesis PDF, supplement, Zenodo 1.3.2 zip, clean reproducibility zip (no Synthea cohort: regenerates differently).
- 25 Nov: Prof. Ferreira's article draft and journal notes uploaded (c69ebb1). First target: Computer Law & Security Review (CLSR).
- 26 Nov: thesis citation gap closed against primary sources (ACM DL, EUR-Lex HTML, Cambridge, IDCS record): Schneier & Kelsey 2(2), Art 68(12), Art 73(1)(e), recitals 19/36/39 only, C-413/23 P para 73, Rak p. 928, KONFIDO, TEHDAS2 D6.3 (2026a) and D7.4 (2026b). No thesis error found. EFTA EEA-Lex status unverified (bot check): Tiger by hand.
- 26 Nov: TRF R-47 (sensitivity.py) and R-48 pushed; release v1.3.3 published on GitHub; Zenodo version DOI 10.5281/zenodo.24562862 (record 24562862; concept 10.5281/zenodo.23819274). Thesis still cites 1.3.0; no computed figure changed.
- 26 Nov: CLSR package built outside this repo (/home/claude/work/article/package/clsr_v0.9, v0.9.1 in progress): anonymised manuscript, two-column preview, title page, cover letter, figures, anonymised code archive (41 tests pass), concordance gate. Article work files are NOT committed here (repo is public; double-anonymised review).
- Open for Tiger: when to make GitHub private (thesis PDF links to GitHub and Streamlit; keep public until after grading); remove article draft docx from main before review?
