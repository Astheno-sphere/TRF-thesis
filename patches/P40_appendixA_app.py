# P40 — Appendix A.14 (source listing of app.py) synced to the app after P39/P39b, and the
# Appendix A prose on the app updated (six tabs). Block edits built by appendix_sync, frozen.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync
from frozen import freeze
EDITS = freeze("P40_appendixA_app", lambda: appendix_sync.block_edits("P40-B"))
N = "671"
A, C5, R = "code_artefacts/README_Appendix_A.md", "Chapter5_Demonstration_v1.md", "demo_app/README_repo.md"
EDITS = EDITS + [
    dict(id="P40-01", file=A,
         old="The demonstration presents five tabs. Tab 1 runs the thesis configuration and reproduces Tables 5.3 and 5.6.",
         new="The demonstration presents six tabs. Tab 1 runs the thesis configuration, reproduces Tables 5.3 and 5.6, and shows the audit-log integrity check and both tamper tests of Section 5.7.",
         why="six tabs"),
    dict(id="P40-02", file=A,
         old="Tab 5 runs the two robustness checks: the independent exhaustive cross-check of Section 5.4 and the erasure-response-period witness of Section 5.6.",
         new="Tab 5 runs the robustness checks: the independent exhaustive cross-check of Section 5.5, the erasure-response-period witness of Section 5.6, and the optional envelope-encryption module of Section 5.8. Tab 6 evaluates the condition of Proposition 3 for any floor and ceiling, with Article 68(12) and politiregisterloven § 17 as presets.",
         why="tab 5 label corrected; tab 6"),
    dict(id="P40-03", file=A,
         old="| `app.py` | Five-tab demonstration viewer over the artefact, never a source of results | 530 |",
         new="| `app.py` | Six-tab demonstration viewer over the artefact, never a source of results | 671 |",
         why="line count"),
    dict(id="P40-04", file=C5,
         old="| `app.py` | 530 | Five-tab viewer over the artefact; never a source of results | No |",
         new="| `app.py` | 671 | Six-tab viewer over the artefact; never a source of results | No |",
         why="line count"),
    dict(id="P40-05", file=R,
         old="Tab 4 Norwegian context, Tab 5 robustness and cross-checks | 524 |",
         new="Tab 4 Norwegian context, Tab 5 robustness and cross-checks (including real envelope encryption), Tab 6 where the ceiling is anchored (Proposition 3) | 671 |",
         why="repo README"),
]
LOST_OK = ["number 5.4", "hedge conditional", "number 530", "number 524"]   # the app's old §5.4 label and "conditional on the reading" wording; old line counts
