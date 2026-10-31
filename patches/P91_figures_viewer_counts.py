# P91 — domino fixes after the app grew (TRF 46a3fcd) and the Figure 4.1/5.1 corrections:
# Ch5 §5.2 and Table 5.1 and Appendix A.2 still said "eight-page" and 825 lines (now 1108);
# Figure 4.1's caption did not say the payload-retention trigger is specified but not run.
LOST_OK = ["number 825"]
EDITS = [
 dict(id='P91-01', file='Chapter5_Demonstration_v1.md',
   old=r"""the eight-page viewer is split across `app.py` and `ui.py`""",
   new=r"""the eleven-page viewer is split across `app.py` and `ui.py`""",
   why="§5.2: viewer now has eleven pages (P90 domino)"),
 dict(id='P91-02', file='Chapter5_Demonstration_v1.md',
   old=r"""| `app.py`, `ui.py` | 825 + 133 | Eight-page viewer over the artefact""",
   new=r"""| `app.py`, `ui.py` | 1108 + 133 | Eleven-page viewer over the artefact""",
   why="Table 5.1: current line count and page count"),
 dict(id='P91-03', file='code_artefacts/README_Appendix_A.md',
   old=r"""| `app.py`, `ui.py` | Eight-page demonstration viewer with live architecture diagrams (Figures 4.1 and 5.1), never a source of results | 825 + 133 |""",
   new=r"""| `app.py`, `ui.py` | Eleven-page demonstration viewer with live architecture diagrams (Figures 4.1 and 5.1), never a source of results | 1108 + 133 |""",
   why="A.2: current line count and page count"),
 dict(id='P91-04', file='Chapter4_TRF_Model_v1.md',
   old=r"""where the controller sets one, the payload retention period) and the optional hand-over""",
   new=r"""where the controller sets one, the payload retention period, which is specified here but not run by the artefact) and the optional hand-over""",
   why="Fig 4.1 caption: mark the proactive trigger as specified-not-implemented, matching §4.8 and the redrawn figure"),
]
