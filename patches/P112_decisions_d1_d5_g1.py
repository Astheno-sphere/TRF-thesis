# P112 — Tiger's decisions D1 to D5 and gap G1 (approved 3 Nov; process/OPEN_CASES.md). Each states a premise or a
# limit the examiner's round-3 attack showed was implicit; no result changes. D1 pilot floor is a controller decision
# (§4.2, abstract); D2 Proposition 1's request-driven case presupposes §4.2 (§4.6, folded into principal step 1 in
# §3.7 so the count of subsidiary premises stays four); D3 Corollary 1.2's activity-content premise; D4 ITI-55
# identifier case conceded (Rival 3, §6.1); D5 what "verifiable" in the title qualifies (§1.4); G1 external-auditor
# objective reported (§7.3).
LOST_OK = []
EDITS = [
 dict(id='P112-01', file='Chapter4_TRF_Model_v1.md',
  old=r"""A period an operator sets without a basis in Union or Member State law would not engage the exemption.""",
  new=r"""A period an operator sets without a basis in Union or Member State law would not engage the exemption. The six-year period of the Norwegian pilot is such a decision, taken by Helsedirektoratet as controller (Appendix D); unless a national legal basis for it is identified it is a policy floor, so that before Article 9 applies on 26 March 2029, and beyond its 36 months after that, retaining the patient link against an erasure request has no secure Article 17(3)(b) basis. That is a finding for the controller rather than a limit on the model: by Corollary 2.2 a lower or absent floor removes collisions and creates none.""", why="D1"),
 dict(id='P112-02', file='Front_Matter_v1.md',
  old=r"""subjects cross-border health data audit records to three retention obligations at once:""",
  new=r"""subjects cross-border health data audit records to three retention requirements at once:""", why="D1: the cross-border floor is a requirement, not shown to be a legal obligation"),
 dict(id='P112-03', file='Chapter4_TRF_Model_v1.md',
  old=r"""Under Semantics I the conflict is not bad luck or rare timing. It is a contradiction, and it can be located to the month.""",
  new=r"""Under Semantics I the conflict is not bad luck or rare timing. It is a contradiction, and it can be located to the month. Its request-driven case presupposes the conclusion of Section 4.2, that the payload is not necessary for the floor's purpose, so that Article 17(3)(b) does not exempt it and an erasure request reaches it. Were the payload necessary, the exemption would apply, C2 would not reach it, and only the ceiling case would remain.""", why="D2"),
 dict(id='P112-04', file='Chapter3_Methodology_v1.md',
  old=r"""Two principal steps in the argument rest on reasoning rather than on any regulatory holding: that an invalidated record continues to satisfy a retention obligation,""",
  new=r"""Two principal steps in the argument rest on reasoning rather than on any regulatory holding: that an invalidated record continues to satisfy a retention obligation (on which the request-driven case of Proposition 1 also rests, since it presupposes that the payload is not necessary for the floor's purpose),""", why="D2, folded into principal step 1"),
 dict(id='P112-05', file='Chapter4_TRF_Model_v1.md',
  old=r"""and, for logs kept at dataset granularity, only where the activity content they retain is itself data concerning health.""",
  new=r"""and, for logs kept at dataset granularity, only where the activity content they retain is itself data concerning health. The corollary also assumes that the activity content, and not only the subject fields, is data concerning health: were it not, Semantics I could keep the payload readable and delete only the subject fields, and the collision would not arise. For patient-level activity, which records and which variables a researcher touched, the premise holds; it is stated here as a premise, not derived.""", why="D3"),
 dict(id='P112-06', file='Chapter4_TRF_Model_v1.md',
  old=r"""the IHE patient-discovery transaction requires the audit message to carry the query segment, name and birth time included (Section 4.3). A deployment cannot minimise it away without departing from the profile.""",
  new=r"""the IHE patient-discovery transaction requires the audit message to carry the query segment, which holds the name and birth time where demographic matching is used (Section 4.3). A deployment cannot minimise it away without departing from the profile. Where an identifier is supplied instead, the segment carries little beyond the identifier, which the mechanism keeps as the subject link in any case, and cross-border invalidation then removes little; the Secure Processing Environment case is unaffected.""", why="D4"),
 dict(id='P112-07', file='Chapter6_Discussion_v1.md',
  old=r"""because the IHE patient-discovery profile requires the patient's identifying query to be recorded in the audit message.""",
  new=r"""because the IHE patient-discovery profile requires the patient's identifying query to be recorded in the audit message; where that query carries an identifier rather than demographics, the payload adds little to the subject link the mechanism keeps (Chapter 4, Section 4.10).""", why="D4"),
 dict(id='P112-08', file='Chapter1_Introduction_v2.md',
  old=r"""The significance of this thesis rests on four convergent factors.""",
  new=r"""A note on the title first. "Verifiable" qualifies the invalidation record, which an auditor can check for attribution and for inclusion in a tamper-evident log, not the erasure itself, which no auditor can verify (Chapter 4, Section 4.9).

The significance of this thesis rests on four convergent factors.""", why="D5"),
 dict(id='P112-09', file='Chapter7_Conclusion_v1.md',
  old=r"""The limitations bounding this contribution are stated canonically in Chapter 3, Sections 3.5 and 3.7,""",
  new=r"""Against the objectives set in Chapter 3, Section 3.2, verifiability by an external auditor is met for the invalidation record, whose attributed entry and inclusion proof the artefact checks against the log root (Chapter 5, Section 5.7), and not met for destruction itself, which no auditor can verify (Chapter 4, Section 4.9). The limitations bounding this contribution are stated canonically in Chapter 3, Sections 3.5 and 3.7,""", why="G1"),
]
