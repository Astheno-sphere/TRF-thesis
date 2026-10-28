# P85 — CONTENT STRENGTHENING, Ch4 §4.9 (R4 residue flank). Adds the current, final EU authority on the
# anonymity threshold — EDPB Guidelines 02/2026 on Anonymisation (Version 1.0, adopted 7 July 2026) —
# alongside the existing Datatilsynet (2015) grounding, in "The limit" paragraph. Hardens the exact flank
# examiners probe (is the surviving residue still personal data?) with the latest standard, and confirms
# the thesis's existing "pseudonymised not anonymous" characterisation. Accurate to the Guidelines:
# the three-criteria test (resist record isolation, linkage, inference by means reasonably likely to be
# used) and that encryption is by nature reversible and is not anonymisation (para 91). ADDITION; no claim
# removed. Reference entry added as EDPB (2026c) — label free for this author.
EDITS = [
 dict(id='P85-01', file='Chapter4_TRF_Model_v1.md',
   old=r"""The residue therefore does not meet the strict Norwegian anonymisation threshold. Datatilsynet's guidance holds that encryption protects rather than anonymises, and that data remain personal while any key or linkage capable of re-identification is retained (Datatilsynet, 2015). By that standard the residue, which keeps metadata identifying the access event, is best characterised as pseudonymised rather than anonymous until the terminal transition.""",
   new=r"""The residue therefore does not meet the strict Norwegian anonymisation threshold. Datatilsynet's guidance holds that encryption protects rather than anonymises, and that data remain personal while any key or linkage capable of re-identification is retained (Datatilsynet, 2015). The European Data Protection Board's Guidelines 02/2026 on anonymisation, adopted on 7 July 2026, set the same bar at Union level: data count as anonymous only where they resist record isolation, linkage and inference by means reasonably likely to be used, and the Guidelines hold that encryption is by its nature reversible and is not anonymisation, so that technical protection alone does not place data beyond the reach of the definition (European Data Protection Board, 2026c). By that standard the residue, which keeps metadata identifying the access event, is best characterised as pseudonymised rather than anonymous until the terminal transition.""",
   why="strengthen R4 residue flank with the current EU anonymisation standard (EDPB Guidelines 02/2026), alongside Datatilsynet; confirms the pseudonymised-not-anonymous framing"),
 dict(id='P85-02', file='Chapter4_TRF_Model_v1.md',
   old=r"""European Data Protection Board. (2026b). *Guidelines 02/2025 on processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB. https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf""",
   new=r"""European Data Protection Board. (2026b). *Guidelines 02/2025 on processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB. https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf

European Data Protection Board. (2026c). *Guidelines 02/2026 on anonymisation* (Version 1.0, adopted 7 July 2026). EDPB. https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf""",
   why="add the EDPB Guidelines 02/2026 on anonymisation reference entry (EDPB 2026c)"),
]
# Adding a reference entry changes the reference-list section; declare it (this is an ADDITION, a gain,
# not a loss of an existing reference).
LOST_OK = ["reference list changed"]
