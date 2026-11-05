# P121 — viewer line counts after the design pass of release 1.3.0 (app.py 1124, ui.py 217); the viewer note says
# what ui.py now holds. Presentation only.
LOST_OK = ["number 1125", "number 136"]
EDITS = [
 dict(id='P121-01', file='Chapter5_Demonstration_v1.md',
  old=r"""| `app.py`, `ui.py` | 1125 + 136 |""", new=r"""| `app.py`, `ui.py` | 1124 + 217 |""", why="Table 5.1"),
 dict(id='P121-02', file='code_artefacts/README_Appendix_A.md',
  old=r"""never a source of results | 1125 + 136 |""", new=r"""never a source of results | 1124 + 217 |""", why="A.2"),
 dict(id='P121-03', file='code_artefacts/README_Appendix_A.md',
  old=r"""`app.py` (1125 lines) holds the pages and the self-checks; `ui.py` (136 lines) holds presentation: the theme, the record life strip, whose Semantics II row it computes from $V^{II}$, and the embedding of the two Archify diagrams.""",
  new=r"""`app.py` (1124 lines) holds the pages and the self-checks; `ui.py` (217 lines) holds presentation: the theme and navigation, the record life strip, whose Semantics II row it computes from $V^{II}$, and the embedding of the two Archify diagrams.""", why="viewer note"),
]
