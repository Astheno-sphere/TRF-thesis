# P02 — salt and ciphertext (M3a; text half of M3b). Decisions D-15 (salt destroyed with the key,
# Tiger 22 Sept) and D-17 (ciphertext deleted at invalidation, Tiger 3 Oct).
# The code already destroys the salt (trf_checker.py apply_invalidation, rec.salt = None) and
# Appendix A already says so; the Chapter 4 and 5 text said the opposite. This patch makes the
# text follow the decided design. Ciphertext deletion in code comes in the code wave (M3b stays
# PARTIAL until then).

EDITS = [
    dict(id="P02-01", file="Chapter4_TRF_Model_v1.md",
         old="*Commitment.* $c(a)$ = Commit($p(a), r(a)$) with a per-record salt $r(a)$. The salt is stored with the metadata and is *not* destroyed at invalidation; destroying it would break the binding property and with it the auditor's ability to verify an opened payload during the pre-invalidation period, while retaining it does not restore readability of the payload, which depends on $k(a)$.",
         new="*Ciphertext.* At $t^{I}(a)$ the ciphertext of $p(a)$ is deleted from the audit store together with $k(a)$. Nothing in Semantics II uses it once the key is gone, and deleting it removes the exposure that a retained ciphertext would carry to future cryptanalytic capability, quantum capability included, over the rest of a ten-year floor (Section 4.9). Key destruction remains the operative erasure for copies the store cannot delete at once, such as replicas and backups: they become unreadable at $t^{I}(a)$ and leave by ordinary rotation.\n\n*Commitment.* $c(a)$ = Commit($p(a), r(a)$) with a per-record salt $r(a)$. The salt is stored with the metadata until invalidation and is destroyed together with $k(a)$ at $t^{I}(a)$. Before invalidation it lets an auditor open the commitment against the payload. After invalidation no opening can be checked, because the payload is no longer readable, while a retained salt would let anyone holding a candidate payload confirm a guess against $c(a)$ (Section 4.9). Destroying the salt does not weaken binding, which is a property of the commitment value: no second payload can be opened against $c(a)$, and after $t^{I}(a)$ no payload can be opened against it at all. A party that holds its own copy of the payload and must later prove that it corresponds to $c(a)$ has to obtain and keep the opening before invalidation; the audit store does not keep one for it.",
         why="M3a, M3b: text contradicted the code and D-15; ciphertext had no stated justification (D-17)"),
    dict(id="P02-02", file="Chapter4_TRF_Model_v1.md",
         old="In the first month after the window, $t(a) + F(a) + 1$, the record undergoes a second invalidation, in which the identifying fields of $m(a)$ and the salt $r(a)$ are destroyed.",
         new="In the first month after the window, $t(a) + F(a) + 1$, the record undergoes a second invalidation, in which the identifying fields of $m(a)$ are destroyed, together with $k(a)$, the salt $r(a)$ and the ciphertext where no earlier invalidation removed them.",
         why="M3a: salt now goes at t^I; a record with no erasure request and no ceiling still holds key, salt and ciphertext at floor expiry, so the terminal transition must remove them"),
    dict(id="P02-03", file="Chapter4_TRF_Model_v1.md",
         old="Theorem 2 leaves a residue: $m(a), c(a), r(a), \\iota(a)$, the accumulator state, and the ciphertext of $p(a)$.",
         new="Theorem 2 leaves a residue: $m(a), c(a), \\iota(a)$ and, where the optional layer is used, the accumulator state. The salt $r(a)$, the key $k(a)$ and the ciphertext of $p(a)$ are destroyed at invalidation (Section 4.8).",
         why="M3a, M3b: residue list follows the decided design"),
    dict(id="P02-04", file="Chapter4_TRF_Model_v1.md",
         old="The salt is retained, which means the residue is not unconditionally unlinkable: a party holding $r(a)$ and a candidate payload can still confirm a match. What has been destroyed is the ability to *recover* the payload, which depends on $k(a)$.",
         new="Because the salt is destroyed with the key, no party can confirm a guessed payload against $c(a)$ after invalidation unless it kept its own opening beforehand. What has been destroyed is both the ability to *recover* the payload, which depended on $k(a)$, and the ability to confirm a guess about it from the audit store, which depended on $r(a)$.",
         why="M3a: the guess-confirmation oracle the supervisor identified is closed by destroying the salt"),
    dict(id="P02-05", file="Chapter4_TRF_Model_v1.md",
         old="By that standard the ciphertext, held together with a retained salt and metadata identifying the access event, is best characterised as pseudonymised rather than anonymous.",
         new="By that standard the residue, which keeps metadata identifying the access event, is best characterised as pseudonymised rather than anonymous until the terminal transition.",
         why="M3a, M3b: the pseudonymisation finding now rests on the metadata, which is what remains"),
    dict(id="P02-06", file="Chapter4_TRF_Model_v1.md",
         old="*The unavoidable residual risk.* Over a ten-year floor, the algorithmic-break horizon is a live concern rather than a formality: ciphertext retained for a decade must be assumed to face cryptanalytic capability that does not exist at the time of encryption. The mechanism mitigates this by ensuring that what is retained long-term is metadata and commitments rather than payload ciphertext wherever the retention purpose permits, but it does not eliminate the risk. This is recorded as a limitation in Chapter 6 rather than resolved here.",
         new="*The residual cryptographic risk.* Over a ten-year floor, the algorithmic-break horizon is a live concern rather than a formality: anything retained for a decade must be assumed to face cryptanalytic capability that does not exist when it is written. Deleting the ciphertext at invalidation (Section 4.8) removes this exposure for the store's own copy, so what is retained long-term is metadata, the commitment and the invalidation entry. The risk is reduced, not eliminated. Copies the store cannot delete at once, such as backups, hold ciphertext until rotation removes them; a record with no invalidation event keeps its ciphertext until the terminal transition; and the commitment must stay hiding across the horizon, which is a requirement on the hash function rather than on a cipher. This is recorded as a limitation in Chapter 6 rather than resolved here.",
         why="M3b: the supervisor noted the risk called 'unavoidable' is removable for the retained copy; what remains is stated"),
    dict(id="P02-07", file="Chapter4_TRF_Model_v1.md",
         old="At floor expiry it performs a terminal transition that destroys the identifying metadata and the salt, leaving",
         new="The salt and the payload ciphertext go with the key. At floor expiry it performs a terminal transition that destroys the identifying metadata, leaving",
         why="M3a, M3b: chapter summary follows the design"),
    dict(id="P02-08", file="Chapter5_Demonstration_v1.md",
         old="append an invalidation entry recording the month, the legal ground, and the authorising actor, and retain metadata, commitment, and salt unchanged.",
         new="destroy the salt with it, append an invalidation entry recording the month, the legal ground, and the authorising actor, and retain metadata and commitment unchanged.",
         why="M3a: §5.6 now describes what the code does (rec.salt = None)"),
]

# "not unconditionally unlinkable" described the retained-salt oracle, which no longer exists.
# The residue is still called pseudonymised (P02-05), so no claim is strengthened beyond the design.
LOST_OK = ["hedge conditional"]
