# P22 — M6a: requirement-by-requirement traceability matrix (Table 4.1) at the end of §4.11, the
# supervisor's minimum for the evaluation step. Only requirements this thesis has read are listed.
# D7.4 rows carry "page to confirm (T-1)" until Tiger checks the PDF; SPUHiN rows are the hearing
# version as inspected (P10). Status vocabulary: Met in the artefact (run shows it) / Met by
# specification (stated, not executed) / No conflict (requirement on the environment, untouched) /
# Open (depends on an interpretation the thesis cannot settle).
C4 = "Chapter4_TRF_Model_v1.md"
MATRIX = """*Traceability.* Table 4.1 sets the mechanism against each requirement it touches, so that the integration analysis above can be checked line by line rather than read as prose. It lists only requirements this thesis has read in the source; the specification's page references are to be confirmed against the published PDF.

*Table 4.1. Requirements traced to the mechanism*

| Requirement | Source | What the mechanism does | Where | Status |
|---|---|---|---|---|
| Electronic health data within the SPE deleted within six months of permit expiry | EHDS Art. 68(12) | Payload key, salt and ciphertext destroyed at $t_\\pi + 6$; subject fields of patient-level logs removed at the same month | §4.7 steps 2–4; `apply_invalidation()` | Met in the artefact (C3 over $\\alpha$ and $\\beta$: 0 violations) |
| Same, "deleted or rendered unrecoverable … including any backups or redundant copies" | TEHDAS2 D7.4, Table 5.2, OPR-6 (page to confirm) | Key destruction renders copies the store cannot delete at once unrecoverable | §4.8 *Ciphertext* | Met by specification; key destruction simulated (§4.9, §6.3) |
| Identifiable logs of access and activities, kept for the period needed to audit, at least one year | EHDS Art. 73(1)(e) | Accessor fields kept identifiable for the full floor; activity committed | §4.3, §4.7; `V_II()` | Met in the artefact (C1 under Semantics II: 0 violations) |
| "All SPE logs MUST identify the actor" | D7.4, Table 5.1, EHDSR-7 (page to confirm) | Actor is an accessor field, never removed within the floor | §4.3 | Met in the artefact |
| "All SPE logs MUST be kept at least for one year" | D7.4, Table 5.1, EHDSR-8 (page to confirm) | Floor parameter $F = 12$ | §4.3 | Met in the artefact |
| Logs available for verification and auditing | D7.4, Table 5.1, EHDSR-6 (page to confirm) | Every access, invalidation and subject-link removal in an append-only Merkle log; inclusion proofs | `MerkleLog`, `integrity()` | Met in the artefact (200/200 verify; tamper tests fail) |
| Whether the audit purpose needs the subject link after the ceiling | EHDS Art. 73(1)(e) read with Art. 68(12) | Removes it; keeps accessor fields | §4.6, §7.4 | Open: interpretation for the supervisory authority |
| Erasure without undue delay, within one month (extendable by two) | GDPR Arts. 17(1), 12(3) | Invalidation at $t_r + \\delta$, $\\delta \\in \\{1, 3\\}$ | §4.4 C2; `--delta-witness` | Met in the artefact (both $\\delta$) |
| Retention only as far as the legal obligation requires | GDPR Arts. 17(3)(b), 5(1)(c) | Keeps accountability content and commitment; removes payload | §4.2 | Met by specification (necessity argument) |
| Not kept in identifiable form longer than necessary | GDPR Art. 5(1)(e) | Terminal transition after the floor | §4.8 *End of life* | Met by specification; not implemented in the checker (§6.1) |
| Key deletion may serve erasure where physical deletion is not possible; threat model documented | EDPB Guidelines 02/2025 v2.0; Aikebaier (2026) on the threat model | Per-record keys under a key-encrypting key; trust assumptions stated | §4.8, §4.9 | Met by specification |
| Audit message records the query segment | IHE ITI-55, §3.55.5.1 | Treated as payload: committed, then invalidated on request | §4.3 | Met in the artefact (cross-border payload models the query) |
| Information-security management system (mandatory); ISO 27001 (recommended); eID login at defined assurance levels; personnel security | SPUHiN (2025), hearing version | Requires none of these to change; operates at the logging boundary | §4.11 | No conflict |
| Reconciliation of log retention with deletion | SPUHiN (2025), hearing version | Not addressed by the criteria at any grade; the mechanism supplies one | §2.6, §4.11 | Gap the thesis addresses |

Three things follow from the table. Every requirement the artefact can execute is met in the run; the requirements met only by specification are the key hierarchy, the terminal transition and the legal necessity argument, none of which a sandbox can demonstrate; and one row is open, which no artefact can close.

"""
EDITS = [dict(id="P22-01", file=C4, old="\n\n## 4.12 Summary", new="\n\n" + MATRIX.rstrip("\n") + "\n\n## 4.12 Summary",
              why="M6a: traceability matrix, Table 4.1")]
