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
- [ ] app UX pass in the same type system (Plex Sans), restrained
- [ ] link supplement from README
- [ ] deck (Slides type), same system
- [ ] thesis: HiMolde title page (blocked on Tiger's upload), freeze check chapters vs code
