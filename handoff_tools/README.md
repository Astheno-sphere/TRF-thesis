# Handoff tools

Run all from the `outputs/` directory.

**inspector.py** — gate every rewrite.
    python3 handoff_tools/inspector.py BEFORE.md AFTER.md "label"
Exit 0 = ADMIT. A REJECT showing only *gained* items is a deliberate logged correction; any *lost* item is a regression. It cannot see changed meaning in plain words, so read every sentence too.

**mathconv.py** — italic-unicode math to LaTeX.
    python3 handoff_tools/mathconv.py IN.md OUT.md
Inspect OUT before committing. It skips lines already containing `$`, but does not understand backtick code spans.

**assemble.py** — rebuild bibliography and submission.
    python3 handoff_tools/assemble.py

**Word-conversion check:**
    pandoc FILE.md -o out.docx && unzip -p out.docx word/document.xml | grep -o '<m:oMath>' | wc -l
