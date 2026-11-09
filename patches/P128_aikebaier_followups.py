# P128 — follow-ups to P126 W-2: Aikebaier (2026) v2 states a one-directional sufficiency result in a preprint;
# four sites still described it as a formal foundation or equivalence.
LOST_OK = []
EDITS = [
 dict(id='P128-01', file='Chapter2_LitReview_v2_FINAL.md', old=r"""which supplies a formal foundation for the erasure semantics this thesis consumes""", new=r"""which gives a formal treatment of the erasure semantics this thesis consumes""", why="preprint, sufficiency only"),
 dict(id='P128-02', file='Chapter2_LitReview_v2_FINAL.md', old=r"""and the erasure side has been formalised (Aikebaier, 2026).""", new=r"""and the erasure side has a formal treatment in a preprint (Aikebaier, 2026).""", why="preprint, sufficiency only"),
 dict(id='P128-03', file='Chapter2_LitReview_v2_FINAL.md', old=r"""and now formally grounded for Article 17 purposes,""", new=r"""and now treated formally for Article 17 purposes in a preprint,""", why="preprint, sufficiency only"),
 dict(id='P128-04', file='Chapter4_TRF_Model_v1.md', old=r"""which connects a Destruction-IND security notion to the Board's description of unintelligibility""", new=r"""which takes a Destruction-IND-CCA security notion to suffice for the Board's description of unintelligibility""", why="v2 notion and direction"),
]
