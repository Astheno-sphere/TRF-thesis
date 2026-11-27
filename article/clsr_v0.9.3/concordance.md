# Concordance: manuscript v0.9.1 against thesis and code

Manuscript: `manuscript.md` (single source). Thesis: `/home/claude/trf-thesis/VERA-SNARK_Thesis_SUBMISSION.md` (read only; line numbers by grep on 26 Nov 2026). Code: anonymised archive `../review_code/` (sha256 of the zip in `../review_code_PROOF.md`). Mechanical check: `python3 concordance_gate.py` (49 checks, passes; exits 1 on any mismatch or missing anchor phrase).

Thesis line numbers are given for the internal record only. They must not appear in any anonymised file.

## 1. Propositions and corollaries

| Article | Article location | Thesis counterpart | Thesis line | Code / output | Note |
|---|---|---|---|---|---|
| Proposition 1 (infeasibility if d <= s + F) | 3.2 | Proposition 1 (Semantics I infeasible if an erasure or ceiling deadline falls in the window) | 939 | `trf_checker.check_semantics_I`; output section "SEMANTICS I ... -> Proposition 1"; `brute_force_semantics_I`; `tests/test_props.py` | Same result; article states it per field with deadline d |
| Proposition 1, last sentence (feasible when every deadline follows the window) | 3.2 | Remark (converse) | 949 | control case `feasible=True` in expected_trf_output | Thesis calls it a Remark, the article folds it into Proposition 1 |
| Anchor paragraph (collides iff e - s <= F - L; common anchor e = s) | 3.2, para after the proof | Proposition 3 (anchoring) | 971 | z3_check.py (Props 1-3, bounded; output prints "P3" and "Proposition 3"); output rid=100 line | Not numbered in the article. v0.9.1: 5.1 now says that "Proposition 3" in the z3_check.py output is this anchor condition |
| No-request collision (39 SPE records) | 5.2 | Corollary 1.2 (SPE case) | 953; results 1243-1259 | output line "Corollary 1.2 witnesses ... : 39" | v0.9.1: 5.1 maps the printed label "Corollary 1.2" to the no-request ceiling collisions ("a longer formal treatment"; thesis not named) |
| Six-year / 120-month cross-border floor values | 2.3, 5.1 | Corollary 1.1 (cross-border case) | 951 | `FLOOR_XBORDER = 120` | Article does not name the corollary |
| Proposition 2 (feasible trajectory under accountability-preserving verification) | 3.3 | Proposition 2 | 983 | `apply_invalidation`, `V_II`, `check_semantics_II`; output "SEMANTICS II ... -> Proposition 2" | Same result |
| Floor value does not matter for Proposition 2 ("any applicable floor") | 3.3 | Corollary 2.2 | 1012 | sensitivity.py (accountability column 0 at all floors) | |
| Relocation of a full log does not resolve Article 17 | 6.1, para 4 | Proposition 4 (location and right) | 1090 | not executed (thesis 1094) | Argued in prose in the article, not as a proposition |
| Corollaries 2.1, 2.3 | not in article | Corollary 2.1, 2.3 | 1010, 1014 | | Omitted from the article |

## 2. Numbers

| Claim in manuscript | Section | Value | Code source (expected-output line or function) | Thesis location |
|---|---|---|---|---|
| Generated records | Abstract, 5.1, 5.2, Table 2 caption | 200 (100 + 100) | expected_trf_output: "Generated 200 records (100 cross-border, 100 SPE access-log)"; `generate(n_primary=100, n_secondary=100)` | Table 5.3, l. 1221-1225 |
| Seed | 5.1 | 20260915 | `SEED = 20260915`; output header | l. 718, 1154 |
| Plaintext violations / records | Abstract, 5.2, Table 2 row 1 | 95 / 90 | "total constraint violations: 95"; "records with >=1 violation : 90/200"; RESULT line | l. 1225-1227; Table 5.5 l. 1292-1293 |
| Cross-border / SPE records with a violation | 5.2 | 37 / 53 | "cross-border (F=120) : 37/100"; "SPE access-log (F=12) : 53/100" | Table 5.3 l. 1223-1224 |
| Request-only / ceiling-only / both | 5.2 | 41 / 44 / 5 | derived: 46 - 5, 90 - 46, 95 - 90 (sensitivity row 120 excluded); recomputed per record by the gate | "five SPE records collide with both C2 and C3", l. 1227 |
| No-request ceiling collisions | 5.2 | 39 | "Corollary 1.2 witnesses (SPE, NO erasure request, still infeasible): 39" | l. 1247 |
| 39 is a subset of the 44 ceiling-only records | 5.2 | 39 of 44 | gate recomputation (`t_r == INF` records all ceiling-only) | not stated as a subset in the thesis |
| Records verified against the log | 5.2 | 200 | "records verifying : 200/200" | l. 2021 (Appendix table), 3275 |
| Payload invalidations: total / erasure / ceiling | 5.2 | 138 / 52 / 86 | "records invalidated : 138/200"; "ground = GDPR Art 17(1) : 52"; "ground = EHDS Art 68(12) : 86" | l. 1311-1313, 1319 |
| Second semantics violations | Abstract, 5.2, Table 2 | 0 | "RESULT Semantics II: 0 violations" | l. 1296-1297 |
| Ceiling removal reduces violations by | 5.2 | 49 | derived 95 - 46; recomputed: records with a C3 violation | not in thesis |
| Violating records drop by | 5.2 | 44 | derived 90 - 46 | not in thesis |
| Ceiling violations persist at 72 and 36 months | 5.2 | 49 | 83 - 34, 66 - 17 (sensitivity output) | not in thesis |
| Response period 3 months | 5.2 | 94 / 89; 39 persist; 0 | sensitivity output last line; expected_delta_witness_output delta 3 row | Table 5.5 l. 1288-1297 |
| Brute-force: 3 infeasible, 1 control feasible | 5.1, 5.2 | 3 / 1 | INDEPENDENT CROSS-CHECK block (feasible=False x3, True x1) | §5.5 l. 1263-1276 |
| Tamper tests (accessor, ground, link) fail; restore verifies | 5.2 | 3 tests | AUDIT-LOG INTEGRITY block | §5.7; l. 2021 |
| Example: s = 7, e = 10, retained to 19, ceiling 16 | 3.2, Fig. 1 | 7, 10, 19, 16 | "rid=100: t_a=7 permit expires t_pi=10 -> C3 from t=16, C1 to t=19" | l. 1252, Figure 5.2 l. 1259 |
| Generator: creation month 0-11; p = 0.40, offset 1-130; SPE expiry 1-12; p = 0.25, offset 1-18 | 5.1 | as stated | `trf_checker.generate` source | Table 5.2, l. 1197-1205 |
| Floors 120 (primary), 12 (SPE); ceiling 6 | 3.1, 5.1 | 120, 12, 6 | `FLOOR_XBORDER`, `FLOOR_SPE`, `CEILING` | l. 865 (F = 12) |
| Sensitivity Table 2, six rows | 5.2, Fig. 3 | 90/95/0, 46/46/0, 78/83/0, 34/34/0, 61/66/0, 17/17/0 | expected_sensitivity_output rows | not in thesis (post-thesis script, sensitivity.py) |
| Invalidations with ceiling excluded | Fig. 3 only | 60 | expected_sensitivity_output, column "invalidated" | not in thesis |
| Python version for the reference run | 5.1, Data availability | 3.12 | base text; v0.9 proof run used 3.13.18 with identical output | |

## 3. Legal numbers (no code source)

Reference numbers in this table follow v0.9.2a numbering ([1] EHDS and [2] GDPR unchanged; TEHDAS2 is now [21], EFTA is now [24]). Pointers such as "ref_verification.md row 8" keep the old row numbers of that file. Old-to-new mapping: CHANGES_vs_original.md section E.

| Claim | Section | Source |
|---|---|---|
| Art 73(1)(e): identifiable logs; access logs at least one year | 1, 2.1, Table 1 | [1]; verified on EUR-Lex HTML 26 Nov 2026 |
| Art 68(12): deletion within six months of permit expiry | 1, 2.1, Table 1 | [1]; verified on EUR-Lex HTML 26 Nov 2026 |
| Art 73(5) implementing acts by 26 March 2027; Art 105 Chapter IV from 26 March 2029 | 2.1 | [1]; ref_verification.md row 1 (ministry-hosted OJ copy) |
| Art 9(2): at least three years from each access | 2.3 | [1]; ref_verification.md row 1 |
| Art 12(3) GDPR: one month, extension by two further months | 2.1 | [2]; not read on EUR-Lex (ref_verification row 2: PARTLY) |
| TEHDAS2 D7.4: one year minimum, five years recommended (OPR-18) | 2.2 | [21]; ref_verification row 8 |
| Regulation marked "Text with EEA relevance" | 2.3 | [1]; title read on the OJ PDF copy (ministry-hosted, as ref_verification row 1), 26 Nov 2026 |
| EEA incorporation pending; application in Norway depends on it | 2.3 | [24] (factsheet not read: bot check); thesis l. 479 "being processed for incorporation through the EEA Joint Committee". TO VERIFY by hand, see open_comments.md |
| EDPB blockchain guidelines v2, paras 102-104: not advisable to register personal data in clear, encrypted or hashed form on a blockchain; store off-chain | 4.3 (new sentence) | [32]; PDF re-read 26 Nov 2026 |
| Norway: secondary-use rules in helseregisterloven; FHI designated coordinating HDAB (19 Oct 2026); gap analysis of 11 Apr 2025: no approved SPE with solutions for control and activity logging | 6.2 (new sentence) | [38], [39]; both pages read 26 Nov 2026 (REFERENCE_AUDIT.md) |
