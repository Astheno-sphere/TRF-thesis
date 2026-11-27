"""Neutralise context leaks in the anonymised review archive (prose only, code fences untouched)."""
import re, sys, pathlib
ROOT = pathlib.Path(sys.argv[1])
MD = ["README.md", "README_REVIEW.md", "docs/Appendix_A.md", "docs/Data_Provenance_Statement.md",
      "docs/VERSION_RECORD.md", "data/synthea_subset/README.md"]
LINE_SUBS = [  # (pattern, replacement) applied to prose lines, in order
    (r"Executable artefact for the MSc thesis \*Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space\* \(\[anonymised for review\]\)\.",
     "Executable artefact accompanying the submitted article (anonymised for review)."),
    (r"^\*Thesis:\* Verifiable Crypto-Erasure.*$", "*Study:* [title withheld for review]"),
    (r"The artefact is publicly available in two forms\.", "The artefact exists in two forms (identifiers withheld for review)."),
    (r"version 1\.3\.0 of the repository, deposited in a public archive,", "version 1.3.0 of the repository"),
    (r"from a fresh clone of the public repository", "from a fresh clone of the repository"),
    (r"Code and documents pushed to GitHub; demonstration deployed", "Code and documents released (details withheld for review)"),
    (r"on WSL or on a university terminal", "on WSL or on any other Linux machine"),
    (r"Every change to the code is logged in \[`CHANGE_TRAIL\.md`\]\(CHANGE_TRAIL\.md\), with the tests that gate it\. Releases are archived in a public repository \(identifier withheld for review\)\.",
     "Every change to the code is logged in a change trail, with the tests that gate it; the trail is withheld from the review archive."),
    (r"`CHANGE_TRAIL\.md` \(R- identifiers\) and in the thesis's own change trail\.",
     "a change trail withheld from the review archive."),
    (r"MSc thesis", "study"),
    (r"[Tt]hesis repository", "source repository"),
    (r"thesis seed", "reference seed"),
    (r"no thesis figure", "no reported figure"),
    (r"thesis figures?", "reported figures"),
    (r"thesis result", "reported result"),
    (r"thesis claim", "reported claim"),
    (r"The Thesis run page", "The reference-run page"),
    (r"\b[Tt]his thesis\b", "this study"),
    (r"\b[Tt]he thesis's\b", "the study's"),
    (r"\b[Tt]hesis's\b", "study's"),
    (r"\bthe thesis\b", "the study"),
    (r"\bThe thesis\b", "The study"),
    (r"\bthesis\b", "study"),
    (r"\bThesis\b", "Study"),
]
DROP = [r"^\*Supervisor:\*"]
for rel in MD:
    p = ROOT / rel
    out, fence = [], False
    for line in p.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("```"):
            fence = not fence; out.append(line); continue
        if not fence:
            if any(re.search(d, line) for d in DROP):
                continue
            for pat, rep in LINE_SUBS:
                line = re.sub(pat, rep, line)
        out.append(line)
    p.write_text("".join(out), encoding="utf-8")
# Title in the checker docstring and its verbatim listing (line count preserved)
OLD = ("Thesis: Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails\n"
       "        under the European Health Data Space.\n")
NEW = "Study: [title withheld for review].\n\n"
for rel in ["trf_checker.py", "docs/Appendix_A.md"]:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    assert s.count(OLD) == 1, rel
    p.write_text(s.replace(OLD, NEW), encoding="utf-8")
print("done")
