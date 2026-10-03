# P12 — code wave: M1 (SPE record model), M3b (ciphertext deleted), M3c (dead branch), M4c (integrity).
# The new file contents are kept beside this patch in patches/P12_payloads/ so the edit is
# reviewable as a diff (git diff --no-index) and replayable. Each edit replaces a whole file;
# patch.py still checks that the file being replaced is exactly the logged "before".
# Verified before applying (3 Oct): Semantics I 90/200, 95 violations, 39 Cor 1.2 witnesses,
# 138 invalidated, Semantics II 0 — unchanged; Norwegian and cross-sector runs byte-identical;
# Synthea measures identical (constructed mean payload 35 -> 43 bytes); --random-salts gives the
# same results; Streamlit app: every button runs without exception (AppTest).
import pathlib
HERE = pathlib.Path(__file__).parent / "P12_payloads"
NEW_CHECKER = (HERE / "trf_checker.new.py").read_text(encoding="utf-8")
NEW_APP = (HERE / "app.new.py").read_text(encoding="utf-8")
OLD_CHECKER = pathlib.Path("demo_app/trf_checker.py").read_text(encoding="utf-8")
OLD_APP = pathlib.Path("demo_app/app.py").read_text(encoding="utf-8")

EDITS = [
    dict(id=f"P12-0{i+1}", file=f, old=OLD_CHECKER, new=NEW_CHECKER,
         why="M1, M3b, M3c, M4c: m_acc/m_subj, subject link removed at ceiling, payload deleted, make_salt/--random-salts, Merkle log + tamper test")
    for i, f in enumerate(["demo_app/trf_checker.py", "repro_package/trf_checker.py", "code_artefacts/trf_checker.py"])
] + [
    dict(id="P12-04", file="demo_app/app.py", old=OLD_APP, new=NEW_APP,
         why="App follows the checker: SPE auditor view (accessor fields, permit, subject link, salt and ciphertext), Synthea sample read before invalidation"),
]
