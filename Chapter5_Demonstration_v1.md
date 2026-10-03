# Chapter 5. Demonstration

*Every figure reported in this chapter was produced by the code listed in Appendix A, executed under seed 20260915. No number here was written before the code that produced it was run.*

---

## 5.1 Purpose and Claim

This chapter discharges Activity 4 of the design science cycle set out in Chapter 3, Section 3.2: demonstration. Its function is narrow and should be stated before the results, so that the results are not read as establishing more than they do.

The chapter demonstrates that the two propositions of Chapter 4 hold on the instances examined. It does not verify them in the proof-assistant sense, it does not measure performance, and it does not deploy anything. Proposition 1 predicts that under plaintext-verifiability semantics the constraint system fails whenever an erasure deadline or a deletion-ceiling deadline falls inside a record's retention window. Proposition 2 predicts that under accountability-preserving semantics the invalidation trajectory satisfies all three constraints for every arrival pattern. The demonstration's job is to make both predictions checkable by execution rather than only by argument.

A subsidiary claim is made for Corollary 1.2, which is the sharpest result in the thesis: that Secure Processing Environment access-log records become infeasible under plaintext semantics *without any erasure request at all*, through the collision of the Article 73(1)(e) one-year retention floor with the Article 68(12) six-month deletion ceiling. If the demonstration produces no witnesses of this kind, the corollary is in trouble. It produces thirty-nine.

## 5.2 Implementation

The checker is a single Python module of 533 lines including documentation, the independent cross-check and the audit-log integrity check, of which 413 are non-blank, non-comment lines and the constraint-evaluation logic proper occupies approximately one hundred. It depends only on the Python standard library: `hashlib` for commitments and the audit log, `json` for log entries, `random` for seeded generation, and `itertools` for the exhaustive cross-check. No cryptographic library, no solver, and no zero-knowledge proof system is used, consistent with the scope commitments of Chapter 1, Section 1.5.

Four further modules accompany it, none of which alters anything the checker reports. Their line counts, and the full source of each, are given in Appendix A.

*Table 5.0a. The artefact as published*

| Module | Lines | What it does | Reports a thesis figure? |
|---|---|---|---|
| `trf_checker.py` | 533 | Constraint evaluation under both semantics, plus the independent exhaustive cross-check and the audit-log integrity check | Yes — Tables 5.1, 5.2a, 5.3 |
| `synthea_layer.py` | 152 | Substitutes real FHIR R4 payloads and compares every figure against the constructed-payload run | Yes — Table 5.4 |
| `norwegian_layer.py` | 135 | Three Norwegian record classes, varying only the floor, the pathway and the arrival of requests | No |
| `cross_sector_check.py` | 110 | The politiregisterloven § 17 instance discussed in Chapter 6, Section 6.9a | No |
| `app.py` | 530 | Five-tab viewer over the artefact; never a source of results | No |

Every command has a recorded console run committed beside it in the repository, one per command, so that a reader who executes a command and diffs the output against its recorded file can distinguish a changed file from a changed result. That distinction matters: if a figure in this chapter ever disagrees with the artefact, the question is which of the two moved, and the recorded runs answer it. The eight Synthea bundles the realism layer reads are committed with the code, so no regeneration is required to reproduce Table 5.4.

Records are represented exactly as the model specifies. Each carries metadata `m` split into accessor fields (the actor, the national contact point or the data permit, the document category, the legal basis, and the outcome) and subject fields (the patient pseudonym); a payload, which stands for the demographic query of the patient-discovery transaction in a cross-border record and for the logged activity in a Secure Processing Environment record; a hiding commitment `c = SHA-256(salt ‖ payload)` with a per-record sixteen-byte salt; a payload key `k`; a creation month `t_a`; a floor parameter `F`; and a pathway marker. Key destruction is modelled as irreversible removal of the key reference from the record's state, and deletion of the ciphertext as removal of the payload, which is the sandbox's analogue of destruction within a custody boundary and is not a claim that the simulation destroys anything cryptographically.

Two record classes are generated, implementing the two floor instances that Chapter 4 absorbed into one parameterised constraint:

- *Cross-border audit records*, `F = 120` months, primary pathway. Erasure requests arrive for a given record with probability 0.40, at a uniformly distributed offset of one to one hundred and thirty months after creation. The offset range deliberately exceeds the window so that some requests fall outside it and the checker is not rigged to find violations.
- *Secure Processing Environment access-log records*, `F = 12` months, secondary pathway. Each carries a permit expiry at a uniformly distributed one to twelve months after creation. Erasure requests arrive with probability 0.25.

One hundred records of each class are generated, matching the population scale fixed in Chapter 3, Section 3.5. Seed 20260915 is fixed and reported; the run is deterministic and reproduces identically.

*Table 5.0. Generation parameters (complete)*

| Parameter | Cross-border audit | SPE access log |
|---|---|---|
| Records generated | 100 | 100 |
| Retention floor *F* | 120 months (eHDSI baseline) | 12 months (Art 73(1)(e)) |
| Pathway $\sigma$ | primary | secondary |
| Creation month *t_a* | uniform [0, 11] | uniform [0, 11] |
| Erasure-request probability | 0.40 | 0.25 |
| Erasure offset from *t_a* | uniform [1, 130] months | uniform [1, 18] months |
| Permit expiry *t_π* | not applicable | *t_a* + uniform [1, 12] months |
| Response period $\delta$ | 1 month (GDPR Art 12(3)) | 1 month |
| Deletion ceiling | not applicable | 6 months (Art 68(12)) |

Erasure-request assignment is drawn independently of permit length, so no record is steered toward violation by the generator.

Payloads are drawn from FHIR R4 resources in patient bundles generated by Synthea (Walonoski et al., 2018), produced with `java -jar synthea.jar -s 20260915 -cs 20260915 -p 100` and yielding 98 usable bundles. The generator was run with `--generate.only_alive_patients=true`, and two of the hundred requested patients did not survive to the end of their simulated lifetime and were therefore not exported. One clinical resource (a Condition, Observation, MedicationRequest, AllergyIntolerance, Immunization, or Procedure) is taken per bundle and serialised as the payload, giving a mean payload of 1,006 bytes against 35 bytes for the constructed strings used during development. Section 5.7 reports the comparison between the two.

## 5.3 Results under Semantics I

Under plaintext-verifiability semantics, $V(a,t) = \alpha(a,t)$, so constraint C1 requires the payload to remain accessible throughout the retention window while C2 and C3 require it to become inaccessible from their respective deadlines. The checker reports every month at which both are required at once.

*Table 5.1. Violations under Semantics I (seed 20260915, n = 200)*

| Record class | Records | With ≥1 violation | Share |
|---|---|---|---|
| Cross-border audit (F = 120) | 100 | 37 | 37% |
| SPE access log (F = 12) | 100 | 53 | 53% |
| **Total** | **200** | **90** | **45%** |

Total constraint violations: 95 across 90 records. The two counts differ because five SPE records collide with both C2 and C3; each is counted once in the per-record column and twice in the violation total. The full decomposition is 41 records violating C2 only, 44 violating C3 only, and 5 violating both: all five necessarily in the secondary pathway, since only that pathway carries both constraints.

Three features of this table require comment, and the third is the one that matters.

First, the violation rate is not one hundred per cent, and this is the correct behaviour rather than a weakness of the result. The rate itself should not be read as an estimate of real frequency, for a reason stated in Chapter 3, Section 3.7: the generator treats every erasure request as valid, whereas in practice many would be lawfully refused under Article 17(3), so real erasure-driven collision rates would be lower than those shown here. Proposition 1 is conditional: it states infeasibility for records whose erasure or ceiling deadline falls inside the retention window. A cross-border record for which no data subject ever exercises Article 17 has no second constraint to collide with C1, and is trivially feasible. Of the one hundred cross-border records, thirty-eight received an erasure request; of those, thirty-seven had a deadline landing inside the one-hundred-and-twenty-month window, and all thirty-seven are among the violations. The single exception is the record whose request arrived beyond the window, which is precisely the case the proposition excludes. The checker therefore reproduces the proposition's conditional structure exactly, including its boundary.

Second, the witnesses are specific and inspectable, which is the property Chapter 3 required of this component. Three examples, verbatim from the run:

> C1 requires V=1 (⇒ α=1) at t=116 within [11,131]; C2 requires α=0 from t=116
> C1 requires V=1 (⇒ α=1) at t=120 within [4,124]; C2 requires α=0 from t=120
> C1 requires V=1 (⇒ α=1) at t=41 within [0,120]; C2 requires α=0 from t=41

Each names the record, the collision month, the two constraints in conflict, and the window within which the conflict arises. A reader who doubts Proposition 1 can take any of these lines and check the arithmetic by hand.

Third, and most consequentially, the Secure Processing Environment class violates at a higher rate than the cross-border class, fifty-three per cent against thirty-seven, despite receiving erasure requests at a *lower* probability. The mechanism behind the inversion should be stated plainly, because an examiner's first reaction will be that the secondary pathway simply carries more constraints. That reaction is correct, and it is the point. Every SPE record faces the Article 68(12) ceiling by construction, while only forty per cent of cross-border records ever face any second constraint at all; the decomposition bears this out, with 49 of the SPE violations structural and only 4 request-driven, against all 37 cross-border violations being request-driven. The inversion is therefore not a sampling accident but the direct signature of a collision that the secondary pathway inherits from Regulation (EU) 2025/327 alone, without any data-subject action. Section 5.4 isolates it.

## 5.4 Corollary 1.2: Infeasibility Without an Erasure Request

Seventy-eight of the one hundred Secure Processing Environment records received no erasure request. Under the received account of the retention–erasure problem, these records should be unproblematic: no data subject has asked for anything, so there is nothing for the retention obligation to conflict with.

*Thirty-nine of them are infeasible under Semantics I. That is exactly half of the records with no erasure request.*

The witnesses, verbatim:

> rid=100: t_a=7, permit expires t_pi=10 → C3 from t=16, C1 to t=19 | collision at t=16
> rid=103: t_a=7, permit expires t_pi=10 → C3 from t=16, C1 to t=19 | collision at t=16
> rid=104: t_a=3, permit expires t_pi=4 → C3 from t=10, C1 to t=15 | collision at t=10

Take the first. The access-log record is created in month seven. Article 73(1)(e) requires the identifiable log to remain verifiable until month nineteen. The data permit expires in month ten, so Article 68(12) requires personal data to be gone from the environment by month sixteen. Months sixteen through nineteen are therefore months in which the same regulation requires the same environment both to retain an identifiable access log and to hold no personal data. No data subject has exercised any right. No deployment baseline is involved. No synthesis across instruments of differing legal weight has occurred. On the reading of Article 68(12) adopted in Chapter 4, Section 4.6, the conflict is internal to Regulation (EU) 2025/327. Under the narrower reading canvassed there, these thirty-nine witnesses lapse and the secondary-use collisions reduce to the nine records in this population whose erasure requests fall inside the retention window (four that collide with C2 only and five that also collide with C3; twenty-two records received requests in all); Proposition 1, Corollary 1.1, and every Semantics II result are unaffected.

The fifty per cent figure has a straightforward structural explanation, and stating it guards against reading the number as more precise than it is. The collision occurs when $t_\pi + 6 \le t_a + 12$, that is when the permit runs six months or less. Permit lengths were drawn uniformly from one to twelve months, so half the draws fall at or below six. The figure is therefore a direct consequence of the permit-length distribution and is not an empirical estimate of how often this occurs in Norwegian practice. What the demonstration establishes is that the collision arises under ordinary parameters rather than contrived ones.

The obvious attack on this figure is that the twelve-month horizon was chosen to produce it. The response is structural: the collision rate scales as $6/\pi_{\max}$ under a uniform permit horizon, so a longer horizon attenuates the rate without altering the existence of the collision, which Proposition 1 establishes independently of any distribution. The twelve-month horizon models the remaining permit duration at the moment an access event is logged, not total project length, and a record created late in a multi-year permit has a short remaining horizon regardless of the project's overall size. No figure in this chapter depends on the rate; the thesis's claim is that the collision occurs, not that it occurs with any particular frequency.

## 5.5 Independent Cross-Check

A checker that implements the constraints incorrectly would produce violations that reflect the implementation rather than the model. To guard against this, the sandbox includes a second, separately written procedure that takes the constraint definitions directly. It searches exhaustively over every possible assignment of the accessibility variable across a fourteen-month horizon, 2¹⁴ = 16,384 assignments per case, and reports whether *any* assignment satisfies C1 under Semantics I together with C2 and C3.

*Table 5.2. Exhaustive search over $\alpha$ assignments (horizon = 14 months)*

| Case | Feasible assignment exists? |
|---|---|
| SPE, no erasure request, permit 3 months | **False** |
| SPE, erasure request at t = 2 | **False** |
| Cross-border (floor scaled to 12 for tractability), erasure at t = 4 | **False** |
| Control: no erasure request, no permit expiry | **True** |

The three conflict cases admit no satisfying assignment whatsoever, which is a stronger statement than the main checker makes: it establishes not merely that the trajectory the checker examined fails, but that no trajectory succeeds. The control case, in which neither C2 nor C3 is active, is feasible: confirming that the search is capable of returning True and that the infeasibility results are not an artefact of a procedure that never succeeds.

This cross-check is separate code, not independent evidence in a stronger sense. It was written in the same AI-assisted process as the main checker and encodes the same constraint definitions from Section 4.4, so it guards against implementation error in the checker and not against error in the model.

The cross-border floor is scaled from one hundred and twenty months to twelve for this check, because exhaustive search over 2¹²⁰ assignments is not computable. The scaling does not affect the logic: Proposition 1's argument depends on the deadline falling inside the window, not on the window's length, and the scaled case preserves that relation. This substitution is noted rather than hidden, and it is the one place in the demonstration where a parameter was altered for tractability.

## 5.5a Witness at the Extended Response Period

Chapter 4, Section 4.4 sets the erasure response period $\delta$ from Article 12(3) GDPR, which allows the controller one month from receipt and permits extension by a further two months for complex or numerous requests. The propositions are stated for arbitrary finite $\delta$, and the model admits $\delta = 3$. That claim is witnessed rather than asserted.

*Table 5.2a. Results at $\delta = 1$ and $\delta = 3$ (seed 20260915, n = 200)*

| Measure | $\delta = 1$ | $\delta = 3$ |
|---|---|---|
| Semantics I: records with violation | 90 | 89 |
| Semantics I: total violations | 95 | 94 |
| Corollary 1.2 witnesses | 39 | 39 |
| Records invalidated | 138 | 138 |
| Semantics II: records with violation | 0 | 0 |
| Semantics II: total violations | 0 | 0 |

Extending the response period moves one record out of violation under Semantics I, which is the expected behaviour: a longer deadline pushes one erasure collision past the end of its retention window, and Proposition 1 excludes exactly that case. Everything else is unchanged. The Corollary 1.2 count is identical because those collisions arise from the deletion ceiling rather than from any erasure request, and so do not involve $\delta$ at all. Semantics II yields zero violations at both settings, as Proposition 2 requires for any finite $\delta$.

The run is reproduced with `python3 trf_checker.py --delta-witness`.

## 5.6 Results under Semantics II

The invalidation trajectory from the constructive proof of Proposition 2 was then applied to every record: destroy the payload key at $t^{I} = \min(t_r + \delta,\; t_\pi + 6)$, destroy the salt with it, append an invalidation entry recording the month, the legal ground, and the authorising actor, and retain metadata and commitment unchanged.

*Table 5.3. Results under Semantics II (same 200 records, same seed)*

| Measure | Value |
|---|---|
| Records invalidated | 138 / 200 |
| — on ground GDPR Article 17(1) | 52 |
| — on ground EHDS Article 68(12) | 86 |
| Records with ≥1 constraint violation | **0 / 200** |
| Total constraint violations | **0** |

Every record that was infeasible under Semantics I is feasible under Semantics II, and no record is made worse. The ninety violating records become zero.

The distribution of invalidation grounds is itself informative. Eighty-six invalidations are triggered by permit expiry under Article 68(12) and only fifty-two by erasure requests under Article 17(1). The majority of invalidation events in this population arise from the regulation's own deletion ceiling rather than from data-subject action: which is consistent with Section 5.4 and reinforces the point that the tri-lateral problem is not reducible to a right-to-be-forgotten problem.

The auditor's view of a record that was infeasible before invalidation, verbatim from the run for record 100:

```text
accessor fields      : True  actor=R-008 permit=DP-015 outcome=success
subject link         : removed month 16
commitment c(a)      : 678ade47c1e6dc03296175e056fd8116...
payload key k(a)     : None   <- destroyed
salt, ciphertext     : None, None   <- destroyed, deleted
invalidation iota(a) : month=16 ground=EHDS Art 68(12)
payload readable?    : False
```

This is the state the mechanism is designed to produce, and it is worth reading against what Semantics I would have demanded. The access event is fully established: which researcher, under which permit, with what outcome. The link to the patient was removed at the ceiling, and its removal is itself a logged entry. The binding to a specific payload survives in the commitment. The invalidation is itself a logged, grounded, attributed event rather than a silent absence. And the payload is unreadable, at month nineteen as at month sixteen. An auditor examining this record learns everything accountability requires and nothing the erasure obligation forbids.

The record is also checked against the audit log. Every access event, invalidation and subject-link removal is an entry in an append-only Merkle log, and condition (i) of Semantics II is tested as an inclusion proof against the log's root rather than as the presence of fields. All two hundred records verify. Altering one accessor field of record 100, or the legal ground of its invalidation entry, makes $V^{II}$ fail; restoring them makes it hold again (Appendix A, A.10). The Semantics II result of Table 5.3 therefore rests on a check that can fail, which the earlier presence test could not.

## 5.7 What the Demonstration Establishes, and What It Does Not

*Established.* Both propositions hold on all two hundred generated instances. Proposition 1's conditional structure is reproduced exactly, including the boundary case of the request falling outside the window. Corollary 1.2 has thirty-nine witnesses in the model: records in which two provisions of one regulation collide over one environment with no data-subject action involved. The infeasibility results survive a separately written exhaustive search that considers every possible accessibility assignment rather than only the trajectory the main checker examines. The invalidation trajectory eliminates every violation without introducing any.

*Not established, and not claimed.* The demonstration does not prove the propositions for all instances; it checks them on the instances generated under one seed, and the exhaustive cross-check covers four small cases rather than the general result. The proofs in Chapter 4, not this chapter, carry the general claim. No performance measurement was taken, and no statement about execution time, throughput, or storage overhead appears anywhere in this thesis. The sandbox does not connect to any National Contact Point, implement the OpenNCP transmission flow, or evaluate consent policies. Key destruction is simulated by removing a reference in program state, which demonstrates the mechanism's logic and demonstrates nothing whatever about whether key destruction can be assured in deployment: the limitation that Chapter 2 drew from the secure-deletion literature and that Chapter 6 engages.

*How the tables should be read.* The Semantics II result of Table 5.3 holds by construction: the checker derives payload accessibility from the same invalidation month that the trajectory of Proposition 2 prescribes, so zero violations is the expected outcome, and a failure would expose an implementation error and not a modelling error. The violation rates of Table 5.1 are functions of the generator parameters in Table 5.0 and are not estimates of real frequency.

*Payload provenance, tested rather than assumed.* Chapter 3, Section 3.6 specifies a realism layer feeding Synthea-generated records into the checker. That layer was built and executed, and its result is reported here because it bears on how much the demonstration's figures depend on the fixtures chosen.

The layer substitutes real FHIR R4 resources for the constructed payload strings and leaves every timing quantity (creation month, erasure arrival, permit expiry, floor, response period) exactly as generated. Mean payload size rises from 43 bytes to 891 with the committed subset and to 1,006 with the full cohort, whose run was recorded before the constructed payloads were revised on 3 October 2026 and shows 35 bytes on the constructed side (Appendix A, A.11). All two hundred commitments change, confirming that the payloads genuinely differ.

*Table 5.4. Constructed against Synthea-generated payloads (same seed, same timings)*

| Measure | Constructed | Synthea | 
|---|---|---|
| Semantics I: records with violation | 90 | 90 |
| Semantics I: total violations | 95 | 95 |
| Corollary 1.2 witnesses (no erasure request) | 39 | 39 |
| Records invalidated | 138 | 138 |
| Semantics II: records with violation | 0 | 0 |
| Semantics II: total violations | 0 | 0 |
| Commitments differing between runs | — | 200 / 200 |

Every reported figure is identical while every commitment differs. This is the expected result and the model would be defective if it were otherwise: no constraint in the TRF Model reads the content of a payload, so the results are functions of timing and accessibility alone. The value of running the comparison rather than asserting the invariance is that a reader can see the claim tested against a case where the inputs demonstrably changed.

The invariance was tested a second time against a different cohort size, because a result that held only at one cohort size would be weaker than it appears. Repeating the comparison with an eight-bundle subset of the same generated cohort raises the mean payload to 891 bytes rather than 1,006, since a different set of clinical resources is drawn, and every payload is then reused roughly twenty-five times across the two hundred records rather than twice. All six measures are again identical to the constructed-payload run, and all two hundred commitments again differ. Neither the size of the cohort nor the frequency with which payloads repeat affects any reported figure, which is the strongest form in which the payload-independence claim can be made from execution.

One limitation of the generated cohort is carried forward. Synthea's default export conforms to US Core profiles with United States demographics and care patterns, not to the Norwegian basisprofiler (HL7 Norway, 2025). The FHIR version matches Norway's, the resource structure is genuine, and the invariance result above establishes that the mismatch cannot affect any figure in this chapter. But no claim of Norwegian clinical representativeness is made for the records. The thesis's Norwegian grounding rests on the infrastructure analysis of Chapter 4, Section 4.11 rather than on the synthetic population.

The complete run, including the exhaustive cross-check over 65,536 assignments, completes in under one-twentieth of a second on ordinary hardware, which is stated only to indicate that reproduction costs a reader nothing and is not offered as a performance result.

The artefact is publicly available, which converts the reproducibility claim from an assertion into something a reader can test while reading. The source repository and a hosted demonstration are listed in Appendix A. The hosted application executes the same unmodified source and verifies, at the point of execution, that its run reproduces the figures reported in this chapter; it reports a failure notice rather than results if it does not. No claim in this thesis depends on the hosted application remaining available, and the repository, not the hosting, is the artefact.

The demonstration therefore supports precisely the claim Chapter 1 made for it: the artefact behaves as specified, and the specification's central results are checkable by a reader who declines to take the proofs on trust.

---

## References (Chapter 5)

HL7 Norway. (2025). *hl7.fhir.no.basis* (Version 2.2.2, released 27 March 2025) [FHIR R4 national base profile package]. Simplifier.net. https://simplifier.net/packages/hl7.fhir.no.basis/2.2.2

Walonoski, J., Kramer, M., Nichols, J., Quina, A., Moesel, C., Hall, D., Duffett, C., Dube, K., Gallagher, T., & McLachlan, S. (2018). Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record. *Journal of the American Medical Informatics Association*, *25*(3), 230–238. https://doi.org/10.1093/jamia/ocx079
