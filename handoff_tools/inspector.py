"""
Integrity inspectors for prose rewriting.
A rewrite is admitted only if EVERY check passes. The rewrite may change sentence
boundaries and wording; it may not change what the thesis claims or cites.
"""
import re, sys, collections

HEDGES = ["contestable","not peer-reviewed","preprint","presumptive","approximately",
 "not established","conditional","does not","cannot","not yet","unverified","unconfirmed",
 "attested","not a proof","corroborat","dispositive","candidate","no requirement",
 "not addressed","not claimed","reduced strength","single-author","industry",
 "narrow","broad reading","not been","inspected","observed","likely","may ","might "]

def body(t):
    return t.split("\n## References")[0]

def cites(t):
    b=body(t)
    paren=re.findall(r"\(([A-ZÅØÆ][^()]{1,120}?(?:n\.d\.|\d{4}[a-z]?))\)", b)
    # narrative form: Author (year) / Author et al. (year) / Author and Author (year)
    narr=re.findall(r"([A-ZÅØÆ][A-Za-zÅØÆåøæ'\-]+(?:\s+et al\.)?(?:,?\s+(?:and|&)\s+[A-ZÅØÆ][A-Za-zÅØÆåøæ'\-]+)?)\s+\((\d{4}[a-z]?)\)", b)
    return collections.Counter(paren + [f"{a} ({y})" for a,y in narr])

def numerals(t):
    return collections.Counter(re.findall(r"\b\d[\d,.]*\b", body(t)))

def articles(t):
    # article number with optional paragraph and point, nothing else
    return collections.Counter(re.findall(r"(?:Articles?|Art\.)\s*(\d+(?:\(\d+\))?(?:\([a-z]\))?)", body(t)))

def hedges(t):
    b=body(t).lower(); return {h: b.count(h) for h in HEDGES}

def refs_section(t):
    return t.partition("\n## References")[2]

def sentences(t):
    b=re.sub(r"^\s*(#|\||>|```|\$\$|-\s).*$","",body(t),flags=re.M)
    s=[x for x in re.split(r"(?<=[.!?])\s+", b) if len(x.split())>3]
    return [len(x.split()) for x in s]

def inspect(before, after, label=""):
    A,B=open(before).read(),open(after).read()
    ok=True; out=[]
    def chk(name, a, b, strict=True):
        nonlocal ok
        good = (a==b)
        if not good: ok=False
        out.append(f"  [{'PASS' if good else 'FAIL'}] {name}")
        if not good:
            if isinstance(a,collections.Counter):
                lost=a-b; gained=b-a
                if lost: out.append(f"         lost:   {dict(list(lost.items())[:6])}")
                if gained: out.append(f"         gained: {dict(list(gained.items())[:6])}")
            elif isinstance(a,dict):
                for k in a:
                    if a[k]!=b.get(k): out.append(f"         '{k}': {a[k]} -> {b.get(k)}")
    chk("citations identical (every (Author, year) preserved)", cites(A), cites(B))
    chk("numerals identical (every number, date, figure)", numerals(A), numerals(B))
    chk("article references identical", articles(A), articles(B))
    ha,hb=hedges(A),hedges(B)
    lost=[k for k in ha if hb.get(k,0)<ha[k]]
    good=not lost
    if not good: ok=False
    out.append(f"  [{'PASS' if good else 'FAIL'}] hedges not weakened (none may decrease)")
    for k in lost: out.append(f"         '{k}': {ha[k]} -> {hb.get(k,0)}")
    chk("reference list untouched", refs_section(A), refs_section(B))
    sa,sb=sentences(A),sentences(B)
    la=sum(1 for x in sa if x>40); lb=sum(1 for x in sb if x>40)
    out.append(f"  [INFO] sentences >40 words: {la} -> {lb} | mean length {sum(sa)/len(sa):.1f} -> {sum(sb)/len(sb):.1f}")
    out.append(f"  [INFO] words: {sum(sa)} -> {sum(sb)}")
    print(f"=== INSPECTION {label} ===");print("\n".join(out))
    print(f"  VERDICT: {'ADMIT' if ok else 'REJECT'}")
    return ok

if __name__=="__main__":
    sys.exit(0 if inspect(sys.argv[1],sys.argv[2],sys.argv[3] if len(sys.argv)>3 else "") else 1)
