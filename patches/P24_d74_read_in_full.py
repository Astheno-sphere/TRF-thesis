# P24 — TIGER_TASKS T-1: D7.4 v1.2 (24 Feb 2026) read in full from the file Tiger supplied
# (supervisor_review/../sources: see RESEARCH_LOG row 36). Results:
#   EHDSR-6/7/8 in Table 5.1 on p. 32 (not 31); OPR-6 in Table 5.2 on p. 43, and its sentence goes on:
#   "while ensuring compliance with applicable legal obligations and traceability or reproducibility
#   requirements where relevant"; its rationale: "The deletion and retention policy should balance
#   these obligations with the mandate to securely terminate the SPE." OPR-8 (p. 47): logs retained
#   for traceability, "protected against tampering" (rationale, ISO/IEC 27002). OPR-17 (p. 52):
#   logging must cover "access to electronic health data", be "proportionate, risk-based, and
#   technically feasible", and "avoid unnecessary collection of detailed user behaviour".
#   OPR-18 (p. 52): one year minimum, "longer retention (5 years) is recommended". Annex 7 (p. 97):
#   "This raises open questions about how accountability and anonymisation obligations intersect.
#   Further guidance will be needed on retention of project-level collaborative metadata."
#   No requirement anywhere on log granularity (searched: record-level, patient-level, individual level).
# Corrections: the gap claim in Ch1/Ch2 said the Joint Action's guidance contained "no treatment" of
# the collision; D7.4 acknowledges a deletion–retention balance and names an open question, without a
# mechanism. The claim is restated precisely, and it is stronger for it.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze, at
PRE = "8364256"
C1, C2, C4 = "Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter4_TRF_Model_v1.md"


def row(text, prefix):
    return next(l for l in text.split("\n") if l.startswith(prefix))


def compute():
    c4 = at(PRE, C4)
    r_opr6 = row(c4, '| Same, "deleted or rendered unrecoverable')
    r_e7, r_e8, r_e6 = row(c4, '| "All SPE logs MUST identify the actor"'), row(c4, '| "All SPE logs MUST be kept at least'), row(c4, "| Logs available for verification")
    new_rows = "\n".join([
        r_opr6.replace("TEHDAS2 D7.4, Table 5.2, OPR-6 (page to confirm)", "TEHDAS2 D7.4, Table 5.2, OPR-6, p. 43"),
        r_e7.replace("D7.4, Table 5.1, EHDSR-7 (page to confirm)", "D7.4, Table 5.1, EHDSR-7, p. 32"),
        r_e8.replace("D7.4, Table 5.1, EHDSR-8 (page to confirm)", "D7.4, Table 5.1, EHDSR-8, p. 32; OPR-18, p. 52 (five years recommended)")
            .replace("| Floor parameter $F = 12$ |", "| Floor parameter $F = 12$; any longer value is a parameter change (Corollary 2.2) |"),
        r_e6.replace("D7.4, Table 5.1, EHDSR-6 (page to confirm)", "D7.4, Table 5.1, EHDSR-6, p. 32; OPR-8, p. 47"),
        "| Logs protected against tampering | D7.4, Table 5.4, OPR-17, and OPR-18, p. 52 | Append-only Merkle log; an altered entry fails its inclusion proof | `MerkleLog`, `integrity()` | Met in the artefact (both tamper tests fail $V^{II}$) |",
        "| Logging proportionate; no unnecessary detail on user behaviour; must cover access to electronic health data | D7.4, Table 5.4, OPR-17, p. 52 | Accessor fields kept; subject fields only where the log is kept per patient record, and removed at the ceiling | §4.3, §4.10 Rival 3 | Met by specification; granularity is the operator's choice, which the specification leaves open |",
        "| Deletion \"while ensuring compliance with applicable legal obligations and traceability or reproducibility requirements\"; the deletion and retention policy to \"balance these obligations\" | D7.4, Table 5.2, OPR-6, p. 43 | Supplies the balance for the logs: what accountability needs is kept, what the ceiling reaches is invalidated | §4.7, §4.8 | Met by specification: the specification asks for the balance and leaves its form open |",
    ])
    old_rows = "\n".join([r_opr6, row(c4, "| Identifiable logs of access and activities"), r_e7, r_e8, r_e6])
    new_block = new_rows.split("\n")
    # keep the Art 73(1)(e) row in its place (second)
    new_block.insert(1, row(c4, "| Identifiable logs of access and activities"))
    return [
        dict(id="P24-01", file=C4, old=old_rows, new="\n".join(new_block),
             why="T-1: D7.4 page numbers; three rows added (OPR-8/17/18 tamper protection, OPR-17 proportionality, OPR-6 balance)"),
        dict(id="P24-02", file=C4,
             old="It lists only requirements this thesis has read in the source; the specification's page references are to be confirmed against the published PDF.",
             new="It lists only requirements this thesis has read in the source, with the page of the specification (TEHDAS2, 2026) where it applies.",
             why="T-1 done"),
        dict(id="P24-03", file=C4, old="(TEHDAS2, 2026, Table 5.1, EHDSR-7)", new="(TEHDAS2, 2026, Table 5.1, EHDSR-7, p. 32)", why="T-1 page"),
        dict(id="P24-04", file=C4, old="(TEHDAS2, 2026, Table 5.2, OPR-6).",
             new="(TEHDAS2, 2026, Table 5.2, OPR-6, p. 43). The same requirement continues: deletion must proceed \"while ensuring compliance with applicable legal obligations and traceability or reproducibility requirements where relevant\", and its rationale leaves it to \"the deletion and retention policy\" to \"balance these obligations\". The specification asks for the balance and does not say how it is struck; for the logs, this mechanism is one way to strike it.",
             why="T-1: OPR-6 read in full; the specification itself names the balance the mechanism supplies"),
        dict(id="P24-05", file=C4,
             old="The version of the specification inspected requires logs to identify the actor and states no requirement for patient-level logging (TEHDAS2, 2026).",
             new="The specification requires logs to identify the actor and to cover \"access to electronic health data\", and requires logging to be \"proportionate, risk-based, and technically feasible\" and to \"avoid unnecessary collection of detailed user behaviour not required for auditability or misuse detection\" (TEHDAS2, 2026, Table 5.4, OPR-17, p. 52). It sets no requirement on the granularity of logs, which leaves the choice, and with it Corollary 1.2, to the operator.",
             why="T-1: OPR-17 read; granularity checked (no requirement anywhere in the document)"),
        dict(id="P24-06", file=C4,
             old="this being the one-year minimum imposed by Article 73(1)(e) of Regulation (EU) 2025/327 (European Parliament and Council of the European Union, 2025).",
             new="this being the one-year minimum imposed by Article 73(1)(e) of Regulation (EU) 2025/327 (European Parliament and Council of the European Union, 2025). The Joint Action's specification recommends five years (TEHDAS2, 2026, Table 5.4, OPR-18, p. 52); by Proposition 3 a longer floor enlarges the set of records whose permit expiry falls inside it, and by Corollary 2.2 no result depends on the value.",
             why="T-1: OPR-18 five-year recommendation"),
        dict(id="P24-07", file=C1,
             old="yet the review conducted for this thesis found no treatment of it, including in the guidance published by the Joint Action drafting the specifications for both provisions.",
             new="yet the review conducted for this thesis found no treatment of it in the literature. The Joint Action's specification for these environments comes closest: it requires deletion at permit expiry \"while ensuring compliance with applicable legal obligations and traceability or reproducibility requirements\", leaves the balance to each operator's policy, and in its expert commentary names \"open questions about how accountability and anonymisation obligations intersect\" (TEHDAS2, 2026, Table 5.2, OPR-6, p. 43; Annex 7, p. 97). It asks for the balance; it does not supply one.",
             why="T-1: the gap claim corrected and sharpened; the Joint Action names the open question"),
        dict(id="P24-08", file=C2,
             old="requires no synthesis across instruments of differing legal weight and no interpretive work by this author: it is stated by one regulation, in adjacent articles of one chapter, about one environment. The review conducted for this thesis located no treatment of it: not in the academic literature, not in the professional commentary on EHDS secondary use, and not in the guidance published by the Joint Action drafting the specifications for both provisions.",
             new="requires no synthesis across instruments of differing legal weight: on the broad reading, for logs kept at patient-record granularity, it is stated by one regulation, in adjacent articles of one chapter, about one environment. The review conducted for this thesis located no treatment of it in the academic literature or in the professional commentary on EHDS secondary use. The Joint Action drafting the specifications comes closest. Its specification requires deletion at permit expiry \"while ensuring compliance with applicable legal obligations and traceability or reproducibility requirements where relevant\" and leaves \"the deletion and retention policy\" to \"balance these obligations\" (TEHDAS2, 2026, Table 5.2, OPR-6, p. 43). Its expert commentary goes further: log keeping \"raises open questions about how accountability and anonymisation obligations intersect\", and \"further guidance will be needed on retention of project-level collaborative metadata\" (Annex 7, p. 97). The body drafting the requirements names the question; no mechanism answering it has been published.",
             why="T-1: 'no interpretive work' overclaimed after D-16; 'not in the Joint Action guidance' corrected; corroboration from the Joint Action itself"),
    ]


EDITS = freeze("P24_d74_read_in_full", compute)

# "inspected" hedged a claim read through a summarising fetch; the document has now been read in full
# and searched for any log-granularity requirement (none), so the claim is stated as checked.
LOST_OK = ["hedge inspected"]
