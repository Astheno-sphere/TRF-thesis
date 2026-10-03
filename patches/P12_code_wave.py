# P12 — code wave: M1 (SPE record model), M3b (ciphertext deleted), M3c (dead branch), M4c (integrity).
# The new file contents are kept beside this patch in patches/P12_payloads/ so the edit is
# reviewable as a diff (git diff --no-index) and replayable. Each edit replaces a whole file;
# patch.py still checks that the file being replaced is exactly the logged "before".
# Verified before applying (3 Oct): Semantics I 90/200, 95 violations, 39 Cor 1.2 witnesses,
# 138 invalidated, Semantics II 0 — unchanged; Norwegian and cross-sector runs byte-identical;
# Synthea measures identical (constructed mean payload 35 -> 43 bytes); --random-salts gives the
# same results; Streamlit app: every button runs without exception (AppTest).
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze, at
HERE = pathlib.Path(__file__).parent / "P12_payloads"
PRE = "e1143af"   # last commit before the code wave


def compute():
    new_checker = (HERE / "trf_checker.new.py").read_text(encoding="utf-8")
    new_app = (HERE / "app.new.py").read_text(encoding="utf-8")
    old_checker, old_app = at(PRE, "demo_app/trf_checker.py"), at(PRE, "demo_app/app.py")
    return [dict(id=f"P12-0{i+1}", file=f, old=old_checker, new=new_checker,
                 why="M1, M3b, M3c, M4c: m_acc/m_subj, subject link removed at ceiling, payload deleted, make_salt/--random-salts, Merkle log + tamper test")
            for i, f in enumerate(["demo_app/trf_checker.py", "repro_package/trf_checker.py", "code_artefacts/trf_checker.py"])] + [
           dict(id="P12-04", file="demo_app/app.py", old=old_app, new=new_app,
                why="App follows the checker: SPE auditor view (accessor fields, permit, subject link, salt and ciphertext), Synthea sample read before invalidation")]


EDITS = freeze("P12_code_wave", compute)
