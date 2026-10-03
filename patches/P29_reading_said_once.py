# P29 — PRES-4 (part 2): the Art 68(12) reading argued once, in §4.6. §1.1 (problem statement) and
# §2.3 (the regime in the review) keep short statements that point to §4.6; §6.2 and §7.4 no longer
# re-argue the grounds.
C6, C7 = "Chapter6_Discussion_v1.md", "Chapter7_Conclusion_v1.md"
EDITS = [
    dict(id="P29-01", file=C6,
         old="The thesis states Corollary 1.2 conditionally rather than adopting either reading. The provision is framed by location rather than provenance, which supports the broad reading; its object is electronic health data, which confines that reading to logs kept at patient-record granularity; and its placement within the data-permit article supports the narrower construction. What makes",
         new="The thesis states Corollary 1.2 conditionally rather than adopting the broad reading or the narrow one, on the grounds set out in Chapter 4, Section 4.6. What makes",
         why="PRES-4: grounds argued once, in §4.6"),
    dict(id="P29-02", file=C7,
         old="The second concerns scope. Article 68(12) requires \"the electronic health data within the secure processing environment\" to be deleted within six months of permit expiry. On the broad reading, which takes the provision's scope from its location, it reaches access logs kept at patient-record granularity, whose subject fields are data concerning health. The competing construction, supported by the provision's placement within the data-permit article, confines it to the permitted dataset. Chapter 4, Section 4.6 shows that Corollary 1.2 stands or falls with this question and that nothing else in the thesis does.",
         new="The second concerns scope: whether Article 68(12), which requires \"the electronic health data within the secure processing environment\" to be deleted within six months of permit expiry, reaches, on the broad reading, access logs kept at patient-record granularity (Chapter 4, Section 4.6). Corollary 1.2 stands or falls with this question, and nothing else in the thesis does.",
         why="PRES-4: the question stated; the grounds left to §4.6"),
]
