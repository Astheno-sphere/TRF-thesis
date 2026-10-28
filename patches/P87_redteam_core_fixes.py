# P87 — red-team core fixes (Tiger-approved F1/F3/F4 + B energy-framing + Parallel AI in declaration).
# F1 (R3b, #1 threat), Ch4 §4.6: concede the single-record tri-lateral collision is broad-reading-only,
#   recentre the narrow-reading contribution on the verifiability semantics. (Honesty = armour.)
# F3 (R3c), Ch4 §4.2: hedge the necessity conclusion to "this thesis's analysis", matching the register.
# F4 (R3d, #2 threat), Ch4 §4.2: extend Corollary 2.3's "if part is needed" concession to the cross-border
#   record, so §4.2 does not assume the controller's purpose is narrower than a DPA might accept.
# B (R5 energy fit), Ch2 §2.7: one sentence making the energy-sector application of the model explicit.
# AI (R4-C2), Front_Matter: name Parallel AI in the Use-of-AI declaration.
EDITS = [
 dict(id='P87-01', file='Chapter4_TRF_Model_v1.md',
   old=r"""rather than choosing one by assertion. Little turns on which reading prevails. Under the narrow reading, Corollary 1.2 lapses, and with it the claim that infeasibility arises without any data-subject action.""",
   new=r"""rather than choosing one by assertion. What turns on the reading is the collision's sharpest form, not the thesis's results. Under the narrow reading, Corollary 1.2 lapses, and with it both the claim that infeasibility arises without any data-subject action and the distinctive case in which a single record is bound by all three regimes at once; the cross-border and Secure Processing Environment settings then each reduce to a retention floor against an erasure right, so that on the narrow reading what distinguishes the contribution from the bilateral crypto-shredding of existing practice is the verifiability semantics and the cross-border instantiation, not the co-location of three constraints on one record.""",
   why="F1/R3b: concede the single-record tri-lateral collision is broad-reading-only; recentre narrow-reading contribution on verifiability semantics + cross-border instantiation"),
 dict(id='P87-02', file='Chapter4_TRF_Model_v1.md',
   old=r"""The narrow reading, or logs kept at dataset granularity, therefore cost the thesis its conditional extension and none of its results.""",
   new=r"""The narrow reading, or logs kept at dataset granularity, therefore cost the thesis its conditional extension (Corollary 1.2) and the single-record tri-lateral collision it carries, but none of Propositions 1 to 4, the mechanism, or the verifiability semantics on which the contribution principally rests.""",
   why="F1/R3b: make the 'what the narrow reading costs' sentence consistent with the concession above"),
 dict(id='P87-03', file='Chapter4_TRF_Model_v1.md',
   old=r"""Retention of accessible plaintext payload for the length of the floor therefore exceeds what Article 17(3)(b) protects. Article 5(1)(c) positively requires that it not be retained where the purpose can be achieved without it.""",
   new=r"""On this thesis's analysis, retention of accessible plaintext payload for the length of the floor therefore exceeds what Article 17(3)(b) protects, and Article 5(1)(c) requires that it not be retained where the purpose can be achieved without it — a reading argued here from the primary instruments, not one a supervisory authority has yet confirmed.""",
   why="F3/R3c: hedge the necessity conclusion to match the register used elsewhere; stop asserting a determination no authority has made"),
 dict(id='P87-04', file='Chapter4_TRF_Model_v1.md',
   old=r"""the accessor fields with the patient link answer it; the patient's name and birth date as typed into the query add nothing to that answer. For a Secure Processing Environment record it is weaker.""",
   new=r"""the accessor fields with the patient link answer it; the patient's name and birth date as typed into the query add nothing to that answer. Should a supervisory authority nonetheless hold part of the payload necessary for a particular accountability purpose — a possibility this thesis does not exclude — the conditional analysis of Corollary 2.3 applies to the cross-border record as it does to the Secure Processing Environment record, and the mechanism retains that part under the same necessity test. For a Secure Processing Environment record it is weaker.""",
   why="F4/R3d: extend Corollary 2.3's concession to the cross-border payload so §4.2 is not self-sealing on purpose scope"),
 dict(id='P87-05', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""That is a retention period per data category, anchored to an event: the form of the floor parameter in Chapter 4, Section 4.3, in a different sector. The extension the data subject controls has no counterpart in the model.""",
   new=r"""That is a retention period per data category, anchored to an event: the form of the floor parameter in Chapter 4, Section 4.3, in a different sector. The extension the data subject controls has no counterpart in the model. The parallel is more than illustrative: an electricity data hub that must retain metering and settlement records for correction while honouring an erasure request faces the same floor-against-right structure the model formalises, so the TRF Model transfers to energy-sector data-retention conflicts without modification — the application in which this programme's logistics-of-information framing is most directly its own.""",
   why="B/R5: make the energy-sector application of the model explicit (one sentence), shoring up programme fit"),
 dict(id='P87-06', file='Front_Matter_v1.md',
   old=r"""Archify was used to generate the thesis's diagrams and figures. All design decisions,""",
   new=r"""Archify was used to generate the thesis's diagrams and figures, and Parallel AI was used as an additional research and source-retrieval assistant. All design decisions,""",
   why="R4-C2: name Parallel AI in the Use-of-AI declaration (use description to be confirmed by Tiger)"),
]
LOST_OK = []
