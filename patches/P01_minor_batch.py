# P01 — minor-issues batch from the 30 Sept review (MIN-01, -02, -03, -04, -08, -09, -11, -12).
# Each edit judged against the supervisor's tracked change for the same passage
# (supervisor_review/draft_with_tracked_accepted.txt); where his wording is adopted, `why` says so.

EDITS = [
    # MIN-01: line counts stated in prose were wrong and inverted (checker 363, layer 152).
    # Refer to Table 5.0a instead of restating counts that the code wave will change again.
    dict(id="P01-01", file="Chapter3_Methodology_v1.md",
         old="The checker is deliberately small, on the order of fifty to one hundred lines, because its purpose is to be read and checked rather than to be impressive.",
         new="The checker is kept small enough to be read and checked in full; Table 5.0a gives its size.",
         why="MIN-01: 'fifty to one hundred lines' was wrong (363). Size now stated once, in Table 5.0a"),
    dict(id="P01-02", file="Chapter3_Methodology_v1.md",
         old="It is larger, on the order of two to four hundred lines, but it is not load-bearing:",
         new="It is smaller than the checker (Table 5.0a) and is not load-bearing:",
         why="MIN-01: 'larger, two to four hundred lines' was wrong (152, smaller than the checker)"),
    # MIN-02
    dict(id="P01-03", file="Chapter3_Methodology_v1.md",
         old="It constructs audit records as the tuples defined in Section 3.4, in two classes:",
         new="It constructs audit records as the tuples defined in Chapter 4, Section 4.3, in two classes:",
         why="MIN-02: wrong cross-reference. Supervisor's tracked wording adopted"),
    # MIN-03
    dict(id="P01-04", file="Chapter1_Introduction_v2.md",
         old="showed that cryptographic commitments and accumulator-based invalidation suffice for the audit-trail problem, and that no SNARK is required.",
         new="showed that cryptographic commitments and a logged invalidation registry suffice for the audit-trail problem, and that no SNARK is required; an accumulator layer is specified in Chapter 4 as optional and is not implemented.",
         why="MIN-03: the accumulator is unimplemented and not load-bearing. Supervisor's tracked substance adopted, parenthesis moved to the end of the sentence"),
    # MIN-04: round 5 named wherever the rounds are counted
    dict(id="P01-05", file="Chapter2_LitReview_v2_FINAL.md",
         old="This review proceeded iteratively across four dated rounds,",
         new="This review proceeded iteratively across four dated search rounds and a fifth, verification-only round,",
         why="MIN-04: Appendix B lists five rounds; round 5 verified locators and ran no discovery queries"),
    dict(id="P01-06", file="Chapter2_LitReview_v2_FINAL.md",
         old="rests on four dated rounds, two of them adversarial,",
         new="rests on four dated search rounds, two of them adversarial,",
         why="MIN-04: the absence claim rests on the discovery rounds only; wording now says so"),
    dict(id="P01-07", file="Chapter2_LitReview_v2_FINAL.md",
         old="| 4 | 16 September 2026 | Adversarial novelty testing, prior art, final currency | 23 |\n| | | **Total** | **59** |",
         new="| 4 | 16 September 2026 | Adversarial novelty testing, prior art, final currency | 23 |\n| 5 | 28 September 2026 | Locator verification and source-standing audit; no discovery queries | 18 locator checks |\n| | | **Total discovery and verification queries, rounds 1–4** | **59** |",
         why="MIN-04: the supervisor asked for round 5 in the table. Figures from Appendix B (18 locator verifications)"),
    dict(id="P01-08", file="Front_Matter_v1.md",
         old="Search query log: 59 queries across four dated rounds, with round purposes and coverage notes",
         new="Search query log: 59 queries across four dated search rounds, a fifth round of 18 locator verifications, round purposes and coverage notes",
         why="MIN-04: list of appendices aligned with Appendix B"),
    # MIN-08
    dict(id="P01-09", file="Appendix_C_Evaluation_Instrument.md",
         old="Its execution status is stated in Chapter 3, Section 3.9.",
         new="Its execution status is stated in Chapter 3, Section 3.8.",
         why="MIN-08: §3.8 is the evaluation design; §3.9 is ethics. Supervisor's tracked wording adopted"),
    # MIN-09
    dict(id="P01-10", file="Chapter5_Demonstration_v1.md", old="survive an separately written", new="survive a separately written",
         why="MIN-09: article. Supervisor's tracked wording adopted"),
    dict(id="P01-11", file="Chapter6_Discussion_v1.md", old="and an separately written", new="and a separately written",
         why="MIN-09"),
    dict(id="P01-12", file="Chapter7_Conclusion_v1.md", old="with an separately written", new="with a separately written",
         why="MIN-09"),
    # MIN-11: witnesses are model instances, not evidence about the world
    dict(id="P01-13", file="Chapter5_Demonstration_v1.md",
         old="Corollary 1.2 has thirty-nine concrete witnesses in which two provisions",
         new="Corollary 1.2 has thirty-nine witnesses in the model: records in which two provisions",
         why="MIN-11: 'concrete witnesses' read as evidence about the world"),
    dict(id="P01-14", file="Chapter6_Discussion_v1.md",
         old="Chapter 5 produced thirty-nine concrete witnesses of it in a population",
         new="Chapter 5 produced thirty-nine witnesses of it in the model, in a population",
         why="MIN-11: supervisor's suggested wording 'witnesses in the model'"),
    # MIN-12: an addendum the examiners will not see
    dict(id="P01-15", file="Chapter1_Introduction_v2.md",
         old="Three components conceptually related to the broader research direction are presented in a separate addendum to the thesis supervisor: a zero-knowledge assertion circuit for healthcare-professional authorisation, a sustainability indicator for proof systems, and a cross-border consent-revocation propagation protocol. The addendum signals future research direction without claiming results that have not been produced.",
         new="Three components related to the broader research direction are outside the scope of this thesis: a zero-knowledge assertion circuit for healthcare-professional authorisation, a sustainability indicator for proof systems, and a cross-border consent-revocation propagation protocol. Results for them have not been produced and are not claimed.",
         why="MIN-12: removed the reference to an addendum examiners will not see; the scope statement stays"),
    dict(id="P01-16", file="Chapter3_Methodology_v1.md",
         old="*Activity 6: Communication.* The thesis itself, together with the supplementary addendum to the supervisor covering research directions deliberately excluded from the thesis scope. Chapters 6 and 7.",
         new="*Activity 6: Communication.* The thesis itself. Chapters 6 and 7.",
         why="MIN-12: same addendum, second mention"),
]

LOST_OK = ["number 3.4", "number 3.9"]
