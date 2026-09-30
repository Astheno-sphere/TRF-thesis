import re, sys
GREEK = {"α": r"\alpha", "δ": r"\delta", "π": r"\pi", "σ": r"\sigma", "ι": r"\iota"}
SYM = {"∈": r"\in", "≤": r"\le", "≥": r"\ge", "∞": r"\infty", "ℕ": r"\mathbb{N}", "δ": r"\delta"}
SETS = {"{0, 1}": r"\{0, 1\}",
        "{primary, secondary}": r"\{\text{primary}, \text{secondary}\}",
        "{C1, C2, C3}": r"\{C1, C2, C3\}"}
L, R = "⟪", "⟫"
LET = "A-Za-zαδπσι"
ATOM = re.compile(r"\*([" + LET + r"])\*(ᴵᴵ|ᴵ|ᵣ|π|\\\*)?(\((\*[" + LET + r"]\*(?:\\\*|′)?(?:,\s*\*[" + LET + r"]\*(?:\\\*|′)?)*)\))?")

def tok(c): return GREEK.get(c, c)

def atom(m):
    base, mod, args = tok(m.group(1)), m.group(2), m.group(4)
    base += {"ᵣ": "_r", "π": r"_\pi", "ᴵ": "^{I}", "ᴵᴵ": "^{II}", "\\*": "^{*}"}.get(mod, "")
    if args:
        parts = []
        for a in re.split(r",\s*", args):
            mm = re.match(r"\*([" + LET + r"])\*(\\\*|′)?", a)
            p = tok(mm.group(1)) + {"\\*": "^{*}", "′": "'"}.get(mm.group(2), "")
            parts.append(p)
        base += "(" + ",".join(parts) + ")"
    return L + base + R

JOIN = r"[\s0-9+\-=<>(),]*"
MERGE = re.compile(re.escape(L) + r"[^⟪⟫]*" + re.escape(R) +
                   r"(?:" + JOIN + re.escape(L) + r"[^⟪⟫]*" + re.escape(R) + r")*" +
                   r"(?:\s*[+\-=<>]\s*[0-9]+)?")

def merge(m):
    inner = re.sub(r"\s+", " ", m.group(0).replace(L, "").replace(R, "")).strip()
    return "$" + inner + "$"

def convert_line(ln):
    if ln.lstrip().startswith(("#", "|", "```", "$$")) or "$" in ln:
        return ln
    s = ATOM.sub(atom, ln)
    for k, v in SETS.items(): s = s.replace(k, L + v + R)
    for k, v in SYM.items(): s = s.replace(k, L + v + R)
    s = MERGE.sub(merge, s)
    return s.replace(L, "$").replace(R, "$")

if __name__ == "__main__":
    src = open(sys.argv[1]).read()
    body, sep, refs = src.partition("\n## References")
    open(sys.argv[2], "w").write("\n".join(convert_line(l) for l in body.split("\n")) + sep + refs)
