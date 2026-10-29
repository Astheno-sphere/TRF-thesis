# P88 — statement-of-contribution: own the contribution TYPE and the negative result (NEXT_SESSION §A).
# Verdict on the 29 Oct drafted paragraph: NOT inserted as a block. Front Matter "Statement of
# Contribution", §6.1, §6.9 and §7.2 already carry its framing, the Semantics I/II split, the timing, and
# the bounds; a new block would duplicate them. Its first move ("on a single cross-border audit record")
# also contradicts P87, which conceded the single-record tri-lateral collision is broad-reading-only and
# confined to SPE logs. Only two moves were genuinely absent, and they are merged here:
#   (1) the contribution TYPE: framing and feasibility, not cryptographic invention; conflict dissolved by
#       definitional precision — hedged to "on the necessity analysis of Section 4.2" (P87-03 register);
#   (2) Proposition 1 owned as a negative result (marks a dead end) — pre-empts R1/R2.
# Applied to the Statement of Contribution and mirrored in §7.2 (the two places the thesis lists the four
# contributions). Abstract, §1.4, §6.1, §6.9 left untouched: each remains consistent with the added text.
EDITS = [
 dict(id='P88-01', file='Front_Matter_v1.md',
   old=r"""This thesis makes four contributions, each stated at the level it can be defended.""",
   new=r"""This thesis makes four contributions, each stated at the level it can be defended. They are contributions of framing and feasibility, not of cryptographic invention: the apparent conflict is dissolved by making precise what a verifiable retained record must be, and not, on the necessity analysis of Chapter 4, Section 4.2, by weakening any of the three obligations.""",
   why="§A move 1: state the contribution type; hedge 'not weakening' to the §4.2 necessity analysis (P87-03 register)"),
 dict(id='P88-02', file='Front_Matter_v1.md',
   old=r"""Proposition 4 shows why relocating a record, the rival that removes it from the environment, does not dissolve the conflict.""",
   new=r"""Proposition 4 shows why relocating a record, the rival that removes it from the environment, does not dissolve the conflict. Proposition 1 is offered as a negative result in its own right: wherever an erasure or deletion deadline falls inside a retention window, it marks as unworkable any design that keeps the payload readable for the length of the floor.""",
   why="§A move 2: own Proposition 1 as a negative result (dead-end marker), pre-empting R1/R2"),
 dict(id='P88-03', file='Chapter7_Conclusion_v1.md',
   old=r"""Four contributions are claimed, each bounded.""",
   new=r"""Four contributions are claimed, each bounded. They are contributions of framing and feasibility, not of cryptographic invention: the conflict is dissolved by precision about what a verifiable retained record must be, not, on the necessity analysis of Chapter 4, Section 4.2, by weakening any obligation.""",
   why="§A move 1 mirrored in §7.2 so the two contribution lists stay concordant"),
 dict(id='P88-04', file='Chapter7_Conclusion_v1.md',
   old=r"""The proofs are informal and the demonstration covers generated instances; neither is presented as more.""",
   new=r"""The proofs are informal and the demonstration covers generated instances; neither is presented as more. Proposition 1 is itself a negative result: it marks as unworkable any design that keeps the payload readable for the length of the floor wherever an erasure or deletion deadline falls inside it.""",
   why="§A move 2 mirrored in §7.2; placed at paragraph end so 'Both were checked' keeps its antecedent (Props 1 and 2)"),
]
