# P60 — Round 5 wave 1: reframe the formal results and close two rigour/clarity items.
#  P60-01  Jo R5[11]: second disjunct of Proposition 1 needs the analogous assumption t_pi+6 >= t(a).
#  P60-02  Jo R5[3]/adversarial H-3: kill the 3-vs-4 "contributions" count clash in 6.9 (section is
#          already titled Theoretical Implications); point to the four contributions in 7.2.
#  P60-03  Jo R5[12]/adversarial A1: say plainly that Propositions 1 and 3 follow almost immediately
#          from the definitions; relocate the weight to the legal-interpretive work and the mechanism.
#  P60-04  adversarial A1/A2 in the abstract: state that the formal results are deliberately elementary,
#          Prop 1 carries the argument, the weight is the legal analysis and mechanism (reading-independent).
EDITS = [
 dict(id='P60-01', file='Chapter4_TRF_Model_v1.md',
   old=r"""The argument for the second disjunct is identical with $t^{*} = t_\pi(a) + 6$ and C3 in place of C2. ∎""",
   new=r"""The argument for the second disjunct is identical, with $t^{*} = t_\pi(a) + 6$ and C3 in place of C2, on the analogous assumption that $t_\pi(a) + 6 \ge t(a)$; should the ceiling deadline precede the record's creation, the contradiction arises at $t(a)$ itself, where C1 and C3 both bind. ∎""",
   why="Jo R5[11]: state the second-disjunct assumption or the t(a) edge case"),

 dict(id='P60-02', file='Chapter6_Discussion_v1.md',
   old=r"""Three contributions to the scholarly conversation follow from the work, each modest and each stated at its actual size.""",
   new=r"""Three theoretical implications follow from the work, each modest and each stated at its actual size. They are implications of the four contributions set out in Chapter 7, Section 7.2, not a competing list.""",
   why="Jo R5[3]/H-3: remove the 3-vs-4 count clash; label implications, cross-refer the four contributions"),

 dict(id='P60-03', file='Chapter4_TRF_Model_v1.md',
   old=r"""The weight of the argument lies elsewhere: in Section 4.2's necessity analysis, which justifies Semantics II, and in Propositions 3 and 4, which say where the conflict arises and where cryptography is necessary.""",
   new=r"""Propositions 1 and 3 follow almost immediately from the definitions, each resolving to a month in which $\alpha$ must be both 1 and 0, and the thesis states this plainly rather than presenting them as hard-won. The weight of the argument lies elsewhere: in Section 4.2's necessity analysis, which justifies Semantics II, in the legal-interpretive work on the Article 9 patient link, the ITI-55 payload and the scope of Article 68(12), and in the mechanism design that Propositions 3 and 4 frame.""",
   why="Jo R5[12]/A1: Props 1 and 3 are near-immediate from definitions; weight is the legal analysis and mechanism"),

 dict(id='P60-04', file='Front_Matter_v1.md',
   old=r"""The contribution is bounded: no novel cryptographic primitive or formal method, informal proofs, simulated key destruction, and two interpretive steps without regulatory authority. The thesis offers a formal characterisation of the conflict, a minimal semantic move that dissolves it, an executable witness, and an integration analysis against Norwegian infrastructure.""",
   new=r"""The contribution is bounded: no novel cryptographic primitive or formal method, informal proofs, simulated key destruction, and two interpretive steps without regulatory authority. The formal results are deliberately elementary: Proposition 1, that some departure from plaintext verifiability is unavoidable, carries the argument, while Proposition 2 verifies that a minimal principled departure suffices. The weight lies in the legal necessity analysis and the mechanism design, not in the proofs. The thesis offers a formal characterisation of the conflict, a minimal semantic move that dissolves it, an executable witness, and an integration analysis against Norwegian infrastructure.""",
   why="A1/A2: state plainly that the formal results are elementary and reading-independent; weight on legal + mechanism"),
]
LOST_OK = []
