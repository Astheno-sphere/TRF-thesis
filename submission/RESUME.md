# Submission package: resume state

Read this first if a session ends mid-task. Updated as each step finishes.

## Decided (Tiger, 8 Nov)
- Supplement is a separate PDF, not a thesis appendix. Thesis goes on Zenodo only after grading.
- Scope now: submission core (thesis, app link, Zenodo DOI, deck) and four supplements bound as one PDF:
  submission index, reproduce card, verification dossier (red teams + code audit + novelty), evidence map,
  policy brief (English and Norwegian). Video skipped. App UX later ("feels basic, kiddish").
- Visual system: oxblood / charcoal ground, cream rules, one gold accent per page, orange for open items only;
  Montserrat headings, Source Serif 4 body, IBM Plex Mono for commands only. No em dashes, no template chrome.
- A whipper agent reviews every text before Tiger sees it.

## Files
- supplement_content.py: all text and figures (sourced from thesis, recorded runs, CODE_REVIEW.md)
- build_supplement.py: HTML template and PDF render (Playwright chromium)
- fonts/: Montserrat, Source Serif 4 (+ italic), IBM Plex Mono

## Steps
- [x] content drafted (supplement_content.py)
- [x] build_supplement.py, render, look at every page (10 pages, layout fits)
- [ ] whipper review (accuracy, em dashes, slop, overclaims), fix
- [ ] commit; link from README
- [ ] deck (Slides type), same system
- [ ] thesis: HiMolde title page (blocked on Tiger's upload), freeze check chapters vs code
