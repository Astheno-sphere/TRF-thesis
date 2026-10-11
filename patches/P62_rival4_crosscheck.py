# P62 — Round 5 wave 3 (prose): Jo R5[13] and R5[15].
#  P62-01  R5[13]: state the commitment's real value plainly and answer whether "delete + logged deletion"
#          is near-equivalent for the cross-border case (Rival 4, 4.10).
#  P62-02  R5[15]: present the exhaustive cross-check as a sanity check (pointwise constraints => month-by-month),
#          let the bounded SMT check carry robustness, but keep the independence rationale (adversarial push-back E2).
EDITS = [
 dict(id='P62-01', file='Chapter4_TRF_Model_v1.md',
   old=r"""The mechanism's advantage over Rival 4 is precisely the verifiability that Chapter 2 identified as absent from the practitioner crypto-shredding pattern.""",
   new=r"""The mechanism's advantage over Rival 4 is precisely the verifiability that Chapter 2 identified as absent from the practitioner crypto-shredding pattern. For the cross-border case, where the subject link is kept through the floor and no party is handed an opening by default, that advantage narrows to the logged, attributed, tamper-evidently bound invalidation entry: there, "delete the record and log the deletion" is close to an equivalent design, and the commitment earns its keep chiefly before invalidation, as substitution detection, and wherever an opening is handed to the data subject or home National Contact Point. It is in the Secure Processing Environment case, and wherever that opening is kept, that the commitment does work the deletion rival cannot.""",
   why="Jo R5[13]: state the commitment's real value; concede near-equivalence of delete+logged-deletion for cross-border"),

 dict(id='P62-02', file='Chapter5_Demonstration_v1.md',
   old=r"""reports whether *any* assignment satisfies C1 under Semantics I together with C2 and C3.""",
   new=r"""reports whether *any* assignment satisfies C1 under Semantics I together with C2 and C3. Because every constraint is pointwise in time, enumerating all assignments is equivalent to checking each month in turn, so this search is best read as a sanity check rather than as independent evidential weight; the bounded SMT check described below carries the robustness argument. Its value is that it is written separately and shares no code with the main checker, so it can catch an implementation error that the checker and its own tests would share.""",
   why="Jo R5[15]: exhaustive search as sanity check, SMT carries robustness, independence rationale kept (E2)"),
]
LOST_OK = []
