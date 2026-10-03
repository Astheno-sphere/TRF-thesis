# P45 — remaining meta commentary named by the audit (PRES-1), and Propositions 3 and 4 made findable
# from the contents (audit, new problem 7): the §4.6 and §4.10 headings name them.
C1, C2, C4, C6, FM = ("Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter4_TRF_Model_v1.md",
                      "Chapter6_Discussion_v1.md", "Front_Matter_v1.md")
EDITS = [
    dict(id="P45-01", file=C1, old="This thesis is bounded by a deliberate and explicit scope. The bounding is not a limitation to be apologised for but a methodological commitment to defensibility within the time and resources available for an MSc thesis.",
         new="This thesis is bounded by a deliberate and explicit scope, set by what can be defended within the time and resources of an MSc thesis.", why="PRES-1"),
    dict(id="P45-02", file=C2, old="Four limitations follow from how the review was conducted and are stated so that they are not inferred from silence.",
         new="Four limitations follow from how the review was conducted.", why="PRES-1"),
    dict(id="P45-03", file=C4, old="moving a record out of the regulated environment, the first rival a reviewer would propose, meets the ceiling",
         new="moving a record out of the regulated environment, the most direct rival design, meets the ceiling", why="PRES-1"),
    dict(id="P45-04", file=C4, old="compares it against the rival designs a reviewer would propose instead,",
         new="compares it against rival designs,", why="PRES-1"),
    dict(id="P45-05", file=C6, old="A word of restraint is owed here. ", new="", why="PRES-1"),
    dict(id="P45-06", file=C4, old="## 4.6 Proposition 1: Infeasibility under Plaintext Verifiability",
         new="## 4.6 Propositions 1 and 3: Infeasibility, and Where the Ceiling Is Anchored", why="Prop 3 findable"),
    dict(id="P45-07", file=C4, old="## 4.10 Rival Designs", new="## 4.10 Rival Designs and Proposition 4", why="Prop 4 findable"),
    dict(id="P45-08", file=FM, old="- 4.6 Proposition 1: Infeasibility under Plaintext Verifiability",
         new="- 4.6 Propositions 1 and 3: Infeasibility, and Where the Ceiling Is Anchored", why="TOC"),
    dict(id="P45-09", file=FM, old="- 4.10 Rival Designs", new="- 4.10 Rival Designs and Proposition 4", why="TOC"),
]
