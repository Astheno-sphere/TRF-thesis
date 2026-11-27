# v0.9.3 change trail (27 Nov 2026)
Base: João's round-2 source (= our v0.9.2 + his round-1 edits). His round-2 notes described changes absent from that file; implemented here and verified.
- Intro: two-queries / same-aggregate audit question.
- 2.1: identification condition (GDPR Art 11(2), EHDS Arts 66(3), 61(3)); request counts stated as upper bound.
- 2.3: Helsedirektoratet privacy notice [25] (six years, health-professional log fields, Art 6(1)(c) + pasientjournalloven s.22, Hdir controller, NHN processor); thesis correspondence (Appendix D, 19 Oct 2026) as support; 72 months = illustrative payload comparison.
- 3.3: new Table 3 (what survives erasure in one permit investigation).
- 4.3: EDPS v SRB reworded (recipient's means); EDPB blockchain paras 32-34 support commitment design.
- 5.1: unit = access event; 17 permit labels, 4-6 expiry months each; sensitivity_secondary.py.
- 5.2: leads with secondary-use results; 60-month floor (100/122, 22/22) stated as parameter property.
- 6.1/6.2: Art 73(2) non-personal downloads; two acceptance tests (cohort selection, output release).
- Refs: 39 -> 40 (new [25], 25-39 renumbered); [31] ECLI added.
- Gate: abstract patterns updated; 9 new checks from expected_secondary_output.txt; 56/56 pass.
- review_code: + sensitivity_secondary.py, test, docs/expected_secondary_output.txt (48 tests pass).
- Cover letter rewritten to final text; draft disclosure verified (Auditing-After-Erasure-EHDS.docx on TRF-thesis main).
- Title page: version DOI placeholder pending TRF 1.3.4 release.
Open: [5] author initials, [7] TISSEC vol/issue (ACM DOI says 2(2); author site 1(3)), [8] pages, [24] EEA-Lex status unverified this round.
## QA round (independent agent, INDEPENDENT_QA_v0.9.3.md)
- S1 tables renumbered by appearance (audit table = Table 2, sensitivity = Table 3). S2/S3 Table 2 rows now use formula/digest (comparable after erasure), caption marks it design-only. S4 Hdir reply cited as personal communication. S5 Health Registry Act clause dropped. S6 Art 73(3) "may be carried out by third parties". S7 ref [1]/[2] article lists. S8 thesis docs removed from review_code. S9 CHECKSUMS regenerated (37 files). S10 5.1 AI tools aligned.
- B1 open: version DOI (needs 1.3.4 release), cover-letter date, 8 [TO CONFIRM by J. Ferreira] items.
- Gate 56/56, review_code 48 tests, zip sha256 9388522b....
- TRF 1.3.4 released 27 Nov 2026: version DOI 10.5281/zenodo.24587633 now on title page.
- Title: added subtitle "Audit Logs, the Right to Erasure and Permit-Based Deletion" (manuscript, title page, cover letter, declaration).
- Keywords: replaced terms already in the title/abstract (EHDS, GDPR, right to erasure, audit log, data retention) with complementary indexed terms: secondary use of health data; secure processing environment; health data access body; GDPR Article 17; cryptographic erasure; tamper-evident logging; data minimisation. Gate 56/56.
