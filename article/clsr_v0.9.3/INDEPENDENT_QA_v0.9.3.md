# Independent QA, v0.9.3 (read-only; line numbers refer to manuscript.md)

Verified: trf_checker.py, sensitivity.py, sensitivity_secondary.py reproduce docs/expected_*.txt byte for byte; pytest 48 passed. Algorithm 1 matches trf_checker.py lines 305-318. Fig. 1 and Fig. 3 values match the outputs.

## 1. Numbers: all correct
Abstract (53/100, nine), 5.2 (9+49-5=53; 58 pairs; 60-month 100/122/22; 95/90; 37+53; 41+44+5=90; 39 subset of 44; 138=52+86; half-open 86/83, 49->41, "eight"; delta=3 94/89), Table 2 (all six rows; 95-49=46; 90-46=44), 5.1 parameters (seed, 0.40, 1-130, 0.25, 1-18, 17 labels, 4-6 expiry months), Fig. 1 (s=7, e=10, d=16, W=7..19) all agree. Abstract is 179 words; 7 keywords. No highlights requirement in clsr_guide.txt. AI declaration is a section before references (line 803). No em dashes in manuscript.md, PDFs, cover letter or title page.
Citations: [1]-[40] all cited, first-appearance order is strictly 1..40, [25] is the Helsedirektoratet privacy notice and is used for exactly that at line 230; numbering after [25] consistent.

## BLOCKER (submission cannot go out as is)
B1. Title_page.docx and Cover_letter.docx still carry placeholders: version DOI "[... TO INSERT AFTER ZENODO ARCHIVES IT]"; cover letter date "[TO FILL on submission]"; eight "[TO CONFIRM by J. Ferreira]" items (name form, affiliation, ORCID, CRediT, funding, competing interest, AI-section sign-off, supervisor recommendation). The cover letter states "All authors have approved the submission" and that the second author "recommends it for publication" while those are unconfirmed. Fix: obtain confirmations, fill, or delete the two unconfirmed sentences until confirmed.

## SHOULD-FIX
S1. Table numbering out of order. Table 3 (lines 361, 369) is cited and appears before Table 2 (first cited line 571, placed 592). Elsevier numbers by order of appearance. Fix: swap labels (current Table 3 -> Table 2, current Table 2 -> Table 3) in text, captions, line 571, 618, 730, Fig. 3 caption, cover/title references, concordance.
S2. Table 3 rows 3-4 (lines 375-376) overclaim against Section 4.1. Line 409-413 requires hiding commitments with independent secret openings; with openings destroyed, a commitment to the executed rule cannot be compared with a separately made commitment to the approved rule, and "released output equals approved output" cannot be shown once the output content is gone unless a copy or plain digest survives. Fix: state that the approval entry and execution/release record reference the same commitment object, or use a plain digest for non-personal rule category and non-personal output (permitted since not erased), and say what an auditor can and cannot verify against the artefact actually released. Adjust "Still established" wording in rows 3-4 and the matching acceptance tests (line 730).
S3. Table 3 and acceptance tests are not exercised by the sandbox (no approval, execution or release records in trf_checker.py). Add one sentence at line 361-367 or 5.2/line 630: "Table 3 is a design specification; the sandbox does not model approval, execution or release records." Otherwise abstract "design satisfied the modelled checks" can be read as covering Table 3.
S4. Line 230: "In correspondence reported in the underlying study, the Directorate stated ..." has no citable source for reviewers (not in references; thesis not cited). Fix: add reference "Helsedirektoratet, written communication, 19 October 2026" (anonymisation-neutral) or delete the sentence and rely on [25]. Title page acknowledgement already names the date.
S5. Line 712: "Health Registry Act (helseregisterloven)" governing secondary use has no support in [39,40] per SOURCE_CHECK (those cover the SPE gap and FHI designation only). Fix: cite the Act, or remove. Also line 712 gap finding is 19 months old; add "(the most recent assessment located)".
S6. Line 730 and 6.2: Article 73(3) "including third-party audits" is stronger than the text ("which may be by third parties" per SOURCE_CHECK). Fix: "regular audits, which may be carried out by third parties".
S7. Reference scope notes incomplete: [1] (line 818) omits arts 14, 61, 66 though cited for 14(1), 61(3), 66(3); [2] (line 820) omits art 11, cited at line 107-110 for 11(2). Add them.
S8. Anonymisation, review_code/docs: Appendix_A.md and VERSION_RECORD.md are thesis documents ("Chapters 1-7", "Chapter 4 Section 4.9", "Tables 5.3", politiregisterloven chapters, "this study", release "1.3.0", dated repository publication 23 Sept 2026, app.py/test_app.py not in the archive). They expose thesis structure, mismatch the manuscript (four propositions, eleven-page viewer, version 1.3.0 vs title page 1.3.4) and contradict README_REVIEW.md. Fix: remove both from the review copy or replace with a short Appendix mapping manuscript sections to scripts.
S9. review_code/CHECKSUMS.md is stale: sensitivity_secondary.py, tests/test_sensitivity_secondary.py and docs/expected_secondary_output.txt are unlisted. Regenerate after S8.
S10. Line 524 vs 803-813: 5.1 discloses only Claude and Parallel AI; the declaration also lists ChatGPT and K-Dense. Fix: delete the tool sentence from 5.1 (declaration is the Elsevier-prescribed place) or make both lists identical.

## NIT
N1. Line 223 "Norway's MyHealth@EU pilot": source [23] describes a project ending end 2025; use "pilot project (2023-2025)" or past tense. [24] status (line 227) was not verifiable in SOURCE_CHECK; re-open once before submission.
N2. Line 603: orphan sentence after Table 2; move to 5.2 first paragraph or Table 2 note.
N3. Line 605: half-open convention also removes one request pair (46->45); text attributes the whole difference (95->86) implicitly to ceiling. Add "(and one request-related pair)".
N4. Abstract does not flag that the nine (and the request part of 53) rest on the every-request-applies upper bound (line 119, 507-509). Add "upper bound" or "assuming every request applies".
N5. README_REVIEW.md says Python 3.11+ (tested 3.13); line 552 says 3.12. Align.
N6. Row 2 of Table 3 ("Who approved") establishes only the approver role, not identity; reword to "which role approved".
N7. Keywords include several multiword terms (guide discourages); acceptable but "erasure", "audit log" could be shortened.
N8. Line 520 and 6.1: section ordering fine; nothing contradicting 2.1/2.3/5.1/5.2/6.1/6.2 otherwise found. 60-month arithmetic (max deadline s+18 <= s+60) is correct under closed and half-open conventions.

## Anonymisation grep result
manuscript.md, both PDFs, all three docx cores (author, lastModifiedBy empty), Figures: no names, institution, Zenodo/GitHub, thesis title. Only hits are review_code/docs (S8) and GitHub URLs for the public Synthea jar (harmless). "the underlying study" phrasing present as intended.
