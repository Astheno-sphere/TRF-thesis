# P64 — Round 5: Jo's own R5 tracked wording edits applied verbatim (his point 5). Safe subset; code
# confirmed to carry --random-salts (os.urandom), so [33]/[34] are consistent. Held: none remaining
# (the awkward double "(Sikt))" of his [43] is applied cleanly as a single gloss).
EDITS = [
 # [2] drop the redundant "Supervisor:" prefix on the keywords-footer artefact line (title page keeps it)
 dict(id='P64-01', file='Front_Matter_v1.md',
   old=r"""Supervisor: Prof. João Ferreira. Artefact: https://github.com/Astheno-sphere/TRF.""",
   new=r"""Artefact: https://github.com/Astheno-sphere/TRF.""", why="JF R5[2]"),
 # [4] Sikt abbreviation in Ethics
 dict(id='P64-02', file='Front_Matter_v1.md',
   old=r"""the Norwegian Agency for Shared Services in Education and Research, from any regional research-ethics committee""",
   new=r"""the Norwegian Agency for Shared Services in Education and Research (Sikt), from any regional research-ethics committee""", why="JF R5[4]"),
 # [18] gloss avviklet
 dict(id='P64-03', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""was formally avviklet by the Ministry of Health and Care Services in February 2023""",
   new=r"""was formally discontinued (avviklet) by the Ministry of Health and Care Services in February 2023""", why="JF R5[18]"),
 # [19] tutorial article
 dict(id='P64-04', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""The tutorial gives no source for the figure.""",
   new=r"""That tutorial article gives no source for the figure.""", why="JF R5[19]"),
 # [20] practitioner-heuristic rewording
 dict(id='P64-05', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""The standard practitioner heuristic for conflicting retention obligations cannot resolve this. A common practitioner heuristic for multi-framework environments is to apply the longest applicable retention period across all frameworks: a rule that works when every obligation is a floor, and fails entirely when one obligation is a ceiling, since extending retention to satisfy the longer floor is precisely what the ceiling forbids.""",
   new=r"""The common practitioner heuristic for multi-framework environments, which is to apply the longest applicable retention period across all frameworks, cannot resolve this: it works when every obligation is a floor, and fails entirely when one obligation is a ceiling, since extending retention to satisfy the longer floor is precisely what the ceiling forbids.""", why="JF R5[20]"),
 # [21] delete the renumbering sentence (de-dup; §1.4 keeps the renumbering point)
 dict(id='P64-06', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""The renumbering of these obligations between the 2022 proposal and the adopted text, from Articles 46 and 50 to Articles 68 and 73, may be one reason the commentary has treated them apart (Chapter 1, Section 1.4).""",
   new="", why="JF R5[21]: delete; renumbering point kept in 1.4"),
 # [22] word order
 dict(id='P64-07', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""the storage-limitation and data-minimisation principles of Article 5(1)(c) and 5(1)(e) GDPR""",
   new=r"""the data-minimisation and storage-limitation principles of Article 5(1)(c) and 5(1)(e) GDPR""", why="JF R5[22]"),
 # [23] colon
 dict(id='P64-08', file='Chapter3_Methodology_v1.md',
   old=r"""Activity 5, Evaluation.""", new=r"""Activity 5: Evaluation.""", why="JF R5[23]"),
 # [32] third trigger in the Ch4 summary
 dict(id='P64-09', file='Chapter4_TRF_Model_v1.md',
   old=r"""destroys the payload key at the earlier of the erasure deadline and the deletion ceiling.""",
   new=r"""destroys the payload key at the earliest of the erasure deadline, the deletion ceiling and any payload retention period the controller sets.""", why="JF R5[32]"),
 # [37] third trigger in the Ch7 summary
 dict(id='P64-10', file='Chapter7_Conclusion_v1.md',
   old=r"""destroys the per-record payload key, with the salt and the ciphertext, at the earlier of the erasure deadline and the deletion ceiling;""",
   new=r"""destroys the per-record payload key, with the salt and the ciphertext, at the earliest of the erasure deadline, the deletion ceiling and any payload retention period the controller sets;""", why="JF R5[37]"),
 # [33] os import in the dependency list
 dict(id='P64-11', file='Chapter5_Demonstration_v1.md',
   old=r"""`random` for seeded generation, and `itertools` for the exhaustive cross-check""",
   new=r"""`random` for seeded generation, `os` for the optional random salts, and `itertools` for the exhaustive cross-check""", why="JF R5[33]"),
 # [34] salt provenance clause (code confirmed to carry --random-salts)
 dict(id='P64-12', file='Chapter5_Demonstration_v1.md',
   old=r"""with a per-record sixteen-byte salt; a payload key""",
   new=r"""with a per-record sixteen-byte salt (derived from the record identifier in the reported run so that it reproduces exactly, and therefore not hiding in that run; drawn from `os.urandom` under `--random-salts`, Appendix A, A.6); a payload key""", why="JF R5[34]/[7]"),
 # [40] Synthea determinism corrected (our own 6 Oct finding; Appendix A.7)
 dict(id='P64-13', file='code_artefacts/README_Appendix_A.md',
   old=r"""Synthea is deterministic under fixed population and clinician seeds, and produces byte-identical bundles in any environment with a compatible JVM.""",
   new=r"""Synthea is deterministic under fixed population and clinician seeds, and reproduces the same patients and clinical events in any environment with a compatible JVM, although file timestamps differ between runs (Section A.5).""", why="JF R5[40]: byte-identical overclaim corrected"),
 # [7]-[14] four nomenclature rows added before the constraints row
 dict(id='P64-14', file='Front_Matter_v1.md',
   old=r"""| C1, C2, C3 | Retention floor, erasure right, and deletion ceiling constraints |""",
   new=r"""| *m*_acc_(*a*), *m*_subj_(*a*) | Accessor fields and subject fields of the event metadata (Section 4.3) |
| *β*(*a*, *t*) | Subject-link variable at month *t* — 1 if the subject fields are readable, 0 otherwise |
| *p*_n_(*a*), *p*_r_(*a*) | Part of the payload that auditing needs, and the remainder (Corollary 2.3) |
| *e*(*a*), *L* | Month of the event a ceiling is anchored to, and the ceiling length in months (Proposition 3) |
| C1, C2, C3 | Retention floor, erasure right, and deletion ceiling constraints |""", why="JF R5[7]-[14]: notation rows for the symbols used in Ch4"),
]
LOST_OK = ["article 46", "article 50", "article 68", "article 73",
           "number 1", "number 46", "number 50", "number 68", "number 73", "number 2022", "number 1.4",
           "hedge may "]  # [21] renumbering sentence removed whole; the point stays in 1.4
