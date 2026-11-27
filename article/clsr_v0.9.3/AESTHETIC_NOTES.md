# Aesthetic and typographic notes (print and Word)

## What changed
1. Listing 1 (raw Python, boxed, monospace) became Algorithm 1, standard pseudocode: Input and Output header, ten numbered lines, bold keywords (if, then, return), mathematical notation matching Section 3 (x(t), c(P), iota, iota_J, s). No comments were needed, so none are shown. The caption states it is a faithful transcription of V_II, trf_checker.py lines 305 to 318, and defines every symbol against the code identifier. It adds no check that the code does not perform; the called function integrity(rec) is named, not expanded.
2. LaTeX: algorithm* (float) plus algpseudocode (algorithmicx), booktabs-weight rules (0.8 pt top and bottom, 0.5 pt under the caption), no box, no monospace, small size, caption in the same size as figure and table captions. Compiles with pdflatex and xelatex.
3. Word: real paragraphs, no table, no text box. Styles Alg Title, Alg Head, Alg L0, Alg L1 and End variants. Numbered lines with tab stops, Times New Roman text, Word equation objects (Cambria Math) for maths, bold keywords, 1 pt top and bottom rules, thin rule under the caption, no shading. Algorithm lines are excluded from Word line numbering so the two numberings do not collide.
4. Word manuscript: Times New Roman 12 pt, 1.5 spacing, numbered headings (bold, bold italic), 10 pt captions with bold label, table rules reduced to booktabs weights (1 pt top and bottom, 0.5 pt under the header, no verticals, no shading), 10 pt air after each table, continuous line numbers (was restarting each page), centred page numbers, widow and orphan control on body styles, keep with next on headings, table captions and figures, keep together on captions.
5. LaTeX two-column preview: microtype, flushend (balanced last page), URLs in the text face instead of Courier, Fig. 1 single column, Figs. 2 and 3 and tables full width (unchanged).
6. Named preview: author_only/Preview_two_column_NAMED.pdf from the same source, built by `./build.sh named`, kept in a separate folder. The build fails if a name or the preview footer appears in either anonymised PDF. The docx and anonymised PDFs remain anonymous.
7. concordance_gate.py: the Listing 1 verbatim check is replaced by a line-by-line mapping check (anchors, quoted strings, full coverage of code lines 309 to 318, no line mapped twice); it regenerates ALGORITHM_MAPPING.md.

## Impeccable checks (print adaptation)
- Typography: one serif family throughout, one scale (12, 10.5, 10 pt in Word; text, small, footnotesize in LaTeX); bold only for keywords and labels, italics only for variables; true quotation marks.
- No em or en dashes introduced; hyphens only in ranges that are source line labels.
- No decoration: no box, shading, colour, icons or ornamental rules; hierarchy by rule weight and indent alone.
- Contrast and measure: black on white, lines under 100 characters in the single column layout, algorithm fits one line per statement.
- Rendered and inspected at 80 dpi: Word (via soffice) algorithm page and Table 2 page, two-column preview pages 1, 7 and 10, review PDF algorithm page, named preview pages 1 and 10.

## Known limits
- LibreOffice renders Word equation objects with wide delimiter spacing in the Word algorithm; Word itself was not available to check. Content is unaffected.
- The ead e-mail line of elsarticle in the named preview is set in the class's monospace face.
