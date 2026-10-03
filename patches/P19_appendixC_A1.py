# P19 — M6b: Appendix C item A1 reworded; the change recorded in one line, as the supervisor asked
# (he proposed the anchor and says it may and should be reworded). The new A1 states what the
# mechanism now lets an auditor verify (logged invalidation, unaltered, checked against the audit
# log since P12) and no longer claims "full confidence" or a "proof" of deletion.
C, M = "Appendix_C_Evaluation_Instrument.md", "Chapter3_Methodology_v1.md"
EDITS = [
    dict(id="P19-01", file=C,
         old="""The four dimensions and their anchor statements are
reproduced as proposed in supervisory feedback, with one already known to overstate what
the thesis claims: item A1 asserts that the mechanism gives auditors *full confidence*,
which Chapter 6, Section 6.3 explicitly does not claim. It is retained verbatim because it
was proposed as the anchor and because silently correcting a supervisor's wording would
misrepresent the record. A pilot is the proper place to resolve it.""",
         new="""The four dimensions and their anchor statements are
reproduced as proposed in supervisory feedback, except item A1, reworded in October 2026 with the
supervisor's agreement because the proposed wording ("full confidence that data was lawfully
deleted") made a claim the thesis does not make (Chapter 6, Section 6.3).""",
         why="M6b: one-line record of the change"),
    dict(id="P19-02", file=C,
         old="| A1 | *The cryptographic proof gives auditors full confidence that data was lawfully deleted at the required timestamp.* |",
         new="| A1 | The mechanism lets an auditor verify that a record's invalidation was logged at the required month and has not been altered since. |",
         why="M6b: states what the mechanism verifiably provides"),
    dict(id="P19-03", file=C,
         old="A note on item A1. The anchor statement asserts that the mechanism gives auditors *full confidence*, which the thesis itself does not claim: Chapter 6, Section 6.3 states that the invalidation entry is an attestation rather than a proof. The item is retained verbatim because it was proposed as the anchor and because disagreement with it would be an accurate response rather than a failure of the instrument. Item A2 exists to capture that distinction directly, and analysis would read A1 and A2 together rather than A1 alone.",
         new="A note on items A1 and A2. A1 asks about what the mechanism lets an auditor verify: that the invalidation was logged and is unaltered, which the audit log's inclusion proofs establish. A2 asks whether that is enough without proof that the key was destroyed, which the mechanism does not provide: Chapter 6, Section 6.3 states that the invalidation entry is an attestation rather than a proof. Analysis reads the two together.",
         why="M6b"),
    dict(id="P19-04", file=M,
         old="And the questionnaire retains verbatim an anchor statement asserting that the mechanism gives auditors full confidence that data was lawfully deleted, which is stronger than the thesis's own claim; a paired item captures the distinction between attestation and proof, and disagreement with the anchor would be an accurate response rather than an instrument failure.",
         new="And the questionnaire pairs an item on what the mechanism lets an auditor verify, that an invalidation was logged and is unaltered, with an item on whether that attestation suffices without proof that the key was destroyed.",
         why="M6b: §3.8 follows Appendix C"),
]
