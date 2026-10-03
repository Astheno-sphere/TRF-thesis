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
| M1 | Define p(a) per record class from the eHDSI audit spec and D7.4; revise the SPE record model in code | PARTIAL | P04, P06 | Cross-border p(a) grounded in ITI-55 (P04); SPE log identifiability grounded in D7.4 EHDSR-7 (P06). Open: SPE record model in code (code wave) |
| M2a | One reading of Art 68(12) carried through Cor 1.2, Thm 2, §4.8 | CLOSED | P04, P05, P07 | Partition reading carried through Ch1, Ch2, Ch4, Ch6, Ch7 (P04, P05, P07) |
| M2b | Rival 6: move the logs out of the SPE at permit closure | CLOSED | P06 | Rival 6 accepted for the ceiling and bounded by Proposition L (P06). Ch6/Ch7 echo in P07 |
| M2c | Rewrite §6.1's opening; lead with the robust result | CLOSED | P07 | §6.1 leads with the robust result, then Proposition L, then the conditional SPE instance |
| M3a | Salt: text, code and change record agree | CLOSED | P02 | D-15: salt destroyed (Tiger, 22 Sept). Text in §4.8/§5.6/§4.9 must follow the code |
| M3b | Ciphertext: delete at invalidation or justify | PARTIAL | P02 | D-17. Text done (P02). Code still keeps the payload after invalidation: code wave |
| M3c | Remove the dead salt branch; seeded generator or `--reproducible` | OPEN |  | Code change; recorded runs must still match or be re-recorded with a logged reason |
| M4a | Theorems renamed Propositions; weight on the §4.2 necessity analysis | OPEN |  | D-18 |
| M4b | Promote the §6.9a anchoring result into Ch4 as a formal result | OPEN |  | D-18 |
| M4c | V_II tests integrity: hash chain over m(a), ι(a); tamper test | OPEN |  | Not blocked. Proposed: Merkle log (RFC 9162 style) rather than a bare chain; tamper test must make V_II fail |
| M4d | Shorten Ch5; violation rates are generator artefacts | OPEN |  | After M4c |
| M5a | Ten-year floor: primary eHDSI source with section, or F=120 illustrative | CLOSED | P09 | Supervisor's fallback taken: F = 120 illustrative; primary agreement cited for what it says (no period). Reopen if the eHDSI annex is obtained |
| M5b | SPUHiN "finalised" claims aligned to what was inspected | CLOSED | P10 | Every claim limited to the hearing version inspected (P10, P10b) |
| M5c | Art 68(12) and Art 73(1)(e) quoted verbatim (OJ English); one more language version | PARTIAL | P04, P07, P08 | Art 68(12) verbatim at every site; Art 73(1)(e) verbatim in Ch1, Ch2, Ch4. Open: one further language version (supervisor's 'ideally') |
| M5d | §2.2 EHDS dates fixed against Art 105; drop the EY source | CLOSED | P03 | Arts 19(1), 105(1)(a) verified 3 Oct |
| M5e | Table 2.1: preprint/practitioner sources in a separate band; Feng et al. 2022 peer-reviewed version? | PARTIAL | P09 | Feng et al. now CAV 2023 (P09). Open: Table 2.1 practitioner/preprint band |
| M6a | Traceability matrix against D7.4 and the SPUHiN checklist | OPEN |  | The evaluation step |
| M6b | Reword Appendix C item A1 ("full confidence"), record in one line | OPEN |  |  |
| M7a | Logistics anchor (UCC customs record-keeping vs destruction orders); §1.4 overreach | OPEN |  | Check UCC Art 51 (3-year floor) against seized-goods destruction; test against the anchoring result |
| M7b | One sentence in §1.5 on the programme fit | OPEN |  |  |
| MIN-01 | §3.6 line counts inverted (checker 363, layer 152) | CLOSED | P01 | Prose now points to Table 5.0a; the code wave must update Table 5.0a, Table F.2 and Appendix A counts |
| MIN-02 | §3.6 "tuples defined in Section 3.4" → 4.3 | CLOSED | P01 |  |
| MIN-03 | §1.6 drop "accumulator-based" | CLOSED | P01 |  |
| MIN-04 | §2.1.4 "four dated rounds" vs Appendix B five | CLOSED | P01 | Fork R1 merged rounds to 7 on the superseded branch; re-judge |
| MIN-05 | §3.4 / Cor 1.1 "ordinary"/"generic case" are frequency claims; soften | OPEN |  |  |
| MIN-06 | §4.4 C1 closed window spans F+1 months | OPEN |  | Half-open interval, or justify |
| MIN-07 | Table 5.0a, A.9c, A.14: "Section 6.9" → 6.9a after renumbering | OPEN |  |  |
| MIN-08 | Appendix C preamble: "Chapter 3, Section 3.9" → 3.8 | CLOSED | P01 |  |
| MIN-09 | "an separately written" ×3 → "a separately written" | CLOSED | P01 |  |
| MIN-10 | §5.3, §5.4, §5.6: witness lines in a code block, one per line | OPEN |  |  |
| MIN-11 | §6.1 "thirty-nine concrete witnesses" → "witnesses in the model" | CLOSED | P01 |  |
| MIN-12 | §1.5 "addendum to the thesis supervisor": remove or make an appendix | CLOSED | P01 |  |
| MIN-13 | Numbering: §5.5a, §6.9a, Appendix A sequence; regenerate TOC | OPEN |  |  |
| MIN-14 | Title page logo placeholders must render | OPEN |  | Embed the logos; check in the PDF |
| MIN-15 | Cite a repository tag or commit, archive on Zenodo with a DOI | OPEN |  |  |
| PRES-1 | Cut defensive meta-commentary by at least half | OPEN |  | Guard counts 19 with a narrow pattern; he counts ~50. Widen the detector before claiming half |
| PRES-2 | Voice: prose in the candidate's own voice, esp. Ch4 and Ch6 | OPEN |  | Tiger's own work; the tools cannot close this |
| PRES-3 | Process material: one statement in the Declaration; Version and Change Record to the repository | OPEN |  |  |
| PRES-4 | Repetition: NCPeH pilot details and the 68(12) reading said once, then cross-referred | OPEN |  |  |
| PRES-5 | Length: check programme guidance; slim Appendix A to tag + SHA-256 + core functions | OPEN |  |  |
