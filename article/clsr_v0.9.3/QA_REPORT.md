# QA report, CLSR package v0.9.1 (26 Nov 2026)

Build: `./build.sh` ran end to end, exit 0 (figures, docx, both LaTeX variants with pdflatex, xelatex compile check, reference-count check, ancillary docx, gate).

| Check | Result |
|---|---|
| References in PDFs (v0.9 defect) | Cause: `build/filter.lua` returned `{RawBlock, table.unpack(el.content), RawBlock}`; Lua keeps only the first value of `table.unpack` inside a constructor, so only [1] reached LaTeX. Fixed: the filter now emits `thebibliography` with 17 `\bibitem`s (elsarticle numbered style, labels [1]-[17], one "References" heading). Preview_two_column.pdf and Manuscript_anonymised.pdf: 17 of 17 entries in order. build.sh exits 1 if a PDF has fewer than 17 |
| pdfLaTeX | Both .tex files compile with pdflatex (iftex switch: T1, inputenc, mathptmx, helvet, courier) and with xelatex (fontspec branch). The two PDFs are now built with pdflatex; xelatex output in build/tex_xe (10 pages, 17 refs). Only non-ASCII characters are á, Í, å |
| LaTeX warnings | No errors, no undefined references. Overfull boxes: 1.9 pt (preview), 2.3 and 6.4 pt (review; Table 1 cell and page output). Not visible at reading size |
| Pages | Preview 10 (was 10), review PDF 31 (was 28; one-column 90 mm Fig. 1 and refs now present), Word render 21 |
| Float gaps | Float parameters relaxed (topfraction 0.9, textfraction 0.07, floatpagefraction 0.75, [!tbp]); Fig. 1 single-column float. All pages of both PDFs rendered at 60 dpi and inspected: no mostly blank page (largest blank run inside the text block 3% on preview pages 1-9, 11% on review pages 1-30; last pages end early as expected). v0.9 preview p8 gap and review p5/p19 gaps gone |
| Figures | Redrawn (FIGURE_DESIGN_NOTES.md). Font pinned to Inter converted to TrueType (figures_src/fonts); figure PDFs embed TrueType subsets and pdftotext/pdffonts report no warnings; checked in greyscale. Fig. 1 90 mm, Figs 2-3 190 mm; text 7-8.5 pt at final width; vector PDF with embedded fonts, PNG 600 dpi, TIFF 1000 dpi; each rendered and read at final size, 2-3 iterations each. Fig. 3 values parsed from docs/expected_sensitivity_output.txt; all 24 values checked against the file |
| Concordance gate | `python3 concordance_gate.py`: GATE PASSED, 49 checks, 0 mismatches |
| Word count | One counter run over both versions (Sections 1-7 with tables and captions; without abstract, listing code, data/AI sections and references; tokens containing a letter or digit): v0.9 6,585 (its QA said 6,586), v0.9.1 6,673; with data availability and AI declaration 6,872. Within 6,000-15,000, near the lower bound |
| Abstract / keywords | 145 words / 6 keywords (unchanged) |
| References | 17; every citation has an entry; first-appearance order 1..17; docx reference list 17 entries in order |
| Em/en dashes | 0 in every md, tex, py, lua, latex template, sh file of the package, in the text of all four docx and in both PDFs |
| Anonymity grep | Terms: abbasia, arshad, ferreira, joão/joao, molde, himolde, høgskolen, astheno, orcid, 0000-0001-9461-9442, github, zenodo, 23819274, 24562862, streamlit, thesis, vera-snark, supervisor, tiger, msc. Over Manuscript_anonymised.docx (all XML parts), both PDFs (text and metadata), manuscript.md/.tex/_review.tex, figure files. Hits: only "European Data Protection Supervisor" (1) (and "MyHealth@EU" for the @ sign). PDF metadata: title only, author/creator/producer empty. Figure PDFs: title "Figure_n" only; PNG/TIFF carry dpi only (random "msc"/"@" byte matches inside TIFF image data are not text) |
| Ancillary docx | Title page, cover letter, declaration each 1 page in soffice. Markers: [TO CONFIRM by J. Ferreira] (name form, affiliation, his CRediT line, supervisor line, AI declaration sign-off), [TO CONFIRM by each author] (funding, competing interests), [TO FILL] (addresses, his ORCID, acknowledgments, date) |
| Sources read 26 Nov 2026 | IHE ITI-55 3.55.5.1 (profiles.ihe.net); EDPB Guidelines 02/2025 v2 paras 32-34, 102-104 (whole PDF searched for "additional information": absent); OJ PDF of Regulation 2025/327 title page ("Text with EEA relevance"). Not reachable: efta.int (bot check), zenodo.org (proxy refused); both left as hand checks |
| Review archive | ../review_code_anonymised.zip unchanged since Rev 2: sha256 957e8b663d714e359e51f221abee231ca0681e6d820c5085eff206b5fb3d2e5f, 42 files, contains sensitivity.py and z3_check.py; identifier grep (thesis, names, institution, handle, ORCID, zenodo) 0 hits |
| Repos | /home/claude/trf-thesis and /home/claude/trf read only; no commits, no pushes |

## Late fixes after independent QA v0.9.1 (26 Nov 2026)
- [11] EFTA factsheet read in browser (status: under scrutiny for incorporation by Iceland, Liechtenstein and Norway); supervisor's original sentence restored, dated 26 November 2026; access date added.
- [2] GDPR and [7] EPRS checked on EUR-Lex and europarl; dates added.
- Title page: postal address (P.O. Box 2110, 6402 Molde, from the institution's fact sheet), acknowledgment of Helsedirektoratet's written answer of 19 October 2026; remaining markers are only for J. Ferreira; cover letter date filled on submission.
- Fig. 3 row label moved off the first gridline.
- Zenodo 1.3.3 (record 24562862) is built from commit 6b0b381, which contains sensitivity.py and docs/expected_sensitivity_output.txt (git ls-tree).
- build.sh rerun: build OK, gate 49/49, 17 references in both PDFs, no em or en dashes.

## v0.9.2a (26 Nov 2026)

Build OK, gate 49 checks 0 mismatches. 39 references, cited set equals 1 to 39, first appearances in order; both PDFs list [1] to [39] in sequence. No U+2010 to U+2015 in sources, docx text or PDF text except U+2212 minus signs inside formulas (as before). Anonymity grep (abbasia, arshad, ferreira, molde, astheno, zenodo, 24562862, thesis) on manuscript.md, both .tex, both PDFs, Manuscript_anonymised.docx: no hit. Earlier lines of this file that say 17 references refer to v0.9.1.
