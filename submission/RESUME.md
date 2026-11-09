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
