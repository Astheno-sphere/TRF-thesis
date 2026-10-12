# P72 — length cut, Ch2 §2.4 (trim 2). The section-closing "Three observations" paragraph re-lists
# and re-cites every system already discussed at length earlier in §2.4 (KONFIDO/Natsiavas,
# ZK-EHR/Albalwy, Health-zkIDM/Bai, zkFL-Health/Sharma, NewbornTime/Brunner, accumulators/Camenisch
# & Lysyanskaya). Keep the three observations as claims, but drop the re-citation list (each cite
# survives at its primary discussion earlier in §2.4) and the re-named systems (each named above),
# replacing with "each reviewed above". The distinctive TEHDAS2 Annex 7 p.96 "named gap" cite is
# KEPT (it is the section's load-bearing close). All dropped cites are declared LOST_OK — the floor
# gate counts the whole-chapter multiset, and every one appears earlier in the chapter.
EDITS = [
 dict(id='P72-01', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""Three observations emerge from this survey. First, the technical components required for a verifiable cryptographic-erasure mechanism for cross-border health audit trails exist in mature form. They include trusted execution environments at the OpenNCP layer, as in KONFIDO (Natsiavas et al., 2021). They include zero-knowledge proof systems applied to healthcare, as in ZK-EHR, Health-zkIDM, and zkFL-Health (Albalwy, 2026; Bai et al., 2022; Sharma et al., 2025). And they include blockchain-anchored consent and audit infrastructures with Norwegian clinical validation, as in NewbornTime (Brunner et al., 2025). They also include cryptographic accumulators with revocation semantics (Camenisch & Lysyanskaya, 2002) and the literature that followed, and a formally grounded cryptographic-erasure foundation. Second, none of these works combines these components to address the specific tension between eHDSI-mandated audit retention, GDPR Article 17 erasure rights, and TEHDAS2 Secure Processing Environment deletion in the cross-border European context. Third, the Joint Action drafting the Secure Processing Environment specification itself records that further guidance is needed on how accountability and anonymisation obligations intersect (TEHDAS2, 2026b, Annex 7, p. 96). The contribution of this thesis is positioned at that named gap.""",
   new=r"""Three observations emerge from this survey. First, the technical components required for a verifiable cryptographic-erasure mechanism for cross-border health audit trails all exist in mature form — trusted execution environments at the OpenNCP layer, zero-knowledge proof systems applied to healthcare, blockchain-anchored consent and audit infrastructures with Norwegian clinical validation, cryptographic accumulators with revocation semantics, and a formally grounded cryptographic-erasure foundation — each reviewed above. Second, none of these works combines these components to address the specific tension between eHDSI-mandated audit retention, GDPR Article 17 erasure rights, and TEHDAS2 Secure Processing Environment deletion in the cross-border European context. Third, the Joint Action drafting the Secure Processing Environment specification itself records that further guidance is needed on how accountability and anonymisation obligations intersect (TEHDAS2, 2026b, Annex 7, p. 96). The contribution of this thesis is positioned at that named gap.""",
   why="de-dup: section-closing summary re-cited/re-named every system already discussed in §2.4; keep the three observations, drop the re-citation list (cites survive earlier) and TEHDAS2 close kept"),
]
# every dropped cite appears earlier in Ch2 at its primary discussion (narrative in §2.4 + Table 2.1
# row), so no reference leaves the chapter or bibliography; the floor gate counts the whole-chapter
# multiset, so each removed form (and each cite's year digit) is a net -1 to declare. NB cites()
# captures a multi-cite parenthetical "(Albalwy, 2026; Bai et al., 2022; Sharma et al., 2025)" as a
# SINGLE key — declared as the group; the three singleton keys in the table are untouched.
LOST_OK = ["citation Natsiavas et al., 2021", "citation Brunner et al., 2025",
 "citation Camenisch & Lysyanskaya, 2002",
 "citation Albalwy, 2026; Bai et al., 2022; Sharma et al., 2025",
 "number 2021", "number 2002", "number 2026", "number 2022", "number 2025"]
