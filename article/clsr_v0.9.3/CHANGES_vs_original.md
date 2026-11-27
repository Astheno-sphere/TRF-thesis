# Changes in manuscript v0.9.1 against the supervisor's original

Original: `../../Auditing-After-Erasure-EHDS.docx` (untouched). Tracked-changes view for the supervisor: `../../Auditing-After-Erasure-EHDS_revised.docx` (author Reviewer-Claude, 9 insertions, 5 deletions, 13 comments). That file shows items A1 to A9 only. Items B1 to B15 were made for v0.9 and items C1 to C9 for v0.9.1; they are not in any tracked-changes file, and this list is their record. No number, proposition, proof or argument was changed. Comments are carried into `open_comments.md`, not into the manuscript.

## A. Changes in the tracked `_revised.docx` (accepted into v0.9)

| # | Section | Before | After | Reason |
|---|---|---|---|---|
| A1 | 5.1, end of last paragraph | (no sentence) | "The script sensitivity.py in the code archive (anonymised for review, entry R-47) reproduces the six rows of Table 2." Further changed in v0.9, see B2 | Table 2 had no stated code source |
| A2 | AI declaration | "ChatGPT (OpenAI) assisted in adapting the research for article length, in drafting and restructuring the text, and in checking sources." | Interim text naming Claude, Parallel AI, ChatGPT (if confirmed), K-Dense. Replaced in v0.9, see B3 | Declaration named only ChatGPT while 5.1 names Claude and Parallel AI |
| A3 | Ref [5] | Iñigo | Íñigo | Spelling on the author's institutional portal |
| A4 | Ref [7] | (European Parliament, 2019) | (European Parliamentary Research Service, Scientific Foresight Unit (STOA), 2019) | Issuer as printed on the study |
| A5 | Ref [8] | tables 5.1 and 5.4, especially OPR-17 and OPR-18 | adds "(the one-year minimum and the recommended five years are in OPR-18; the corresponding requirement EHDSR-8 is in table 5.1)" | Retention figures are in OPR-18, not OPR-17 |
| A6 | Ref [10] | Veikart ... 2025-2031, Q3 2026 | Veikart ... 2025-2031, delmål 4C (accessed 26 November 2026) | "Q3 2026" not found on the roadmap |
| A7 | Ref [12] | RFC 6962 (2013), § 2.1 ... | adds "RFC 6962 is obsoleted by RFC 9162." | RFC Editor status |
| A8 | Ref [15] | ... EU:C:2025:645, paras 74-86 | adds "(judgment of 4 September 2025)" | Date missing; verified on EUR-Lex |
| A9 | Ref [17] | [2026] OJ L 2026/2083 | OJ L, 2026/2083, 21.9.2026 | Official OJ citation form |

## B. Changes made only in v0.9 (not in any tracked-changes file)

| # | Section | Before | After | Reason |
|---|---|---|---|---|
| B1 | Whole text | 17 footnotes, OSCOLA-like | Numbered citations [1] to [17] in square brackets before the punctuation, in order of first appearance (order unchanged); reference list after the AI declaration | CLSR reference style |
| B2 | 5.1 | "(anonymised for review, entry R-47)" (from A1) | "supplied as supplementary material (anonymised for review)" | R-47 points to a change trail removed from the review archive; required wording for the code archive |
| B3 | AI declaration | Interim text (A2) | "During the preparation of this work the authors used ChatGPT (OpenAI) to assist with drafting and language editing, Claude (Anthropic) to assist with drafting, source verification, code review and reproduction of the numerical results, and Parallel AI for web research support. Open-source scientific-writing skill instructions (K-Dense) were used within Claude. After using these tools/services, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article." The base's last sentence (pointer to Section 5.1) kept | Text supplied by the authors; ChatGPT use confirmed 26 Nov 2026; final pending Prof. Ferreira's sign-off |
| B4 (superseded by C5) | Data and code availability | ends "An identifying repository citation is withheld during anonymised review." | adds "For review, the materials are provided as the code archive supplied as supplementary material (anonymised for review); the synthetic data and code will be deposited in a public archive, and their persistent identifier will be disclosed after review." (future tense because sensitivity.py is not yet in any archived release) | CLSR research data Option C; anonymity |
| B5 | 2.1, end of para 2 | (no sentence) | "Table 1 summarises the three duties as modelled." | CLSR: every table cited in the text |
| B6 | 3.2, end of anchor paragraph | (no sentence) | "Fig. 1 shows this example." plus Fig. 1 and caption | Figure call-out |
| B7 | 4.1, para 2 | "appends a record of the transition. The" | "appends a record of the transition (Fig. 2). The" plus Fig. 2 and caption | Figure call-out |
| B8 | 5.1, para 2 | "verify against its Merkle log. In this" | "verify against its Merkle log (Listing 1). In this" plus Listing 1 (verbatim `V_II`, trf_checker.py lines 305-318) and caption | One code listing showing the invalidation check |
| B9 | 5.2, end of para 3 | (no sentence) | "Fig. 3 plots the six scenarios of Table 2 together with the number of scheduled invalidations." plus Fig. 3 and caption | Figure call-out; Fig. 3 adds the invalidation counts 138 and 60 from sensitivity.py output |
| B10 | Tables 1, 2 | Word tables, caption above as bold paragraph | Editable tables with captions; cell text unchanged; Table 2 numbers checked by concordance_gate.py | CLSR: editable tables |
| B11 | Text and references | en dashes (U+2013) in "record-constraint pair" and in the ranges 17-19, 2025-2031, 32-34, 102-104, 74-86 | hyphens | House rule for this package: no en or em dashes |
| B12 | References, form | Footnote form, author full names, link labels ("Official text.", "Judgment." etc.) | Elsevier numbered form: initials, LTWA journal abbreviations (Eur. J. Risk Regul.; Int. J. Law Inf. Technol.; Comput. Law Secur. Rev.; ACM Trans. Inf. Syst. Secur.; J. Am. Med. Inform. Assoc.), volume (issue) (year) pages, DOI as https URL; link labels dropped, URLs printed | CLSR reference style |
| B13 | References, content added from verification | [3] 15 (4) 928; [6] 2 (2) 159; [15] EU:C:2025:645; [16] 25 (3) 230 | [3] 15 (4) 928-938; [6] 2 (2) (1999) 159-176 (comment on vol/issue resolved: ACM DL, May 1999); [15] ECLI:EU:C:2025:645; [16] 25 (3) 230-238 | Verified page ranges and identifiers (ref_verification.md; ACM DL and EUR-Lex read 26 Nov 2026) |
| B14 | References, URLs and access dates | Footnote hyperlinks, access date only in [10] and [11] | "(accessed 26 November 2026)" added to [1], [2], [8], [9], [14], [15], [12], [17] (pages confirmed on 26 Nov 2026); [10] roadmap link changed from the "regionale-helseforetak" page to the verified 4C page; [12] URL changed from rfc-editor.org/info/rfc6962/ to the verified rfc-editor.org/rfc/rfc6962; [17] URL changed from the Publications Office record to the verified EUR-Lex ELI PDF; [11] keeps "status accessed 25 November 2026"; [7] no access date (official page not confirmed); [3]-[6], [13], [16] DOI only | CLSR: web references need URL and access date |
| B15 | Front matter | "Keywords European Health Data Space, GDPR, ..." | "Keywords:" with the same six keywords separated by semicolons (LaTeX: elsarticle keyword block) | CLSR: 1 to 7 keywords |

## C. Changes made in v0.9.1 (26 Nov 2026)

| # | Section | Before (v0.9) | After (v0.9.1) | Reason |
|---|---|---|---|---|
| C1 | 2.3, IHE paragraph | "In the IHE baseline, the audit message records the patient-discovery query segment in an encoded field." | "In the IHE baseline, the audit messages of both the Initiating and the Responding Gateway record the patient-discovery query segment in an encoded field, and only the Responding Gateway's message also identifies each patient whose demographics it returned." | ITI-55 3.55.5.1 read 26 Nov 2026 (comment 4) |
| C2 | 2.3, EEA sentence | "The European Free Trade Association's register lists the EHDS Regulation as under scrutiny for incorporation into the European Economic Area Agreement as of 25 November 2026 [11]." | "The EHDS Regulation is marked as text with EEA relevance [1], but its incorporation into the European Economic Area Agreement is pending, and its application in Norway depends on that incorporation [11]." | No dated status the authors cannot show; "pending" matches the thesis wording; EEA relevance read on the OJ title (comment 5). Hand check still open |
| C3 | 4.3 | "The final EDPB blockchain guidelines discuss designing for erasure, including effective anonymisation and the role of additional information [14]." | "The final EDPB blockchain guidelines discuss designing for erasure, including planning at the design stage to render personal data anonymous where actual deletion is technically impracticable [14]." | "additional information" is not in the Guidelines; only the unsupported clause replaced, with para 103 (comment 6) |
| C4 | 5.1, end of para 2 | (no sentence) | Output-label sentence: "Proposition 1"/"Proposition 2" = Propositions 1 and 2; "Corollary 1.2" = no-request ceiling collisions (5.2); "Proposition 3" in z3_check.py output = anchor condition after Proposition 1 (3.2); attributed to "a longer formal treatment of the model" | Reviewers running the code see these labels (comment 2) |
| C5 | Data and code availability | "An identifying repository citation is withheld ... will be deposited in a public archive, and their persistent identifier will be disclosed after review." | "The synthetic data and code are archived in a public repository (link withheld for anonymised review; given on the title page). For review, an anonymised copy of the code and synthetic data is supplied as supplementary material." | Decision B: Zenodo 1.3.3 published |
| C6 | Ref [11] | "... 32025r0327> (status accessed 25 November 2026)." | "... 32025r0327>." | Factsheet never read; date removed |
| C7 | Ref [15] | URL .../TXT/PDF/?uri=celex%3A62023CJ0413 | .../TXT/HTML/?uri=CELEX:62023CJ0413 | The URL recorded as verified in ref_verification.md |
| C8 | Figures 1-3 | v0.9 drawings | Redrawn (see FIGURE_DESIGN_NOTES.md); Fig. 1 now 90 mm single column; content, notation and values unchanged; Fig. 3 footnote "200 synthetic records" became "Synthetic cohort, seed 20260915" | Editorial redesign; Fig. 2 label contrast (QA) |
| C9 | Title page, cover letter, declaration (not the manuscript) | Author order [TO CONFIRM]; data "will be deposited"; thesis-disclosure placeholder | AAA first and corresponding, JF second; Zenodo version and concept DOIs; cover letter sentence that the article derives from the first author's MSc thesis and that the manuscript does not cite the thesis, repository or DOI; markers reduced to JF approvals, [TO FILL] facts and per-author declarations | Decisions A to C |

Build only (no text change): references now appear in both PDFs (filter bug), .tex compiles with pdflatex and xelatex, float placement relaxed.

Unchanged on purpose: title; abstract (145 words); every sentence of Sections 1 to 7 other than B5 to B9 and C1 to C4; 'lead with the law' structure (open for JF); model name TRF; the 5.1 sentence on AI use in the underlying study; "Python 3.12".

## v0.9.1 late changes (26 Nov 2026, after browser checks)

| ID | Section | Before (v0.9.1 draft) | After | Reason |
|---|---|---|---|---|
| D1 | 2.3, ref [11] | 'marked as text with EEA relevance [1], but its incorporation ... is pending' | Supervisor's original sentence restored: register lists the Regulation as under scrutiny for incorporation as of 26 November 2026 [11] | EFTA factsheet read 26 Nov; original claim correct, date updated to the check date |
| D2 | ref [2] | no publication date | OJ L 119/1, 4.5.2016 | EUR-Lex HTML read |
| D3 | ref [7] | 2019 | 24 July 2019, accessed 26 November 2026 | europarl Think Tank page read |
| D4 | Fig. 3 | row label 'Primary-use floor' touching first gridline | moved above the row labels, right-aligned | layout |

## E. Changes made in v0.9.2a (26 Nov 2026): reference coverage, keywords, indexability

Scope: references, keywords, abstract wording, three new sentences. No number, proposition, proof, table, figure or result was changed; `concordance_gate.py` passes (49 checks). Basis and checks for every added source: `REFERENCE_AUDIT.md` (internal). Scores and rubric: `INDEXING_SCORECARD.md` (internal).

| # | Section | Before | After | Reason |
|---|---|---|---|---|
| E1 | References | 17 | 39; Elsevier numbered style, renumbered by first appearance by script (keys, then numbers); build.sh now requires 39 | Coverage for CLSR; 22 added, 12 from the thesis bibliography (class a), 10 checked on official pages (class b), see audit |
| E2 | Citation appends (existing sentences) | e.g. "opt-out [5]." | "opt-out [5,6]." and the other appends: Intro (opt-out, audit logging, ledgers, design science, formal specification), 2.1 (HDAB, Art 17(3) exceptions), 2.2 (identifiers removed), 4.2 (RFC 9162; recovery paths), 4.3 (residual identification, recital 26), 6.2 (audit profiles), 6.3 (erasure by unrecoverability) | Each reference sits on a sentence it supports or contrasts; wording of those sentences unchanged |
| E3 | Intro, after the ledger sentence (new sentence 1) | (none) | "Redactable-signature and chameleon-hash schemes instead permit authorised modification of signed or chained content without breaking verification [12,13,14], whereas the design proposed here keeps the log append-only and appends an invalidation entry." (one sentence) | Rival approaches were not discussed; the second sentence restates the existing design (4.1) |
| E4 | 4.3, after the [32] sentence (new sentence 2) | (none) | "The same guidelines advise against registering personal data on a blockchain in clear, encrypted or hashed form and recommend off-chain storage [32], so the design keeps erasable values outside the log (Section 4.1) and treats any commitment or invalidation entry that remains on it as subject to the residual-data assessment above." (one sentence) | Counter-view in the EDPB guidelines para 104 (open comment 10): answered by pointing to the existing rationale, without claiming that commitments are non-personal |
| E5 | 6.2, start of the second paragraph (new sentence 3) | (none) | "In Norway, secondary use is governed in part by the Health Registry Act (helseregisterloven), the Norwegian Institute of Public Health is the designated coordinating health data access body, and the Directorate of Health's gap analysis found no approved secure processing environment with solutions for control and activity logging as of 11 April 2025 [38,39]." (one sentence) | Norwegian legal setting. Helsedataservice is not named as HDAB because the FHI page names FHI; pasientjournalloven not cited (no section read) |
| E6 | Abstract | "The European Health Data Space requires identifiable logs for auditing secure processing environments ... The General Data Protection Regulation can also require erasure of particular fields. This article models when these constraints collide and proposes a way to preserve audit evidence after erasure." | "The European Health Data Space (EHDS) requires identifiable audit logs for secure processing environments ... The General Data Protection Regulation (GDPR) can also require erasure of particular fields under the right to erasure. This article models when these data retention and deletion constraints collide and proposes a way to preserve audit evidence after cryptographic erasure." | Search terms in the abstract; claims and numbers unchanged; 157 words (was 145 per C-list; limit 250) |
| E7 | Keywords | European Health Data Space; GDPR; right to erasure; audit logs; secure processing environments; cryptographic erasure | EHDS; GDPR; right to erasure; audit log; secure processing environment; cryptographic erasure; data retention | Title duplicate removed, singular forms, 7 of 7; see scorecard |
| E8 | build.sh | `-ge 17` | `-ge 39` | New reference count |
| E9 | concordance.md | old numbers | section 3 renumbered; two rows added | Numbering |

Old to new numbering (existing references):

| Old | New |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 7 |
| 7 | 9 |
| 8 | 21 |
| 9 | 22 |
| 10 | 23 |
| 11 | 24 |
| 12 | 25 |
| 13 | 29 |
| 14 | 32 |
| 15 | 33 |
| 16 | 34 |
| 17 | 37 |

New references (new number, source):

| New | Source |
|---|---|
| 6 | Martani et al 2026 (Health Policy) |
| 8 | Crosby, Wallach 2009 |
| 10 | Finck 2018 (EDPL) |
| 11 | Politou et al 2021 |
| 12 | Ateniese et al 2017 |
| 13 | Ateniese et al 2005 |
| 14 | Johnson et al 2002 |
| 15 | Hevner et al 2004 |
| 16 | Feng et al 2023 |
| 17 | Petrocnik 2025 |
| 18 | EDPB CEF report on erasure (2026) |
| 19 | Art 29 WP Opinion 05/2014 |
| 20 | EDPB Guidelines 02/2026 (draft) |
| 26 | RFC 9162 |
| 27 | Reardon et al 2013 |
| 28 | Boneh, Lipton 1996 |
| 30 | EDPB Guidelines 01/2025 (consultation version) |
| 31 | Breyer C-582/14 |
| 35 | IHE ATNA |
| 36 | ISO 27789:2021 |
| 38 | Helsedirektoratet gap analysis (Apr 2025) |
| 39 | FHI role in EHDS (Oct 2026) |

Notes: (i) in-text numbers 5, 7 and 9 now sit beside new numbers in multi-cites. (ii) Not changed: title, model name, section structure, all numbers, Table 1, Table 2, Figures 1 to 3, Listing 1, AI declaration. (iii) The old pointers in earlier sections of this file and in open_comments.md, QA_REPORT.md and ref_verification.md use the old numbers.
