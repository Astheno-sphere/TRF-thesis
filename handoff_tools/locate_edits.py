#!/usr/bin/env python3
"""Locate a supervisor's tracked changes in the markdown sources, word by word (Round 4 method).

    python3 handoff_tools/locate_edits.py supervisor_review/<name>_changes.txt patches/P<NN>_jf_tracked.edits.json

For each changed span it searches for the smallest context (new-text words on the left, old-text words on
the right) that occurs exactly once across the chapter files, applies it in memory, and moves on, so the
output can be applied in order by patch.py as a frozen patch. Spans it cannot place are printed for manual
handling (typically: whole new paragraphs, table cells, text next to equations, reference entries).
Always review the result and dry-run it before applying; delete script artefacts such as 'TOTAL n'.
"""
import re, sys, json, difflib
src, outp = sys.argv[1], sys.argv[2]
files = ['Front_Matter_v1.md', 'Chapter1_Introduction_v2.md', 'Chapter2_LitReview_v2_FINAL.md', 'Chapter3_Methodology_v1.md',
         'Chapter4_TRF_Model_v1.md', 'Chapter5_Demonstration_v1.md', 'Chapter6_Discussion_v1.md', 'Chapter7_Conclusion_v1.md',
         'code_artefacts/README_Appendix_A.md', 'Appendix_B_Search_Log.md', 'Appendix_C_Evaluation_Instrument.md']
T = {f: open(f, encoding='utf-8').read() for f in files}
edits, manual = [], []
for b in open(src, encoding='utf-8').read().split('=== [')[1:]:
    num = int(b.split(']')[0])
    m = re.search(r'\nOLD: (.*)\nNEW: (.*?)(\nCOMMENT|\nTOTAL|\Z)', b, re.S)
    if not m:
        continue
    a, c = m.group(1).split(' '), m.group(2).rstrip('\n').split(' ')
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, c, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        found = None
        for k in (6, 5, 4, 3, 2, 1):
            for kr in (3, 2, 1, 0):
                L, R = c[max(0, j1 - k):j1], a[i2:i2 + kr]
                o = re.sub(' +', ' ', ' '.join(L + a[i1:i2] + R)).strip()
                n = re.sub(' +', ' ', ' '.join(L + c[j1:j2] + R)).strip()
                if not o or o == n:
                    continue
                hits = [f for f in files if T[f].count(o) == 1]
                if len(hits) == 1 and sum(T[f].count(o) for f in files) == 1:
                    found = (hits[0], o, n); break
            if found:
                break
        if found:
            f, o, n = found; T[f] = T[f].replace(o, n, 1)
            edits.append(dict(id=f"PXX-{len(edits)+1:02d}", file=f, old=o, new=n, why=f"supervisor tracked change [{num}]"))
        else:
            manual.append((num, ' '.join(a[max(0, i1 - 6):i2 + 3])[:160], ' '.join(c[j1:j2])[:160]))
json.dump(edits, open(outp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"{len(edits)} placed -> {outp} (rename PXX to the patch ID); {len(manual)} need manual placement:")
for x in manual:
    print(x)
