#!/usr/bin/env python3
"""Surgical patcher. Usage: python3 handoff_tools/patch.py patches/<file>.py [--dry]

A patch file defines EDITS = [dict(id, file, old, new, why, count=1), ...].
Every edit is checked first: `old` must occur exactly `count` times in the
file's *current* state (edits apply in order, so later edits see earlier ones).
If any check fails, NOTHING is written and the failures are listed.
On success, each touched file is written once, and a line per edit is
appended to patches/APPLIED.log with before/after md5 of the file.

Gates added 3 Oct 2026:
- An edit ID already in APPLIED.log aborts the run (IDs are never reused).
- Every touched prose file is put through inspector.py's measures. Anything LOST
  (a citation, a number, an article reference, a hedge) aborts the run unless the
  patch declares it in LOST_OK = ["<item as printed>", ...]. Gains are reported only.
  A deliberate removal is then on the record in the patch file itself.
After applying: add the CHANGE_TRAIL row, run handoff_tools/trail_check.py, commit "<ID>: ...".
"""
import hashlib, importlib.util, pathlib, sys, datetime, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import inspector as I

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
    used = set()
    if pathlib.Path('patches/APPLIED.log').exists():
        used = {l.split(' | ')[2].strip() for l in open('patches/APPLIED.log', encoding='utf-8') if l.count(' | ') >= 5}
    fails += [f"{e['id']}: ID already used in APPLIED.log" for e in m.EDITS if e['id'] in used]
    lost_ok = set(getattr(m, 'LOST_OK', []))
    for f in state:
        if not f.endswith('.md'):
            continue
        A = pathlib.Path(f).read_text(encoding='utf-8'); B = state[f]
        lost = []
        for name, fn in (('citation', I.cites), ('number', I.numerals), ('article', I.articles)):
            lost += [f"{name} {k}" for k in (fn(A) - fn(B))]
        ha, hb = I.hedges(A), I.hedges(B)
        lost += [f"hedge {k}" for k in ha if hb.get(k, 0) < ha[k]]
        gained = [f"citation {k}" for k in (I.cites(B) - I.cites(A))] + [f"article {k}" for k in (I.articles(B) - I.articles(A))]
        undeclared = [x for x in lost if x not in lost_ok]
        print(f'INSPECT {f}: lost {len(lost)} ({len(lost) - len(undeclared)} declared), gained {len(gained)}')
        for x in gained: print(f'   + {x}')
        for x in lost: print(f"   - {x}{'' if x in lost_ok else '   <- UNDECLARED'}")
        fails += [f'{f}: lost {x} not declared in LOST_OK' for x in undeclared]
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
    print('NEXT: CHANGE_TRAIL row(s), python3 handoff_tools/assemble.py, python3 handoff_tools/trail_check.py, commit')

if __name__ == '__main__':
    main()
