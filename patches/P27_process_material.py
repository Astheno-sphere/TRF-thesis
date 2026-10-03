# P27 — PRES-3: "Keep one concise statement in the Declaration ... and move the Version and Change
# Record to the repository." The abandoned May draft, its unverifiable citations and the withdrawn
# ethics claim are now stated once, in the Declaration. Removed or reduced: §2.1.4 Round 0 paragraph,
# §2.1.5 criterion sentence about the earlier draft, §2.1.6 limitation sentence, §3.9 two sentences.
# The Version and Change Record (Tables F.1, F.2) leaves the front matter; its content goes to the
# repository as docs/VERSION_RECORD.md (pushed with this patch's companion commit).
import pathlib, sys, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze, at
F, C2, C3 = "Front_Matter_v1.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter3_Methodology_v1.md"


def compute():
    pre = subprocess_head()
    fm, c2, c3 = at(pre, F), at(pre, C2), at(pre, C3)
    version_block = fm[fm.index("## Version and Change Record"):fm.index("## Table of Contents")]
    round0 = next(p for p in c2.split("\n\n") if p.startswith("Round 0 requires explanation."))
    return [
        dict(id="P27-01", file=F,
             old=" Any claim to the contrary appearing in earlier drafts of this project is withdrawn.", new="",
             why="PRES-3: merged into the single statement below"),
        dict(id="P27-02", file=F,
             old="An audit conducted in May 2026 identified citations in the earlier draft to works that do not exist; that draft has been discarded in its entirety and every citation in the present work has been checked against a primary or retrievable source.",
             new="An earlier draft of this project, discarded in May 2026, contained citations to works that do not exist and a statement of ethics approval that was never obtained; every citation in the present work has been checked against a primary or retrievable source.",
             why="PRES-3: the one statement about the earlier draft"),
        dict(id="P27-03", file=F, old=version_block, new="",
             why="PRES-3: Version and Change Record moved to the repository (docs/VERSION_RECORD.md)"),
        dict(id="P27-04", file=C2, old=round0,
             new="Round 0 is the exploratory reading that preceded the documented rounds. Its queries were not recorded, and it contributes nothing to the absence claim of Section 2.9, which rests on the four documented search rounds.",
             why="PRES-3: Round 0 reduced to what the search record needs"),
        dict(id="P27-05", file=C2,
             old=" The last of these was applied to the thesis's own earlier draft. That draft carried twenty-eight distinct citations, of which approximately fourteen could not be verified against any primary or publisher record; the draft was discarded rather than repaired, and the verification audit that established this is recorded in the project's working log of 25 May 2026.",
             new="", why="PRES-3: stated once, in the Declaration"),
        dict(id="P27-06", file=C2,
             old="The exploratory phase preceding the documented rounds is acknowledged but not claimed as evidence, because its queries were never recorded; only the resulting draft survives, and it is used in this chapter solely as an artifact demonstrating the absence of a protocol.",
             new="The exploratory phase before round 1 is not claimed as evidence, because its queries were never recorded.",
             why="PRES-3"),
        dict(id="P27-07", file=C2, old="Round 2 tested the claims of an earlier draft and led to its abandonment.",
             new="Round 2 tested the claims carried forward from the exploratory phase.", why="PRES-3"),
        dict(id="P27-08", file=C3,
             old=" This is stated explicitly because an earlier draft of this project asserted an institutional review board approval that did not exist; the correction is recorded here as a matter of research integrity.",
             new="", why="PRES-3: stated once, in the Declaration"),
        dict(id="P27-09", file=C3,
             old=" These commitments respond directly to the failures identified in the earlier draft of this project, and their explicit statement here is intended to make them checkable by the examiner rather than merely asserted.",
             new="", why="PRES-3"),
    ]


def subprocess_head():
    import subprocess
    return subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                          cwd=pathlib.Path(__file__).resolve().parent.parent).stdout.strip()


EDITS = freeze("P27_process_material", compute)

# Every loss is inside removed process material: the Version and Change Record tables (dates, line
# counts, equation counts), the Round 0 paragraph and the earlier-draft sentences (24 May 2026, 28
# citations, approximately fourteen). Listed from the dry run, each checked against the removed text.
LOST_OK = ["hedge approximately", "hedge may ", "number 0", "number 09", "number 1", "number 11", "number 110", "number 135", "number 152", "number 159", "number 16", "number 18", "number 19", "number 2", "number 2026", "number 21", "number 23", "number 24", "number 25", "number 28", "number 3", "number 4.8", "number 5", "number 5.", "number 5.1", "number 5.2", "number 5.3", "number 5.4", "number 526", "number 533", "number 6.", "number 67", "number 7", "number 891"]
