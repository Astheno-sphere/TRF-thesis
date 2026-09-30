# Viva Preparation: The Five Hard Questions

**Defence:** first week of December 2026, Høgskolen i Molde
**Thesis:** *Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space*

These are the five questions most likely to be asked in a way you cannot deflect. Each is
written as an examiner would put it, not as a friendly prompt. For each: why it gets asked,
the answer, where the evidence is, and what not to say.

The general rule for all five: the thesis is stronger when you concede the limit first and
then state what survives it. Every one of these questions has a concession in it that you
have already written down somewhere in the document. Reach for the concession before the
defence.

---

## Q1. "This is a logistics degree. Where is the logistics?"

**Why it gets asked.** Your programme is Sustainable Energy Logistics. Your thesis is a
constraint-satisfaction model over cryptographic commitments. An examiner from the faculty
will want to know it belongs in their discipline, and the question may come from someone
who is not hostile but is genuinely unsure.

**The answer.** Information logistics is the movement of an object through a network under
constraints imposed at each node, and that is exactly the object of study. A cross-border
audit record is generated at one node, transits a defined six-step gateway protocol, comes
to rest in a repository governed by one authority, and is subject to obligations imposed by
a different authority in a different jurisdiction. The thesis asks when those obligations
can be jointly satisfied along that path. The formulation is a feasibility question over a
flow under multi-jurisdictional constraint, which is a logistics question whatever
vocabulary it is expressed in.

Then make it concrete: the constraint that creates the whole problem, the six-month
deletion ceiling, is anchored to an external event, the expiry of a data permit. Section
6.9a shows that a floor and a ceiling coexist peacefully when one instrument fixes both
from the same origin, and collide when the ceiling is anchored elsewhere. That is a
statement about where in a network an obligation attaches, and it is the thesis's most
transferable finding.

**Evidence:** Chapter 4, Section 4.11 (infrastructure analysis); Chapter 6, Section 6.9a
(cross-sector test); Chapter 3 on the design-science framing.

**Do not say:** that logistics is "broadly about flows so this counts". That answer sounds
like a retrofit. Do not apologise for the topic either.

---

## Q2. "Article 68(12) says data must be deleted from the Secure Processing Environment. Do the environment's own access logs count as 'data within the environment'?"

**Why it gets asked.** Because Corollary 1.2 depends on the answer, and an examiner who has
read Section 4.6 knows it. This is the sharpest question in the set and the one where an
overclaim would be most damaging.

**The answer.** Concede immediately: the reading is contestable and the thesis says so. The
provision sits within the data-permit article, and a narrower construction confines it to
the dataset supplied under the permit rather than to everything the environment generates.
The thesis adopts the broad reading on textual grounds, that the provision is framed by
location rather than by provenance and that the Regulation uses the narrower "made
available under the data permit" formulation freely elsewhere when it means it.

Then give the map, because this is the part that protects you: the broad reading is load
bearing for **Corollary 1.2 only**. Theorem 1, Theorem 2, Corollary 1.1 and the mechanism
all stand under the narrow reading. If an examiner rejects the broad reading, you lose one
corollary and keep the contribution. Say that before they work it out themselves.

**Evidence:** Chapter 4, Section 4.6; the conditionality is stated at the point of use, not
buried in limitations.

**Do not say:** that the question is settled, or that the Commission will clarify it. No
implementing act on this point has been published, and asserting otherwise is checkable in
the room.

---

## Q3. "Your permits expire between one and twelve months. Is that realistic? Real research permits run for years."

**Why it gets asked.** Because it looks like the parameter was chosen to manufacture
collisions, and if it was, the violation rate is an artefact.

**The answer.** Two moves, in this order.

First, concede the empirical gap plainly: no Norwegian permit-duration statistics were used,
because none were available to the research. The distribution is a modelling assumption and
is recorded as one.

Second, and this is the substantive answer: the result does not depend on it. A longer
permit moves the ceiling later, which changes *how many* records collide, not *whether*
collision is possible. Theorem 1 is conditional by construction: it states infeasibility for
records whose erasure or ceiling deadline falls inside the retention window, and is silent
about records where it does not. The violation rate of 47.5 per cent is a property of the
generated population, not a claim about Norwegian practice, and Chapter 5 says so in the
same paragraph that reports it. The delta witness makes the same point from the other
direction: tripling the erasure response period from one month to three moves the count from
95 violations to 94 and changes nothing structural.

**Evidence:** Chapter 5, Section 5.3 (the rate is not an estimate of real frequency);
Table 5.2a (the delta witness); Chapter 3, Section 3.7 (stated abstractions).

**Do not say:** that the permit range is representative. You do not know that.

---

## Q4. "Semantics II is your own definition. No regulator has endorsed it. Why should anyone accept that an invalidated record still satisfies a retention obligation?"

**Why it gets asked.** Because it is the thesis's central move and it has no external
authority behind it. An examiner who wants to test whether you understand your own
contribution will ask this one.

**The answer.** Do not defend it as settled law. Defend it as a defensible reading, stated
as such, and say which authority does and does not support it.

What supports it: the European Data Protection Board's Guidelines 02/2025 accept that where
physical deletion is not technically possible, deleting the decryption key can render
personal data unintelligible and so serve the erasure obligation. That is the erasure half.

What does not support it: no instrument states that an invalidated record discharges a
*retention* obligation. That is the thesis's own argument, built from the necessity boundary
of Article 17(3)(b), the minimisation principle of Article 5(1)(c), and the accountability
purpose the retention obligations serve. The argument is that the accountability function of
a cross-border audit record, who accessed what, when, from where, under which legal basis,
with what outcome, does not require continued access to the clinical payload. That is a
reading, and Chapter 6 calls it a reading.

Then state the honest position: the thesis establishes that the constraint system is
satisfiable under that definition. Whether a supervisory authority would accept the
definition is a question the thesis identifies as open and proposes a Datatilsynet sounding
to answer. An examiner cannot ask for more than a correctly labelled claim.

**Evidence:** Chapter 4, Section 4.9; Chapter 6, Sections 6.2 and 6.3; Chapter 7, Section 7.4.

**Do not say:** that the EDPB endorses it. The Board's guidelines are about erasure, not
about discharging retention, and the distinction is exactly what the question is testing.

---

## Q5. "Your proofs are informal. Why should I believe Theorem 1?"

**Why it gets asked.** Because "theorem" sets an expectation, and prose proofs in a
logistics thesis invite the question of whether the formality is decorative.

**The answer.** The proofs are informal in presentation and constructive in substance.
Theorem 1 is a pigeonhole argument over a single binary variable: at the collision month one
constraint requires the variable to be 1 and another requires it to be 0, and no assignment
satisfies both. Theorem 2 is proved by exhibiting a trajectory and verifying all three
constraints against it, which is the strongest kind of feasibility proof there is, since it
produces the witness rather than asserting existence.

Then give the part that answers the real worry. The thesis does not ask to be believed on
the prose. `brute_force_semantics_I()` is written independently of `check_semantics_I()`,
takes the constraint definitions directly, and enumerates all 2^14 assignments of the
accessibility variable over a fourteen-month horizon. Two independent implementations agree
on every case. The control case, in which neither the erasure right nor the ceiling is
active, returns feasible, which establishes that the search can succeed when it should
rather than failing for a trivial reason. Anyone can clone the repository and run it.

**Evidence:** Chapter 4, Sections 4.6 and 4.7; Chapter 5, Section 5.4; Tab 5 of the live
demonstration; `docs/expected_trf_output.txt`.

**Do not say:** that the model was formalised in a proof assistant. It was not, and Chapter
3 records that as a limitation and as future work.

---

## Two more they may ask, worth having ready

**"Your synthetic data is American."** Yes. Synthea's default export is US Core with United
States demographics; it ships no Norwegian module, and the thesis states this rather than
implying otherwise. The FHIR version, R4, matches the version the Norwegian basisprofiler
constrain. The reason it cannot affect any result is the payload-independence demonstration:
substituting real FHIR resources for the constructed strings changes every one of the two
hundred commitments and not one reported figure, and that holds at two different cohort
sizes. The model reads timing and accessibility, never payload content.

**"You cannot prove a key was destroyed."** Correct, and the thesis says so in three places
rather than one. Key destruction is simulated by removing a reference in program state. NIST
SP 800-88 Revision 2 recognises cryptographic erase as a purge-grade technique precisely
because, within a documented key-management boundary, it offers high assurance, but it
defines the honest boundary of the guarantee. The invalidation entry is an attestation, not
a proof, and Section 6.3 says exactly that.

---

## How to prepare

Rehearse the concession, not the defence. For each question above, the first sentence out of
your mouth should be the limit, and the second should be what survives it. An examiner who
hears you volunteer the weakness stops probing for it.

Have three things open and runnable: the repository, the live demonstration, and
`docs/expected_trf_output.txt`. If a number is challenged, run it. That is the one move
available to you that most candidates do not have.

Know the four figures cold: 95 violations across 90 of 200 records, 39 Corollary 1.2
witnesses that received no erasure request at all, 138 invalidations, zero violations under
Semantics II.
