# Review Tracker — Prof. Ferreira, 30 Sept 2026

One row per item in the emailed review (`supervisor_review/review_email_text_2026-09-30.txt`).
`handoff_tools/trail_check.py` reads this table. Rules it enforces:

- Status is one of `OPEN`, `BLOCKED`, `PARTIAL`, `CLOSED`, `DECLINED`.
- A `CLOSED` or `PARTIAL` row must name at least one patch ID, and every ID named must exist in `patches/APPLIED.log`.
- A `CLOSED` row whose guard (in `handoff_tools/guards.json`, `item` field) has not reached its goal is an error.
- `DECLINED` needs a reason in Evidence: we answer his point with evidence, we do not ignore it.

His authority is the emailed text. His tracked changes in the returned .docx are proposals, judged
passage by passage when the patch for that passage is written.

| Item | What he asked | Status | Patches | Evidence / note |
|---|---|---|---|---|
| M1 | Define p(a) per record class from the eHDSI audit spec and D7.4; revise the SPE record model in code | CLOSED | P04, P06, P12, P14, P42, P43 | SPE p(a) fields named and tied to D7.4 OPR-17; cross-border p(a) tied to ITI-55 and the patient-identification step, eHDSI audit spec stated as not obtained; Semantics I reframed as the semantics of a log that keeps its payload readable, no current-practice claim (P42); Synthea payloads stated as stand-ins (P43) |
| M2a | One reading of Art 68(12) carried through Cor 1.2, Thm 2, §4.8 | CLOSED | P04, P05, P07, P42 | Ceiling = electronic health data at every site; §6.2 consistent with Rival 6; §5.4 notes relocation removes the 39 (P42) |
| M2b | Rival 6: move the logs out of the SPE at permit closure | CLOSED | P06 | Rival 6 accepted for the ceiling and bounded by Proposition L (P06). Ch6/Ch7 echo in P07 |
| M2c | Rewrite §6.1's opening; lead with the robust result | CLOSED | P07 | §6.1 leads with the robust result, then Proposition L, then the conditional SPE instance |
| M3a | Salt: text, code and change record agree | CLOSED | P02 | D-15: salt destroyed (Tiger, 22 Sept). Text in §4.8/§5.6/§4.9 must follow the code |
| M3b | Ciphertext: delete at invalidation or justify | CLOSED | P02, P12 | Text (P02) and code (P12): ciphertext deleted at invalidation |
| M3c | Remove the dead salt branch; seeded generator or `--reproducible` | CLOSED | P12 | make_salt() and --random-salts; dead branch gone (guard 1 → 0) |
| M4a | Theorems renamed Propositions; weight on the §4.2 necessity analysis | CLOSED | P15, P16, P17, P18, P42, P44 | 'propositions rather than theorems' (P42); repo README Propositions (P44, public R-26) |
| M4b | Promote the §6.9a anchoring result into Ch4 as a formal result | CLOSED | P15 | Proposition 3 in Ch4 §4.6, stated precisely (collision needs L ≤ F; anchor decides visibility); §6.9a corrected |
| M4c | V_II tests integrity: hash chain over m(a), ι(a); tamper test | CLOSED | P12, P14 | Merkle log (RFC 6962), inclusion proofs in V_II, two tamper tests fail V_II; reported in §5.6 |
| M4d | Shorten Ch5; violation rates are generator artefacts | PARTIAL | P31, P43, P46 | Rate interpretation removed (§5.3, §5.4); repetition cut. Ch5 is about 4,000 words against 3,386 in the reviewed draft because of the integrity and envelope-encryption results he asked for in M4c/M3b |
| M5a | Ten-year floor: primary eHDSI source with section, or F=120 illustrative | CLOSED | P09, P42, P44 | Ten-year floor 'as reported' and illustrative at every site, code comment included |
| M5b | SPUHiN "finalised" claims aligned to what was inspected | CLOSED | P10 | Every claim limited to the hearing version inspected (P10, P10b) |
| M5c | Art 68(12) and Art 73(1)(e) quoted verbatim (OJ English); one more language version | PARTIAL | P04, P07, P08, P42 | Art 68(12) and Art 73(1)(e) both verbatim from the OJ English text (P42). Open: one further language version (his 'ideally'; T-10) |
| M5d | §2.2 EHDS dates fixed against Art 105; drop the EY source | CLOSED | P03 | Arts 19(1), 105(1)(a) verified 3 Oct |
| M5e | Table 2.1: preprint/practitioner sources in a separate band; Feng et al. 2022 peer-reviewed version? | CLOSED | P09, P20 | Feng peer-reviewed (P09); Table 2.1 bands (P20) |
| M6a | Traceability matrix against D7.4 and the SPUHiN checklist | PARTIAL | P22, P24 | D7.4 traced row by row in Table 4.1. Open: the SPUHiN checklist row by row needs the hearing-version checklist file, which is not in the working sources |
| M6b | Reword Appendix C item A1 ("full confidence"), record in one line | CLOSED | P19 | A1 reworded; one-line record in Appendix C |
| M7a | Logistics anchor (UCC customs record-keeping vs destruction orders); §1.4 overreach | CLOSED | P11, P43 | UCC anchor; seafarer and OECD material cut; §1.4 overreach rewritten (P43) |
| M7b | One sentence in §1.5 on the programme fit | CLOSED | P11 | One sentence in §1.5 |
| MIN-01 | §3.6 line counts inverted (checker 363, layer 152) | CLOSED | P01 | Prose now points to Table 5.0a; the code wave must update Table 5.0a, Table F.2 and Appendix A counts |
| MIN-02 | §3.6 "tuples defined in Section 3.4" → 4.3 | CLOSED | P01 |  |
| MIN-03 | §1.6 drop "accumulator-based" | CLOSED | P01 |  |
| MIN-04 | §2.1.4 "four dated rounds" vs Appendix B five | CLOSED | P01 | Fork R1 merged rounds to 7 on the superseded branch; re-judge |
| MIN-05 | §3.4 / Cor 1.1 "ordinary"/"generic case" are frequency claims; soften | CLOSED | P21 | §3.4, Cor 1.1, Ch4 summary |
| MIN-06 | §4.4 C1 closed window spans F+1 months | CLOSED | P21 | Closed window justified in §4.4 |
| MIN-07 | Table 5.0a, A.9c, A.14: "Section 6.9" → 6.9a after renumbering | CLOSED | P14 | Table 5.0a and Appendix A ×3 |
| MIN-08 | Appendix C preamble: "Chapter 3, Section 3.9" → 3.8 | CLOSED | P01 |  |
| MIN-09 | "an separately written" ×3 → "a separately written" | CLOSED | P01 |  |
| MIN-10 | §5.3, §5.4, §5.6: witness lines in a code block, one per line | CLOSED | P14, P25 | §5.3, §5.4, §5.6 verbatim code blocks |
| MIN-11 | §6.1 "thirty-nine concrete witnesses" → "witnesses in the model" | CLOSED | P01 |  |
| MIN-12 | §1.5 "addendum to the thesis supervisor": remove or make an appendix | CLOSED | P01 |  |
| MIN-13 | Numbering: §5.5a, §6.9a, Appendix A sequence; regenerate TOC | CLOSED | P38, P41, P43 | Also C.1a folded into C.1 (P43) |
| MIN-14 | Title page logo placeholders must render | OPEN |  | Embed the logos; check in the PDF |
| MIN-15 | Cite a repository tag or commit, archive on Zenodo with a DOI | OPEN |  |  |
| PRES-1 | Cut defensive meta-commentary by at least half | CLOSED | P26 | 84 → 31 matches (−63%) with the widened detector; remaining hits carry argument or are PRES-3 process material |
| PRES-2 | Voice: prose in the candidate's own voice, esp. Ch4 and Ch6 | OPEN |  | Tiger's own work (TIGER_TASKS T-7) |
| PRES-3 | Process material: one statement in the Declaration; Version and Change Record to the repository | CLOSED | P27, P43, P44 | Process residue removed from §2.1.4, §2.9, §5.7, §6.8, the Declaration (one statement), the checker header (P43, P44) |
| PRES-4 | Repetition: NCPeH pilot details and the 68(12) reading said once, then cross-referred | CLOSED | P28, P29, P43, P46 | Pilot detail in §2.2 only (§1.1 now points there); §2.3 points to §4.6; Synthea limitations once in §3.5 (P43, P46) |
| PRES-5 | Length: check programme guidance; slim Appendix A to tag + SHA-256 + core functions | OPEN |  |  |
