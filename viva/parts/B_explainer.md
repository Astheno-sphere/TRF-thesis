# B. The core explainer

Read in order: each chapter defines its symbols before using them. Worked examples use the values `trf_checker.py` produces under seed 20260915; records the thesis does not name (38, 97, 102, 132, 133) are marked "from the checker". Pages are printed pages (body = PDF page minus 14). "Slide n (id)" is the deck position and file. The `r` and `m` link parameters act only on the `witness` page. Semantics I and II in the thesis are Reading I and II on the slides.

# B1. The problem in one record

## B1.1 Record 3: a cross-border audit record, month by month

**The event.** A Norwegian patient falls ill abroad; a clinician there requests her patient summary through the local National Contact Point for eHealth (NCPeH); the Norwegian NCPeH answers and writes one audit record. That record, not the health record, is the subject (§1.2, p. 3).

**What is created.** Record 3 in the generated run: created in month $t(a) = 11$ under the illustrative floor $F = 120$; actor `HP-003` via contact point `FI`; patient pseudonym `PSN-0003`; payload `<ITI-55 QBP name=N003 birthTime=1943 rid=3>`, standing for the demographic query that the IHE patient-discovery transaction (ITI-55) requires both gateways to record (§4.3, p. 52); commitment beginning `358f2a6ab39376d7`. An erasure request arrives in month $t_r = 115$. There is no permit: $t_\pi = \infty$.

| Month | What happens | What each rule demands |
|---|---|---|
| 11 | Access; record written to the audit repository | Floor starts: the record must be verifiable in every month from 11 to $11 + 120 = 131$ |
| 12 to 114 | Nothing new | Floor only. No conflict: the payload may stay readable |
| 115 | Patient asks for erasure under Art 17 GDPR | The controller has $\delta = 1$ month to act |
| 116 | Erasure deadline $t_r + \delta = 116$ | Erasure: payload unreadable from 116 onwards. Floor: record still verifiable |
| 116 to 131 | Both rules bind | If "verifiable" means "readable", the payload must be readable and unreadable in each of these 16 months ($131 - 116 + 1 = 16$) |
| 132 | Floor window has closed | No rule demands readability; the specified terminal transition would remove identifying metadata here (not implemented) |

**Where the demands collide.** The first collision month is 116. The checker prints this witness verbatim (§5.3, p. 83):

`C1 requires V=1 (=> alpha=1) at t=116 within [11,131]; C2 requires alpha=0 from t=116`

**The Norwegian value changes the timing, not the logic.** Under the pilot's six years ($F = 72$, Appendix D, p. 168) record 3's window is months 11 to 83, so its month-115 request falls outside and it does not collide. A request in any month 11 to 82 would (Corollary 1.1, B3.2).

Point to: §1.2, p. 3; §5.3, p. 83; slides 3 (record) and 4 (strip); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

## B1.2 Record 100: a research-environment log, month by month

**The event.** A researcher with a data permit works inside a Secure Processing Environment (SPE), which logs every access.

**What is created.** Record 100 in the generated run: created in month $t(a) = 7$ under $F = 12$ (Art 73(1)(e)); secondary pathway, reached by the ceiling ($\rho = 1$, which the generator sets for every SPE record to model the broad reading, §5.2, p. 80); actor `R-008` under permit `DP-015`; pseudonym `PSN-0000`; payload `<SPE-activity query=cohort-extract rid=100>`; commitment beginning `678ade47c1e6dc03`. The permit expires in month $t_\pi = 10$. No request ever arrives: $t_r = \infty$.

| Month | What happens | What each rule demands |
|---|---|---|
| 7 | Researcher's query logged | Floor: verifiable in every month 7 to $7 + 12 = 19$ |
| 8 to 9 | Nothing new | Floor only |
| 10 | Data permit expires | Ceiling clock starts: six months |
| 11 to 15 | Ceiling running | Floor only binds |
| 16 | Ceiling deadline $t_\pi + 6 = 16$ | Ceiling: electronic health data gone from the SPE from 16. Floor: identifiable log still verifiable |
| 16 to 19 | Both bind | Under "verifiable means readable": readable and gone in 4 months ($19 - 16 + 1 = 4$) |
| 20 | Floor window has closed | Nothing demands readability |

**Where the demands collide.** Months 16 to 19. The checker's witness (§5.4, p. 84):

`rid=100: t_a=7 permit expires t_pi=10 -> C3 from t=16, C1 to t=19 | collision at t=16`

**Why it is sharper than record 3.** Nobody asked for anything: two articles of one regulation collide in one environment. That is Corollary 1.2 (B3.3), on the broad reading of Art 68(12) only.

Point to: §5.4, p. 84; Figure 5.2, p. 85; slide 5 (research); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

## B1.3 Where each rule comes from

**The erasure right: Art 17 GDPR, with Art 12(3).** Article 17(1) GDPR gives the data subject the right to obtain erasure of personal data concerning her "without undue delay" where one of its grounds applies, and the controller has its own duty to erase on those grounds (§2.3, p. 18). Article 12(3) sets the response time: within one month of receipt, extendable by two further months for complex or numerous requests. The model writes this as $\delta = 1$, with $\delta = 3$ as the extended case (§4.4, p. 54). Of the Art 17(3) exemptions, (b) legal obligation, (c) public health and (d) research matter here. The model treats every request as valid, which inflates how often collisions occur in the run, not whether they can (§3.7, p. 45).

**The deletion ceiling: Art 68(12) EHDS.** Regulation (EU) 2025/327 provides that "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit" (§4.4, p. 55; quoted at §2.3, p. 19). It is a ceiling: a latest date by which something must be gone. It has no exemption parallel to Art 17(3)(b) (§2.3, p. 20). It applies from 26 March 2029 (§6.8, p. 98).

**The SPE floor: Art 73(1)(e) EHDS.** The same Regulation requires of an SPE "the keeping of identifiable logs of access to and activities in the secure processing environment for the period necessary to verify and audit all processing operations in that environment; logs of access shall be kept for at least one year" (§2.3, p. 19). This gives $F = 12$. The Joint Action's specification recommends five years (OPR-18), and by Corollary 2.2 no result depends on the value (§4.3, p. 53).

**The cross-border floor: eHDSI and ATNA.** The IHE ATNA profile prescribes no retention period; the floor comes from the deployment binding (§2.3, p. 17). A tutorial article reports ten years as the eHDSI baseline but gives no source (Simjanoska Misheva et al., 2025). The contact-point agreement requires audit trails and states no period (eHealth Network, 2017, clause II.4.2), nor does Implementing Regulation (EU) 2026/2083 (§2.3, p. 18). Helsedirektoratet replied on 19 October 2026 that the specifications leave the period to national law and the pilot uses six years, production undecided (Appendix D, p. 168). From 26 March 2029, Art 9(2) EHDS gives three years where the audit record is what a patient's access information is produced from (§4.3, p. 53). So the floor is a parameter: 120 illustrative, 72 pilot, 36 under Art 9(2), 12 for SPE logs.

**Which reading is contested.** Two things are contested, and the thesis says so.

1. *Whether Art 68(12) reaches the SPE's own access logs.* Broad reading: scope is set by location ("within the secure processing environment"), and a patient-level entry reveals cohort membership, which is health data. Narrow reading: the provision sits in the data-permit article and concerns the permit dataset. Harmonising reading: it reaches the logs but yields to Art 73(1)(e) (§4.6, pp. 58 to 59). Only Corollary 1.2 and the conditional branch of Corollary 2.3 depend on this (§6.2, p. 93).
2. *Whether an invalidated record still satisfies a retention obligation.* No regulator or court has said so (§6.2, p. 92). This is the authority question behind Semantics II.

Point to: §2.3, pp. 17 to 20; §4.4, pp. 54 to 55; §4.6, pp. 58 to 59; Appendix D, p. 168; slides 14 (limits) and 21 (q-reading); <https://trfhimolde.streamlit.app/?p=start>

## B1.4 Why Article 17(3)(b) does not make the problem vanish

The first objection any lawyer raises: Art 17(3)(b) exempts processing "necessary for compliance with a legal obligation". Audit retention is a legal obligation. So erasure never reaches the audit record, and there is no conflict.

The thesis answers in three steps (§2.3, pp. 19 to 20; §4.2, p. 49).

1. *The exemption is bounded by necessity.* It protects only what the obligation needs. Article 5(1)(c) GDPR (data minimisation) still applies to whatever is kept.
2. *What does the obligation need?* Its purpose is accountability: that an access happened, by whom, when, under what authority, with what result. The accessor fields answer that. The patient's name and birth date as typed into the query do not add to the answer. So keeping the payload readable for the whole floor exceeds what Art 17(3)(b) protects. This is "a reading argued here from the primary instruments, not one a supervisory authority has yet confirmed" (§4.2, p. 49).
3. *The ceiling has no such exemption.* Article 68(12) binds whatever balance is struck for the floor.

So the conflict survives in a narrowed form: not "may the record be kept?" but "how much of it may stay readable, for how long?" (§2.3, p. 20).

The patient link differs. Art 9(1) to (2) EHDS lets patients see who accessed their data "for at least three years from each date of access", which needs the link; so keeping it is necessary for a legal obligation, once Art 9 applies and where it binds this controller (§4.2, p. 50). Hence cross-border records keep the link through the floor; SPE logs lose it at the ceiling.

Point to: §2.3, pp. 19 to 20; §4.2, pp. 49 to 50; slide 6 (fixes); <https://trfhimolde.streamlit.app/?p=start>

# B2. The TRF model, symbol by symbol

## B2.1 The symbol table

The model is "one record, one clock, and one main question asked every month. Can the payload still be read?" (§4.3, p. 51). Time is counted in whole months $t \in \mathbb{N}$, with $t = 0$ the month the system starts.

| Symbol | Plain meaning | Unit | Where it comes from | Record 3 | Record 100 |
|---|---|---|---|---|---|
| $m_{\mathrm{acc}}(a)$ | Accessor fields: who acted, when, under which basis or permit, outcome | fields | Accountability purpose (§4.2) | HP-003, FI, PatientSummary, Art9(2)(h), success | R-008, DP-015, SPE-AccessLog, DataPermit, success |
| $m_{\mathrm{subj}}(a)$ | Subject fields: the link to the patient | fields | Design partition (§4.3) | PSN-0003 | PSN-0000 |
| $p(a)$ | Payload: what the record carries about what was accessed | bytes | ITI-55 query (cross-border); logged activity (SPE) | ITI-55 query string | SPE-activity string |
| $c(a)$ | Hiding, binding commitment to the payload, $\mathrm{Commit}(p(a), r(a))$ | hash value | Design (§4.3, §4.9) | `358f2a6a...` | `678ade47...` |
| $r(a)$ | Per-record salt for the commitment | 16 bytes in the code | Design | derived from rid in the reported run | same |
| $k(a)$ | Payload key | key | Envelope encryption (§4.8) | `KEY-000003` (toy) | `KEY-000100` (toy) |
| $t(a)$ | Month of the access event | month | The event | 11 | 7 |
| $F(a)$ | Retention floor | months | National law or pilot decision; Art 73(1)(e) | 120 (illustrative; pilot 72) | 12 |
| $\sigma(a)$ | Pathway: primary or secondary use | label | Where the record arose | primary | secondary |
| $t_r(a)$ | Month an erasure request arrives; $\infty$ if none | month | Art 17 GDPR | 115 | $\infty$ |
| $\delta$ | Erasure response period | months | Art 12(3) GDPR | 1 | 1 |
| $t_\pi(a)$ | Month the data permit expires; $\infty$ for primary records | month | Data permit | $\infty$ | 10 |
| $\rho(a)$ | 1 if the ceiling reaches the record (its entry is itself electronic health data in the SPE) | 0 or 1 | Reading of Art 68(12) | not defined (primary) | 1 (broad reading) |
| $P(a)$ | Payload retention period the controller may set; $\infty$ if none | months | Art 5(1)(c) and (e) GDPR | $\infty$ (artefact) | $\infty$ (artefact) |
| $t^{I}(a)$ | Invalidation month, $\min(t_r + \delta,\ t_\pi + 6,\ t + P)$ | month | Proof of Proposition 2 | 116 | 16 |
| $\alpha(a,t)$ | 1 if the controller can read the payload in month $t$ | 0 or 1 | The model's state variable | 1 up to 115, 0 from 116 (Sem. II run) | 1 up to 15, 0 from 16 |
| $\beta(a,t)$ | 1 if the subject fields can be read in the SPE in month $t$ | 0 or 1 | Broad reading only | unconstrained, stays 1 through floor | 1 up to 15, 0 from 16 |
| $V(a,t)$ | Whether the record counts as verifiable in month $t$ | 0 or 1 | Defined by the semantics | must be 1 for months 11 to 131 | must be 1 for months 7 to 19 |
| $\iota(a)$ | Invalidation entry: record, month, legal ground, authorising actor, hash of key identifier | log entry | Design (§4.8) | month 116, GDPR Art 17(1), DPO | month 16, EHDS Art 68(12), DPO |
| $e(a)$, $L$ | Anchor month of a ceiling, and its length (Proposition 3) | months | Any ceiling | not applicable | $e = 10$, $L = 6$ |
| $p_n(a)$, $p_r(a)$ | Part of the payload auditing needs; the rest (Corollary 2.3) | bytes | Extension of the model | $p_n$ empty in the run | $p_n$ empty in the run |

Notes on the table.

- The record is the tuple $a = (m(a), p(a), c(a), k(a), t(a), F(a), \sigma(a))$, with metadata $m(a) = m_{\mathrm{acc}}(a) \cup m_{\mathrm{subj}}(a)$ and no clinical content (§4.3, p. 51).
- Arithmetic is over $\mathbb{N} \cup \{\infty\}$ with $\infty + n = \infty$. A request concerns data already recorded, so $t_r(a) \ge t(a)$, and $\delta \ge 1$ (§4.3, p. 53).
- The floor is a parameter of the record, a form taken from chain-of-custody practice in logistics (§4.3, p. 52; §2.7, p. 31).
- In the checker the key is a reference that is removed; `crypto_envelope.py` uses real AES-256-GCM keys (§5.2, p. 80).

Point to: §4.3, pp. 51 to 53; Nomenclature, p. xii; slide 7 (model); <https://trfhimolde.streamlit.app/?p=start>

## B2.2 C1, the retention floor

**The rule in English.** For as long as the retention period runs, the record must count as verifiable.

**The formula.**
$$
V(a,t) = 1 \qquad \forall\, t \in \big[\, t(a),\; t(a) + F(a) \,\big]
$$

**Why the window is closed, so it spans $F + 1$ months.** The obligations are minimums: "at least one year". A record written during month $t(a)$ has completed $F$ full months only during month $t(a) + F$. So the conservative reading of "at least" demands verifiability through that month too. The window $[t(a), t(a)+F(a)]$ contains the integers $t(a), t(a)+1, \dots, t(a)+F(a)$: that is $F + 1$ of them. A half-open window $[t(a), t(a)+F(a))$ would end one month earlier and "would shorten every obligation by up to a month" (§4.4, p. 54).

*Worked example where it matters (record 97, from the checker, not named in the thesis).* Record 97 is cross-border: $t(a) = 7$, $F = 120$, so the closed window is months 7 to 127. Its request arrives in month 126, so with $\delta = 1$ the deadline is $126 + 1 = 127$: the last month of the window. On the closed window, month 127 needs both readable and gone: a collision. On a half-open window ending at 126 there would be none. With $\delta = 3$ the deadline moves to 129, which is outside 127, so the collision disappears. Record 97 is exactly the one record that leaves violation in Table 5.5 (90 to 89 generated records, 95 to 94 violations; §5.6, p. 87).

**C1 is a lower bound on $V$.** It says $V$ may not drop to 0 before the window ends. It sets a minimum duration for a property. It says nothing about $\alpha$ directly.

Point to: §4.4, p. 54; Table 5.5, p. 87; slide 7 (model); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

## B2.3 C2, the erasure right

**The rule in English.** After a valid erasure request, the payload must stop being readable within the response period, and stay unreadable.

**The formula.** For every record with $t_r(a) < \infty$:
$$
\alpha(a,t) = 0 \qquad \forall\, t \ge t_r(a) + \delta
$$

**Reading it.** The deadline month is $t_r + \delta$. From the start of that month onwards, $\alpha$ must be 0. If $t_r = \infty$, the condition "for every $t \ge \infty$" covers no month: C2 is vacuous.

**C2 is an upper bound on $\alpha$.** It caps how long the payload may remain readable. It says nothing about $V$.

*Record 3.* $t_r + \delta = 115 + 1 = 116$, so $\alpha(3,t) = 0$ for every $t \ge 116$.

Point to: §4.4, p. 54; slide 7 (model); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

## B2.4 C3, the deletion ceiling, with $\rho$ and $\beta$

**The rule in English.** In a research environment, health data must be gone six months after the permit ends. On the broad reading, this reaches log entries that are themselves health data.

**The switch $\rho$.** $\rho(a) = 1$ where the log entry is itself electronic health data within the environment. Broad reading: $\rho = 1$ for entries at patient-record granularity, and for dataset-granularity entries only where their activity content is health data. Narrow reading: $\rho = 0$ for every access log (§4.4, p. 55).

**The formula.** For every record with $\sigma(a) = \text{secondary}$ and $\rho(a) = 1$:
$$
\alpha(a,t) = 0 \qquad \forall\, t \ge t_\pi(a) + 6
$$
and, where the subject fields are electronic health data within the environment,
$$
\beta(a,t) = 0 \qquad \forall\, t \ge t_\pi(a) + 6 .
$$

**Why $\beta$ exists.** The single variable $\alpha$ covers the payload. On the broad reading the ceiling also reaches the patient link in an SPE log. So the model needs one more yes-or-no: can the subject fields still be read? Where the broad reading does not apply, $\beta$ is unconstrained and plays no part in any result (§4.3, p. 53).

**C3 is an upper bound on $\alpha$** (and on $\beta$).

*Record 100.* $t_\pi + 6 = 10 + 6 = 16$, so $\alpha(100,t) = 0$ and $\beta(100,t) = 0$ for every $t \ge 16$.

Point to: §4.4, p. 55; §4.3, p. 53; slides 7 (model) and 21 (q-reading); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

## B2.5 Lower bound on V, upper bound on alpha, and why "tri-lateral"

The thesis states the whole problem in one sentence: "C1 is a lower bound on the persistence of a property; C2 and C3 are upper bounds on the persistence of accessibility. Whether they conflict depends entirely on whether $V$ is defined in terms of $\alpha$" (§4.4, p. 55).

C1 says $V = 1$ *at least until* $t + F$; C2 and C3 say $\alpha = 0$ *no later than* their deadlines. If $V$ is $\alpha$, both act on one variable and contradict whenever a "gone by" deadline falls inside the "keep until" window. If $V$ is not $\alpha$, they act on different variables and need never meet.

**Why "tri-lateral".** The model has three constraint *types*: a floor (keep), a right (erase on request), a ceiling (delete after an external event). It is not a count of legal instruments. The floor is one parameterised constraint with two instances: the long cross-border floor and the one-year SPE floor. A national floor can be substituted without changing the model (§3.4, p. 40; Corollary 2.2, p. 61).

Point to: §4.4, p. 55; §3.4, p. 40; slide 7 (model); <https://trfhimolde.streamlit.app/?p=start>

## B2.6 Why a monthly grid, and what that convention costs

**Why months.** Every obligation in the system is stated in months or years, and the shortest deadline, the Art 12(3) response period, is one month (§4.3, p. 51). A coarser grid would lose that deadline. A finer one would add nothing the law states.

**What it costs.** Three things.

1. *Boundary months can be grid artefacts.* The law counts a month from the day of receipt; the model makes the deadline bind from the start of month $t_r + \delta$, so requests on the first and the last day of a month get the same model deadline. A record whose deadline lands within a month of the window's end (like record 97) could classify differently on a day grid. That moves boundary counts, not the propositions.
2. *The window convention is a choice.* The closed window is the conservative reading of "at least" (B2.2). It can only add a collision in the last month, never remove one.
3. *Expressiveness.* One binary variable cannot express field-level redaction or nested timing (§3.7, p. 45); Corollary 2.3 relaxes this once.

Point to: §4.3, p. 51; §4.4, p. 54; §3.7, pp. 44 to 45; slide 14 (limits); <https://trfhimolde.streamlit.app/?p=start>

## B2.7 The two semantics of "verifiable"

No instrument defines "verifiable", and neither semantics is stipulated by the instruments (§4.5, p. 56). The thesis states both precisely.

**Semantics I (plaintext verifiability).**
$$
V^{I}(a,t) = \alpha(a,t)
$$
A record is verifiable exactly when its payload can be read. A record whose payload cannot be produced counts as broken.

*Not a straw man.* The 2017 OpenNCP reference source stored every audit message whole and readable, refused modification and had no purge logic; the 2026 schema (9.1.0) keeps the columns, deployments not inspected. So Semantics I is "the de facto semantics of deployed audit repositories ... rather than ... a legal requirement" (§4.5, p. 56).

**Semantics II (accountability-preserving verifiability).**
$$
V^{II}(a,t) = 1 \iff \text{(i)} \wedge \text{(ii)} \wedge \text{(iii)}
$$
where, at month $t$:

- (i) $m_{\mathrm{acc}}(a)$ is intact and unmodified, and so is $m_{\mathrm{subj}}(a)$ unless its removal is recorded under (iii);
- (ii) $c(a)$ is present and binding;
- (iii) if $\alpha(a,t') = 1$ for some $t' < t$ and $\alpha(a,t) = 0$, or likewise for $\beta$, then an invalidation entry $\iota(a)$ recording the transition, its month, its legal ground and its authorising actor is present in the audit trail and is itself covered by (i).

**Why each condition is there.**

- Without (i), a record with altered "who and when" would still count. The accountability content is the point of the record.
- Without (ii), nothing ties the access event to one specific payload. An auditor could not tell, even before invalidation, whether one record's content had been swapped for another's. Dropping (ii) turns the design into Rival 4 (B6.3).
- Without (iii), a silent disappearance of the payload would count as verifiable. That is the "trivial semantics under which every record counts as verifiable always" which the thesis itself rejects (§4.7, p. 62).

**An accurate analogy: customs records.** Customs authorities may order presented goods to be destroyed (Union Customs Code, Article 197), while the declaration documents must be kept for at least three years (Article 51). The two do not collide, because destruction reaches the goods and record-keeping reaches the documents. The record of a destroyed consignment, including the fact of its destruction, is kept for the full period (§2.7, p. 31). Semantics II does the same for an audit record: accountability attaches to the record of the access and of its payload's invalidation, not to the payload's continued existence. Semantics I is the customs rule that would say "the declaration counts only while the goods are still in the warehouse". Where the analogy stops: in customs the goods and the documents are different objects by design; in an audit record they begin in the same record, so the mechanism has to separate them (§2.7, p. 31).

Point to: §4.5, pp. 55 to 56; §2.7, p. 31; slide 8 (word); <https://trfhimolde.streamlit.app/?p=start>

# B3. The propositions and corollaries, in depth

The thesis calls these propositions because "their proofs are short once the semantics are fixed" (§4.7, p. 62). Propositions 1 to 3 are proved informally; Proposition 4 is argued from a stated legal premise (§1.5, p. 9). The order below follows the thesis: Proposition 1 and its corollaries, Proposition 3, then Proposition 2 and its corollaries, then Proposition 4.

## B3.1 Proposition 1 (infeasibility under Semantics I)

**(a) Formal statement** (§4.6, p. 57).

> *Proposition 1.* Under Semantics I, the constraint system $\{C1, C2, C3\}$ is infeasible for any record $a$ such that
> $$ t_r(a) + \delta \le t(a) + F(a) \quad\text{ or }\quad t_\pi(a) + 6 \le t(a) + F(a). $$
> The second disjunct is tested only for records the ceiling reaches, that is, with $\sigma(a)$ = secondary and $\rho(a) = 1$.

**(b) Plain reading.** If readable is what verifiable means, then any record whose erasure deadline falls on or before the last month of its retention window, or (for a record the ceiling reaches) whose ceiling deadline does, has no possible schedule of readability that obeys all three rules.

"Infeasible" means: no assignment of 0s and 1s to $\alpha(a,t)$, month by month, satisfies all the constraints at once.

**(c) Proof, step by step.**

1. Take a record satisfying the first disjunct. Define $t^{*} = t_r(a) + \delta$.
2. By hypothesis, $t^{*} \le t(a) + F(a)$.
3. Requests arrive after the access that created the record, so $t_r(a) \ge t(a)$; with $\delta \ge 1$, $t^{*} \ge t(a) + 1 > t(a)$.
4. From steps 2 and 3, $t(a) \le t^{*} \le t(a) + F(a)$: month $t^{*}$ lies inside the closed window.
5. C1 therefore requires $V(a,t^{*}) = 1$.
6. Under Semantics I, $V^{I}(a,t^{*}) = \alpha(a,t^{*})$, so C1 requires $\alpha(a,t^{*}) = 1$.
7. C2 requires $\alpha(a,t) = 0$ for every $t \ge t_r(a) + \delta = t^{*}$; in particular $\alpha(a,t^{*}) = 0$.
8. $\alpha(a,t^{*})$ is a single number. It cannot be 1 and 0. No assignment satisfies C1 and C2 together, so none satisfies $\{C1, C2, C3\}$.
9. Second disjunct: repeat with $t^{*} = t_\pi(a) + 6$ and C3 in place of C2. This needs C3 to bind, which is why $\sigma = \text{secondary}$ and $\rho = 1$ are required. If the ceiling deadline fell before creation ($t_\pi + 6 < t(a)$), the contradiction arises at $t(a)$ itself, where C1 and C3 both bind. $\blacksquare$

**The converse** (§4.6, p. 57). If neither disjunct holds, set $\alpha = 1$ on every month of the window and $\alpha = 0$ afterwards. C1 holds. C2 and C3, where they bind at all, bind only after the window. So Proposition 1 is an exact characterisation: infeasible if and only if a binding deadline falls inside the window.

**(d) Why each hypothesis is needed.**

- *The deadline must fall inside the window ($\le$, not $<$).* Counterexample when dropped: record 38 (from the checker; the thesis describes it without naming it), cross-border, $t = 10$, window 10 to 130, has its request in month 138, deadline 139. Since $139 > 130$, the converse schedule works: readable to 130, unreadable from 131. Record 38 is the single cross-border request outside its window, "precisely the case the proposition excludes" (§5.3, p. 83). The $\le$ (rather than $<$) matters because the window is closed: record 97's deadline equals the window's last month and it does collide (B2.2).
- *$\sigma = \text{secondary}$ and $\rho = 1$ on the ceiling disjunct.* Counterexample: take record 100 but suppose the narrow reading, so $\rho = 0$. Then $t_\pi + 6 = 16 \le 19$ still holds arithmetically, but C3 does not bind. Set $\alpha = 1$ on months 7 to 19 and 0 afterwards: C1 holds and there is no C2 (no request). The record is feasible. A Proposition 1 without the scope sentence would therefore declare a feasible record infeasible. Likewise C3 is defined only for secondary records, so a primary record has no ceiling to collide with. The code shows the effect at population level: `sensitivity.py` with the ceiling excluded gives 46 violating records at $F = 120$, which is $37 + 9$, the cross-border collisions plus the nine SPE erasure-driven ones the thesis gives for the narrow reading (§5.4, p. 84). (The sensitivity outputs are code output, not thesis claims.)
- *Semantics I.* Under Semantics II, step 6 fails: $V$ no longer equals $\alpha$. That is the whole of Proposition 2.

**(e) Worked example by hand.** Record 3: $t^{*} = 115 + 1 = 116$; window end $11 + 120 = 131$; $116 \le 131$, so infeasible. In month 116, C1 says $\alpha = 1$ and C2 says $\alpha = 0$. Population check, in the model: of 100 generated cross-border records, 38 received a request, 37 had deadlines inside the window, all 37 violate (§5.3, p. 83). Record 132 (SPE, from the checker, not named in the thesis) satisfies both disjuncts: $t = 1$, window 1 to 13, request month 4 so deadline 5, permit month 7 so ceiling 13. It is one of the five records violating both C2 and C3, which is why 90 records carry 95 violations.

**(f) What it does NOT claim.**

- Nothing about how often requests arrive or how often permits end near a log entry (§4.6, p. 57; §3.7, p. 45).
- That the law requires Semantics I. It is the de facto semantics of one reference implementation (§4.5, p. 56).
- The request-driven case presupposes §4.2's conclusion that the payload is not necessary for the floor's purpose. Were it necessary, Art 17(3)(b) would exempt it and only the ceiling case would remain (§4.6, p. 57).

**(g) Likely attack and reply.**

*"This is trivial. A binary variable cannot be 0 and 1."* Reply: "Yes, and the thesis says so: it resolves to a month in which $\alpha$ must be both 1 and 0 (§4.7, p. 62). Its value is as a negative result. It shows that any design keeping the payload readable for the length of the floor is unworkable wherever a binding deadline falls inside the window. So some departure from readability is unavoidable. Proposition 2 then shows a minimal departure suffices."

Point to: §4.6, p. 57; §5.3, p. 83; slides 9 (result) and 24 (q-proofs); <https://trfhimolde.streamlit.app/?p=propositions>

## B3.2 Corollary 1.1 (cross-border case)

**(a) Statement** (§4.6, p. 57).

> *Corollary 1.1 (cross-border case).* For cross-border audit records, $F(a)$ is the period left to national law: 72 months in the Norwegian pilot, as set by Helsedirektoratet as controller, 120 as reported in the literature and used illustratively in Chapter 5. The system is infeasible for record $a$ whenever an erasure request arrives at any month $t_r(a) \le t(a) + F(a) - \delta$: that is, at any point but the last $\delta$ months of the window, whatever its length, so, under the baseline response period, a request in any of the 72 months from $t(a)$ to $t(a) + 71$ collides with the pilot's six-year floor.

**(b) Plain reading.** Under the pilot floor, a request in any but the window's last month collides.

**(c) Derivation.**

1. Proposition 1's first disjunct: $t_r + \delta \le t + F$.
2. Subtract $\delta$: $t_r \le t + F - \delta$.
3. Requests satisfy $t_r \ge t$. So colliding request months are $t, t+1, \dots, t + F - \delta$: that is $F - \delta + 1$ months.
4. With $F = 72$, $\delta = 1$: $72 - 1 + 1 = 72$ months, from $t$ to $t + 71$.
5. The window has $F + 1 = 73$ months, $t$ to $t + 72$. A request in month $t + 72$ has deadline $t + 73$, outside. $\blacksquare$

**(e) Worked example.** Record 3 under $F = 72$: colliding request months 11 to 82. Its actual request (115) is outside, so no collision. Under $F = 120$: colliding months 11 to 130; 115 is inside.

**(f) Not claimed.** How often patients exercise Art 17 (§4.6, p. 57).

**(g) Attack.** *"Your ten years is unsourced."* Reply: "Agreed, it is illustrative. The operator wrote that no specification fixes a period and the pilot uses six years (Appendix D). The corollary holds at any value."

Point to: §4.6, p. 57; Appendix D, p. 168; slide 4 (strip); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

## B3.3 Corollary 1.2 (SPE case, no erasure request)

**(a) Statement** (§4.6, p. 57), first four sentences:

> *Corollary 1.2 (Secure Processing Environment case).* For Secure Processing Environment access logs, $F(a) = 12$ and $\sigma(a)$ = secondary. Suppose the permit expires at or before the sixth month of the record's retention window, so that $t_\pi(a) + 6 \le t(a) + 12$. Then C1 and C3 are contradictory at $t^{*} = t_\pi(a) + 6$ by the argument above, provided C3 reaches the record. *Where it does, no erasure request is required.*

The corollary also assumes, as a stated premise, that the activity content, not only the subject fields, is data concerning health.

**(b) Plain reading.** If a researcher's log entry is written in the last six months of a permit, the one-year keep rule outlasts the six-month delete rule. Under readable-verifiability that is a contradiction, and no patient had to do anything.

**(c) Proof.**

1. Rearrange the hypothesis: $t_\pi + 6 \le t + 12 \iff t_\pi - t \le 6$. The remaining permit duration when the entry is written is at most six months.
2. Let $t^{*} = t_\pi + 6$. With $t_\pi \ge t$ (permit live when the entry is written), $t^{*} > t$, so $t^{*}$ is inside $[t, t+12]$.
3. C1 under Semantics I: $\alpha(a,t^{*}) = 1$.
4. C3 (with $\rho = 1$): $\alpha(a,t^{*}) = 0$.
5. Contradiction, with $t_r = \infty$ throughout. $\blacksquare$

**(d) Why each hypothesis is needed.**

- *$\rho = 1$.* On the narrow reading C3 does not bind and the record is feasible (B3.1(d)).
- *Activity content is health data.* If only the subject fields were health data, Semantics I could keep the payload readable and delete only the subject fields at the ceiling. The collision would not arise (§4.6, p. 57).
- *Remaining duration $\le 6$.* Counterexample: record 102 (from the checker, not named in the thesis): $t = 5$, $t_\pi = 12$, ceiling $18$, floor end $17$. Since $18 > 17$, the floor ends one month before the ceiling binds; feasible.

**(e) Worked example and the count.** Record 100: $t_\pi - t = 10 - 7 = 3 \le 6$; collision months 16 to 19. In the generated run, 78 SPE records had no request, and 39 of them collide (§5.4, p. 84).

*Why exactly half.* The generator draws the permit length $t_\pi - t$ uniformly from $\{1, \dots, 12\}$. Collision needs a length of at most 6: 6 values out of 12, so one half (§5.4, p. 85). That 39 of 78 is exactly one half is how this seed fell. With a five-year permit and the remaining duration drawn uniformly over 60 months, the share is $6/60 = 1/10$. In general it falls as $6/\pi_{\max}$, but never to zero: "every permit used in its final six months produces colliding entries, whatever the distribution of permit lengths" (§5.4, p. 85).

*The decomposition (generated records).* Of 53 violating SPE records, 49 are ceiling-driven (44 C3 only, 5 both) and 4 request-only. The 44 are the 39 witnesses plus 5 with requests after their windows; on the narrow reading they lapse, leaving 9 (§5.3, p. 83; §5.4, p. 84).

**(f) Not claimed.** Frequency; that the broad reading is correct; reach over dataset-level logs without health content. It is "a conditional extension" (§4.6, p. 58).

**(g) Attack.** *"Article 68(12) is about the permit dataset, not the logs."* Reply: "That is the narrow reading, and it is respectable; I state Corollary 1.2 conditionally. If it wins, I lose Corollary 1.2 and the conditional branch of Corollary 2.3, and nothing else: an SPE log then collides only through an erasure request (§4.6, p. 59; §6.2, p. 93)." Do not say the three-way collision survives the narrow reading.

Point to: §4.6, pp. 57 to 59; §5.4, pp. 84 to 85; Figure 5.2, p. 85; slides 5 (research), 21 (q-reading) and 23 (q-permits); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

## B3.4 Proposition 3 (anchoring) and the anchor condition

**(a) Statement** (§4.6, p. 60).

> *Proposition 3 (anchoring).* Let a record's floor of $F$ months run from its creation month $t(a)$, and let a ceiling of $L$ months run from an event at month $e(a) \ge t(a)$. Under Semantics I, the floor and the ceiling are jointly satisfiable for $a$ if and only if $e(a) + L > t(a) + F$. Hence (i) if the ceiling is anchored to the same event as the floor, $e(a) = t(a)$, they are satisfiable for every record if and only if $L > F$, a condition decidable from the text alone; and (ii) if the ceiling is anchored to an external event, then whenever $L \le F$ they fail for exactly those records with $e(a) - t(a) \le F - L$, a set that the text does not reveal and each record's history determines.

The brief's "$e - s \le F - L$" is this condition with $s = t(a)$, the creation month.

**(b) Plain reading.** A ceiling clashes with a floor only if it ends on or before the floor ends. With one shared start, the statute shows the clash on its face. With a different start, the statute can look harmless, and only each record's dates reveal it.

**(c) Proof, step by step.**

1. C1 under Semantics I demands $\alpha = 1$ on the set $A_1 = \{t(a), \dots, t(a)+F\}$.
2. The ceiling demands $\alpha = 0$ on the set $A_0 = \{e(a)+L, e(a)+L+1, \dots\}$.
3. A contradiction exists if and only if $A_1 \cap A_0 \neq \emptyset$.
4. Since $e(a) \ge t(a)$ and $L \ge 1$, the first month of $A_0$ satisfies $e(a) + L > t(a)$, so $A_0$ starts after $A_1$ starts.
5. Two sets of consecutive months, the second starting after the first starts, overlap if and only if the second starts no later than the first ends: $e(a) + L \le t(a) + F$.
6. So they are jointly satisfiable if and only if $e(a) + L > t(a) + F$; then the schedule "readable before $e + L$, unreadable from $e + L$" meets both.
7. Case (i): put $e = t$. The condition becomes $t + L > t + F$, that is $L > F$. It does not mention any record's history, so it can be read off the text.
8. Case (ii): rearrange the failure condition $e + L \le t + F$ into $e - t \le F - L$. The left side is each record's own delay between log entry and anchor event. $\blacksquare$

**Why (ii) needs $L \le F$.** If $L > F$ then $F - L < 0$. Since $e \ge t$, the left side $e - t \ge 0$. A non-negative number cannot be at most a negative one, so no record ever fails. A collision of any kind therefore needs a ceiling no longer than the floor, whichever way it is anchored. "What the anchor decides is whether the collision can be seen" (§4.6, p. 60).

**(d) Why the hypotheses are needed.**

- *$e(a) \ge t(a)$.* It restricts the statement to the cases treated. If the anchor event preceded creation, the condition $e + L > t + F$ still holds, and a ceiling already passed at creation makes the record infeasible from $t(a)$ (§4.6, p. 60). The Z3 check uses the same restriction.
- *Semantics I.* Under Semantics II the floor does not read $\alpha$, so there is nothing to collide.

**(e) Worked examples by hand.**

- *Record 100.* $F = 12$, $L = 6$, $e = t_\pi = 10$, $t = 7$. $F - L = 6$; $e - t = 3 \le 6$: collides. Equivalently $e + L = 16 \le 19$. Overlap length $19 - 16 + 1 = 4$ months.
- *Record 102.* $e - t = 12 - 5 = 7 > 6$: clear, by one month ($18 > 17$).
- *Politiregisterloven §17* (§6.10, p. 100). In the thesis's Norwegian, "lagres i minst 1 år og slettes senest etter 3 år" (candidate's translation: stored for at least one year and deleted at the latest after three years): $F = 12$, $L = 36$, both from the log entry (a reading of the sentence's syntax, which the provision does not state in words). Case (i): $L = 36 > 12 = F$, so no collision without a request. The generated run: 60 records, 7 violate, none without an erasure request (§6.10, p. 100). The cross-sector module's printed witness, rid 906, is erasure-driven: log at month 0, erasure deadline 11, inside the floor. [CHECK: §17 text not verified against Lovdata; flagged open in the existing notes.]

**(f) Not claimed.** Frequency. That §17 expressly anchors both limbs at the entry: it is a reading (§6.10, p. 101). That other sectors have external-anchor ceilings: MiFID II and Elhub are candidates not yet tested (§6.10, p. 101; §2.7, p. 30).

**(g) Attack.** *"This is just interval overlap."* Reply: "Yes. Its value is diagnostic: it corrected my own expectation that any floor plus ceiling collides (§17 does not), and it gives the implementing acts a drafting test: look for a ceiling no longer than a floor, anchored to a different event (§6.8, p. 98)."

Point to: §4.6, p. 60; §6.10, pp. 100 to 101; slides 20 (q-logistics) and 30 (q-props34); <https://trfhimolde.streamlit.app/?p=anchor>

## B3.5 Proposition 2 (feasibility under Semantics II)

**(a) Statement** (§4.7, p. 60).

> *Proposition 2.* Under Semantics II, the constraint system $\{C1, C2, C3\}$ is jointly satisfiable for every record $a \in A$, for every arrival pattern of erasure requests $\{t_r(a)\}$ and permit expiries $\{t_\pi(a)\}$, and for every floor parameter $F(a) \in \mathbb{N}$.

**(b) Plain reading.** If verifiable means accountable, every record has a schedule obeying all three rules, whatever the dates and the floor.

**(c) Proof (constructive), step by step.** Define the invalidation month
$$
t^{I}(a) = \min\big(\, t_r(a) + \delta,\;\; t_\pi(a) + 6,\;\; t(a) + P(a) \,\big),
$$
with the minimum of infinite terms equal to $\infty$. Build this trajectory:

1. For $t < t^{I}(a)$: $\alpha(a,t) = 1$. Keep $m(a)$, $c(a)$, $k(a)$, $p(a)$.
2. At $t = t^{I}(a)$, if finite: destroy $k(a)$; where the ground is Art 68(12) and C3 reaches the subject fields, remove $m_{\mathrm{subj}}(a)$ and set $\beta = 0$; append $\iota(a)$ with month, ground (Art 17(1), Art 68(12), or Art 5(1)(c) and (e) where $P$ fixed the month), what was removed, and the authorising actor; keep $m_{\mathrm{acc}}(a)$ and $c(a)$ unchanged.
3. For $t > t^{I}(a)$: $\alpha = 0$, and $\beta = 0$ where step 2 removed the subject fields. Keep $m_{\mathrm{acc}}(a)$, $c(a)$, $\iota(a)$.
4. If C3 reaches the subject fields and $t^{I}(a) < t_\pi(a) + 6$ (a request or $P$ came first), remove $m_{\mathrm{subj}}(a)$ at $t_\pi(a) + 6$, set $\beta = 0$ from then, and append a second entry recording it.

Edge case: if $t^{I}(a) \le t(a)$, the payload is never held readable; set $\alpha = 0$ from $t(a)$ and append $\iota(a)$ at $t(a)$. C1 still holds, because Semantics II does not read $\alpha$.

Now check each constraint.

- *C2.* If $t_r < \infty$, then $t^{I} \le t_r + \delta$ because a minimum is no larger than any of its terms. From $t^{I}$ onwards $\alpha = 0$, so $\alpha = 0$ for all $t \ge t_r + \delta$. If $t_r = \infty$, C2 is vacuous.
- *C3.* If $\sigma = \text{secondary}$ and $t_\pi < \infty$, then $t^{I} \le t_\pi + 6$, so $\alpha = 0$ from $t_\pi + 6$. $\beta = 0$ from $t_\pi + 6$, by step 2 if the ceiling fixed $t^{I}$, by step 4 if something earlier did. Otherwise vacuous.
- *C1.* Take any $t$ in $[t(a), t(a) + F(a)]$. (i) holds: no step modifies $m_{\mathrm{acc}}$, and the only removal of $m_{\mathrm{subj}}$ is recorded. (ii) holds: no step removes $c(a)$, and $c(a)$ is not derived from $k(a)$, so destroying the key does not affect it. (iii): if $\alpha(a,t) = 1$, vacuous; if $\alpha(a,t) = 0$, then $t \ge t^{I}$, and step 2 put $\iota(a)$ in the trail, step 3 keeps it, and it is covered by (i). Same for $\beta$ through steps 2 and 4. So $V^{II}(a,t) = 1$ throughout the window. $\blacksquare$

Nothing in the argument depends on the value of $F(a)$ or on the arrival times. That is where "for every" comes from.

**(d) Why each element is needed.**

- *The minimum over all triggers.* If invalidation waited for a later deadline, the earlier constraint would fail in between. Record 132 (from the checker, not named in the thesis): erasure deadline 5, ceiling 13. Invalidating at 13 would leave the payload readable in months 5 to 12, violating C2.
- *Step 4.* Without it, record 132's subject link would survive after month 13, because the month-5 invalidation was on the Art 17(1) ground and did not remove it. C3 over $\beta$ would fail. The checker logs a separate entry: month 13, removed `patient_pseudonym`, ground EHDS Art 68(12).
- *Keeping $c(a)$ and logging $\iota(a)$.* Without them, Z3 finds counterexamples (B3.9).
- *Semantics II itself.* Under Semantics I, the record 3 schedule above fails C1 in months 116 to 131.

**(e) Worked examples by hand.**

- *Record 3.* $t^{I} = \min(115 + 1, \infty, \infty) = 116$. Ground GDPR Art 17(1). Patient link kept (cross-border). Readable months 11 to 115; from 116 key, salt and ciphertext gone; $\iota$ logged at 116.
- *Record 100.* $t^{I} = \min(\infty, 10 + 6, \infty) = 16$. Ground EHDS Art 68(12). Subject link removed at 16 with its own logged entry. Months 16 to 19 now satisfy C1, because (i), (ii), (iii) all hold.
- *Record 133 (tie, from the checker).* $t = 11$, request 25, permit 20: $\min(26, 26) = 26$. The code records a tie under Art 17(1) "since it is the act that triggered erasure". Four such ties exist in the generated run (§5.7, p. 88). On a tie, step 2 as worded removes subject fields only on the Art 68(12) ground and step 4 needs a strict $<$, so read the two together: the code removes the link at month 26 anyway, under its own Art 68(12) entry, and C3 over $\beta$ holds.
- *Population (generated).* 138 invalidated: all 38 cross-border records with requests plus all 100 SPE records. 52 on Art 17(1), 86 on Art 68(12). Zero violations (Table 5.6, p. 87).

**(f) Not claimed** (§4.7, p. 63). That the solution is lawful (that needs the residue analysis). That key destruction can be verified externally: $\iota(a)$ is an attested record, not a proof. That the semantics is endorsed by any authority.

**(g) Attack.** *"You defined Semantics II so that this works."* Reply: "The objection has force, and the thesis concedes its premise and denies its conclusion (§4.7, p. 62). The mathematics is modest. Any number of semantics admit a solution, including a trivial one where everything is verifiable always. The claim is that this semantics is a defensible reading, grounded in the necessity limit of Art 17(3)(b), the minimisation principle of Art 5(1)(c), and the accountability purpose. It keeps every element accountability needs and discards only what it does not. Proposition 1 carries the other half: some departure is unavoidable."

Point to: §4.7, pp. 60 to 63; Table 5.6, p. 87; slides 9 (result) and 11 (audit); <https://trfhimolde.streamlit.app/?p=propositions>

## B3.6 Corollaries 2.1 and 2.2

**(a) Statements** (§4.7, p. 61).

- *Corollary 2.1.* "The construction requires no coordination between the erasure process and the retention process, and no knowledge at the time a record is created of whether an erasure request will ever arrive. The invalidation month is determined entirely by events as they occur."
- *Corollary 2.2.* "Because $F(a)$ is arbitrary in the proof, the result holds simultaneously for an illustrative ten-year cross-border floor, the six-year floor of the Norwegian pilot and the one-year Secure Processing Environment floor, and for any national floor substituted for either. The model is tri-lateral in constraint type and indifferent to the number of floor instances."

**(b) Plain reading.** 2.1: the system does not need to predict the future; it reacts when a request or expiry happens. 2.2: whatever floor the law or the controller picks, the same mechanism works.

**(c) Proof.** 2.1: $t^{I}$ is a minimum of event times. Each term becomes known when its event occurs (or when the controller sets $P$), and until then the record is simply readable. 2.2: $F(a)$ appears in the C1 check only as the end of the window, and the C1 argument holds for any $t$ in any window. $\blacksquare$

**(e) Example.** Record 3 was written in month 11 with no knowledge of month 115. `sensitivity.py` shows zero Semantics II violations at floors 120, 72 and 36 (code output, not in the thesis). Section 4.2 adds that "a lower or absent floor removes collisions and creates none" (p. 51).

**(f) Not claimed.** That the floor value never matters: it drives the Semantics I counts.

**(g) Attack.** *"Then why argue about six versus ten years?"* Reply: "It changes which requests collide under readable-verifiability, not whether the mechanism works. That the six-year period has no identified national legal basis is a finding for the controller, not a limit on the model (§4.2, p. 51)."

Point to: §4.7, p. 61; §4.2, p. 51; slide 9 (result); <https://trfhimolde.streamlit.app/?p=propositions>

## B3.7 Corollary 2.3 (sensitivity to what auditing needs)

**(a) Statement** (§4.7, p. 62).

> *Corollary 2.3 (sensitivity to what auditing needs).* Extend the model with one accessibility variable per part of the payload, which the single-variable model of Section 4.3 cannot express, and partition the payload as $p(a) = p_n(a) \cup p_r(a)$, where $p_n(a)$ is any part that auditing turns out to need, and retain $p_n(a)$ with the accessor fields. The trajectory of Proposition 2, with $p_r(a)$ in place of $p(a)$, satisfies C1 and C2, and it satisfies C3 unless $p_n(a)$ is itself electronic health data within the environment on the broad reading of Article 68(12). In that case C1 and C3 collide over $p_n(a)$, by the argument of Proposition 3, for exactly the records it identifies under case (ii).

Exits named: relocation (Rival 6), dataset-granularity logging, the narrow reading, or anonymising $p_n(a)$.

**(b) Plain reading.** If an auditor needs part of what was logged, keep that part. That works everywhere except where the kept part is health data inside a research environment, where the old collision returns for that part.

**(c) Proof sketch, step by step.**

1. Replace $p$ by $p_r$ in steps 1 to 4 of Proposition 2; add $p_n$ to what condition (i) keeps intact.
2. C1 holds as before.
3. C2 holds for $p_r$ as before; for $p_n$ through Art 17(3)(b), which applies because $p_n$ is by assumption necessary.
4. C3: if $p_n$ is not electronic health data, it is not reached; met. If it is, C3 needs it gone from $t_\pi + 6$, while C1 needs it intact to $t + F$. By Proposition 3 these overlap for exactly the records with $t_\pi - t \le F - 6$. $\blacksquare$

**(d) Why the extension is needed.** The base model has one $\alpha$ per record, so it cannot keep part of a payload. Why the collision arises: $p_n$ is kept under condition (i) "without the logged-removal exception that the subject fields have" (§4.7, p. 62).

**(e) Example (hypothetical, not a run result).** If part of record 100's activity content were needed and counted as health data, it would collide over months 16 to 19, as in B1.2.

**(f) Not claimed.** That auditing does need part of the payload. For cross-border records the thesis argues it does not; for SPE logs the argument is weaker, which is why this corollary exists (§4.2, p. 50).

**(g) Attack.** *"So your solution fails exactly where it matters?"* Reply: "Only for a needed part that is also health data inside an SPE on the broad reading, exactly as Corollary 1.2 fails, with the same exits (§4.7, p. 62)."

Point to: §4.7, p. 62; slide 21 (q-reading); <https://trfhimolde.streamlit.app/?p=propositions>

## B3.8 Proposition 4 (location and right), argued from a stated premise

**(a) Statement** (§4.10, p. 72).

> *Proposition 4 (location and right).* *This result depends on a legal premise stated here as an explicit assumption, not derived from the model: that a controller receiving a relocated record receives the erasure obligation of Article 17(1) GDPR with it.* Let a ceiling be anchored to a location, requiring data to be absent from that location after a deadline, and let a right be anchored to the data subject, requiring data to be inaccessible to any controller holding them after a deadline. Under Semantics I, and granting that assumption, relocating a record before the ceiling's deadline satisfies the ceiling and the floor together, while the floor and the right remain infeasible for every record satisfying the first disjunct of Proposition 1.

**(b) Plain reading.** Exporting the logs out of the SPE when the permit closes gets past the delete-from-here rule. It does not get past the right to erasure, because that right follows the data to whoever holds them.

**(c) Argument, step by step.**

1. The ceiling quantifies over a place; after relocation the record is not there, so the ceiling holds.
2. On the rival's premise (Art 73(1)(e) fixes how long, not where), the floor is met at the new location.
3. The right quantifies over a controller: Art 17(1) binds whoever holds the data. Premise: the receiver inherits it.
4. So C1 and C2 bind the new holder as before, and Proposition 1's first-disjunct argument applies unchanged. $\blacksquare$

**(d) Why the premise is needed, and its status.** Step 5 is a legal claim, not mathematics. If it were false, relocation would also escape the right, and Rival 6 would become stronger; Propositions 1 to 3 would stand (§4.10, p. 72). The proposition is stated over the model extended informally with location and controller, which §4.3 does not represent; the artefact does not execute it (§4.10, p. 72). Hence "argued from a stated premise", not "proved".

**(e) Worked example (record 132, from the checker, not named in the thesis).** $t = 1$, window 1 to 13, request month 4 (deadline 5), permit month 7 (ceiling 13). Export before month 13 satisfies the ceiling. The month-5 erasure deadline still sits inside the window at the new controller, so readable-verifiability still fails in months 5 to 13.

**(f) Not claimed.** That relocation is unlawful: it is accepted as a sufficient answer to Corollary 1.2. Nor that it is free: the subject fields move to a second controller, so data are moved, not reduced (§4.10, p. 72).

**(g) Attack.** *"This is an assumption with a proof attached."* Reply: "Largely yes: it is a legal argument given the form of a proposition so its premise is explicit (§4.10, p. 72). It shows which part of the conflict no relocation escapes: the request-driven part."

Point to: §4.10, p. 72; §6.1, p. 91; slides 6 (fixes) and 30 (q-props34); <https://trfhimolde.streamlit.app/?p=anchor>

## B3.9 What exhaustive search and Z3 check, and what they do not

**Exhaustive search** (§5.5, p. 85). A separate function, `brute_force_semantics_I`, enumerates every assignment of $\alpha$ over a 14-month horizon: $2^{14} = 16{,}384$ assignments per case. It asks whether any assignment satisfies C1 (under Semantics I), C2 and C3.

| Case | Feasible? |
|---|---|
| SPE, no request, permit 3 months | False |
| SPE, request at $t = 2$ | False |
| Cross-border, floor scaled to 12, request at $t = 4$ | False |
| Control: no request, no expiry | True |

"No trajectory succeeds" is stronger than "the checker's trajectory fails", and the control shows the search can say True. But every constraint is pointwise in time, so enumeration equals checking each month in turn: "a sanity check rather than independent evidential weight" (§5.5, p. 85). Its value is separate code sharing only $\delta$ and the ceiling, with a test comparing the two on every boundary month. The floor is scaled to 12 because $2^{120}$ assignments cannot be enumerated. In all $4 \times 16{,}384 = 65{,}536$ assignments; 65,535 are evaluated, as the control stops at its first success (§5.8, p. 90).

**Z3 bounded check** (§5.5, p. 86). `z3_check.py` poses each claim as a request for a counterexample within bounds: creation 0 to 12, floor 1 to 120, $\delta$ 1 to 3, request and anchor up to a horizon of 140, ceiling 1 to 120. "Unsat" means no counterexample exists within the bounds. Run output: 9 of 9 checks unsat (Proposition 1 both directions; Proposition 2; Proposition 3 general and both cases in both directions); the sanity check is sat; four broken variants are refuted (Proposition 2 without $\iota$, without $c$, without the subject-link entry; Proposition 3 shifted by one month).

**What the Proposition 2 check really checks.** The code comment says the accountability conjuncts are set true by construction, "so this check verifies the timing of the trajectory, not that accountability is preserved". Its evidential weight lies in the refuted mutations: remove an element and the check fails (§5.5, p. 86).

**The honest limit.** All three were written in the same AI-assisted process from the §4.4 constraints. They check the code against the encoding, and the propositions against the constraints as encoded, not the constraints against the law (§5.5, p. 86; §6.7, p. 97). In one line: "The checks test my code against my model, not my model against the law."

Point to: §5.5, pp. 85 to 86; Appendix A.23 to A.24, pp. 150 to 153; slides 12 (evidence) and 24 (q-proofs); <https://trfhimolde.streamlit.app/?p=robust>

# B4. The mechanism: Crypto-Erasure by Invalidation

"The proof of Proposition 2 is also a build sheet" (§4.8, p. 63). Each step below exists because the proof, or the residue analysis, needs it.

## B4.1 Envelope encryption with a data key per record

**What it is.** Each record's payload is encrypted under its own data key $k(a)$. The data keys are themselves encrypted ("wrapped") under a key-encrypting key held in a hardware security module (HSM) or an equivalent custody boundary. Destroying $k(a)$ means destroying the wrapped key and any cached copies inside that boundary (§4.8, p. 63; Barker, 2020).

**Why per record.** A permit expiry invalidates one permit's records; an erasure request, one person's. The sets intersect without nesting, so no per-person or per-permit key serves both (§4.8, p. 63). A key-share design (a share per subject and per permit) would avoid per-record keys; named, not built (Cachin et al., 2013).

**Why keys at all, when the store deletes the ciphertext.** "Nothing in the TRF Model distinguishes key destruction from deletion of the payload: both set $\alpha$ to zero" (§4.8, p. 65). Keys earn their place for copies the store cannot delete at once, such as backups, which the specification reaches: data "MUST be deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies" (TEHDAS2, 2026b, OPR-6, p. 43). For those copies key destruction secures unintelligibility, not erasure (EDPB Guidelines 02/2025).

**In the artefact.** The checker removes a key reference. The optional `crypto_envelope.py` uses real per-record AES-256-GCM keys, wrapped under a key-encrypting key. Run output on the 200 generated records: all decrypt before invalidation; 138 keys destroyed; 138 refuse; 62 still read; record 3's ciphertext tried under the 62 surviving keys opens 0 times (§5.8, p. 89). The custody object stands in for an HSM, so destruction is in program memory.

Point to: §4.8, pp. 63 to 65; §5.8, p. 89; slides 10 (mechanism) and 25 (q-keys); <https://trfhimolde.streamlit.app/?p=built>

## B4.2 The hiding and binding commitment, and the salt

**Definitions.** A commitment $c = \mathrm{Commit}(p, r)$ is a short value fixed at write time:

- *Hiding:* someone who holds $c$ but not the salt $r$ learns nothing about $p$.
- *Binding:* nobody can find a second payload $p' \neq p$ and salt $r'$ with $\mathrm{Commit}(p', r') = c$.

The code uses $c = \mathrm{SHA\text{-}256}(r \Vert p)$ with a 16-byte salt (§5.2, p. 80): binding rests on collision resistance, hiding on a random, secret salt.

**Why a bare hash of a name leaks.** Suppose $c = H(p)$, unsalted, with $p$ a name and birth date. An adversary need not invert $H$: she hashes candidate payloads (names from a register; a century has about 36,525 birth dates) until one matches $c$. The same works for a diagnosis code or a formulary medicine: the space is small (§4.9, p. 68). An unsalted hash would therefore be surviving personal data, and the mechanism "would have relocated the erasure problem rather than solved it" (p. 68). With a random 128-bit salt, each guess must also guess the salt: $2^{128}$ possibilities.

**Why the salt is destroyed with the key.** Before invalidation the salt lets an auditor open the commitment, which detects substitution. After invalidation a retained salt would let anyone with a candidate payload confirm a guess, so it goes at $t^{I}$. Binding is unaffected: it is a property of $c$ (§4.8, p. 65). A party that must later prove its own copy (the patient, the home contact point) has to be handed the opening at write time.

**The honest caveat.** In the reported run the salt is derived from the record identifier, `bytes[(rid*7 + i) % 256]`, so every run reproduces exactly; that commitment is therefore not hiding in that run. The flag `--random-salts` draws salts from `os.urandom`, as a deployment must (§5.2, p. 80). The salt of the subject-field commitment is derived the same way.

Point to: §4.8, p. 65; §4.9, p. 68; §5.2, p. 80; slides 10 (mechanism) and 27 (q-residue); <https://trfhimolde.streamlit.app/?p=built>

## B4.3 The Merkle log, inclusion proofs, and what a root proves

**What it is.** Every access event, invalidation and subject-link removal is appended to a Merkle log with RFC 6962 hashing (§4.8, p. 66):
$$
\text{leaf} = H(\texttt{0x00} \Vert \text{data}), \qquad \text{node} = H(\texttt{0x01} \Vert \text{left} \Vert \text{right}).
$$
The two prefixes keep a leaf from ever being confused with an internal node. The root is the single hash at the top.

**What enters a leaf.** Accessor fields, creation month, payload commitment, salted subject commitment; never the payload or subject fields, so the log never needs rewriting (p. 66).

**Inclusion proof.** To show one entry is in the log, give the sibling hash at each level from the leaf to the root. The verifier rehashes upwards and compares with the root. The proof length is about $\log_2 n$. In the generated run the log has 438 entries: 200 access events + 138 invalidations + 100 subject-link removals. Each inclusion proof has 9 sibling hashes (from the code). For a billion entries it is about thirty (§6.5, p. 96).

**What a root proves.** Given a root the auditor trusts, a valid proof shows that an entry with exactly these bytes sits in the log. Alter one byte and the proof fails. The run's three tamper tests: altering record 100's actor, record 100's invalidation ground, or record 3's patient link each makes $V^{II}$ false; restoring them makes it true (§5.7, p. 88).

**What it does not prove.** The artefact recomputes the root from its own leaves. That detects divergence between a record and its logged events, not a rewrite of the whole log by the operator. Catching a rewrite needs earlier roots published or countersigned outside the operator, and consistency proofs between roots (Laurie et al., 2013): specified, not implemented (§4.9, p. 69; §5.7, p. 88). Hence "tamper-evident", not stronger.

Point to: §4.8, p. 66; §4.9, p. 69; §5.7, p. 88; §6.5, p. 96; slides 11 (audit) and 29 (q-roots); <https://trfhimolde.streamlit.app/?p=run>

## B4.4 The invalidation entry

**What it is.** $\iota(a)$ holds the record identifier, the invalidation month, the legal ground, the authorising actor, and a hash of the destroyed key's identifier, not of the key (§4.8, p. 65). It is appended, never edited: "Invalidation is an event that is logged, not an event that erases the log." Key-management guidance anticipates such a record: after destruction a key's "previous existence may be recorded (e.g., in metadata or audit logs)" (Barker, 2020, §7.6; thesis p. 66).

**Why it is there.** It is condition (iii) of Semantics II. Even alone it is worth adopting: it "costs little and converts an unexplained absence into an accountable one" (§6.8, p. 98).

*Record 100's entry in the generated run:* month 16, ground EHDS Art 68(12), authorised by DPO; a second entry records the subject-link removal at month 16. (In the toy code the key-identifier hash is not hiding, since the toy key names are predictable.)

Point to: §4.8, pp. 65 to 66; §6.8, p. 98; slide 11 (audit); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

## B4.5 What survives, and why that gives $V = 1$ under Semantics II

| What survives | Which condition it serves |
|---|---|
| Accessor fields $m_{\mathrm{acc}}(a)$, checked by inclusion proof | (i) |
| Subject fields, while kept (cross-border: whole floor), checked by their salted commitment | (i) |
| Commitment $c(a)$, in the log leaf | (ii) |
| $\iota(a)$ and any subject-link removal entry, in the log | (iii), and covered by (i) |

What goes at $t^{I}$: key, salt, ciphertext; and for patient-level SPE logs, the subject fields at the ceiling.

So in every month of the window, (i), (ii) and (iii) hold, and $V^{II} = 1$ while $\alpha = 0$. The auditor can then establish four things: the access happened, with its attributes; some payload was bound at write time and has not been swapped; it was invalidated, when, on what ground, by whom; each entry is as first written. The auditor cannot read the payload, and cannot verify that the key is gone (§4.8, p. 66).

Point to: §4.8, p. 66; §5.7, p. 88; slide 11 (audit); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=19>

## B4.6 One record through the mechanism: record 100

| Month | State of record 100 | $\alpha$ | $\beta$ | $V^{II}$ |
|---|---|---|---|---|
| 7 | Access logged. Payload encrypted under its own key; commitment `678ade47...` and salted subject commitment computed; access leaf appended | 1 | 1 | 1 |
| 8 to 9 | Unchanged | 1 | 1 | 1 |
| 10 | Permit DP-015 expires; the Health Data Access Body's portal supplies the date (§4.11, p. 73); ceiling deadline 16 fixed, so $t^{I} = 16$ unless an earlier request arrives | 1 | 1 | 1 |
| 11 to 15 | Unchanged; payload still readable to an authorised auditor | 1 | 1 | 1 |
| 16 | Invalidation: key destroyed, salt destroyed, ciphertext deleted; subject field PSN-0000 and its salt removed; two entries appended (ground EHDS Art 68(12), DPO) | 0 | 0 | 1 |
| 17 to 19 | Accessor fields, commitment and entries remain; inclusion proofs verify | 0 | 0 | 1 |
| 20 | Floor over. Specified terminal transition: identifying metadata destroyed, logged (not implemented) | 0 | 0 | not required |

*Variant:* record 132 (from the checker) loses its payload at month 5 on Art 17(1) and its subject link at month 13 on Art 68(12): step 4 of Proposition 2.

Point to: §4.7, pp. 60 to 61; §4.8, p. 67; Figure 5.2, p. 85; slide 11 (audit); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

## B4.7 The honest boundary: key custody, backups, HSM

**Attested, not proven.** The entry records that a named actor destroyed a named key in a named month on a named ground. An auditor can check that the claim was made, by whom and when, and that it has not been altered. An auditor cannot check that the claim is true (§6.3, p. 94). The further from the storage medium an approach works, the harder destruction is to assert, and cryptographic erasure is the limiting case (Reardon et al., 2013).

**An HSM narrows the gap without closing it.** A FIPS 140-3 validated module puts destruction inside a tested boundary, but validation attests the module's design, not any particular destruction (§6.3, p. 94).

**Backups.** Copies the store cannot delete at once become unreadable at $t^{I}$ and leave by rotation. Until then they remain personal data: a bounded residue, stated as such (§4.9, p. 69).

**The trust assumptions** (§4.9, p. 69): the controller destroys when it says and kept no outside copy; the custody boundary retains and leaks nothing; the log operator does not rewrite history (detectable only with published roots); the accumulator manager, if used; hash and cipher hold over the horizon.

**What would close it.** Proof of secure erasure, or certified deletion, whose public verifiability is open (Broadbent & Islam, 2020); the entry could then carry a proof with no change to the model (§7.5, p. 108). Against deletion logged in the same log, the mechanism's edge is the commitment (§6.3, p. 95).

Point to: §4.9, pp. 69 to 70; §6.3, pp. 94 to 95; slide 25 (q-keys); <https://trfhimolde.streamlit.app/?p=robust>

## B4.8 Residual identifiability

**The finding.** The residue is pseudonymised, not anonymous, until the terminal transition. "Any claim that the mechanism achieves anonymisation would be false" (§4.9, p. 69).

**The sources.**

- Datatilsynet (2015): encryption protects rather than anonymises; data stay personal while any key or linkage capable of re-identification is kept.
- EDPB draft Guidelines 02/2026 (version 1.0, adopted 7 July 2026, for consultation): anonymous only if the data resist isolation, linkage and inference by means reasonably likely to be used; encryption is reversible and is not anonymisation (§4.9, p. 68).
- CJEU, *EDPS v SRB* (C-413/23 P, 4 September 2025), paras 73 and 76 to 77: pseudonymised data may not be personal for a recipient who cannot lift the pseudonymisation, but remain personal for the controller who holds the additional information. The repository controller holds both the subject link and the accessor's identity, so for it the residue is personal data (§4.9, p. 69).
- *Breyer* (C-582/14) is the earlier case on identification through a third party's additional data. [CHECK: Breyer is not cited in the thesis; background only, do not attribute it to the thesis.]

**Why it is nonetheless defensible.** The test is erasure, not anonymisation, and the store meets it by deletion (§4.9, p. 69). Against enumerating a small set of accessors against a surviving leaf hash, the specification adds a per-entry nonce, destroyed at the terminal transition: not implemented (§4.9, p. 68).

Point to: §4.9, pp. 68 to 69; §4.8, p. 67; slide 27 (q-residue); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=19>

## B4.9 Why this is not "just crypto-shredding", a blockchain, or redactable signatures

**Crypto-shredding.** The technique is established; no new cryptography is claimed. The practitioner pattern is bilateral and "asserts that erasure occurred" (§4.8, p. 66); the thesis adds the ceiling, a model, a verifiability semantics and a checkable record (§2.4, p. 25). Concede: the model cannot tell key destruction from deletion, so keys rest on backups (OPR-6), not a proposition.

**Blockchain and redactable structures.** A ledger never forgets, which is where erasure fails (Finck); redactable designs let an editor rewrite history. This log keeps a chain's tamper evidence, is never edited, and never holds erasable content (§2.4, pp. 23 to 25). Row-by-row comparison: B6.2.

Point to: §2.4, pp. 21 to 25; §4.8, p. 66; slides 18 (q-chain) and 28 (q-rival4); <https://trfhimolde.streamlit.app/?p=built>

# B5. Why the method fits: Design Science Research

## B5.1 Hevner (2004) and Peffers (2007) as the thesis uses them

**Hevner et al. (2004)** supply the paradigm. Design science builds and evaluates artefacts (constructs, models, methods, instantiations). Utility is judged against the problem environment; rigour against the knowledge base (§3.1, p. 37).

**Peffers et al. (2007)** supply the six-activity process, mapped onto chapters (§3.2, p. 38):

| Activity | Thesis |
|---|---|
| 1 Problem identification and motivation | Chapters 1 and 2 |
| 2 Objectives of a solution | §1.3: joint satisfaction, accountability kept, auditor-verifiable, fits Norway |
| (inserted) Formal modelling | §3.3: the problem stated as a feasibility question before design |
| 3 Design and development | Chapter 4: model, semantics, propositions, mechanism |
| 4 Demonstration | Chapter 5 |
| 5 Evaluation | Chapters 5 and 6 |
| 6 Communication | The thesis; Chapters 6 and 7 |

The entry point is problem-centred. An earlier iteration went from technology (zero-knowledge SNARKs) to problem; the formal analysis showed that machinery unnecessary, and dropping it "is itself an instance of the design cycle operating as intended" (§3.2, p. 38). Hence the name VERA-SNARK (p. x).

**Why DSR** (§3.1, p. 37). Interviews give description, not a mechanism; a systematic review gives synthesis, but the gap is a missing design; a pure formal-methods study (Feng et al., 2023) gives a model without an artefact.

Point to: §3.1 to §3.3, pp. 37 to 39; slide 19 (q-snark); <https://trfhimolde.streamlit.app/?p=start>

## B5.2 Which artefact types the work produces

The thesis claims two of Hevner's four levels (§3.3, p. 38):

- a **model**: the TRF Model, a formal representation of the domain and its constraints;
- a partial **instantiation**: the sandbox (checker, realism layer, viewer, optional modules), over synthetic data.

It claims no deployed system. The candidate's own reading, not the thesis's: the mechanism specification (§4.8) could also be described as a **method**, and the notation and two semantics as **constructs**. Say this only as a reading, since §3.3 names two levels.

Point to: §3.3, p. 38; §5.2, p. 79; slide 16 (close); <https://trfhimolde.streamlit.app/?p=built>

## B5.3 What was evaluated, and how

The evaluation is analytical (§3.7, p. 44):

- *Internal validity:* do the constraints translate the instruments, are the semantics distinct, do the propositions follow, is the mechanism the witness? Assessed by proof and by the executable checks (B3.9).
- *External validity:* compatibility with verified infrastructure, requirement by requirement in Table 4.1 (p. 74). Weaker than deployment, and not presented as equivalent.
- *Reliability:* determinism; fixed seed 20260915; every command has a recorded output.

In Venable et al.'s (2016) terms, the evaluation is artificial, not naturalistic. Utility, efficacy in operation and acceptance are not evaluated (§6.6, p. 96). The falsifiable part of the Semantics II result is the inclusion-proof check (§5.7, p. 88).

Point to: §3.7, p. 44; Table 4.1, p. 74; §6.6, p. 96; slide 12 (evidence); <https://trfhimolde.streamlit.app/?p=ledger>

## B5.4 Why interviews were designed but not run

Appendix C specifies the instrument: eight experts, two each from data protection, health IT architecture, SPE operation and information logistics; a semi-structured guide; 16 Likert items over utility, regulatory alignment, operational viability and audit integrity (§3.8, p. 46). Interview question seven asks whether Art 68(12) reaches the logs; item A2 asks whether attested destruction suffices (§6.6, p. 97).

It was not run because it would process personal data about identifiable professionals, needing Sikt notification with four to six weeks' lead time, and a revision of the scope, ethics and originality statements, which are accurate as submitted (§3.8, p. 46). It is the first item of future work (§7.5, p. 107).

Point to: §3.8, p. 46; Appendix C, p. 160; §7.5, p. 107; no slide; <https://trfhimolde.streamlit.app/?p=start>

## B5.5 Hevner's seven guidelines mapped to the thesis

The thesis does not tabulate Hevner's seven guidelines. **This is the candidate's own mapping.**

| Guideline (Hevner et al., 2004) | Where the thesis meets it |
|---|---|
| 1 Design as an artefact | TRF Model; mechanism specification; sandbox (Ch 4 to 5) |
| 2 Problem relevance | EHDS collision; Norway's live NCPeH pilot; rules apply 2029 (Ch 1, §6.8) |
| 3 Design evaluation | Proofs; exhaustive search and Z3; 200-record demonstration; Table 4.1 (Ch 5, §4.11) |
| 4 Research contributions | Four bounded contributions (Statement of Contribution, pp. ix to x) |
| 5 Research rigour | Primary legal sources; stated proofs; reproducible code with fixed seed (Ch 3, App A) |
| 6 Design as a search process | Six rival designs tested (§4.10); SNARK design dropped (§3.2) |
| 7 Communication of research | Thesis; NORS 2025 presentation; public app and archive (§1.6, App A) |

Point to: §3.1 to §3.3, pp. 37 to 39; Statement of Contribution, pp. ix to x; slide 16 (close); <https://trfhimolde.streamlit.app/?p=ledger>

# B6. Novelty and the competitors

## B6.1 What is new, and what is borrowed

**New, in the reviewed literature** (Statement of Contribution, p. ix; §2.8, p. 34; §2.10, p. 36):

1. The formal characterisation of a floor, a right and a ceiling acting together on one record, with verifiability as the parameter that decides feasibility.
2. The finding that the conflict lies in an implicit semantic assumption, not in the obligations (§6.9, p. 99).
3. Proposition 3: a ceiling collides only if no longer than the floor, and its anchor decides whether the text shows it.
4. The mechanism specified for the cross-border health audit trail, with its residue analysed and placed on the Norwegian substrate.
5. The information-logistics expression of the problem (§2.10, p. 36).

**Borrowed, with source** (§2.4 to §2.5, pp. 21 to 27):

| Element | Source |
|---|---|
| Compliance as satisfiability, counterexamples as violations | Feng et al. (2023); Arfelt et al. (2019) for GDPR monitoring |
| Hash-chained tamper-evident logs | Schneier & Kelsey (1999) |
| Merkle trees; logarithmic proofs | Merkle (1988); Crosby & Wallach (2009) |
| Public append-only logs, RFC 6962 hashing | Laurie et al. (2013), Certificate Transparency |
| Cryptographic erase; key hierarchies | NIST SP 800-88 Rev. 2; Barker (2020) |
| Deleting by forgetting keys, on deadlines or policies | Boneh & Lipton (1996); Perlman (2005); Geambasu et al. (2009); Cachin et al. (2013) |
| Dynamic accumulators (specified, not built) | Camenisch & Lysyanskaya (2002) |

**Not claimed** (p. x): no new primitive, no new formal method, no "first-ever" framework, no deployment, no proof of key destruction.

Point to: Statement of Contribution, pp. ix to x; §2.8, pp. 32 to 34; §2.10, p. 36; slide 16 (close); <https://trfhimolde.streamlit.app/?p=ledger>

## B6.2 The rival designs compared

| Rival | What it gives | Why it fails here | How TRF differs |
|---|---|---|---|
| Do nothing: rely on Art 17(3)(b) (Rival 1) | Floor met | Exemption covers only what is necessary; Art 68(12) has none (p. 70) | Keeps only what necessity protects |
| Anonymise the record (Rival 2) | C2 and C3 met | Destroys accountability; Art 73(1)(e) requires identifiable logs. Breaks C1 (p. 70) | Keeps accessor fields identifiable |
| Pseudonymise only (§1.2) | Looks like a middle way | Reversible, so still personal data (Recital 26); erasure not met (§1.2, p. 3) | Deletes payload, key, salt; residue stated as pseudonymised |
| Minimise at capture (Rival 3) | Less to erase; compatible | ITI-55 puts the query in the audit message, so the standard, not the deployment, sets the payload (p. 71) | Works alongside it; handles what must be captured |
| Delete the whole entry and log it (Rival 4) | C2, C3; a trace | Fails C1: no commitment, so (ii) fails, by definition (p. 71) | Conceded "close to an equivalent design" for cross-border; edge is the bound, attributed entry and substitution detection; real work in SPE logs |
| Recoverable encrypted copies, DePaul (Rival 5) | Right for two floors with a known purge date | Keyed copies stay personal data: what the ceiling forbids (pp. 71 to 72) | Destroys recoverability, keeps accountability |
| Move the logs out at permit closure (Rival 6) | Meets the ceiling; accepted for Corollary 1.2 | Leaves the right untouched (Proposition 4); moves subject fields to a second controller (p. 72) | Meets ceiling and right in place |
| Crypto-shredding pattern (VeritasChain, 2026) | Per-subject key destroyed on request | Bilateral; asserted; no model or verifiability semantics (§2.4, p. 25) | Adds ceiling, model, semantics, checkable record |
| Redactable blockchain, chameleon hash, redactable or sanitizable signatures | Erasure inside an integrity structure | Weakens binding; an editor can rewrite history (§2.4, p. 23) | Log never edited; erasable content never enters it |
| Blockchain audit log (KONFIDO) | Immutable cross-border traceability | Immutability against erasure left unresolved; SGX hardware dependency (§2.4, p. 21) | Software only; personal data kept off the log |
| SNARK designs (ZK-EHR, Albalwy 2026; early VERA-SNARK) | Credential proofs hiding identity | Access control in one jurisdiction, not retention (p. 22); unnecessary here (§3.2) | Commitments and a logged registry suffice; ZK only for proving completeness of invalidation (§7.5) |
| Access control (SecuPi, 2025) | Restricts who may read | Data remain, so no ceiling is met (p. 95) | Makes data unreadable |
| Ledger crypto-erasure SoK (Aikebaier, 2026, preprint) | Erasure-side security notion | Excludes retention law by scope (p. 24) | Treats all three; its fifth open problem |

Point to: §4.10, pp. 70 to 73; §2.4, pp. 21 to 25; Table 2.1, p. 32; slides 6 (fixes), 18 (q-chain), 28 (q-rival4) and 30 (q-props34); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

## B6.3 The two strongest novelty attacks

*"This is framing, not a contribution."* Reply: "It is a contribution of framing and feasibility, and the Statement of Contribution says so on its first line (p. ix). The framing has teeth: Proposition 1 rules out a whole class of designs, Proposition 3 gives a drafting test that corrected my own expectation on §17, and the mechanism follows from the proof."

*"DePaul already did key-lifecycle reconciliation."* Reply: "It reaches the same engineering insight, and the thesis credits it. The decisive difference is direction: it meets a floor by keeping recoverable copies, which a ceiling forbids. It also lacks verifiability semantics, and its purge date is fixed in advance, whereas a request comes when the patient chooses (§2.4, p. 24)."

Point to: Statement of Contribution, p. ix; §2.4, p. 24; §4.10, pp. 71 to 72; slide 28 (q-rival4); <https://trfhimolde.streamlit.app/?p=anchor>
