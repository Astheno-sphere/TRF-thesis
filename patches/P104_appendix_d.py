# P104 — Appendix D (correspondence with public authorities), per Tiger 2 Nov ("i have his permission").
# The six-year pilot figure now has a checkable primary record; §2.3 points to it; TOC lists it.
LOST_OK = []
EDITS = [
 dict(id='P104-01', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""personal communication, 19 October 2026). The reported ten-year""",
  new=r"""personal communication, 19 October 2026); the reply is reproduced, with permission, in Appendix D. The reported ten-year""",
  why="back-reference to the reproduced primary record"),
 dict(id='P104-02', file='Front_Matter_v1.md',
  old=r"""- C.8 Data protection, if executed""",
  new=r"""- C.8 Data protection, if executed

**Appendix D. Correspondence with Public Authorities**

- D.1 Helsedirektoratet, on the retention of the cross-border audit trail
- D.2 Datatilsynet, on the two principal interpretive questions""", why="TOC entry"),
]
