# P90 — keep Appendix A.1 true after the app gained three pages (TRF 46a3fcd, 30 Oct 2026):
# Start here, The four propositions, Claim ledger; Thesis run now shows results on open.
# No result module changed, so no figure, listing or console output in the thesis moves.
EDITS = [
 dict(id='P90-01', file='code_artefacts/README_Appendix_A.md',
   old=r"""The demonstration has eight pages. *Witness a record*""",
   new=r"""The demonstration has eleven pages. *Start here* states the problem and sets out a walk through the remaining pages in the order of the thesis. *The four propositions* quotes each proposition from Chapter 4 with the limits the thesis states for it, shows the corresponding figures from the checker, and runs the bounded SMT check of Section 5.5, including the deliberately broken variants it must refute; Proposition 4, which rests on a legal premise, is marked as argued and not executed. *Claim ledger* sets each figure reported in Chapter 5 beside the same figure recomputed when the page opens. *Witness a record*""",
   why="A.1: describe the three new pages so the appendix stays true to the live demonstration"),
 dict(id='P90-02', file='code_artefacts/README_Appendix_A.md',
   old=r"""*Thesis run* reproduces Tables 5.3 and 5.6""",
   new=r"""*Thesis run* reproduces, on opening, Tables 5.3 and 5.6""",
   why="A.1: Thesis run now executes on opening rather than on a button"),
]
