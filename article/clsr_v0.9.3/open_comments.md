# Open comments for the authors (v0.9.1, 26 Nov 2026; items 29 to 34 added for v0.9.2a)

Numbering note: reference numbers quoted in items 1 to 28 are the v0.9.1 numbers. v0.9.2a has 39 references; the old-to-new table is in CHANGES_vs_original.md section E (old [11] EFTA is now [24], old [14] EDPB is now [32], old [9] IHE is now [22], old [6] is now [7], old [7] is now [9]).

Source: the 13 comments in `Auditing-After-Erasure-EHDS_revised.docx` (ids 0 to 12) plus items raised while building v0.9 and v0.9.1. Status: OPEN needs a decision or a check by hand (owner named); RESOLVED is kept for the trail. Owners: AAA = Arshad Akhtar Abbasia (first, corresponding author); JF = João Ferreira (second author).

Markers left in the files: `[TO CONFIRM by J. Ferreira]` (his approval), `[TO CONFIRM by each author]` (funding, competing interests), `[TO FILL]` (facts still missing). All must be gone before upload. The anonymised manuscript carries no markers.

## Must settle before submission

| # | Item | Status | Owner | What to do |
|---|---|---|---|---|
| 1 | Ref [11] EFTA EEA-Lex (comment 5) | RESOLVED 26 Nov | - | Factsheet read in browser 26 Nov 2026: legal status 'under scrutiny for incorporation into the EEA Agreement by Iceland, Liechtenstein and Norway'. Supervisor's original sentence restored with the date 26 November 2026; access date added to [11] |
| 2 | AI declaration | RESOLVED for AAA; sign-off OPEN | JF | Decision C: text confirmed by AAA (Ferreira used ChatGPT; Abbasia used Claude and Parallel AI; K-Dense skills within Claude). Cover letter carries "[TO CONFIRM by J. Ferreira: sign-off of that section]". Keep the exact section title if he edits it |
| 3 | Author order and corresponding author | RESOLVED (decision C, 26 Nov) | | AAA first and corresponding, JF second; title page and cover letter updated; Editorial Manager order must match |
| 4 | Title page items | PARTLY OPEN | JF / AAA | JF: name form, affiliation, his CRediT line. AAA: postal addresses of affiliation and corresponding author, JF ORCID (ask him), acknowledgments ([TO FILL]); funding and competing interests ([TO CONFIRM by each author]) |
| 5 | Cover letter | PARTLY OPEN | JF / AAA | Thesis-derivation sentence for the editor added (decision A). JF: supervisor-recommends line, AI declaration sign-off, name form, affiliation. AAA: date on submission |
| 6 | Model name "TRF" and file names as anonymity risk (comment 3) | RESOLVED (decision A, 26 Nov) | | Name kept: "Tri-Lateral Retention Feasibility (TRF) model" (hyphenation as in the thesis; the thesis capitalises "Model", the article keeps lower-case "model" as the authors wrote it). The manuscript does not cite the thesis, its repository or the code DOI; the cover letter tells the editor (not reviewers) that the article derives from the MSc thesis. Residual: name, file names and seed are searchable |
| 7 | Public thesis repository holds the draft article docx | OPEN | AAA | Not settled by decision A. Prior-dissemination and anonymity risk. Decide whether to remove the draft from the repository (do not rewrite history without deciding) |
| 8 | Data and code disclosure | RESOLVED (decision B, 26 Nov) | | Zenodo release 1.3.3 (includes sensitivity.py) published 26 Nov 2026 per the coordinator: version DOI 10.5281/zenodo.24562862, concept DOI 10.5281/zenodo.23819274. Manuscript: "are archived in a public repository (link withheld for anonymised review; given on the title page)"; no DOI in any anonymised file (grep clean). Title page carries both DOIs. zenodo.org was blocked by the proxy, so the DOIs were not resolved from here. Local corroboration (read only): the code repository's latest commit is 6b0b381 "R-48: release 1.3.3 (sensitivity script archived; metadata)", CITATION.cff and .zenodo.json say version 1.3.3 and name concept DOI 10.5281/zenodo.23819274. Open both DOIs once before upload. The review archive (Rev 2) is not byte-identical to the Zenodo release (viewer and README removed, one printed line reworded), so the manuscript says "an anonymised copy", not "the same materials" |
| 9 | Ref [9] IHE ITI-55 (comment 4) | RESOLVED 26 Nov | | profiles.ihe.net ITI-55, 3.55.5.1 read 26 Nov 2026: both the Initiating and the Responding Gateway audit messages carry the base64 QueryByParameter in ParticipantObjectQuery; only the Responding Gateway message has Patient participant objects (0..n, patient ID in HL7 CX, one per patient whose demographics were returned); Initiating: "No patient identifiers are included in this audit message." 2.3 reworded to name both actors |
| 10 | Ref [14] EDPB (comment 6) | RESOLVED 26 Nov | | Guidelines 02/2025 v2 read 26 Nov 2026: "additional information" appears nowhere in the document. 4.3 keeps the sentence and drops only the unsupported clause: "discuss designing for erasure, including planning at the design stage to render personal data anonymous where actual deletion is technically impracticable [14]" (para 103; paras 102-104 cover erasure by design). Note for the authors: para 104 advises against putting personal data on a blockchain in clear, encrypted or hashed form; the article's append-only log holds commitments, so a reviewer may raise it. No text added on this (would be a new argument) |
| 11 | "Lead with the law" (comment 1) | OPEN, option kept | JF | Structural choice for JF: open the Introduction with the Art 68(12) / Art 73(1)(e) tension, then the SPE scenario and the model. Text unchanged |
| 12 | Proposition numbering vs checker labels (comment 2) | RESOLVED 26 Nov | | One sentence added at the end of the AI/reproduction paragraph in 5.1: output labels follow "a longer formal treatment of the model"; "Proposition 1/2" = Propositions 1/2; "Corollary 1.2" = no-request ceiling collisions (5.2); "Proposition 3" in z3_check.py output = the anchor condition after Proposition 1 (3.2). Mapping from concordance.md and the recorded outputs; thesis not named |

## Should check

| # | Item | Status | Owner | Note |
|---|---|---|---|---|
| 13 | Ref [1] (comment 9) | MOSTLY RESOLVED | AAA | Art 68(12), 73(1)(e), recitals verified on EUR-Lex HTML; title "(Text with EEA relevance)" read on the OJ PDF copy. Art 2(2) not read on EUR-Lex; OJ date not printed in [1] |
| 14 | Ref [2] GDPR | RESOLVED 26 Nov | - | EUR-Lex HTML (CELEX 32016R0679, OJ L 119, 4.5.2016) read: recital 26, art 4(15), arts 5, 12, 17, 18, 19 headings and text present as cited; publication date added |
| 15 | Ref [15] | URL FIXED; pinpoint OPTION | AAA | URL changed to the EUR-Lex HTML (CELEX:62023CJ0413), the URL recorded as verified in ref_verification.md (INDEPENDENT_QA fix a). Option: add para 73 |
| 16 | Ref [7] | RESOLVED 26 Nov | - | europarl.europa.eu Think Tank page EPRS_STU(2019)634445 opened: 'Blockchain and the General Data Protection Regulation', Study, 24 July 2019; date and access date added |
| 17 | LTWA abbreviations | CHECK | AAA | Not run through the LTWA tool |
| 18 | Ref [16] | CHECK | AAA | "et al." kept; all ten authors not verified |
| 19 | Notes inside references [8], [12] | CHECK | copy editor | Kept as in the base |
| 20 | Ref [10] combines two documents | CHECK | copy editor | Split if asked |
| 21 | Python version | NOTE | | Text says 3.12; reproduction ran 3.13.18 with identical output |
| 22 | Highlights | CHECK | AAA | Check the Editorial Manager form; not written |
| 23 | Word count | NOTE | | See QA_REPORT.md; near the 6,000 lower bound |
| 24 | First author is a student | NOTE | | Supervisor line in the cover letter [TO CONFIRM by J. Ferreira] |
| 25 | Review archive residual "thesis" hits | RESOLVED 26 Nov | | Rev 2 zip sha256 957e8b66...2e5f; re-checked 26 Nov (v0.9.1): no thesis/name/ORCID/zenodo hits |
| 26 | LaTeX sources | RESOLVED 26 Nov (v0.9.1) | | Template now compiles with pdflatex (iftex switch: T1, mathptmx, helvet, courier) and with xelatex; both PDFs are built with pdflatex. Word route stays the recommended upload |
| 27 | [6] ACM DL check (INDEPENDENT_QA fix b) | CHECK | AAA | CHANGES calls 2(2) 159-176 "ACM DL read"; ref_verification says not confirmed. Open doi 10.1145/317087.317089 once |
| 28 | Missing references in PDFs | RESOLVED 26 Nov (v0.9.1) | | Cause: Lua filter truncated the reference list to [1] (table.unpack mid-constructor). Now a thebibliography with 17 bibitems; build.sh fails if a PDF has fewer than 17 |

## Resolved earlier (v0.9)

| Comment | Item | Resolution |
|---|---|---|
| 0 | Title page | Title_page.docx created |
| 7 | sensitivity.py / R-47 | Script in the anonymised archive and in Zenodo 1.3.3; R-47 removed |
| 8 | AI declaration | Replaced with the authors' text (see 2) |
| 10 | Ref [6] | TISSEC 2(2), 159-176, May 1999 (see 27) |
| 11 | Ref [8] | Pinpoint corrected (A5) |
| 12 | Ref [10] | "Q3 2026" replaced; roadmap link to the 4C page |
| 29 | New references (v0.9.2a) | CHECK | AAA, JF | 22 added; basis in REFERENCE_AUDIT.md (internal). Class (a) items were taken from the thesis bibliography and their DOIs were not re-resolved (doi.org blocked from the sandbox). Open each DOI once |
| 30 | [30] EDPB Guidelines 01/2025 pseudonymisation | CHECK | AAA | Cited as the version for public consultation (adopted 16 Jan 2025, para 22 read). One listing page suggested a final version exists; the consultation page lists only v1. Replace with the final version and its paragraph if it exists |
| 31 | [20] EDPB Guidelines 02/2026 anonymisation | NOTE | AAA | v1.0, adopted 7 July 2026, consultation open to 30 Oct 2026; update if a final version appears before submission |
| 32 | [31] Breyer C-582/14 | CHECK | AAA | Official pages read give case, parties and date only; no ECLI or paragraph number is printed. Add ECLI and paras from EUR-Lex by hand if wanted |
| 33 | LTWA abbreviations of new references (comment 17) | CHECK | AAA | Eur. Data Prot. Law Rev.; IEEE Trans. Emerg. Top. Comput.; MIS Q.; Health Policy; Lect. Notes Comput. Sci.; Proc. 18th USENIX Secur. Symp. not run through the LTWA tool. Crosby-Wallach and Boneh-Lipton page ranges are from the thesis bibliography; the USENIX pages read did not print pages |
| 34 | Norwegian sentence in 6.2 (new sentence 3) | CHECK | JF | Names FHI as designated coordinating HDAB (FHI page of 19 Oct 2026). Helsedataservice is not named as HDAB; pasientjournalloven and Normen not cited (not read). The Ministry's draft implementing law (consultation closed 28 Sep 2026 per the FHI page) is not mentioned |
| 35 | Controlled vocabularies | OPEN | AAA | MeSH, EuroVoc and ACM CCS checks not completed (session limit); see INDEXING_SCORECARD.md section 3 |
| 36 | Titles | OPEN | AAA, JF | Three title options in INDEXING_SCORECARD.md section 4; none applied |
