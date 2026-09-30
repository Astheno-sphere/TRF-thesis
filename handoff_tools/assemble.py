"""
Rebuild the consolidated bibliography from the chapter reference lists, then the
submission assembly. Run from the outputs directory:  python3 handoff_tools/assemble.py
"""
import re, os

CHS = ["Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter3_Methodology_v1.md",
       "Chapter4_TRF_Model_v1.md", "Chapter5_Demonstration_v1.md", "Chapter6_Discussion_v1.md",
       "Chapter7_Conclusion_v1.md"]
APPS = ["code_artefacts/README_Appendix_A.md", "Appendix_B_Search_Log.md", "Appendix_C_Evaluation_Instrument.md"]

def bibliography():
    label = {f: f"Ch{i+1}" for i, f in enumerate(CHS)}; entries = {}
    for f in CHS:
        m = re.search(r"\n## References[^\n]*\n(.*)$", open(f).read(), re.S)
        if not m: continue
        for line in m.group(1).split("\n"):
            line = line.strip()
            if not line or line.startswith(("#", "*(", "---", ">")) or not re.match(r"^[A-ZÅØÆ]", line): continue
            n = re.sub(r"[^a-z0-9]", "", line.lower())[:60]
            if n in entries:
                p = entries[n]; entries[n] = (p[0] if len(p[0]) >= len(line) else line, p[1] | {label[f]})
            else:
                entries[n] = (line, {label[f]})
    srt = sorted(entries.values(), key=lambda x: re.sub(r"[^A-Za-z]", "", x[0]).lower())
    hdr = open("Consolidated_Bibliography.md").read().split("## References")[0]
    body = "\n".join(f"{t} `{' '.join(f'[{c}]' for c in sorted(ch, key=lambda x: int(x[2:])))}`\n" for t, ch in srt)
    open("Consolidated_Bibliography.md", "w").write(hdr + "## References\n\n" + body + "\n")
    have = sum(1 for t, _ in srt if "doi.org" in t or "http" in t)
    print(f"bibliography: {len(srt)} entries, {have} with DOI/URL")

def submission():
    parts = ["# Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space\n",
             "Arshad Akhtar Abbasia, MSc Sustainable Energy Logistics, Høgskolen i Molde\n",
             "Supervisor: Prof. João Ferreira.\n",
             "Artefact: https://github.com/Astheno-sphere/TRF\n",
             "Demonstration: https://trfhimolde.streamlit.app/\n", "\n---\n",
             open("Front_Matter_v1.md").read(), "\n\\pagebreak\n\n---\n"]
    for f in CHS:
        t = re.split(r"\n---\n\n## References", open(f).read())[0]
        parts.append(re.split(r"\n## References", t)[0].rstrip() + "\n\n\\pagebreak\n\n---\n")
    bib = re.sub(r"`\[Ch[^`]*`", "", open("Consolidated_Bibliography.md").read()).split("## References", 1)[1]
    parts.append("# References\n" + bib.rstrip() + "\n\n\\pagebreak\n\n---\n")
    for a in APPS:
        parts.append(open(a).read().rstrip() + "\n\n\\pagebreak\n\n---\n")
    out = "\n".join(parts); open("VERA-SNARK_Thesis_SUBMISSION.md", "w").write(out)
    print(f"submission: {len(re.findall(r'[A-Za-zÅØÆåøæ0-9]+', out))} words")

if __name__ == "__main__":
    bibliography(); submission()
