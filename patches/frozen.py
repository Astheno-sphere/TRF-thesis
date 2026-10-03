"""Freeze a generated patch's edits so the patch can be replayed and audited after it is applied.

A patch that computes its EDITS from the files at import time finds nothing to do once applied,
which made trail_check's base-diff replay blind to it (found 3 Oct, B-26). Generated patches now
call freeze(name, compute): the first call computes the edits and writes patches/<name>.edits.json;
every later import loads that file. The JSON is the record; the compute function is how it was made.
"""
import json, pathlib, subprocess

HERE = pathlib.Path(__file__).resolve().parent


def freeze(name, compute):
    p = HERE / f"{name}.edits.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    edits = compute()
    p.write_text(json.dumps(edits, ensure_ascii=False, indent=1), encoding="utf-8")
    return edits


def at(ref, path):
    """A file's text at a git ref (used to rebuild edits for patches applied before freezing)."""
    return subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True,
                          cwd=HERE.parent, check=True).stdout
