# P63 — Round 5 wave 3 (prose): Jo R5[17]. Table A.2 / Table 5.1 list eight .py files; 5.2 said
# "Six further modules". The undercount came from the viewer being two files (app.py, ui.py) on one
# table row. Make 5.2 agree with the eight files and explain the split.
EDITS = [
 dict(id='P63-01', file='Chapter5_Demonstration_v1.md',
   old=r"""Six further modules accompany it, none of which alters anything the checker reports.""",
   new=r"""Seven further modules accompany it, bringing the artefact to eight Python files in all; the eight-page viewer is split across `app.py` and `ui.py`, which Table 5.1 lists on a single row. None of the seven alters anything the checker reports.""",
   why="Jo R5[17]: align the module count with the eight .py files of Table 5.1 / Appendix Table A.2"),
]
LOST_OK = []
