# Chapter 4. The Tri-Lateral Retention Feasibility Model and the Crypto-Erasure by Invalidation Mechanism

*Theorem statements and proofs in this chapter are the author's own. Regulatory claims are anchored to the primary instruments cited at each point.*

---

## 4.1 Purpose and Structure of the Chapter

This chapter contains the analytical core of the thesis. It does three things in sequence, and the sequence matters because each step licenses the next.

First, it establishes what the law actually requires to be retained, as distinct from what current practice retains. This is the necessity analysis begun in Chapter 2, Section 2.3, and it produces the decomposition on which the model rests.

Second, it constructs the Tri-Lateral Retention Feasibility (TRF) Model: a formal representation of the retention regimes as constraints over discretised time, together with two candidate semantics for what it means for an audit record to be verifiable. Within that model it states and proves two results. Theorem 1 establishes that under the semantics implicit in current practice the constraint system is infeasible. Theorem 2 establishes that under an alternative semantics the system is jointly satisfiable, and its proof is constructive: it exhibits the mechanism that achieves satisfaction.

Third, it specifies that mechanism, Crypto-Erasure by Invalidation, in enough detail to be implemented, analyses the residue it leaves behind against the legal threshold that residue must clear, compares it against the rival designs a reviewer would propose instead, and maps it onto the Norwegian infrastructure verified in Chapter 2.

The order of exposition follows the order in which the thesis has developed the problem: the cross-border primary-use case is treated first throughout, with the Secure Processing Environment case following as the second and sharper instance.

A note on what the theorems are and are not. They are mathematical statements about a model, proved informally at the standard of rigour normal for design-science work, and checked executably in Chapter 5. They are not machine-checked, and they are not claims about the world independent of the model's fidelity. Their force depends entirely on whether the constraints faithfully translate the instruments, which is why Section 4.2 documents that translation claim by claim rather than asserting it.

## 4.2 What Must Be Retained: The Necessity Analysis

The decomposition that makes the model possible is not a modelling convenience. It is derived from the legal position established in Chapter 2, Section 2.3, and it must be stated precisely because everything downstream inherits it.

Article 17(3)(b) GDPR exempts from erasure processing that is necessary for compliance with a legal obligation. The audit-retention obligations are such obligations. But the exemption is bounded by necessity, and Article 5(1)(c) requires that personal data be adequate, relevant, and limited to what is necessary for the purposes of processing. The question is therefore not whether an audit record may be retained, but which parts of it necessity protects.

The purpose that the retention obligations serve is accountability: establishing, after the fact, that a particular access occurred, by whom, when, under what authority, and with what result. That purpose is served by the event metadata. It is not served by continued controller access to the clinical content of the document that was exchanged. A supervisory authority investigating whether a Spanish clinician's access to a Norwegian patient summary in March 2027 was lawful needs to know that the access occurred, which clinician performed it, under which eIDAS assertion, against which consent policy, and whether it succeeded. It does not need to read the patient's medication list to answer that question.

This yields the central claim of the necessity analysis: *the accountability function of a cross-border audit record is discharged by its metadata and by a binding commitment to its payload, and does not require the payload to remain accessible.* Retention of accessible plaintext payload for ten years therefore exceeds what Article 17(3)(b) protects. Article 5(1)(c) positively requires that it not be retained where the purpose can be achieved without it.

Two supports and one limit should be recorded. The Norwegian Data Protection Authority's internal-control guidance places exactly this weighing on the controller, requiring determination of lawful retention periods and deletion deadlines through explicit balancing of purpose, business need, and both retention rights and retention duties (Datatilsynet, n.d.-a). The Authority's privacy-by-design guidance equates anonymisation with deletion (Datatilsynet, n.d.-b), which is what permits a transformed record to satisfy an erasure obligation at all. The limit is that the same Authority sets a high threshold for when data cease to be personal: encryption protects data rather than rendering them unidentifiable, and data remain personal while any key or linkage capable of re-identification is retained (Datatilsynet, 2015). The residue left by the mechanism must therefore be analysed against that threshold rather than assumed to clear it, which is the work of Section 4.9.

## 4.3 The Model: Objects and Notation

Let the time domain be discretised into months, indexed by $t \in \mathbb{N}$, with $t = 0$ the month in which the system begins operation. Monthly granularity is chosen because every obligation in the system is expressed in months or years, and because the shortest deadline in the system, the erasure response period, is one month.

Let $A$ be the set of audit records. Each record $a \in A$ is generated by a single access event and is represented as a tuple

$$
a = \big(\, m(a),\; p(a),\; c(a),\; k(a),\; t(a),\; F(a),\; \sigma(a) \,\big)
$$

where:

- $m(a)$ is the *event metadata*: the actor identifier, the actor's national contact point, the patient pseudonym, the document category accessed, the legal basis and consent policy applied, the timestamp, and the outcome. Metadata contains no clinical content.
- $p(a)$ is the *personal-data payload*: the content of the clinical document exchanged.
- $c(a)$ is a *commitment* to the payload, $c(a)$ = Commit($p(a), r(a)$), where $r(a)$ is a per-record random salt. The commitment scheme is required to be *hiding* (the commitment reveals nothing about the payload to an adversary without the salt) and *binding* (no second payload can be opened against the same commitment). The requirement that it be hiding rather than a bare hash is a consequence of Section 4.9 and is not optional.
- $k(a)$ is the *payload key*: the key material under which $p(a)$ is stored.
- $t(a)$ is the month in which the access event occurred.
- $F(a) \in \mathbb{N}$ is the *retention floor* applying to the record, expressed in months.
- $\sigma(a) \in \{\text{primary}, \text{secondary}\}$ is the *pathway* in which the record arose.

The floor is a parameter of the record rather than a constant of the model. The form is taken from chain-of-custody practice in physical cross-border logistics, where a consignment carries one custody record whose retention parameter is set by whichever jurisdiction's regime governs it, rather than a separate ledger per jurisdiction; Chapter 2, Section 2.7 sets out the correspondence. In the present setting it takes two values:

- $F(a) = 120$ for cross-border audit records held in ATNA-compliant audit repositories, this being the ten-year minimum imposed by the eHDSI deployment baseline for MyHealth@EU operations (Simjanoska Misheva et al., 2025). The IHE ATNA profile itself prescribes no retention period; the floor arises from the deployment binding, and the model is correct only if this distinction is preserved.
- $F(a) = 12$ for access and activity logs of Secure Processing Environments, this being the one-year minimum imposed by Article 73(1)(e) of Regulation (EU) 2025/327 (European Parliament and Council of the European Union, 2025).

Two event processes act on records. An *erasure request* arrives for record $a$ at month $t_r(a)$ if the data subject exercises Article 17 in respect of the personal data underlying that record; if no request arrives, $t_r(a) = \infty$. A *permit expiry* occurs at month $t_\pi(a)$ for records with $\sigma(a)$ = secondary, being the month in which the data permit under which the processing occurred expires; for primary-pathway records $t_\pi(a) = \infty$.

Finally, let $\alpha(a,t) \in \{0, 1\}$ be the *payload-accessibility variable*: $\alpha(a,t) = 1$ if the controller can recover $p(a)$ in intelligible form at month $t$, and 0 otherwise. This single binary variable per record per month is the entire state space of the model, and its minimality is deliberate: the conflict turns on exactly one question, which is whether the payload is readable, and a formulation that admits no other state variable cannot obscure that question behind modelling detail. The cost of that minimality is that the model cannot represent field-level redaction, where some elements of a payload are erased and others retained; Chapter 3, Section 3.7 records this as a stated abstraction.

Let $V(a,t) \in \{0, 1\}$ denote whether record $a$ *counts as verifiable* at month $t$. $V$ is not defined yet; defining it is the subject of Section 4.5, and the two competing definitions are what the theorems distinguish.

## 4.4 The Three Constraints

Each regime is now expressed as a constraint on the trajectory of $\alpha$ and $V$.

*C1: Retention floor.* For every record $a$ and every month $t$ with $t(a) \le t \le t(a) + F(a)$:

$$
V(a,t) = 1 \qquad \forall\, t \in \big[\, t(a),\; t(a) + F(a) \,\big]
$$

The record must count as verifiable throughout its retention window. Source: eHDSI deployment baseline for $F = 120$; Article 73(1)(e) EHDS for $F = 12$.

*C2: Erasure right.* For every record $a$ for which a valid erasure request arrives at $t_r(a) < \infty$, and for every month $t \ge t_r(a) + \delta$:

$$
\alpha(a,t) = 0 \qquad \forall\, t \ge t_r(a) + \delta
$$

The payload must cease to be accessible within the response period $\delta$. Source: Article 17(1) GDPR, with $\delta$ determined by Article 12(3) GDPR, which requires the controller to act without undue delay and in any event within one month of receipt, extendable by two further months for complex or numerous requests provided the data subject is informed within the first month. The model takes $\delta = 1$ as the baseline and admits $\delta = 3$ as the extended case; results are stated for arbitrary finite $\delta$ and do not depend on which is chosen. Constraint C2 is triggered only by a *valid* request. The model does not represent the Article 17(3) exemptions under which a controller may lawfully refuse, and so treats every arriving request as valid; Chapter 3, Section 3.7 explains why this affects the frequencies reported in Chapter 5 but not the theorems.

*C3: Deletion ceiling.* For every record $a$ with $\sigma(a)$ = secondary and every month $t \ge t_\pi(a) + 6$:

$$
\alpha(a,t) = 0 \qquad \forall\, t \ge t_\pi(a) + 6
$$

Personal data must not remain accessible in the Secure Processing Environment more than six months after permit expiry. Source: Article 68(12) EHDS as operationalised by TEHDAS2 (2025).

The structural asymmetry between C1 on one hand and C2–C3 on the other is the whole problem. C1 is a lower bound on the persistence of a property; C2 and C3 are upper bounds on the persistence of accessibility. Whether they conflict depends entirely on whether $V$ is defined in terms of $\alpha$, which is the question Section 4.5 makes explicit.

## 4.5 Two Semantics of Verifiability

*Semantics I: plaintext verifiability.* A record counts as verifiable exactly when its payload is accessible:

$$
V^{I}(a,t) = \alpha(a,t)
$$

This is the semantics implicit in the design of audit systems that predate the erasure right. Under it, an audit record whose payload cannot be produced is treated as an incomplete or broken record, and audit integrity is understood as the continued producibility of what was accessed. No instrument in the system states this semantics; it is inherited from practice, which is precisely why it has not been examined.

*Semantics II: accountability-preserving verifiability.* A record counts as verifiable when its accountability content is intact and any loss of payload accessibility is itself accounted for:

$$
V^{II}(a,t) = 1 \iff \text{(i)} \wedge \text{(ii)} \wedge \text{(iii)}
$$

where, at month $t$: (i) $m(a)$ is intact and unmodified; (ii) $c(a)$ is present and binding; and (iii) if $\alpha(a,t') = 1$ for some $t' < t$ and $\alpha(a,t) = 0$, then an invalidation entry $\iota(a)$ recording the transition, its month, its legal ground, and its authorising actor, is present in the audit trail and is itself covered by (i).

Under Semantics II an audit record that has lost its payload is not a broken record. It is a complete record of an access event *and* of the lawful invalidation of that event's payload. The audit trail grows rather than shrinks when erasure occurs.

Neither semantics is stipulated by the instruments. Section 4.10 argues that Semantics II is the better reading of what the instruments require; the theorems below establish what follows from each.

## 4.6 Theorem 1: Infeasibility under Plaintext Verifiability

> *Theorem 1.* Under Semantics I, the constraint system $\{C1, C2, C3\}$ is infeasible for any record $a$ such that
>
> $$
> t_r(a) + \delta \le t(a) + F(a) \quad\text{or}\quad t_\pi(a) + 6 \le t(a) + F(a).
> $$

*Proof.* Take a record $a$ satisfying the first disjunct, and let $t^{*} = t_r(a) + \delta$. By hypothesis $t^{*} \le t(a) + F(a)$, and since erasure requests arrive after the access that generates the record, $t^{*} \ge t(a)$. Hence $t^{*}$ lies within the retention window, so C1 requires $V(a,t^{*}) = 1$. Under Semantics I, $V^{I}(a,t^{*}) = \alpha(a,t^{*})$, so C1 requires $\alpha(a,t^{*}) = 1$. But C2 requires $\alpha(a,t) = 0$ for all $t \ge t_r(a) + \delta = t^{*}$, so C2 requires $\alpha(a,t^{*}) = 0$. The two requirements are contradictory, and no assignment of $\alpha$ satisfies both. The argument for the second disjunct is identical with $t^{*} = t_\pi(a) + 6$ and C3 in place of C2. ∎

*Corollary 1.1 (cross-border case).* For cross-border audit records, $F(a) = 120$. The system is infeasible for record $a$ whenever an erasure request arrives at any month $t_r(a) \le t(a) + 120$ − $\delta$: that is, at any point in the first nine years and eleven months of a ten-year window under the baseline response period. Infeasibility is therefore not an edge case arising from unusual timing; it is the generic case, avoided only if no data subject exercises Article 17 in respect of any record for essentially the whole of its retention life.

*Corollary 1.2 (Secure Processing Environment case).* For Secure Processing Environment access logs, $F(a) = 12$ and $\sigma(a)$ = secondary. Suppose the permit expires at or before the sixth month of the record's retention window, so that $t_\pi(a) + 6 \le t(a) + 12$. Then C1 and C3 are contradictory at $t^{*} = t_\pi(a) + 6$ by the argument above. *On the broad reading of Article 68(12) defended below, no erasure request is required.* The infeasibility then follows from two provisions of a single regulation acting on a single environment. Article 73(1)(e) requires the identifiable log to remain verifiable for twelve months, and Article 68(12) requires personal data to be gone from the environment six months after permit expiry. Where the remaining permit duration at the time the log is written is six months or less, the two windows necessarily overlap. The model makes no claim about how often this occurs in practice; the collision's existence, not its frequency, is what Corollary 1.2 asserts.

Corollary 1.2 is the sharpest form of the thesis's problem statement. It shows that the conflict does not depend on the exercise of a data-subject right, on the eHDSI deployment baseline, or on any synthesis across instruments of differing legal weight. It is internal to Regulation (EU) 2025/327.

*The interpretive condition on which Corollary 1.2 depends.* The corollary holds if, and only if, the deletion obligation of Article 68(12) reaches the identifiable access logs that Article 73(1)(e) requires to be kept. That condition is contestable and must be stated as such rather than assumed, because the corollary is the sharpest claim in this thesis and a reader is entitled to see its weakest joint.

The textual case for the broad reading is that the provision governs *the data within the secure processing environment*, a formulation defined by location rather than by provenance. It does not say "the data made available under the data permit," though the Regulation uses that narrower formulation freely elsewhere, and the access logs are indisputably data within the environment. On that reading Article 68(12) reaches them, and Corollary 1.2 follows.

The contextual case for the narrow reading is that the provision sits within the data-permit article, adjacent to provisions on permit duration, extension, and storage fees, and that the mischief it addresses is the indefinite retention of permitted datasets after the purpose that justified them has lapsed. On that reading the obligation attaches to the permit dataset, the access logs fall outside it, and no collision between Articles 68(12) and 73(1)(e) arises.

This thesis adopts the broad reading and states the grounds rather than asserting the conclusion. But the architecture of the results is deliberately such that little turns on which reading prevails, and that should be made explicit. Under the narrow reading, Corollary 1.2 lapses, and with it the claim that infeasibility arises without any data-subject action. Theorem 1 itself is untouched, because its first disjunct concerns erasure requests rather than permit expiry: identifiable access logs remain personal data whoever provided them, they remain within the scope of Article 17, and a request arriving inside the twelve-month floor collides with Article 73(1)(e) exactly as the cross-border case collides with the eHDSI floor. Corollary 1.1 is untouched entirely. Theorem 2, the mechanism, and the residue analysis are untouched, since they are indifferent to which instrument generates the deadline.

The narrow reading therefore costs the thesis its sharpest instance and none of its results. The broad reading, if correct, adds a collision that requires no data subject to act. Chapter 6 treats the resolution of this interpretive question as a matter for supervisory authority rather than for this author, alongside the authority question concerning verifiability itself.

## 4.7 Theorem 2: Feasibility under Accountability-Preserving Verifiability

> *Theorem 2.* Under Semantics II, the constraint system $\{C1, C2, C3\}$ is jointly satisfiable for every record $a \in A$, for every arrival pattern of erasure requests $\{t_r(a)\}$ and permit expiries $\{t_\pi(a)\}$, and for every floor parameter $F(a) \in \mathbb{N}$.

*Proof (constructive).* Define the following trajectory for an arbitrary record $a$. Let

$$
t^{I}(a) = \min\big(\, t_r(a) + \delta,\;\; t_\pi(a) + 6 \,\big)
$$

be the *invalidation month*, with the convention min($\infty, \infty) = \infty$. Construct the trajectory:

1. For $t < t^{I}(a)$: set $\alpha(a,t) = 1$. Retain $m(a), c(a), k(a)$, and $p(a)$.
2. At $t = t^{I}(a)$, if finite: destroy $k(a)$ irreversibly; append to the audit trail an invalidation entry $\iota(a)$ recording the month, the legal ground (Article 17(1) or Article 68(12) as applicable), and the authorising actor; retain $m(a)$ and $c(a)$ unchanged.
3. For $t > t^{I}(a)$: set $\alpha(a,t) = 0$. Retain $m(a), c(a)$, and $\iota(a)$.

It must be shown that this trajectory satisfies all three constraints.

*C2 is satisfied.* If $t_r(a) < \infty$ then $t^{I}(a) \le t_r(a) + \delta$ by construction, and by steps 2–3, $\alpha(a,t) = 0$ for all $t \ge t^{I}(a)$, hence for all $t \ge t_r(a) + \delta$. If $t_r(a) = \infty$, C2 is vacuous.

*C3 is satisfied.* If $\sigma(a)$ = secondary and $t_\pi(a) < \infty$ then $t^{I}(a) \le t_\pi(a) + 6$, and by the same steps $\alpha(a,t) = 0$ for all $t \ge t_\pi(a) + 6$. Otherwise C3 is vacuous.

*C1 is satisfied.* Let $t$ be any month in the retention window, $t(a) \le t \le t(a) + F(a)$. Condition (i) holds because no step of the construction modifies or removes $m(a)$. Condition (ii) holds because no step removes $c(a)$; the commitment is not derived from $k(a)$ and its persistence is unaffected by key destruction. For condition (iii): if $\alpha(a,t) = 1$ the condition is vacuous; if $\alpha(a,t) = 0$ then $t \ge t^{I}(a)$, and step 2 has placed $\iota(a)$ in the audit trail, where step 3 retains it, and $\iota(a)$ is covered by (i). Hence $V^{II}(a,t) = 1$ throughout the window. The terminal transition of Section 4.8 takes place after the window and is not part of this trajectory.

All three constraints are satisfied, for arbitrary arrival times and arbitrary $F(a)$. ∎

*Corollary 2.1.* The construction requires no coordination between the erasure process and the retention process, and no knowledge at the time a record is created of whether an erasure request will ever arrive. The invalidation month is determined entirely by events as they occur.

*Corollary 2.2.* Because $F(a)$ is arbitrary in the proof, the result holds simultaneously for the ten-year cross-border floor and the one-year Secure Processing Environment floor, and for any national floor substituted for either. The model is tri-lateral in constraint type and indifferent to the number of floor instances.

*A note on what kind of result this is.* An objection should be anticipated rather than left for a reader to formulate: that Theorem 2 proves little, because Semantics II was defined in full knowledge of the trajectory that satisfies it. The objection has force and the response is to concede its premise and deny its conclusion. The mathematical content of Theorem 2 is indeed modest: once verifiability is decoupled from payload accessibility, the existence of a satisfying trajectory is close to immediate, and the proof is a verification rather than a discovery. But the substantive claim of this chapter was never that a satisfying trajectory exists under some semantics; any number of semantics would admit one, including trivial semantics under which every record counts as verifiable always. The claim is that *this* semantics is a defensible reading of what the retention obligations require, grounded in the necessity boundary of Article 17(3)(b), the minimisation principle of Article 5(1)(c), and the accountability purpose the obligations serve. It is also the weakest departure from current practice that achieves feasibility, preserving every element of the audit record that the accountability purpose needs and discarding only what it does not. Theorem 1 carries the load that Theorem 2 does not: it establishes that *some* departure is unavoidable, because the status quo admits no solution at all. Theorem 2 then shows that a principled and minimal departure suffices. The legal defensibility of Semantics II is argued in Section 4.2 and its want of authority is confronted in Chapter 6, Section 6.2; it is not established by the theorem, and no reader should take the theorem as establishing it.

*What the theorem does and does not establish.* It establishes that the constraint system as formalised admits a solution, and exhibits one. It does not establish that the exhibited solution is lawful (that depends on whether the residue it leaves clears the legal threshold, which Section 4.9 addresses) nor that key destruction can be verified by an external party, which Section 4.10 concedes it cannot. The invalidation entry specified in Section 4.8 is an *attested* record of destruction, not a *proof* of it; the proof-of-secure-erasure and certified-deletion literatures reviewed in Chapter 2, Section 2.4 mark that boundary, and Chapter 6 treats it as the outer limit of the contribution. Theorem 2 is a mathematical result about a model, and its value is that it converts a question that has been debated qualitatively into one with a definite answer under stated assumptions.

## 4.8 The Mechanism: Crypto-Erasure by Invalidation

The trajectory constructed in the proof of Theorem 2 is the specification of the mechanism. This section states it as an implementable design.

*Key hierarchy.* Each record's payload is encrypted under a per-record data key $k(a)$. Per-record rather than per-subject or per-dataset granularity is required because the invalidation events of Theorem 2 occur at record granularity: a permit expiry invalidates the records of one permit, while an erasure request invalidates the records relating to one data subject, and these sets intersect without nesting. Data keys are themselves held under a key-encrypting key in a hardware security module or equivalent custody boundary. Destruction of $k(a)$ is effected by destruction of the wrapped data key and any cached copies, within the documented custody boundary.

*Ciphertext.* At $t^{I}(a)$ the ciphertext of $p(a)$ is deleted from the audit store together with $k(a)$. Nothing in Semantics II uses it once the key is gone, and deleting it removes the exposure that a retained ciphertext would carry to future cryptanalytic capability, quantum capability included, over the rest of a ten-year floor (Section 4.9). Key destruction remains the operative erasure for copies the store cannot delete at once, such as replicas and backups: they become unreadable at $t^{I}(a)$ and leave by ordinary rotation.

*Commitment.* $c(a)$ = Commit($p(a), r(a)$) with a per-record salt $r(a)$. The salt is stored with the metadata until invalidation and is destroyed together with $k(a)$ at $t^{I}(a)$. Before invalidation it lets an auditor open the commitment against the payload. After invalidation no opening can be checked, because the payload is no longer readable, while a retained salt would let anyone holding a candidate payload confirm a guess against $c(a)$ (Section 4.9). Destroying the salt does not weaken binding, which is a property of the commitment value: no second payload can be opened against $c(a)$, and after $t^{I}(a)$ no payload can be opened against it at all. A party that holds its own copy of the payload and must later prove that it corresponds to $c(a)$ has to obtain and keep the opening before invalidation; the audit store does not keep one for it. The scheme must be hiding: an adversary holding $c(a)$ and lacking $r(a)$ must learn nothing about $p(a)$. A bare unsalted hash of the payload does not satisfy this and must not be used, for the reason given in Section 4.9.

*The invalidation registry.* Invalidation entries are appended to the audit trail as first-class records. Each entry $\iota(a)$ contains the identifier of the invalidated record, the invalidation month, the legal ground, the authorising actor, and a commitment to the destroyed key's identifier: not to the key itself. The registry is append-only. Invalidation is an event that is logged, not an event that erases the log.

*Accumulator-based validity witnesses.* The set of currently valid (non-invalidated) records is maintained in a dynamic cryptographic accumulator supporting efficient revocation (Camenisch & Lysyanskaya, 2002). This provides an auditor with a succinct proof that a given record either is or is not currently valid, without the auditor enumerating the registry. The accumulator is an efficiency and verifiability layer, not a load-bearing component of the theorems: Theorem 2 holds if validity is established by linear scan of the registry, and the accumulator makes that check succinct. The accumulator is specified but not implemented in the artefact (Section 6.1). Dynamic accumulators of the Camenisch and Lysyanskaya type also require a trusted accumulator manager holding a trapdoor, which adds a trust assumption stated in Section 4.9.

*The auditor's view.* After invalidation, an external auditor examining record $a$ can establish four things. The access event occurred, with all its accountability attributes, which follows from $m(a)$. A specific payload was bound to that event, which follows from $c(a)$. The payload was invalidated, and the auditor can see when, on what legal ground, and by whom, from $\iota(a)$. And the record's current validity status is as claimed, which follows from the accumulator witness where that layer is used, and otherwise from a scan of the registry. What the auditor cannot do is read the payload. This is the intended state, and it is the difference between this mechanism and the practitioner crypto-shredding pattern reviewed in Chapter 2, Section 2.4: that pattern retains ciphertext and asserts that erasure occurred, whereas this mechanism produces a verifiable record of what was invalidated and under what authority.

*End of life at floor expiry.* The constraints of Section 4.4 govern the record's behaviour through its retention window, but the window ends, and the model would be incomplete if it said nothing about what follows. After $t = t(a) + F(a)$, the last month of the closed window on which C1 is defined, the retention obligation lapses, and with it the necessity that justified retaining $m(a)$ under Article 17(3)(b). Because the metadata contains the patient pseudonym and the actor identifier, it is personal data, and the storage-limitation principle of Article 5(1)(e) GDPR requires that it not be kept in identifiable form longer than the purpose demands. The mechanism therefore specifies a terminal transition. In the first month after the window, $t(a) + F(a) + 1$, the record undergoes a second invalidation, in which the identifying fields of $m(a)$ are destroyed, together with $k(a)$, the salt $r(a)$ and the ciphertext where no earlier invalidation removed them. What remains is a non-identifiable residue, being the event type, the document category, the outcome, and the commitment, which is sufficient for statistical and assurance purposes and insufficient to relate the record to any data subject. The terminal transition is itself logged, and the record's final state is the only state in the mechanism that is intended to be anonymous rather than pseudonymous in the sense of Section 4.9. Where a longer-running obligation applies to the same record (a national archival duty, or litigation hold) the terminal transition is deferred and the floor parameter $F(a)$ is set to the longer period, which is the parameterisation the model already supports.

*Applying the mechanism to the two cases.* For the cross-border primary-use case, the mechanism operates at the audit repository of the National Contact Point, at the point where the ATNA audit record is written. For the Secure Processing Environment case, it operates at the environment's access-logging boundary. The identifiable log required by Article 73(1)(e) is written with its personal-data content committed rather than retained in plaintext beyond the ceiling. At $t_\pi(a) + 6$, the environment therefore holds a complete, identifiable, verifiable log of access with no recoverable personal-data payload. The environment is thereby cleared of accessible personal data at the ceiling while continuing to satisfy the floor to its full twelve months.

## 4.9 Residue Analysis

Theorem 2 leaves a residue: $m(a), c(a), \iota(a)$ and, where the optional layer is used, the accumulator state. The salt $r(a)$, the key $k(a)$ and the ciphertext of $p(a)$ are destroyed at invalidation (Section 4.8). Whether the mechanism is lawful depends on whether this residue sits on the correct side of the threshold at which data cease to be personal. This section performs that analysis, and it is included because Chapter 2 identified its absence as the fourth gap in the literature.

*The threat.* Finck's analysis for the European Parliament establishes that hashed or encrypted data likely remain personal data under GDPR so long as re-identification remains possible (Finck, 2019; Finck, 2018). Applied to this mechanism, the threat is direct: if $c(a)$ is an unsalted hash of the payload, then an adversary who can guess candidate payloads can confirm a guess by recomputing the hash. For clinical documents drawn from a constrained space (a diagnosis code, a medication from a formulary) the guessing space may be small enough to make this practical. An unsalted commitment would therefore be a surviving item of personal data, and the mechanism would have relocated the erasure problem rather than solved it.

*The response.* This is why the hiding property is a requirement of the design and not an implementation preference. With a per-record salt $r(a)$ of adequate length, confirming a guessed payload requires the salt; the commitment alone leaks nothing. Because the salt is destroyed with the key, no party can confirm a guessed payload against $c(a)$ after invalidation unless it kept its own opening beforehand. What has been destroyed is both the ability to *recover* the payload, which depended on $k(a)$, and the ability to confirm a guess about it from the audit store, which depended on $r(a)$.

*The honest limit.* The residue therefore does not meet the strict Norwegian anonymisation threshold. Datatilsynet's guidance holds that encryption protects rather than anonymises, and that data remain personal while any key or linkage capable of re-identification is retained (Datatilsynet, 2015). By that standard the residue, which keeps metadata identifying the access event, is best characterised as pseudonymised rather than anonymous until the terminal transition. This thesis does not claim otherwise, and any claim that the mechanism achieves anonymisation would be false.

*Why the mechanism is nonetheless defensible.* The applicable legal test is not anonymisation but erasure. The European Data Protection Board's Guidelines 02/2025 accept that where physical deletion is not technically possible, deleting the decryption key can render data unintelligible and so serve the erasure obligation. They maintain at the same time that encrypted and hashed data may remain personal data, and that the unintelligibility holds at least until the algorithm is broken (European Data Protection Board, 2026b). The requirement that the controller document the threat model under which the data are considered unrecoverable is not the Board's formulation. It is Aikebaier's (2026) interpretation, which connects a Destruction-IND security notion to the Board's criterion, and it is adopted here as a design discipline rather than asserted as a regulatory requirement. The final version 2.0, adopted on 7 July 2026 after public consultation, sharpens rather than softens the constraint this places on the present mechanism: it confirms that both metadata and content may in principle constitute personal data, and that this may extend to encrypted and hashed data. The residue characterisation of this section is therefore the one the Board's final position requires, and a thesis claiming anonymisation for that residue would now be contradicted by the guidance it relies upon. Aikebaier's (2026) systematisation formalises this correspondence, establishing an equivalence proposition between a Destruction-IND security notion and the Board's unrecoverability criterion. The design consequence is that the mechanism's lawfulness rests on a documented threat model, which must state: the custody boundary within which key destruction occurs; the assumed adversary's access to that boundary; the leakage assumptions for the hardware holding key material; and the algorithmic-break horizon over which the ciphertext's confidentiality is assumed to hold. A mechanism deployed without that documentation would not satisfy the Board's condition however sound its cryptography.

*The trust assumptions, stated explicitly.* Because key destruction is attested rather than proven, the mechanism's guarantees rest on a set of assumptions that a deploying institution must be willing to accept, and naming them is part of the documentation the Board's condition requires.

The controller is trusted to execute destruction when the invalidation entry says it did, and to have had no copy of the key outside the custody boundary at that moment. The custody boundary itself, whether a hardware security module or an equivalent key-management service, is trusted not to retain recoverable key material after a destruction instruction, and not to leak it through side channels during its lifetime. The audit-trail operator is trusted not to remove or alter entries, which the append-only construction makes detectable but not impossible. Where the optional accumulator layer is used, its manager is also trusted, since a party holding the accumulator trapdoor can forge validity witnesses. And the cryptographic assumption is that the commitment scheme remains binding and hiding, and the payload cipher remains unbroken, across the retention horizon.

What an external auditor can verify without any of this trust is bounded and worth stating precisely. The auditor can verify that the metadata is internally consistent, that an invalidation entry exists with its month, ground and authorising actor, and that the entry is bound into the append-only trail. The auditor can also verify that a commitment survives, to which a payload could be opened if one were produced. What the auditor cannot verify is that the key is gone. That gap is the difference between attestation and proof, and it closes only with hardware-backed or cryptographically certified deletion, which Chapter 6, Section 6.3 treats as the boundary of this contribution.

*The residual cryptographic risk.* Over a ten-year floor, the algorithmic-break horizon is a live concern rather than a formality: anything retained for a decade must be assumed to face cryptanalytic capability that does not exist when it is written. Deleting the ciphertext at invalidation (Section 4.8) removes this exposure for the store's own copy, so what is retained long-term is metadata, the commitment and the invalidation entry. The risk is reduced, not eliminated. Copies the store cannot delete at once, such as backups, hold ciphertext until rotation removes them; a record with no invalidation event keeps its ciphertext until the terminal transition; and the commitment must stay hiding across the horizon, which is a requirement on the hash function rather than on a cipher. This is recorded as a limitation in Chapter 6 rather than resolved here.

## 4.10 Rival Designs

A reviewer will propose alternatives. Five are treated here, and each is rejected for a stated reason rather than by assertion.

*Rival 1: Rely on the Article 17(3)(b) exemption and retain in full.* This is the dissolution argument answered in Chapter 2, Section 2.3 and Section 4.2 above. It fails on the necessity boundary: the exemption protects retention that the legal obligation requires, and Section 4.2 established that the accountability purpose does not require payload accessibility. It fails additionally and decisively in the Secure Processing Environment case, where Article 68(12) admits no exemption parallel to Article 17(3)(b), so that Corollary 1.2's infeasibility survives the argument entirely.

*Rival 2: Anonymise the audit record instead.* If the record were genuinely anonymised, Datatilsynet's equation of anonymisation with deletion would discharge the erasure obligation (Datatilsynet, n.d.-b). But genuine anonymisation of a cross-border audit record destroys its accountability function: an audit trail that cannot identify which clinician accessed which patient's record is not an audit trail, and Article 73(1)(e) requires the logs to be *identifiable* in terms. Anonymisation satisfies C2 and C3 by violating C1.

*Rival 3: Minimise the payload at capture, so that nothing needs erasing.* Recording less at the outset is good practice and is compatible with this mechanism. It does not solve the problem, because the metadata that the accountability purpose requires, the patient pseudonym linking the access to a data subject, is itself personal data, and is precisely what an erasure request targets. Minimisation shrinks the payload; it does not remove the record from the scope of Article 17.

*Rival 4: Delete the record and log the deletion.* This is the closest rival and deserves the most care. Deleting the audit record while logging that a deletion occurred satisfies C2 and C3, and preserves a trace. It fails C1 under both semantics: under Semantics I trivially, and under Semantics II because condition (ii) fails: no commitment survives, so the auditor can establish that *something* was deleted but not that the deleted item was the payload bound to that specific access event. The distinction matters in adversarial conditions. A controller who deletes records and logs deletions can conceal the substitution of one record for another; a controller bound to a surviving commitment cannot. The mechanism's advantage over Rival 4 is precisely the verifiability that Chapter 2 identified as absent from the practitioner crypto-shredding pattern.

*Rival 5: Retain recoverable encrypted copies until the later date.* This is the resolution developed in the closest prior art, the DePaul retention-and-purging programme reviewed in Chapter 2, Section 2.4. It holds encrypted copies in shadow tables and backups, with each copy's key selected to expire on the governing purge date, and effects purging by destroying that key (Scope, Rasin, Lenard, Heart, & Wagner, 2022; Scope & Rasin, 2025). Where both obligations are floors and the purge date is fixed in advance, this is the right design.

It cannot work against a ceiling, and the reason is the residue analysis of Section 4.9 applied in reverse. A copy whose key still exists is recoverable, and recoverable ciphertext held together with the means of decryption remains personal data under the threshold set out in Chapter 2, Section 2.3. Retaining such copies to satisfy the Article 73(1)(e) floor is therefore exactly what the Article 68(12) ceiling forbids of the environment holding them. The prior art satisfies a retention obligation by preserving recoverability; the mechanism specified here satisfies one by destroying recoverability and preserving accountability instead. That inversion, rather than any difference in cryptographic technique, is what the tri-lateral case requires.

*The critique that is not a rival.* SecuPi (2025) argues that cryptographic erasure introduces operational complexity in row-level encryption scenarios and that auditable key management adds rather than removes overhead. This is not an alternative design for the problem; it is a cost objection, and it is partly correct. Per-record key granularity in a high-volume audit repository is an operational burden. The response is that the burden is the price of a solution to a problem that has none otherwise, and that the burden falls on audit records rather than on clinical data stores, which is the smaller of the two surfaces. Chapter 6 engages this critique at length rather than dismissing it.

## 4.11 Integration with the Norwegian Infrastructure

The mechanism is specified against the Norwegian infrastructure as verified in Chapter 2, Section 2.6, not against an idealisation of it.

*Primary use: the National Contact Point.* Norway's NCPeH is in live pilot operation at the Bodø and Stjørdal emergency clinics, receiving patient summaries from Portugal, Czechia, and Finland, with expansion to further emergency clinics requested (Helsedirektoratet, 2026). The mechanism attaches at the sixth step of the OpenNCP transmission flow, where the ATNA audit record is written to the audit repository. It requires no change to service discovery, patient discovery, document retrieval, pivot translation, or the security and consent module. This placement is deliberate: it is the narrowest point of the flow at which the intervention achieves its purpose, and interventions at the other five steps would touch the interoperability surface that Member States have agreed and Norway has implemented.

*Secondary use: Helsedataservice and the Secure Processing Environments.* Helsedataservice holds decision authority for eleven central health registries (Folkehelseinstituttet, 2024). The mechanism attaches at the access-logging boundary of the Secure Processing Environment rather than inside the environment's analytical machinery. This placement is forced by the empirical finding that the Norwegian environment landscape is fragmented well beyond the three NORTRE nodes, extending to controller-provided servers, folders, and in some cases consumer cloud services and disconnected personal computers (SPUHiN, 2024). A mechanism requiring capabilities of the environment would fail against that reality; a mechanism operating on the log the environment must in any case produce does not.

*Compatibility with the national criteria.* The finalised Norwegian criteria for Secure Processing Environments require an information-security management system as mandatory, recommend ISO 27001 certification, and require eID-based authentication at defined assurance levels (SPUHiN, 2025). The mechanism requires nothing beyond these: key custody within a documented boundary is an information-security-management concern of exactly the kind the mandatory requirement already covers. It adds no requirement that the criteria do not already impose, which was the design constraint derived from Chapter 2's third gap.

*Relation to the pending implementing acts.* The binding technical requirements for Secure Processing Environments are to be laid down by Commission implementing acts under Article 73(5) EHDS, due by 26 March 2027 (European Parliament and Council of the European Union, 2025), after the submission of this thesis. The secondary-use provisions they will operationalise become applicable on 26 March 2029 under Article 105. The specification published by TEHDAS2 during 2026 as deliverable D7.4 is the best available anticipation of their content (TEHDAS2, 2026). The mechanism is therefore specified against a moving target, and the appropriate claim is compatibility with the infrastructure as currently specified rather than compliance with requirements not yet adopted. Chapter 6 treats the implications of this timing for the thesis's policy relevance.

## 4.12 Summary

This chapter formalised the tri-lateral retention conflict as a constraint-satisfaction problem over a single binary accessibility variable per record, with the retention floor parameterised so that the ten-year cross-border audit floor and the one-year Secure Processing Environment log floor are instances of one constraint. It proved that under the plaintext-verifiability semantics implicit in current practice the system is infeasible, generically so in the cross-border case and, critically, without any erasure request at all in the Secure Processing Environment case, where two retention provisions of a single regulation collide over a single environment. It proved that under an accountability-preserving semantics the system is jointly satisfiable for every arrival pattern and every floor, and the proof exhibited the trajectory that achieves satisfaction. That trajectory, specified as Crypto-Erasure by Invalidation, retains metadata and a hiding commitment, and destroys the payload key at the earlier of the erasure deadline and the deletion ceiling. It appends the invalidation to the audit trail as a first-class, witnessed event. The salt and the payload ciphertext go with the key. At floor expiry it performs a terminal transition that destroys the identifying metadata, leaving a non-identifiable statistical residue, so that the record's whole life cycle, not merely its retention window, is accounted for under the storage-limitation principle.

The mechanism's residue was analysed rather than assumed: it is pseudonymised rather than anonymous by the strict Norwegian standard, it is defensible under the erasure test the European Data Protection Board has articulated provided the threat model is documented, and its long-horizon cryptographic risk is real and recorded. The limitations bearing on this chapter, the informal proof standard and the conditionality on honest key destruction among them, are those stated canonically in Chapter 3, Section 3.7 and are not restated here. Five rival designs were considered and rejected on stated grounds, and the principal cost objection was acknowledged rather than dismissed. The integration analysis placed the mechanism at the two narrowest points of the Norwegian infrastructure at which it achieves its purpose, requiring nothing of the substrate that the finalised national criteria do not already require.

Chapter 5 demonstrates both theorems executably, over synthetic records generated as described in Chapter 3.

---

## References (Chapter 4)

Aikebaier, Y. (2026). *SoK: Cryptographic erasure on public ledgers: Application-layer architectures, key-lifecycle adversaries, and GDPR Art. 17 equivalence* (Cryptology ePrint Archive, Paper 2026/1109). https://eprint.iacr.org/2026/1109 [Preprint; not peer-reviewed]

Camenisch, J., & Lysyanskaya, A. (2002). Dynamic accumulators and application to efficient revocation of anonymous credentials. In *Advances in Cryptology — CRYPTO 2002* (LNCS 2442, pp. 61–76). Springer. https://doi.org/10.1007/3-540-45708-9_5

Datatilsynet. (2015). *Anonymisering av personopplysninger: veileder*. Norwegian Data Protection Authority. https://www.datatilsynet.no/globalassets/global/dokumenter-pdfer-skjema-ol/regelverk/veiledere/anonymisering-veileder-041115.pdf

Datatilsynet. (n.d.-a). *Etablere internkontroll* [Guidance]. Norwegian Data Protection Authority. https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/etablere-internkontroll/

Datatilsynet. (n.d.-b). *Innebygd personvern og personvern som standard* [Guidance]. Norwegian Data Protection Authority. https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/innebygd-personvern-og-personvern-som-standard/

European Data Protection Board. (2026b). *Guidelines 02/2025 on processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB. https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf

European Parliament and Council of the European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. http://data.europa.eu/eli/reg/2016/679/oj

European Parliament and Council of the European Union. (2025). Regulation (EU) 2025/327 of 11 February 2025 on the European Health Data Space. *Official Journal of the European Union*. http://data.europa.eu/eli/reg/2025/327/oj

Finck, M. (2018). Blockchains and data protection in the European Union. *European Data Protection Law Review*, *4*(1), 17–35. https://doi.org/10.21552/edpl/2018/1/6

Finck, M. (2019). *Blockchain and the General Data Protection Regulation: Can distributed ledgers be squared with European data protection law?* European Parliament, STOA/EPRS.

Folkehelseinstituttet. (2024). *Helsedata* [Department page describing Helsedataservice, the national health data access body]. Norwegian Institute of Public Health. https://www.fhi.no/om/organisasjon/helsedata/

Helsedirektoratet. (2026). *MyHealth@EU, Helsedirektoratet* [National e-health portfolio measure]. Norwegian Directorate of Health. https://www.helsedirektoratet.no/digitalisering-og-e-helse/nasjonal-e-helseportefolje/tiltak-i-nasjonal-e-helseportefolje/myhealth-eu-helsedirektoratet

National Institute of Standards and Technology. (2025). *Special Publication 800-88 Revision 2: Guidelines for media sanitization* (R. Chandramouli & E. Hibbard). NIST. https://doi.org/10.6028/NIST.SP.800-88r2

Scope, N. C., & Rasin, A. (2025). *Systems and methods for data retention and purging* (U.S. Patent No. 12,425,209 B2, granted 23 September 2025). U.S. Patent and Trademark Office. https://patents.google.com/patent/US12425209B2/en

Scope, N., Rasin, A., Lenard, B., Heart, K., & Wagner, J. (2022). Harmonizing privacy regarding data retention and purging. In *Proceedings of the 34th International Conference on Scientific and Statistical Database Management (SSDBM 2022)* (pp. 1–12). ACM. https://doi.org/10.1145/3538712.3538718

SecuPi. (2025). *Crypto-shredding is not nirvana for right of erasure or RTBF compliance* [Industry commentary]. https://secupi.com/crypto-shredding-is-not-nirvana-for-right-of-erasure-or-rtbf-compliance/



SPUHiN. (2024). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (Draft, 29 November 2024; project 101128232, Milestone M10). Helsedirektoratet & Folkehelseinstituttet. https://helsedata.no/contentassets/bdc68d971f1343ed92fb3d3673fb9905/helsedataradet/utkast---recommendations-for-minimum-requirements-for-secure-processing-environments-in-norway_29.11.2024-1.pdf

SPUHiN. (2025). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (Deliverable D5.2, project 101128232; version issued for public hearing, July–October 2025) [Project deliverable]. Helsedirektoratet & Folkehelseinstituttet. The hearing page has since been withdrawn and no stable public locator for this version could be established; the deliverable number and the hearing window are confirmed on the project page at https://www.helsedirektoratet.no/om-oss/forsoksordninger-og-prosjekter/fair-secure-provision-and-use-of-health-data-in-norway-spuhin

TEHDAS2. (2025). *Guideline for Health Data Access Bodies on the procedures and formats for data access* (D6.3, Version 1.5, final draft, 17 September 2025). TEHDAS2 Joint Action. https://tehdas.eu/wp-content/uploads/2025/09/draft-guideline-for-health-data-access-bodies-on-the-procedures-and-formats-for-data-access.pdf

TEHDAS2. (2026). *Technical specification for Health Data Access Bodies on the implementation of secure processing environments* (D7.4, Version 1.2, 24 February 2026). TEHDAS2 Joint Action. https://doi.org/10.5281/zenodo.20266473
