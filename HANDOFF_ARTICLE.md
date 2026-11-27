# Handoff: journal article (read this first when resuming the paper)

Last updated 28 Nov 2026. Author: Arshad Akhtar Abbasia. Co-author: Prof. João Ferreira.

## State
- Manuscript: **CLSR v0.9.3**, "Auditing After Erasure in the European Health Data Space: Audit Logs, the Right to Erasure and Permit-Based Deletion".
- Source and full package: `article/clsr_v0.9.3/` (single source `manuscript.md`; `bash build.sh` rebuilds docx, PDFs, title page, cover letter, declaration and runs `concordance_gate.py`, 56 checks, must pass).
- Anonymised review code: `article/review_code/` (48 tests pass; README maps every result to its script).
- Code archive: TRF **1.3.4**, version DOI 10.5281/zenodo.24587633, concept DOI 10.5281/zenodo.23819274 (github.com/Astheno-sphere/TRF, tag v1.3.4). The thesis cites 1.3.0 (10.5281/zenodo.23989242).
- Change log: `article/clsr_v0.9.3/CHANGES_v0.9.3.md`. Source check: `SOURCE_CHECK_v0.9.3.md`. Independent QA: `INDEPENDENT_QA_v0.9.3.md`.
- Sent to João 27-28 Nov 2026 (11 files) for approval.

## Open before any submission
1. João approves v0.9.3, the new title and keywords.
2. [TO CONFIRM by J. Ferreira] items on title page, cover letter, declaration (name form, affiliation, ORCID, CRediT, funding/interests, AI statement, "recommends" line).
3. Reference details: [5] author initials, [7] TISSEC volume/issue (ACM DOI 2(2) vs author site 1(3)), [8] pages, [24] EEA-Lex status.
4. Cover letter date on submission day.
5. Ask Hans Löwe Larsen (Helsedirektoratet) permission to cite his 19 Oct 2026 reply as personal communication (draft in session notes; the article survives without it via ref [25], the public privacy notice).

## If retargeting to another journal (João's notes: `Journal-Recommendation-and-Submission-Notes.docx`)
- **International Data Privacy Law** (OUP): first alternative if foregrounding GDPR Art 17 and identifiability. ≤10,000 words incl. footnotes, double-anonymised, **OSCOLA footnotes** (convert numbered refs), abstract.
- **International Journal of Law and Information Technology** (OUP): second alternative. Word/RTF, **abstract ≤150 words** (ours is 179, must cut), **5-10 keywords**, OSCOLA footnotes.
- Work needed for either: citation style conversion (numbered -> OSCOLA footnotes), abstract trim, re-run gate, new cover letter naming the journal, check the journal's AI policy and prior-publication policy (thesis + public draft `Auditing-After-Erasure-EHDS.docx` must be disclosed).

## Rules carried over
- Every number must come from code; gate before delivery. Primary sources only for law. No em dashes. Commits authored by Arshad, Claude as co-author trailer. Nothing public without Arshad's yes.
