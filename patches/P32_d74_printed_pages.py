# P32 — D7.4 page numbers made consistent: the printed page number throughout.
# Checked 4 Oct 2026 against the PDF Tiger uploaded (sources/TEHDAS2_D7.4_v1.2.pdf), page by page:
# the printed number is the PDF page index minus one. EHDSR-6/7/8 (Table 5.1) printed p. 31;
# OPR-6 (Table 5.2) printed p. 43 (already correct); OPR-8 printed p. 46; OPR-17/OPR-18
# (Table 5.4) printed p. 51; Annex 7 open question printed p. 96. The earlier "p. 32"
# (RESEARCH_LOG row 36) was the PDF index, so T-1's original "p. 31" was right.
C1, C2, C4 = "Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter4_TRF_Model_v1.md"
EDITS = [
    dict(id="P32-01", file=C1, old="Table 5.2, OPR-6, p. 43; Annex 7, p. 97)", new="Table 5.2, OPR-6, p. 43; Annex 7, p. 96)", why="printed page"),
    dict(id="P32-02", file=C2, old="collaborative metadata\" (Annex 7, p. 97)", new="collaborative metadata\" (Annex 7, p. 96)", why="printed page"),
    dict(id="P32-03", file=C4, old="(TEHDAS2, 2026, Table 5.4, OPR-18, p. 52); by Proposition 3", new="(TEHDAS2, 2026, Table 5.4, OPR-18, p. 51); by Proposition 3", why="printed page"),
    dict(id="P32-04", file=C4, old="(TEHDAS2, 2026, Table 5.1, EHDSR-7, p. 32)", new="(TEHDAS2, 2026, Table 5.1, EHDSR-7, p. 31)", why="printed page"),
    dict(id="P32-05", file=C4, old="(TEHDAS2, 2026, Table 5.4, OPR-17, p. 52). It sets", new="(TEHDAS2, 2026, Table 5.4, OPR-17, p. 51). It sets", why="printed page"),
    dict(id="P32-06", file=C4, old="| D7.4, Table 5.1, EHDSR-7, p. 32 |", new="| D7.4, Table 5.1, EHDSR-7, p. 31 |", why="printed page"),
    dict(id="P32-07", file=C4, old="| D7.4, Table 5.1, EHDSR-8, p. 32; OPR-18, p. 52 (five years recommended) |", new="| D7.4, Table 5.1, EHDSR-8, p. 31; OPR-18, p. 51 (five years recommended) |", why="printed page"),
    dict(id="P32-08", file=C4, old="| D7.4, Table 5.1, EHDSR-6, p. 32; OPR-8, p. 47 |", new="| D7.4, Table 5.1, EHDSR-6, p. 31; OPR-8, p. 46 |", why="printed page"),
    dict(id="P32-09", file=C4, old="| D7.4, Table 5.4, OPR-17, and OPR-18, p. 52 |", new="| D7.4, Table 5.4, OPR-17, and OPR-18, p. 51 |", why="printed page"),
    dict(id="P32-10", file=C4, old="| D7.4, Table 5.4, OPR-17, p. 52 |", new="| D7.4, Table 5.4, OPR-17, p. 51 |", why="printed page"),
]
LOST_OK = ["number 97", "number 52", "number 32", "number 47"]   # PDF indices replaced by printed page numbers
