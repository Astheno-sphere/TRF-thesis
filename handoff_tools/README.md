# Handoff tools

Run all from the `outputs/` directory.

**inspector.py** — gate every rewrite.
    python3 handoff_tools/inspector.py BEFORE.md AFTER.md "label"
Exit 0 = ADMIT. A REJECT showing only *gained* items is a deliberate logged correction; any *lost* item is a regression. It cannot see changed meaning in plain words, so read every sentence too.

**mathconv.py** — italic-unicode math to LaTeX.
    python3 handoff_tools/mathconv.py IN.md OUT.md
Inspect OUT before committing. It skips lines already containing `$`, but does not understand backtick code spans.

**trail_check.py** — the trail inspector. Run after every patch and before every commit or package.
    python3 handoff_tools/trail_check.py [--full] [--remote]
Must end `TRAIL INTACT`. Its patterns live in `guards.json`; review status in `REVIEW_TRACKER.md`.

**patch.py** — the only way chapter text changes.
    python3 handoff_tools/patch.py patches/<ID>_<name>.py [--dry]
Aborts on any anchor mismatch, a reused ID, or an undeclared loss (list deliberate losses in `LOST_OK`).

**verify_base.py** — wording differences between the chapters and the reviewed draft.

**assemble.py** — rebuild bibliography and submission.
    python3 handoff_tools/assemble.py

**Word-conversion check:**
    pandoc FILE.md -o out.docx && unzip -p out.docx word/document.xml | grep -o '<m:oMath>' | wc -l
