# P77 — structural move (Tiger-approved). Relocate the §2.1.6 prospective Boolean-search protocol
# table (B1-B6 + filters) out of Chapter 2 into Appendix B, where this replication apparatus belongs.
# §2.1.6 keeps its methodological point (a prospective protocol exists; it was NOT the instrument
# used) and now points to Appendix B. Nothing in the thesis references B1-B6 outside §2.1.6, and the
# "Section 2.1.6 provides that protocol" pointer at §2.1.1 still resolves. Zero value lost: the table
# is verbatim preserved, only moved. Reduces Ch2 BODY (Appendix B is not counted in the chapter body).
EDITS = [
 dict(id='P77-01', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""The following strings are offered so that a researcher may test this review's conclusions against a systematic sweep of indexed databases. They were not the instrument used here, and are stated prospectively.

| # | Target | String |
|---|---|---|
| B1 | Scopus, Web of Science | `TITLE-ABS-KEY(("crypto-shredding" OR "cryptographic erasure" OR "crypto erasure" OR "secure deletion" OR "data sanitization") AND ("GDPR" OR "right to erasure" OR "right to be forgotten"))` |
| B2 | Scopus, IEEE Xplore | `TITLE-ABS-KEY(("audit log" OR "audit trail" OR "access log") AND ("retention" OR "retention period") AND ("erasure" OR "deletion") AND ("conflict" OR "tension" OR "reconcil*"))` |
| B3 | Scopus, PubMed | `TITLE-ABS-KEY(("European Health Data Space" OR "EHDS" OR "MyHealth@EU" OR "eHDSI") AND ("secure processing environment" OR "audit" OR "retention" OR "erasure"))` |
| B4 | Scopus, IEEE Xplore, ACM | `TITLE-ABS-KEY(("formal verification" OR "satisfiability" OR "temporal logic" OR "constraint satisfaction") AND ("regulatory compliance" OR "legal compliance" OR "GDPR"))` |
| B5 | Scopus, Web of Science | `TITLE-ABS-KEY(("health data" OR "electronic health record") AND ("cross-border" OR "cross border") AND ("privacy" OR "data protection") AND ("Norway" OR "Nordic" OR "EEA"))` |
| B6 | IACR ePrint, arXiv | `("certified deletion" OR "proof of secure erasure" OR "provable deletion") AND ("verifiab*" OR "attestation")` |

Filters for replication: publication years 2018 to 2026 for B1, B2, B4 and B6; unrestricted for B3 and B5, since the relevant regulatory material predates the window. Document types: articles, conference papers, reviews, and preprints. Languages: English and Norwegian.""",
   new=r"""A prospective Boolean protocol, offered so that a researcher may test this review's conclusions against a systematic sweep of indexed databases, is set out in Appendix B (Table B.1). It was not the instrument used here, and is stated prospectively.""",
   why="structural move: relocate the B1-B6 protocol table + filters to Appendix B; keep the §2.1.6 methodological point + pointer"),
 dict(id='P77-02', file='Appendix_B_Search_Log.md',
   old=r"""The closest prior art, the DePaul retention-and-purging programme and United States Patent 12,425,209, was located during the adversarial round 4 through patent-database searching, which sits outside the query tooling this log records. That search is noted here rather than omitted, because a log claiming completeness while containing no query capable of finding the most important prior-art item in the review would misrepresent itself.""",
   new=r"""The closest prior art, the DePaul retention-and-purging programme and United States Patent 12,425,209, was located during the adversarial round 4 through patent-database searching, which sits outside the query tooling this log records. That search is noted here rather than omitted, because a log claiming completeness while containing no query capable of finding the most important prior-art item in the review would misrepresent itself.

## Prospective Boolean protocol for replication

The following strings are offered so that a researcher may test the review's conclusions (Chapter 2, Section 2.1.6) against a systematic sweep of indexed databases. They were not the instrument used in this thesis, and are stated prospectively.

*Table B.1. Prospective Boolean search strings.*

| # | Target | String |
|---|---|---|
| B1 | Scopus, Web of Science | `TITLE-ABS-KEY(("crypto-shredding" OR "cryptographic erasure" OR "crypto erasure" OR "secure deletion" OR "data sanitization") AND ("GDPR" OR "right to erasure" OR "right to be forgotten"))` |
| B2 | Scopus, IEEE Xplore | `TITLE-ABS-KEY(("audit log" OR "audit trail" OR "access log") AND ("retention" OR "retention period") AND ("erasure" OR "deletion") AND ("conflict" OR "tension" OR "reconcil*"))` |
| B3 | Scopus, PubMed | `TITLE-ABS-KEY(("European Health Data Space" OR "EHDS" OR "MyHealth@EU" OR "eHDSI") AND ("secure processing environment" OR "audit" OR "retention" OR "erasure"))` |
| B4 | Scopus, IEEE Xplore, ACM | `TITLE-ABS-KEY(("formal verification" OR "satisfiability" OR "temporal logic" OR "constraint satisfaction") AND ("regulatory compliance" OR "legal compliance" OR "GDPR"))` |
| B5 | Scopus, Web of Science | `TITLE-ABS-KEY(("health data" OR "electronic health record") AND ("cross-border" OR "cross border") AND ("privacy" OR "data protection") AND ("Norway" OR "Nordic" OR "EEA"))` |
| B6 | IACR ePrint, arXiv | `("certified deletion" OR "proof of secure erasure" OR "provable deletion") AND ("verifiab*" OR "attestation")` |

Filters for replication: publication years 2018 to 2026 for B1, B2, B4 and B6; unrestricted for B3 and B5, since the relevant regulatory material predates the window. Document types: articles, conference papers, reviews, and preprints. Languages: English and Norwegian.""",
   why="structural move: receive the B1-B6 protocol table + filters into Appendix B as Table B.1, pointing back to §2.1.6"),
]
# Ch2 loses the two filter-years as numerals; they move verbatim into Appendix B (Table B.1).
# Ch2 also loses the hedge token "preprint" (from "…reviews, and preprints" in the filters line);
# it moves verbatim into Appendix B and "preprint" still occurs elsewhere in Ch2.
LOST_OK = ["number 2018", "number 2026", "hedge preprint"]
