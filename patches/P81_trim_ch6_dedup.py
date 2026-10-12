# P81 — length cut, Ch6 §6.6 + §6.8 (low-value cross-chapter dedup). §6.6 re-describes the Appendix C
# instrument (home: Appendix C + §3.8); §6.8 re-describes the SPUHiN checklist grades (home: §2.6).
# Collapse both to the load-bearing points + pointers. KEPT: §6.6's connection of Q7/A2/O1–O4 to the
# open questions (line 79, untouched); §6.8's timing argument, the dates, and the decisive "no
# reconciliation requirement" gap conclusion.
EDITS = [
 dict(id='P81-01', file='Chapter6_Discussion_v1.md',
   old=r"""An instrument for answering them has been designed and is specified in full in Appendix C. It comprises an eight-person expert panel spanning data protection, health IT architecture, Secure Processing Environment operation, and information logistics, and a session structure in which participants describe current practice before being shown the mechanism. It also comprises a demonstration script that runs the artefact and states its limitations before participants are invited to find them, a semi-structured interview guide, and a sixteen-item closed-response instrument across perceived utility, regulatory alignment, operational viability, and audit integrity.""",
   new=r"""An instrument for answering them has been designed and is specified in full in Appendix C: an eight-person expert panel spanning data protection, health IT architecture, Secure Processing Environment operation, and information logistics, a demonstration-led session structure, a semi-structured interview guide, and a sixteen-item closed-response instrument across perceived utility, regulatory alignment, operational viability, and audit integrity.""",
   why="de-dup: §6.6 re-described the Appendix C instrument (home Appendix C/§3.8); collapse to panel + dimensions + pointer, keep the Q7/A2/O1–O4 connections in the next paragraph"),
 dict(id='P81-02', file='Chapter6_Discussion_v1.md',
   old=r"""The compliance checklists, in the hearing version inspected, address information-security management, identity assurance, and access governance, and the 2024 draft makes identifiable access logs mandatory for at least one year (Chapter 4, Section 4.11). They grade an information-security management system as mandatory and ISO 27001 certification as recommended, and require eID-based authentication at defined assurance levels. No requirement addressing the reconciliation of retention with erasure and deletion appears among them.""",
   new=r"""The compliance checklists, in the hearing version inspected, address information-security management, identity assurance, and access governance, and the 2024 draft makes identifiable access logs mandatory for at least one year (Chapter 4, Section 4.11); their grades are set out in Chapter 2, Section 2.6. No requirement addressing the reconciliation of retention with erasure and deletion appears among them.""",
   why="de-dup: §6.8 re-stated the SPUHiN checklist grades (home §2.6); point to §2.6, keep the one-year fact + the decisive no-reconciliation gap"),
]
# §6.8 drops "ISO 27001" here (home §2.6 retains it); the numeral 27001 falls by one in Ch6.
LOST_OK = ["number 27001"]
