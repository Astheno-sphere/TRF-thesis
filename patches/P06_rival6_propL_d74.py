# P06 — Rival 6 and Proposition L (M2b, D-16), D7.4 evidence into §4.6 and §4.8, Rival 3 aligned
# with §4.2 and M1 (the supervisor noted Rival 3 conceded that Art 17 targets m(a), which the
# mechanism keeps).
# D7.4 = TEHDAS2 (2026), v1.2 final, 24 Feb 2026, retrieved 3 Oct via tehdas.eu PDF (text
# extraction, cross-checked across two fetches): Table 5.1 EHDSR-7 "All SPE logs MUST identify the
# actor" (p. 31); EHDSR-8 "All SPE logs MUST be kept at least for one year" (p. 31); Table 5.2 OPR-6
# "All electronic health data within the environment MUST be deleted or rendered unrecoverable
# within six months of permit expiry, including any backups or redundant copies" (p. 43).
# A third fetch gave a different OPR-6 text; page numbers to be confirmed by Tiger in the PDF.

EDITS = [
    dict(id="P06-01", file="Chapter4_TRF_Model_v1.md",
         old="access is restricted to \"authorised natural persons listed in the data permit\" (point (a)), and the handling of data to \"authorised identifiable individuals\" (point (c)).",
         new="access is restricted to \"authorised natural persons listed in the data permit\" (point (a)), and the handling of data to \"authorised identifiable individuals\" (point (c)). The Joint Action's specification for these environments reads Article 73(1)(e) the same way: \"All SPE logs MUST identify the actor\" (TEHDAS2, 2026, Table 5.1, EHDSR-7).",
         why="D-16 evidence: the SPE specification ties log identifiability to the actor"),
    dict(id="P06-02", file="Chapter4_TRF_Model_v1.md",
         old="Key destruction remains the operative erasure for copies the store cannot delete at once, such as replicas and backups: they become unreadable at $t^{I}(a)$ and leave by ordinary rotation.",
         new="Key destruction remains the operative erasure for copies the store cannot delete at once, such as replicas and backups: they become unreadable at $t^{I}(a)$ and leave by ordinary rotation. The specification for Secure Processing Environments accepts exactly this: electronic health data \"MUST be deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies\" (TEHDAS2, 2026, Table 5.2, OPR-6).",
         why="D-17 evidence: D7.4 OPR-6 accepts 'rendered unrecoverable' including backups"),
    dict(id="P06-03", file="Chapter4_TRF_Model_v1.md",
         old="A reviewer will propose alternatives. Five are treated here,",
         new="A reviewer will propose alternatives. Six are treated here,",
         why="M2b: Rival 6 added"),
    dict(id="P06-04", file="Chapter4_TRF_Model_v1.md",
         old="*Rival 3: Minimise the payload at capture, so that nothing needs erasing.* Recording less at the outset is good practice and is compatible with this mechanism. It does not solve the problem, because the metadata that the accountability purpose requires, the patient pseudonym linking the access to a data subject, is itself personal data, and is precisely what an erasure request targets. Minimisation shrinks the payload; it does not remove the record from the scope of Article 17.",
         new="*Rival 3: Minimise the payload at capture, so that nothing needs erasing.* Recording less at the outset is good practice and is compatible with this mechanism; where a deployment can minimise, the mechanism has less to invalidate. For cross-border records it does not dissolve the problem, because the payload is put there by the standard rather than by the deployment: the IHE patient-discovery transaction requires the audit message to carry the query segment, name and birth time included (Section 4.3). A deployment cannot minimise it away without departing from the profile. In the Secure Processing Environment case minimisation is a genuine alternative for the ceiling: a log kept at dataset granularity carries no subject fields and falls outside Article 68(12) on either reading, at the cost of patient-level traceability. The version of the specification inspected requires logs to identify the actor and states no requirement for patient-level logging (TEHDAS2, 2026). Minimisation does not remove from the scope of Article 17 the payload the standard requires, which is the case Proposition L below shows no relocation or reduction of the log can escape.",
         why="M1, M2b: Rival 3 no longer claims Art 17 targets the pseudonym (contradicted §4.2); dataset-level logging conceded as a real alternative for the ceiling"),
    dict(id="P06-05", file="Chapter4_TRF_Model_v1.md",
         old="\n\n*The critique that is not a rival.*",
         new="""\n\n*Rival 6: Move the logs out of the environment at permit closure.* If Article 68(12) is read by location, exporting the access logs at permit closure to an audit store outside the environment, held for instance by the health data access body, satisfies it literally without cryptography, on the premise that Article 73(1)(e) fixes how long the logs are kept and not where. The rival is correct about the ceiling, and this thesis accepts it as a sufficient answer to Corollary 1.2. It does not answer the erasure right, for a reason that is general enough to state as a result.

> *Proposition L (location and right).* Let a ceiling be anchored to a location, requiring data to be absent from that location after a deadline, and let a right be anchored to the data subject, requiring data to be inaccessible to any controller holding them after a deadline. Under Semantics I, relocating a record before the ceiling's deadline satisfies the ceiling and the floor together, while the floor and the right remain infeasible for every record satisfying the first disjunct of Theorem 1.

*Proof.* The ceiling quantifies over the location: after relocation the record is not in it, so the ceiling holds, and on the rival's premise the floor is met at the new location. The right quantifies over the controller: Article 17(1) obliges the controller holding the data to erase them, and a controller receiving the record receives the obligation with it. Relocation therefore leaves C1 and C2 as they were, and the argument of Theorem 1 applies unchanged. ∎

Two consequences follow. Cryptographic invalidation is necessary for the request-driven conflict, which no relocation escapes, and optional for the location-anchored one, where relocation is a lawful alternative. And relocation is not free. The exported log still carries its subject fields, now held by a second controller for the rest of the floor, so the personal data have been moved rather than reduced; where those fields are electronic health data, they are held outside the measures Article 73(1) prescribes for such data. The partition of Section 4.7 meets the ceiling without moving anything, and does so with the same mechanism that meets the right.

*The critique that is not a rival.*""",
         why="M2b: Rival 6 answered; Proposition L stated and proved (D-16, D-18)"),
]
