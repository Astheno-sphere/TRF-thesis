#!/usr/bin/env python3
"""Extract every tracked change and comment from a supervisor's reviewed .docx (Round 4 method, 6 Oct 2026).

    python3 handoff_tools/extract_review.py supervisor_review/<file>.docx supervisor_review/<name>_changes.txt

Writes one block per marked paragraph: OLD (deletions kept, insertions dropped), NEW (insertions kept,
deletions dropped), and the text of every comment anchored in it. Then use locate_edits.py to place them.
"""
import sys, zipfile
from lxml import etree
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q = lambda t: '{%s}%s' % (W, t)
src, out = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src)
doc = etree.fromstring(z.read('word/document.xml'))
com = etree.fromstring(z.read('word/comments.xml')) if 'word/comments.xml' in z.namelist() else None
comments = {c.get(q('id')): ''.join(c.itertext()) for c in com.iter(q('comment'))} if com is not None else {}
def txt(el, mode):
    o = []
    for e in el.iter():
        if e.tag == q('t'):
            if mode == 'old' and q('ins') in [a.tag for a in e.iterancestors()]:
                continue
            o.append(e.text or '')
        elif e.tag == q('delText') and mode == 'old':
            o.append(e.text or '')
    return ''.join(o)
n = 0
with open(out, 'w', encoding='utf-8') as f:
    for p in doc.iter(q('p')):
        has = p.find('.//' + q('ins')) is not None or p.find('.//' + q('del')) is not None
        cids = [c.get(q('id')) for c in p.iter(q('commentRangeStart'))] + [c.get(q('id')) for c in p.iter(q('commentReference'))]
        if not has and not cids:
            continue
        n += 1
        f.write(f"=== [{n}]\n")
        if has:
            f.write("OLD: " + txt(p, 'old') + "\nNEW: " + txt(p, 'new') + "\n")
        else:
            f.write("PARA: " + txt(p, 'new')[:600] + "\n")
        for c in dict.fromkeys(cids):
            f.write(f"COMMENT {c}: {comments.get(c, '')}\n")
    f.write(f"TOTAL {n}\n")
print(f"{n} marked paragraphs, {len(comments)} comments -> {out}")
