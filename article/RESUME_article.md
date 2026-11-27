# Article workstream (CLSR first) - resume log

Draft: Auditing-After-Erasure-EHDS.docx (from Prof. Ferreira, uploaded 25 Nov). Notes: Journal-Recommendation-and-Submission-Notes.docx.
Working copies here only. Do NOT push article files to the public TRF-thesis repo; ask Tiger about removing the draft docx from main (not deleted).

## 26 Nov 2026
- Numbers reproduced against trf_checker.py (all match draft): 95 violations / 90 records; 37 cross-border + 53 SPE; request-only 41, ceiling-only 44, both 5; 39 no-request ceiling collisions; 138 invalidations = 52 erasure + 86 ceiling; 94 / 89 at a 3-month response; Table 2 six rows exact.
- Sensitivity script added to TRF repo as R-47 (sensitivity.py, docs/expected_sensitivity_output.txt), local commit 8caaacb, NOT pushed, no new Zenodo version.
- CLSR facts found: normally 6,000-15,000 words; abstract max 250; title page and anonymised manuscript as separate files; double anonymised; AI declaration section titled "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process". Elsevier shop page: CLSR strongly encourages PhD students without their degree not to submit unless the supervisor confirms (applies to PhD, not MSc; confirm with Prof. Ferreira anyway).
- Guide-for-authors page itself could not be fetched; reference style, highlights, CRediT still to confirm on the live guide.
- Draft docx metadata is clean (no creator, no names in text).
- Reference verification: sonnet agent running, output /home/claude/work/article/ref_verification.md.

## Next
1. Read ref_verification.md; fix wrong refs.
2. Opus agent: tracked-changes revision of a copy of the draft (apply: true-by-construction framing, Prop 1 framing, sensitivity script reference, AI declaration, verified citations; lead-with-law as comment only).
3. Anonymised review copy of code (grep Abbasia, Arshad, Molde, HiMolde, Ferreira, Astheno, ORCID, email).
4. Email Tiger -> Prof. Ferreira (co-authorship, order, corresponding author, ChatGPT use, supervisor confirmation).

## 26 Nov 2026 (later)
- Thesis gap check (primary sources in browser): Schneier & Kelsey ACM DL = TISSEC 2(2) 159-176 May 1999 (thesis right); C-413/23 P para 73 on EUR-Lex supports thesis sentence; Rak claim is in the abstract (p.928, pp 928-938); KONFIDO author order matches the IDCS 2019 record; EHDS Art 68(12) and 73(1)(e) wording confirmed on EUR-Lex HTML; recitals mentioning logs are 19, 36, 39 only, none on SPEs; thesis cites D6.3 correctly as TEHDAS2 2026a (separate deliverable), OPR pinpoints under D7.4 correct. Result: no thesis error found. EFTA EEA-Lex behind bot check: Tiger to check by hand.
- CLSR guide read in browser (clsr_guide.txt): Word single column only, two-column only for LaTeX; numbered [n] refs Elsevier style; 1-7 keywords; abstract <=250; figures separate files; research data Option C (deposit + link or statement); AI declaration section exact title; AI may create explanatory diagrams and data visualisations.
- TRF-thesis repo is PUBLIC (gh api, private=false); draft docx sits on main. Ask Tiger.
- AI declaration: Ferreira used ChatGPT; Tiger used Claude, Parallel, K-Dense (skills in Claude).
- Review code archive built (package/review_code*). CLSR package v0.9 being built by opus agent in package/clsr_v0.9/.

## 26 Nov 2026 (v0.9 package build, opus agent)
- [done] Task 1 archive: CHANGE_TRAIL.md removed, prose neutralised (tools/neutralise_archive.py in clsr_v0.9), title out of trf_checker.py docstring, CHECKSUMS regenerated, zip rebuilt, fresh venv 54 passed 2 skipped, both diffs empty, PROOF updated.
- [done] manuscript.md (clsr_v0.9/manuscript.md; body derived by tools/make_manuscript_body.py from pandoc --track-changes=accept of _revised.docx, then call-outs/figures/listing/refs added).
- [done] Figures 1-3 (figures_src/*.py -> Figures/). Next: build/ (reference.docx, filter.lua, templates), build.sh, then title page etc, concordance gate, QA.
- [done] v0.9 package complete in package/clsr_v0.9 (build.sh green, gate 44/44, QA_REPORT.md). Open items in open_comments.md (EFTA [11] by hand, TO CONFIRMs, TRF name, IHE [9], EDPB [14], lead-with-law, Prop numbering).
- CLSR package v0.9 built (package/clsr_v0.9, build.sh), independent QA: PASS WITH FIXES. Applied: [6] and [15] recorded as verified (ref_verification addendum); review archive rev 2 (viewer + repo README removed, thesis wording scrubbed, tests/test_outputs.py, 41 passed, zip 957e8b66...). Not done: cosmetic float gaps in Preview p8 and review PDF p5/p19, Fig 2 low-contrast label. Delivered /home/claude/out/CLSR_package_v0.9.zip.
- 26 Nov late: TRF 1.3.3 released (GitHub release via browser, commit 6b0b381; Zenodo record 24562862, DOI 10.5281/zenodo.24562862). CLSR v0.9.1 built (refs fixed in PDFs, figures redesigned, IHE/EDPB/EFTA/GDPR/EPRS closed, title page filled), independent QA PASS WITH FIXES, fixes applied, gate 49/49. Delivered /home/claude/out/CLSR_package_v0.9.1.zip. Waiting on J. Ferreira items only.
- 27 Nov: v0.9.2 merged (39 refs, 7 keywords, Algorithm 1, named preview, scorecard 52->75). Independent ref QA NOT completed (rate limit): verify 22 new refs before submission. /home/claude/out/CLSR_package_v0.9.2.zip
