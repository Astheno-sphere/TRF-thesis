# Figure design notes, v0.9.1 (26 Nov 2026)

Guidance used: impeccable skill (craft floor: refuse gradients, glow, decorative shadows, rounded-box scaffolds, one-sided bars, unicode-as-icon, monospace as costume; verify by looking at the render at shipping size) and the dataviz skill (form first, colour last; thin marks; solid hairline grids, never dashed; direct labels; no number on every point unless the values are the point; text in text inks; check the anti-pattern list).

## System

| Item | Choice |
|---|---|
| Sizes | Fig. 1 single column, 90 x 64 mm. Figs 2 and 3 double column, 190 mm wide (84 and 64 mm high). Drawn at final size; LaTeX places Fig. 1 at natural width in one column, Figs 2-3 across both columns (scale 0.97 at the 5p text width) |
| Type | Inter, pinned (Montserrat not installed). The OTF (CFF) release caused font-type mismatch warnings in the figure PDFs, so Regular, Italic and SemiBold were converted to TrueType with fontTools and shipped in figures_src/fonts as "InterFig" (SIL OFL 1.1, licence copied); style.py stops if the font is missing, so no fallback face can silently change label widths. Fig. 1: 7 to 7.5 pt. Figs 2-3: 8 to 8.5 pt, so the Word page (160 mm text width, scale 0.84) still prints at 6.7 pt or more. Maths in Inter italic via mathtext; notation copied from the manuscript |
| Palette | Charcoal #1B1C20 ink; oxblood #5E1A21 as the only accent (the deadline, the conflict, "ceiling applies"); greys #55565B (secondary text, 7.4:1 on white), #8A8A8E (fills), #BDBDC0 (hairlines). Gold #C9A23A defined but not used: no element needed a second accent |
| Rules | 0.4 to 0.6 pt solid hairlines; no dashes; no boxes around text; no legend boxes |
| Greyscale / CVD | Identity never rests on hue alone: Fig. 1 rows are grey solid, hatched outline and dark solid, each labelled; Fig. 3 uses filled circle (applies) vs hollow square (excluded) plus direct labels |
| Export | Vector PDF with embedded fonts, PNG 600 dpi, TIFF 1000 dpi; PDF metadata title only |

## Critique against the anti-pattern lists (after iteration)

| Figure | v0.9 problem | v0.9.1 | Iterations |
|---|---|---|---|
| 1 | 190 mm-style layout with left labels; rounded cream callout box with gold border; dashed guides; legend-like row labels at left | 90 mm; row labels sit directly above their rows; conclusion "d <= s + F infeasible" set as oxblood text beside the conflict cells, no box; guides solid hairlines; event values under the axis | 3 renders: (1) guide lines struck through row labels, "month t" collided with tick 20, L label clipped, conflict label carried an unsourced paraphrase; (2) labels given a white knockout, tick label 20 dropped (19 is labelled as s + F), label reduced to "Conflict", canvas extended; (3) re-render in the pinned TrueType font, checked in colour and greyscale; accepted |
| 2 | Four rounded boxes (pill-box scaffold), one cream-filled with gold border; hatched "invalidation entry" with low-contrast oxblood text over hatching (QA finding); long footer sentence | Four columns under hairline heading rules, numbered stages, deadline stage in oxblood; log leaves as plain rectangles, invalidation entry solid oxblood with white text (contrast about 12:1); x(t) and V(t) drawn as two state lines with the deadline d marked, the footer wording kept as their labels | 3 renders: (1) arrow from stage 1 crossed the log heading, auditor arrow detached; (2) heading moved under the log, auditor path made one connected line; deadline tick crossed the V(t) label; (3) tick split to the bars only, accepted |
| 3 | Four lollipop panels with separate x-scales, bottom legend, alpha lines | Dumbbell panels on one shared 0-150 scale; oxblood dot = ceiling applies, hollow square = excluded; direct labels in the last panel where the two marks are furthest apart, no legend; every value printed (the values are the point of Table 2, so the "no number on every point" rule is waived deliberately); coincident zeros drawn as dot inside square | 3 renders: (1) direct labels collided in panel 1, y-axis title clipped, zero marks hid each other; (2) labels moved to panel 4, zero marks nested, title collided; (3) title moved above the rows, accepted |

Values: Fig. 1 parses docs/expected_trf_output.txt (record 100 line and header); Fig. 3 parses docs/expected_sensitivity_output.txt (six rows, seed). No number is typed into either script; the v0.9 footnote "200 synthetic records" was a typed value and is now "Synthetic cohort, seed 20260915" (seed parsed).

Residual: in the internal single-column review PDF (text width 137 mm) Figs 2-3 scale to 0.72, so their smallest text prints at about 5.8 pt there; the uploaded Word file and the journal's 190 mm print are not affected.

Greyscale check (26 Nov, all three PNGs converted to greyscale and inspected): Fig. 1 rows stay distinct (mid grey solid, hatched outline, near-black solid) and are labelled; Fig. 2 event and invalidation entries are both dark but labelled in white; Fig. 3 reads by shape (filled circle vs hollow square) and by the direct labels. Figure PDFs: fonts InterFig Regular/Italic/SemiBold embedded as TrueType subsets; pdftotext and pdffonts report no warnings.
