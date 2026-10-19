# P84 — two confirmations from Tiger (20 Oct). (1) Ch7 §7.4 enquiry sentence: the Datatilsynet send
# date (23 Sept 2026) is confirmed correct and kept; the stale clause saying the Helsedirektoratet
# enquiry "was likewise unanswered" is corrected — it was answered 19 Oct 2026 and folded into §2.3
# (P83). (2) Front_Matter Declaration, Use-of-AI: name Archify for diagram/figure generation
# (R4-C2 / R3-AI), which HiMolde permits. Both are factual-accuracy edits; no claim removed.
EDITS = [
 dict(id='P84-01', file='Chapter7_Conclusion_v1.md',
   old=r"""The enquiry to Datatilsynet on the GDPR-side questions was sent on 23 September 2026; no response had been received at the time of submission, and the parallel enquiry to Helsedirektoratet on the ten-year floor was likewise unanswered.""",
   new=r"""The enquiry to Datatilsynet on the GDPR-side questions was sent on 23 September 2026; no response had been received at the time of submission. The parallel enquiry to Helsedirektoratet on the audit-retention floor was answered on 19 October 2026, and its substance is incorporated in Chapter 2, Section 2.3.""",
   why="factual update: Datatilsynet send date confirmed (23 Sept 2026); Helsedirektoratet enquiry now answered (19 Oct 2026, folded into §2.3 via P83) — corrects the stale 'unanswered' clause"),
 dict(id='P84-02', file='Front_Matter_v1.md',
   old=r"""for drafting and redrafting prose to the author's direction, and for writing the Python code in Appendix A. All design decisions, the model's formulation, the interpretive legal arguments, and the acceptance or rejection of every suggestion are the author's own, and the author is answerable for the whole.""",
   new=r"""for drafting and redrafting prose to the author's direction, and for writing the Python code in Appendix A; Archify was used to generate the thesis's diagrams and figures. All design decisions, the model's formulation, the interpretive legal arguments, and the acceptance or rejection of every suggestion are the author's own, and the author is answerable for the whole.""",
   why="R4-C2/R3-AI: name Archify (diagram/figure tool) in the Use-of-AI declaration, per HiMolde's permitted use"),
]
LOST_OK = []
