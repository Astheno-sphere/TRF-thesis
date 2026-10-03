# P20 — M5e: Table 2.1 split into bands so that unreviewed sources do not sit as rows among
# peer-reviewed systems. Band 3 holds the arXiv preprint (Sharma et al., 2025), the ePrint SoK
# (Aikebaier, 2026) and the practitioner pattern (VeritasChain, 2026). Also: the SPUHiN row still
# read "Norwegian policy, final" (P10's grep looked for "finalis", missed "final"), now "hearing version".
import pathlib
C2 = "Chapter2_LitReview_v2_FINAL.md"
t = pathlib.Path(C2).read_text(encoding="utf-8")
rows = {k: next(l for l in t.split("\n") if l.startswith(k)) for k in
        ["| KONFIDO", "| ZK-EHR", "| Health-zkIDM", "| zkFL-Health", "| NewbornTime", "| SPUHiN D5.2", "| Ledger crypto-erasure", "| Practitioner crypto-shredding"]}
old_block = "\n".join(rows[k] for k in rows)
band = lambda s: f"| ***{s}*** | | | | | | |"
spuhin = rows["| SPUHiN D5.2"].replace("| Yes — Norwegian policy, final |", "| Yes — Norwegian policy, hearing version |")
assert spuhin != rows["| SPUHiN D5.2"]
new_block = "\n".join([band("Peer-reviewed systems"), rows["| KONFIDO"], rows["| ZK-EHR"], rows["| Health-zkIDM"], rows["| NewbornTime"],
                       band("National policy framework"), spuhin,
                       band("Preprints and practitioner sources (not peer-reviewed; compared for position only)"),
                       rows["| zkFL-Health"], rows["| Ledger crypto-erasure"], rows["| Practitioner crypto-shredding"]])
EDITS = [
    dict(id="P20-01", file=C2, old=old_block, new=new_block,
         why="M5e: three bands; preprint and practitioner sources separated; SPUHiN row 'final' corrected (M5b residue)"),
    dict(id="P20-02", file=C2,
         old="The table makes the position of the contribution explicit against both its architectural and its analytical neighbours.",
         new="The table makes the position of the contribution explicit against both its architectural and its analytical neighbours. Rows in the third band are not peer-reviewed; they are compared for the position they occupy, and no claim of the thesis rests on any of them alone.",
         why="M5e: what the third band may and may not carry"),
]
if __name__ == "__main__":
    print(new_block)
