#!/usr/bin/env python3
"""Surgical patcher. Usage: python3 handoff_tools/patch.py patches/<file>.py [--dry]

A patch file defines EDITS = [dict(id, file, old, new, why, count=1), ...].
Every edit is checked first: `old` must occur exactly `count` times in the
file's *current* state (edits apply in order, so later edits see earlier ones).
If any check fails, NOTHING is written and the failures are listed.
On success, each touched file is written once, and a line per edit is
appended to patches/APPLIED.log with before/after md5 of the file.
"""
import hashlib, importlib.util, pathlib, sys, datetime

def md5(b): return hashlib.md5(b.encode() if isinstance(b, str) else b).hexdigest()[:12]

def main():
    pf = pathlib.Path(sys.argv[1]); dry = '--dry' in sys.argv
    spec = importlib.util.spec_from_file_location('p', pf); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    state, before, fails, log = {}, {}, [], []
    for e in m.EDITS:
        f = e['file']
        if f not in state:
            state[f] = pathlib.Path(f).read_text(encoding='utf-8'); before[f] = md5(state[f])
        n = state[f].count(e['old']); want = e.get('count', 1)
        if n != want:
            fails.append(f"{e['id']}: {f} expected {want} match(es), found {n}"); continue
        state[f] = state[f].replace(e['old'], e['new'])
        log.append((e['id'], f, e['why']))
    if fails:
        print('ABORTED, nothing written:'); [print('  ' + x) for x in fails]; sys.exit(1)
    if dry:
        print(f'DRY RUN OK: {len(log)} edits across {len(state)} files'); return
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    with open('patches/APPLIED.log', 'a', encoding='utf-8') as L:
        for f, t in state.items():
            pathlib.Path(f).write_text(t, encoding='utf-8')
        for i, f, why in log:
            L.write(f"{ts} | {pf.name} | {i} | {f} | {before[f]} -> {md5(state[f])} | {why}\n")
    print(f'APPLIED {len(log)} edits across {len(state)} files'); [print(f'  {f}: {before[f]} -> {md5(t)}') for f, t in state.items()]

if __name__ == '__main__':
    main()
