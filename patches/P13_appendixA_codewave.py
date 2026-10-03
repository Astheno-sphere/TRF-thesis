# P13 — Appendix A follows the code wave (P12): listings and console outputs synced from the files
# by handoff_tools/appendix_sync.py (block edits P13-Bnn), prose updated (P13-nn).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync

A = "code_artefacts/README_Appendix_A.md"
EDITS = appendix_sync.block_edits("P13-B") + [
    dict(id="P13-01", file=A, old="including the independent exhaustive cross-check | 363 |",
         new="including the independent exhaustive cross-check and the audit-log integrity check | 533 |", why="line count after P12"),
    dict(id="P13-02", file=A, old="| `app.py` | Five-tab demonstration viewer over the artefact, never a source of results | 526 |",
         new="| `app.py` | Five-tab demonstration viewer over the artefact, never a source of results | 530 |", why="line count after P12"),
    dict(id="P13-03", file=A,
         old="Implements the TRF Model of Chapter 4 directly. Records are the seven-element tuples of Section 4.3.",
         new="Implements the TRF Model of Chapter 4 directly. Records are the seven-element tuples of Section 4.3, with the metadata split into accessor fields and subject fields. A Secure Processing Environment record carries a researcher and a permit rather than a clinician and a contact point, and its payload stands for the logged activity; a cross-border record's payload stands for the demographic query that the IHE patient-discovery transaction puts into the audit message.",
         why="M1: the record model as revised"),
    dict(id="P13-04", file=A,
         old="(destroy the payload key and the commitment salt at `min(t_r + δ, t_π + 6)`, append a grounded invalidation entry, retain metadata and commitment) and then verifies all three constraints.",
         new="(destroy the payload key and the commitment salt and delete the payload at `min(t_r + δ, t_π + 6)`; remove the subject fields of a Secure Processing Environment record at `t_π + 6`; append a grounded entry for each; retain the accessor fields and the commitment) and then verifies all three constraints, including C3 over the subject link.\n- `integrity()` and the `MerkleLog` class give condition (i) of Semantics II real content. Every access event, invalidation and subject-link removal is appended to an append-only Merkle log using RFC 6962 hashing, and `V_II` checks each of a record's entries against the current root with an inclusion proof. The run includes two tamper tests, an altered accessor field and an altered invalidation ground, under which `V_II` fails, and a restore after which it holds.",
         why="M4c, M3b, D-16 described"),
    dict(id="P13-05", file=A,
         old="Salts are derived deterministically from the record identifier so that runs reproduce exactly. That derivation is for reproducibility only:",
         new="By default `make_salt()` derives each salt from the record identifier so that runs reproduce exactly; `--random-salts` draws them from `os.urandom` instead and gives the same results. The derivation is for reproducibility only:",
         why="M3c"),
    dict(id="P13-06", file=A,
         old="Key destruction is modelled as setting the key reference to `None`.",
         new="Key destruction is modelled as setting the key reference to `None`, and deletion of the ciphertext as setting the payload to `None`.",
         why="M3b"),
    dict(id="P13-07", file=A,
         old="Mean payload size rises from 35 bytes to 1,006.",
         new="Mean payload size rises from 43 bytes to 891 with the committed subset (to 1,006 with the full cohort, recorded on 28 September when the constructed payloads averaged 35 bytes; see A.11).",
         why="constructed payloads changed in P12"),
    dict(id="P13-08", file=A,
         old="| Reference commitment, record 100 | `11087780fd192c8f…` | §5.6 |",
         new="| Audit-log integrity | 200 / 200 records verify; both tamper tests fail V_II | §5.6 |\n| Reference commitment, record 100 | `678ade47c1e6dc03…` | §5.6 |",
         why="M4c result; commitment after P12"),
    dict(id="P13-09", file=A,
         old="It is unchanged across the salt-handling refactor documented in the thesis change log, which is the intended behaviour.",
         new="It changed once, on 3 October 2026, when the Secure Processing Environment payload was redefined as the logged activity (Chapter 4, Section 4.3). Under `--random-salts` it differs on every run, by design.",
         why="commitment after P12"),
    dict(id="P13-10", file=A,
         old="It depends on the Python standard library only. Line count: 363.",
         new="It depends on the Python standard library only. Line count: 533.", why="line count after P12"),
    dict(id="P13-11", file=A,
         old="if the run disagrees with Chapter 5. Line count: 526.",
         new="if the run disagrees with Chapter 5. Line count: 530.", why="line count after P12"),
    dict(id="P13-12", file=A,
         old="Produced by command 4 against the regenerated 98-bundle cohort. This is the run Chapter 5, Section 5.7 reports at a mean payload of 1,006 bytes.",
         new="Produced by command 4 against the regenerated 98-bundle cohort. This is the run Chapter 5, Section 5.7 reports at a mean payload of 1,006 bytes. It was recorded on 28 September 2026, before the code revision of 3 October, and its constructed-payload mean (35 bytes) reflects the earlier constructed strings; no measure in it depends on them, as the subset run in A.11b, recorded after the revision, shows.",
         why="historical record stated as such"),
]

# Old line counts (363, 526) and the old SPE auditor line (actor=HP-026) leave with the code they described.
LOST_OK = ["number 363", "number 526", "number 026", "number 4.8"]  # 4.8: code comment "§4.8" now written "s4.8"
