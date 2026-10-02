#!/usr/bin/env python3
"""Check the chapter files against the draft the supervisor reviewed.

Usage: python3 handoff_tools/verify_base.py

Renders every markdown block of the front matter and chapters to plain text with pandoc,
compares prose lines (8+ words) against supervisor_review/draft_as_reviewed_tracked_rejected.txt,
and reports every line whose wording differs. Layout-only artefacts are filtered: TOC page
numbers, title-page fields, chapter reference-list variants (the draft has one consolidated
bibliography), equation spacing, and the hand-written contents list that Word's TOC replaces.

On the base (tag joao-base-v1) the expected result is: 0 wording differences.
After patching, every difference listed should correspond to a logged patch.
"""
import difflib, re, subprocess, sys

DRAFT = "supervisor_review/draft_as_reviewed_tracked_rejected.txt"
FILES = ["Front_Matter_v1.md", "Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md",
         "Chapter3_Methodology_v1.md", "Chapter4_TRF_Model_v1.md", "Chapter5_Demonstration_v1.md",
         "Chapter6_Discussion_v1.md", "Chapter7_Conclusion_v1.md"]


def norm(s):
    s = s.replace(" ", " ").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-")
    s = re.sub(r"^\s*(\d+\.|[-*•])\s+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def squash(s):  # ignore spacing differences inside maths and numbering
    return re.sub(r"[\s\d.]", "", s)


def is_artefact(f, s):
    if re.match(r"^[A-ZÅØÆ].{1,160}?\((\d{4}[a-z]?|n\.d\.)\)\.", s):  # reference-list entry
        return True
    if re.search(r"\^\(|_\(|[∀≤≥]", s):  # rendered equation
        return True
    if f == "Front_Matter_v1.md" and (s.startswith(("A Design Science Study", "Master of Science"))
                                      or re.match(r"^(Introduction|Literature Review|Methodology and|The Tri-Lateral|Demonstration|Discussion|Conclusion|Appendix [ABC])[^:]{0,90}:", s)):
        return True
    return False


def collect():
    """Return (prose lines checked, differences as (file, ours, closest draft line), missing draft lines)."""
    md_lines = []
    for f in FILES:
        for block in open(f, encoding="utf-8").read().split("\n\n"):
            if block.lstrip().startswith(("|", "```", "    ")):
                continue
            plain = subprocess.run(["pandoc", "-f", "markdown", "-t", "plain", "--wrap=none"],
                                   input=block, capture_output=True, text=True).stdout
            for ln in plain.split("\n"):
                n = norm(ln)
                if len(n.split()) >= 8:
                    md_lines.append((f, n))
    draft = [norm(l) for l in open(DRAFT, encoding="utf-8").read().split("\n")]
    draft = [d for d in draft if len(d.split()) >= 8]
    dset = set(draft)
    dsq = {squash(d) for d in draft}
    diffs = []
    for f, s in md_lines:
        s2 = re.sub(r"^Chapter \d+\. ", "", s)
        if s in dset or s2 in dset or squash(s) in dsq or is_artefact(f, s):
            continue
        best = difflib.get_close_matches(s, draft, n=1, cutoff=0.55)
        diffs.append((f, s, best[0] if best else None))
    mset = {s for _, s in md_lines}
    missing = [d for d in draft if d not in mset and squash(d) not in {squash(s) for s in mset}
               and len(d.split()) >= 12 and not re.search(r"\s\d{1,3}$", d)]
    return md_lines, diffs, missing


def main():
    md_lines, diffs, missing = collect()
    print(f"prose lines checked: {len(md_lines)} | wording differences: {len(diffs)}")
    for f, s, d in diffs:
        print(f"\n[{f}]\n  ours : {s[:220]}\n  draft: {(d or '(no counterpart)')[:220]}")
    print(f"\ndraft prose lines (12+ words) with no counterpart in the chapters: {len(missing)}"
          " (tables, code and appendix text are expected here)")
    sys.exit(0)


if __name__ == "__main__":
    main()
