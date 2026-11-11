# P133 — examiner pass of 12 Nov 2026 (pre-submission). Six surgical edits, no new claims, no new citations.
# 01 Ch4 §4.6: Proposition 1's second disjunct is scoped to records the ceiling reaches (sigma = secondary, rho = 1),
#    as C3 itself is (§4.4). Unscoped, the statement was false for a secondary record with rho = 0 and no request,
#    while §4.6 says Proposition 1 survives the narrow reading.
# 02 Ch4 §4.6: the converse of Proposition 1 stated as a remark; §5.5's control case already relies on it.
# 03 Ch5 §5.3: "49 of the SPE violations ... and 4" counted records, not violations (53 records, 58 violations).
# 04 Ch5 §5.7: the tie rule behind 52/86 is stated (four records, both deadlines in one month, recorded under Art 17(1)).
# 05 Ch5 §5.8: Corollary 1.2's thirty-nine witnesses carry the broad-reading condition, as in §4.6 and the abstract.
# 06 Ch7 §7.1: Proposition 4 restated with its legal premise, as §4.10 states it.
LOST_OK = []
EDITS = [
 dict(id='P133-01', file='Chapter4_TRF_Model_v1.md',
   old=r"""> t_r(a) + \delta \le t(a) + F(a) \quad\text{ or }\quad t_\pi(a) + 6 \le t(a) + F(a).
> $$""",
   new=r"""> t_r(a) + \delta \le t(a) + F(a) \quad\text{ or }\quad t_\pi(a) + 6 \le t(a) + F(a).
> $$
>
> The second disjunct is tested only for records the ceiling reaches, that is, with $\sigma(a)$ = secondary and $\rho(a) = 1$.""",
   why="scope the ceiling disjunct as C3 is scoped"),
 dict(id='P133-02', file='Chapter4_TRF_Model_v1.md',
   old=r"""the contradiction arises at $t(a)$ itself, where C1 and C3 both bind. ∎
""",
   new=r"""the contradiction arises at $t(a)$ itself, where C1 and C3 both bind. ∎

*Remark (converse).* If neither disjunct holds, the system is feasible under Semantics I: set $\alpha(a,t) = 1$ for every month of the retention window and $\alpha(a,t) = 0$ afterwards. C1 then holds, and C2 and C3, where they bind at all, bind only after the window has closed. Proposition 1 is therefore an exact characterisation of infeasibility under Semantics I, and it is this converse that the control case of Section 5.5 exercises.
""",
   why="state the converse the sandbox already relies on"),
 dict(id='P133-03', file='Chapter5_Demonstration_v1.md',
   old="49 of the SPE violations are structural and 4 request-driven",
   new="49 of the 53 violating SPE records are ceiling-driven and 4 request-only",
   why="records, not violations"),
 dict(id='P133-04', file='Chapter5_Demonstration_v1.md',
   old="only fifty-two by erasure requests under Article 17(1).",
   new="only fifty-two by erasure requests under Article 17(1); four records whose two deadlines fall in the same month are recorded under Article 17(1).",
   why="state the tie rule the artefact applies"),
 dict(id='P133-05', file='Chapter5_Demonstration_v1.md',
   old="collide over one environment with no data-subject action involved.",
   new="collide over one environment with no data-subject action involved, on the broad reading of Article 68(12) for logs kept at patient-record granularity.",
   why="carry the condition Section 4.6 attaches to Corollary 1.2"),
 dict(id='P133-06', file='Chapter7_Conclusion_v1.md',
   old="And moving a record out of the regulated environment meets the ceiling but not the right to erasure.",
   new="And moving a record out of the regulated environment meets the ceiling but not the right to erasure, on the legal premise that a controller receiving the record receives the obligation with it.",
   why="restate Proposition 4 with its premise"),
]
