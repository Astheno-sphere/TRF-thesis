# P26 — PRES-1: defensive meta-commentary cut. Every hit of a widened detector (84 matches,
# 74 sentences) was read; about half are cut or shortened here. Kept where the phrase carries
# argument: "deliberately high threshold" (Datatilsynet), "deliberately narrow" (NCPeH scope),
# "honest key destruction" (the trust assumption, a term), "rather than asserted as a regulatory
# requirement" (Aikebaier), "analysed against that threshold rather than assumed to clear it".
# Process material about the abandoned May draft is PRES-3 (P27), not here.
# Two substantive fixes found while reading: §4.10 said every rival is "rejected", but Rival 6 is
# accepted for the ceiling (P06); §6.9a's diagnostic question contradicted Proposition 3 (P15).
F, C1, C2, C3, C4, C5, C6, C7 = ("Front_Matter_v1.md", "Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md",
    "Chapter3_Methodology_v1.md", "Chapter4_TRF_Model_v1.md", "Chapter5_Demonstration_v1.md", "Chapter6_Discussion_v1.md",
    "Chapter7_Conclusion_v1.md")
CUTS = [
    (F, "Where verification of a source remains incomplete, the incompleteness is flagged in the text rather than concealed.", "Where verification of a source remains incomplete, the text says so."),
    (C1, "A note on nomenclature records the design's evolution honestly. ", ""),
    (C1, "The thesis's novelty claim is therefore layered and deliberately bounded:", "The thesis's novelty claim is therefore layered and bounded:"),
    (C1, "It deliberately employs lighter machinery,", "It employs lighter machinery,"),
    (C2, "It is not a systematic review, and the distinction is stated at the outset rather than left to inference.", "It is not a systematic review."),
    (C2, "cannot be reconstructed honestly for rounds 1 and 2", "cannot be reconstructed for rounds 1 and 2"),
    (C2, "A further explanation is procedural and worth recording, because the apparent obviousness of the conflict otherwise invites the question of why it has not been addressed.", "A further explanation of why the conflict has not been addressed is procedural."),
    (C2, "But it defines the honest boundary of any crypto-erasure guarantee: the mechanism's properties are conditional on honest and verifiable key-lifecycle management,", "But it defines the boundary of any crypto-erasure guarantee: the mechanism's properties are conditional on honest and verifiable key-lifecycle management,"),
    (C2, "A third adjacent body is the closest prior art to the mechanism proposed in this thesis, and honest scholarship requires it be surfaced rather than left for a reviewer to find.", "A third adjacent body is the closest prior art to the mechanism proposed in this thesis."),
    (C2, "and this tradition must be reviewed both to anchor the method and to bound the novelty claim honestly.", "and reviewing it both anchors the method and bounds the novelty claim."),
    (C2, "The significance for this thesis is double-edged and is stated plainly.", "The significance for this thesis is double-edged."),
    (C2, "The instantiation developed in Chapter 4 also deliberately employs lighter machinery", "The instantiation developed in Chapter 4 also employs lighter machinery"),
    (C2, "The weight this can bear must be stated with the claim rather than left at its first mention: the work is a single-author preprint with industry affiliation and no peer review, and a reader is entitled to discount it accordingly.", "The work is a single-author preprint with industry affiliation and no peer review, and carries correspondingly less weight."),
    (C3, "That correction is itself an instance of the design cycle operating as intended, and is recorded rather than concealed.", "That correction is itself an instance of the design cycle operating as intended."),
    (C3, "This thesis deliberately employs a lighter formalism", "This thesis employs a lighter formalism"),
    (C3, "Because the formulation is deliberately light,", "Because the formulation is light,"),
    (C3, "These limitations are real and are recorded here rather than omitted. They do not, however,", "These limitations do not, however,"),
    (C3, "has two layers, separated deliberately so that", "has two layers, separated so that"),
    (C3, "Two features of the design are worth stating here rather than leaving to the appendix.", "Two features of the design matter here."),
    (C4, "and it must be stated precisely because everything downstream inherits it.", "and everything downstream inherits it."),
    (C4, "Two supports and one limit should be recorded.", "Two sources support it and one limits it."),
    (C4, "But the architecture of the results is deliberately such that little turns on which reading prevails, and that should be made explicit.", "Little turns on which reading prevails."),
    (C4, "are both cases of one condition, stated here because it is the structural content of the problem rather than a property of either instrument.", "are both cases of one condition, the structural content of the problem rather than a property of either instrument."),
    (C4, "An objection should be anticipated rather than left for a reader to formulate: that Proposition 2 proves little,", "One objection is that Proposition 2 proves little,"),
    (C4, "*The honest limit.*", "*The limit.*"),
    (C4, "*The trust assumptions, stated explicitly.*", "*The trust assumptions.*"),
    (C4, "What an external auditor can verify without any of this trust is bounded and worth stating precisely.", "What an external auditor can verify without any of this trust is bounded."),
    (C4, "A reviewer will propose alternatives. Six are treated here, and each is rejected for a stated reason rather than by assertion.", "Six alternative designs are considered. Five are rejected for stated reasons; the sixth is accepted for the ceiling alone and bounded by Proposition 4."),
    (C4, "The mechanism's residue was analysed rather than assumed: it is pseudonymised", "The mechanism's residue is pseudonymised"),
    (C5, "Its function is narrow and should be stated before the results, so that the results are not read as establishing more than they do.", "Its function is narrow."),
    (C5, "The mechanism behind the inversion should be stated plainly, because an examiner's first reaction will be that the secondary pathway simply carries more constraints. That reaction is correct, and it is the point.", "The inversion has a simple mechanism: the secondary pathway carries more constraints."),
    (C5, "This substitution is noted rather than hidden, and it is the one place", "It is the one place"),
    (C5, "That claim is witnessed rather than asserted.", "That claim is witnessed here at $\\delta = 3$."),
    (C5, "*Payload provenance, tested rather than assumed.*", "*Payload provenance.*"),
    (C6, "The consequence must be stated without softening. ", ""),
    (C6, "and it is the honest ceiling of the contribution.", "and it is the ceiling of the contribution."),
    (C6, "That boundary is where an active research programme sits, and naming it locates the thesis honestly within the field rather than overstating its reach.", "That boundary is where an active research programme sits."),
    (C6, "The timing argument is the strongest claim to practical relevance this thesis makes, and it is worth stating with the calendar in front of it.", "The timing argument is the strongest claim to practical relevance this thesis makes."),
    (C6, "This is an absence observed in the published checklists rather than established against the full deliverable, which remains on the verification register; the claim is stated at that strength deliberately.", "The absence is observed in the hearing version of the checklists, not established against the deliverable as submitted."),
    (C6, "It suggests that the diagnostic question for any candidate instance is not whether a floor and a ceiling both exist, which is common, but whether they are anchored to the same event, which is not.", "It suggests that the diagnostic question for any candidate instance is not whether a floor and a ceiling both exist, which is common, but whether a ceiling no longer than the floor is anchored to a different event, which is not (Chapter 4, Proposition 3)."),
    (C6, "That is a deliberate methodological position and not an apology, and it is worth defending explicitly because an examiner may read it either way.", "That is a methodological position, not an apology."),
    (C6, "disclosed and distinguished rather than omitted.", "disclosed and distinguished."),
    (C6, "Its honest ceiling is that", "Its ceiling is that"),
    (C7, "The residue it leaves is characterised honestly as pseudonymised", "The residue it leaves is characterised as pseudonymised"),
    (C7, "They are not restated here, because each was priced into the claim before the claim was made and a conclusion that re-enumerates them adds length rather than candour.", "They are not restated here."),
    (C7, "which is the honest statement of where this thesis is weakest.", "which states where this thesis is weakest."),
    (C7, "are named rather than concealed, and the means of settling them", "are named, and the means of settling them"),
]
EDITS = [dict(id=f"P26-{i:02d}", file=f, old=o, new=n, why="PRES-1: meta-commentary cut" if "Proposition" not in n or "diagnostic" not in n else "PRES-1; Proposition 3 consistency")
         for i, (f, o, n) in enumerate(CUTS, 1)]

# "may" was in "because an examiner may read it either way", part of the meta-commentary cut.
LOST_OK = ["hedge may "]
