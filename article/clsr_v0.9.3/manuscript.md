---
title: "Auditing After Erasure in the European Health Data Space: Audit Logs, the Right to Erasure and Permit-Based Deletion"
lang: en-GB
abstract: |
  What must a health data access body be able to prove after the data behind an access log have been erased? The European Health Data Space Regulation sets a one-year minimum for access logs and a six-month limit after permit expiry for deleting electronic health data in a secure processing environment. We examine when those duties, or an applicable erasure duty under the General Data Protection Regulation, reach the same field. A design that requires the original field to remain readable becomes infeasible if deletion falls within its retention window. Where an audit can establish who acted, under which permit and with what recorded outcome, that evidence can survive the removal of patient links and payloads. In a fixed simulation, plaintext verification produced conflicts for 53 of 100 secondary-use records under a broad reading of the deletion rule and nine when the permit ceiling excluded log fields. The proposed design satisfied the modelled checks in both cases. Its feasibility depends on the questions an auditor must answer and on independent assurance that copies and recovery keys have been retired.

keywords:
  - secondary use of health data
  - secure processing environment
  - health data access body
  - GDPR Article 17
  - cryptographic erasure
  - tamper-evident logging
  - data minimisation
---

::: {.docxonly}
**Keywords:** secondary use of health data; secure processing environment; health data access body; GDPR Article 17; cryptographic erasure; tamper-evident logging; data minimisation
:::

# 1 Introduction

A secure processing environment gives a researcher controlled access to
health data under a permit. A later investigation may ask who ran an
operation, what authority covered it and whether the operation stayed
within the permit. The evidence becomes more durable if the environment
stores the command, its parameters and any patient identifiers in the
audit record. Those same fields can perpetuate access to health
information after the permit has ended or after a patient has
established a right to erasure. An operator therefore needs to decide
which facts an audit record must prove, which data are necessary to
prove them and how long those data may remain accessible. The facts
differ by question. Two queries can return the same aggregate even
though one of them omitted a condition in the permit. A record that the
result was approved shows who approved it. It does not show which filter
ran, or that the version released was the one approved.

The European Health Data Space (EHDS) Regulation makes this a design question for operators preparing for Chapter IV, which generally applies from 26 March 2029. Article 73(1)(e) requires identifiable logs of access and
activities for the time necessary to verify and audit operations, with a
minimum of one year for access logs. Article 68(12) requires deletion of
electronic health data in the environment within six months of permit
expiry [1]. Article 17 of the General Data Protection Regulation (GDPR)
separately requires erasure where a ground applies and an exception does
not protect the processing [2]. These provisions start their clocks at
different events and apply to different objects. A one-year audit floor
and a six-month ceiling can overlap for a particular field. The two
numbers alone cannot establish that they do.

This article asks when a design that preserves the original payload
becomes infeasible and which evidence could support an audit after the
payload has been removed. The Tri-Lateral Retention Feasibility (TRF)
model locates the overlap at field level. It treats the meaning of
verifiability as a design choice subject to legal requirements. The
analysis establishes an exact conflict criterion for plaintext
verification in the model and constructs a feasible trajectory when the
required audit evidence survives erasure. Norway's cross-border
primary-use infrastructure supplies a comparison in which a different
retention rule and a different accountability question apply.

Research on secondary use in the EHDS has examined when anonymisation
and pseudonymisation are available in secure processing
environments [3]. Related legal work addresses the GDPR basis for
repurposing health data [4] and the scope and effect of the EHDS opt-out [5,6]. Research on audit logging provides designs for preserving integrity [7,8]. Work on distributed ledgers has examined controlled
deletion and the legal status of information left behind [9,10,11]. Redactable-signature and chameleon-hash schemes instead permit authorised modification of signed or chained content without breaking verification [12,13,14], whereas the design proposed here keeps the log append-only and appends an invalidation entry. The
question here concerns which evidence must remain readable when a
retention floor, an individual erasure obligation and a permit-based
deletion ceiling bear on the same system. An integrity proof can help
answer that question only after the necessary audit evidence has been
defined.

The study combines legal analysis, a discrete-time specification and a design-science demonstration [15]. The legal analysis separates the text of
the two regulations from the assumptions that determine whether a field
is necessary and whether the ceiling covers it. The principal interpretive question is whether the permit-based deletion rule reaches a copy of health data made for audit. We read Article 68(12) in its permit context and alongside the auditing function in Article 73. The simulation varies the disputed scope instead of assigning a probability to either interpretation. The specification formalises those assumptions as inputs [16] and proves feasibility results
conditional on them. A synthetic sandbox exercises the resulting design
at a fixed seed. Its observations concern the implementation and the
scenario, while the proofs concern the model. Institutional
acceptability, system performance and real-world rates remain questions
for further evaluation.

# 2 Retention and deletion in the EHDS

## 2.1 Three duties with different objects

In the secondary-use pathway, health data access bodies provide
data-permit access through a secure processing environment (SPE) [17].
Article 73(1)(e) requires identifiable logs of access and activities for
the period necessary to check operations and sets a minimum of one year
for access logs. The one-year value therefore sets a lower bound for the
access logs studied here. Activity records need an assessment of the
applicable purpose and period. Article 68(12) imposes its ceiling on
electronic health data within the environment and anchors it to permit
expiry. The regulation provides for implementing acts on SPE
requirements under Article 73(5) by 26 March 2027. Under Article 105,
the general application date for Chapter IV is 26 March 2029, subject to
the exceptions stated there.

Article 17(1) GDPR requires erasure without undue delay where one of the
grounds applies. Article 17(3)(b) protects processing to the extent
necessary to comply with a legal obligation, and Article 5(1)(c) limits
personal data to what the purpose requires. Other exceptions can apply,
including for qualifying public-health or research processing under
Article 17(3)(c) and (d). Those exceptions require their own analysis of the particular purpose and conditions [18]. A public-interest basis for
processing a research dataset does not settle the necessity of keeping a
copy of it in a log. The model assigns an erasure deadline only after
determining that a duty applies to the field in question.

Identification is a further condition. Under Article 11(2) GDPR, a
controller that can demonstrate it is not in a position to identify the
data subject need not apply Articles 15 to 20, including erasure, unless
the data subject supplies information enabling identification [2]. In
the EHDS secondary-use pathway, pseudonymised data are provided only
where anonymised data cannot serve the purpose, and the information
needed to reverse the pseudonymisation is held by the health data access
body or a trusted third party (Article 66(3)). Health data users must not
re-identify or attempt to re-identify the persons concerned (Article
61(3)) [1]. An erasure request concerning data in an environment
therefore reaches, in practice, a party able to link the request to the
logged fields, and the user may lack that ability by design. The
simulation treats every generated request as applicable to the field,
which makes its request-related counts an upper bound. Article 12(3)
governs when controllers must provide information on action taken on a
request. Its standard one-month period, and possible extension by two
further months with timely notice, supply simulation parameters. The
prohibition on undue delay continues to govern erasure. The model also
treats the prospective secondary-use opt-out in Article 71 EHDS as a
distinct entitlement. Table 1 summarises the three duties as modelled.

Table: **Table 1.** Duties modelled for secure processing environments. The model treats the scope and timing of each duty separately.

| **Duty** | **Object and trigger** | **Question for the operator** |
|:-----------|:------------------------------------|:------------------------------|
| EHDS Article 73(1)(e) | Identifiable access and activity logs. Access logs have a one-year minimum measured from the access event in the model. | Which evidence is necessary to identify and audit the operation? |
| GDPR Article 17 | Personal data for which an erasure ground applies, subject to the exceptions. A valid request can trigger the response workflow. | Which fields have a binding erasure deadline and which still serve a legal obligation? |
| EHDS Article 68(12) | Electronic health data within the SPE, due for deletion within six months after the permit expires. | Which logged fields are electronic health data covered by this obligation? |

## 2.2 Which log fields does the ceiling cover?

A contextual reading of Article 68(12) ties deletion to data made
available for permitted secondary use. The provision sits within the
data-permit article. On this reading, the environment's own access logs
have a separate accountability purpose and are governed by Article
73(1)(e) and applicable data-protection rules. The study represents this
reading by disabling the permit-based ceiling for audit records, while
leaving it in force for the underlying data. It leaves bilateral
conflicts possible where a system insists on keeping a field readable
and a valid Article 17 duty reaches that field.

A broader reading gives weight to the words "within the secure
processing environment". A log field that copies or otherwise reveals
electronic health data may satisfy that description even though the
provenance of the field is a log. The analysis then turns on content and
linkability. A record of which researcher opened an environment and when
ordinarily concerns the researcher's behaviour. A record linking an
identifiable patient to a health encounter or to an extraction for a
particular condition may also reveal health information about the
patient. Dataset-level logging reduces the need to hold patient
identifiers, although a retained query or output can still disclose
patient-level information. The unit of classification is the actual
field and its context. Article 2(2) includes personal and non-personal
electronic health data. Removing identifiers from health information can
change its status under the GDPR while leaving the separate Article 68(12) question open [19,20]. The broad reading does not entail a universal
deletion date for every field in every log.

A harmonising reading would give effect to the retention duty for fields
necessary to audit the processing and apply the ceiling to additional
health information within its scope. That approach demands a concrete
account of necessity. For an access log, an actor, permit reference,
time, data category and outcome may identify the access sufficiently.
Auditing whether a query stayed within its permit can require additional
context, such as the operation type, a dataset-version reference, the
policy under which the query was evaluated or some of the original
query. If a decision turns on the exact values returned for particular
patients, preserving a summary and a commitment can leave the auditor
unable to resolve it. Conversely, where a permit and a policy decision
record give the necessary detail, preserving a full output in the log
adds disclosure without an equivalent evidentiary benefit.

The final sentence of Article 68(12) supplies a practical boundary. At the health data user’s request, the health data access body may keep the formula used to create the requested dataset [1]. A cohort definition expressed as age bands, a diagnosis category and a date range could let a reviewer examine the selection rule after expiry. It would not establish which patients appeared in the result on a particular day. A purported formula that enumerates patient identifiers would itself require assessment as health data. The permission identifies a specific object, holder and trigger. It gives no general permission to retain query histories or patient-level outputs. Nor does permission to retain the formula establish that its retention is necessary for every audit.

Read together, Articles 68 and 73 give the strongest case for retaining independently necessary evidence about the use of a permit and for deleting a copied patient-level result whose only function was to supply the researcher with health data. The difficult case is a value that serves both functions. Here the access body should identify the particular audit finding that would become impossible without that value and ask whether a less revealing record, prepared when the operation occurs, would support the same finding. If the answer is no, a commitment alone cannot resolve the legal question. The two ceiling settings in the demonstration bracket this decision. A field-by-field assessment could place records from the same permit in different settings.

TEHDAS2's technical specifications provide a concrete reference point
for interpreting the accountability purpose. The joint-action
specification covers several categories of operations, calls for
identifying the actor and requires secure storage of SPE access logs for
at least one year. The one-year minimum reflects Article 73(1)(e). The
specification separately recommends five years to support effective
auditing. A deployment that adopts a longer applicable retention period
increases the interval during which a permit-based ceiling can overlap
it. The specification helps identify relevant audit operations, while
the division between evidence and health data still calls for a decision
about what each field discloses and what a later review requires [21].

## 2.3 Necessity in cross-border primary use

In primary care, the corresponding audit question may include whose data
were accessed. Article 9 EHDS gives individuals information on access to
their personal electronic health data through the health professional
access service and requires that information to remain available for at
least three years from each access, where the provision applies. Article 105 phases in Article 9 by data category, beginning in March 2029 and March 2031 for the categories in Article 14(1)(a)–(c) and (d)–(f), respectively [1]. A
repository that supplies the information may need to retain a usable
link to the patient. The argument applies to an entity bound by, or
acting for an entity bound by, that duty and to the access events that
it covers. A national gateway's location in an exchange is insufficient
to establish the duty or its duration. A controller must identify the
applicable legal basis and the evidence needed for the patient-facing
service.

The IHE Cross Gateway Patient Discovery transaction (ITI-55) illustrates
why the payload and link should be considered separately. In the IHE baseline, the audit messages of both the Initiating and the
Responding Gateway record the patient-discovery query segment in an
encoded field, and only the Responding Gateway's message also identifies
each patient whose demographics it returned. The query can include identifying details such as
name and birth time. An audit may need a patient link to answer whose
data were sought and a result to explain whether the match succeeded.
Retention of the original demographics still requires a purpose-specific
case, particularly if the purpose for keeping them was to resolve a
patient match. A dispute over the exact demographics supplied could
justify retaining particular fields for a defined period. The IHE
transaction is a technical baseline, and a deployment's applicable
profile and obligations determine how that baseline is implemented [22].

Norway's MyHealth@EU pilot provides a setting for this comparison. The
Norwegian Directorate of Health describes participation through a
national contact point and an initial capability for Norwegian
healthcare personnel to retrieve health information for visiting
patients [23]. This is evidence of an implementation pathway. The European Free Trade Association's register lists the EHDS Regulation as under scrutiny for incorporation into the European Economic Area Agreement as of 26 November 2026 [24]. The use of Article 9 as a
prospective benchmark and the use of illustrative repository retention
values are consequently distinct from claims about current Norwegian
legal obligations. For the MyHealth@EU search-and-view module, the Directorate's privacy notice states that the log records the health professional's name, HPR number, role, type of institution, place of treatment and time of lookup, and that these data are kept as part of the log for six years. It names Article 6(1)(c) GDPR and section 22 of the Patient Records Act (pasientjournalloven) as the basis, the Directorate as controller and Norsk helsenett as processor [25]. That period concerns accessor evidence. In a written reply of 19 October 2026 (personal communication), the Directorate stated that six years had been decided for the pilot and that the period for full production remains its decision as controller. Neither source sets a period for patient-query payloads. The 72-month value applied to a readable payload in Section 5 is therefore an illustrative comparison. The ten-year value used in the supplied
sandbox is an illustrative long floor. The study evaluates the
difference made by both values and by a 36-month scenario. Article
68(12) is assigned only to covered health data in a secondary-use SPE.

# 3 The Tri-Lateral Retention Feasibility model

## 3.1 Evidence, fields and clocks

Consider an audit record created in month $s$. It contains accessor
information $A$, a link $J$ to the patient where the activity calls for
one, and a payload $P$ such as demographic query content or logged
activity. A role or operation attribute is included in $A$ only if the
auditor needs it and it can be retained lawfully. The partition need not
coincide with table columns or a single physical record. For example, a
dataset identifier in the accessor record might have to be treated as
patient-linked if the dataset identifies one person. The proof can be
applied to each independently recoverable field or group of fields.

Let $F$ denote the applicable floor in months and
$W = \{ s,\ldots,s + F\}$ the retention window on the model's monthly
grid. Let $x(t)$ be 1 when the controller can recover a selected payload
field in intelligible form at month $t$. A separate variable can
represent recovery of a patient link. Let $V(t)$ be 1 when the evidence
meets the chosen verification requirement at month $t$. The floor
demands $V(t) = 1$ throughout $W$. Each applicable deletion duty sets a
deadline after which the field must be unavailable, represented as
$x(t) = 0$ for $t \geq d$. Let $d_{R}$ be the deadline for a field
subject to a valid erasure obligation and $d_{C} = e + 6$ the ceiling
when it reaches the field, where $e$ is the month of permit expiry. An
inapplicable deadline has value $\infty$. Multiple deadlines can apply
to a field. A link can have a deadline of its own even after earlier
erasure of the payload.

The code uses a closed window, which includes the month in which the
floor is reached. This is a conservative convention for monthly data
with no ordering within a month. At the resolution of a real timestamp,
legal and operational rules must specify the instant at which the floor
ceases to bind and the deadline becomes effective. A half-open interval
that allows deletion exactly at the end of retention changes the
equality case in the result below. Article 17's requirement to erase
without undue delay and any earlier operational deletion schedule can
also require action before a simulated month boundary.

## 3.2 Plaintext verification

In the first semantics, verification requires the original selected
field to be readable. Even if the design also checks integrity and
provenance, $V(t) = 1$ entails $x(t) = 1$. For the minimal form of this
semantics, the selected field's readability is the only additional
constraint once the other audit evidence is available.

**Proposition 1.** A binding deletion deadline $d$ for a field required
for plaintext verification makes the model infeasible whenever
$d \leq s + F$. For multiple deletion deadlines, $d$ is the earliest
applicable deadline. With the other audit evidence available, the
minimal plaintext model has a feasible trajectory when every applicable
deadline follows the window.

**Proof.** If $d \leq s + F$, set $t^{*} = \max(s,d)$. The retention
floor requires $x\left( t^{*} \right) = 1$ because $t^{*}$ lies in $W$.
Deletion requires $x\left( t^{*} \right) = 0$ because $t^{*} \geq d$. If
every deadline follows the window, keep the field readable in $W$ and
make it unavailable by the earliest deadline. This meets the modelled
constraints. The argument applies per field. A duty to erase one field
and a duty to verify using a different field have no such contradiction.

This also explains the role of the anchor. A ceiling of length $L$
starting at $e \geq s$ can collide only if $L \leq F$. It collides for
an individual record exactly when $e - s \leq F - L$, under the
inclusive convention. A common anchor $e = s$ makes the overlap a
property of the periods alone. When the ceiling starts at permit expiry,
the result depends on how close the access was to expiry. An entry
created at month 7, with a one-year floor and permit expiry at month 10,
is retained through model month 19 and reaches the ceiling at month 16.
If the ceiling covers the field, the collision occurs at month 16
without an erasure request. For an entry further from expiry, the
ceiling can fall after its retention window even under the same
statutory periods. Fig. 1 shows this example.

![**Fig. 1.** Proposition 1 for the example in Section 3.2. An audit entry is created at month $s = 7$ with a one-year floor, $F = 12$, so the retention window is $W = \{s, \ldots, s + F\} = \{7, \ldots, 19\}$. The permit expires at month $e = 10$ and the ceiling deadline is $d = d_{C} = e + 6 = 16$. Because $d \leq s + F$, plaintext verification requires $x(t) = 1$ and deletion requires $x(t) = 0$ from $t^{*} = \max(s, d) = 16$ to the end of the window. Values are read from the checker output for record 100 of the reference run.](Figures/Figure_1.png){#fig1 width=90mm}

The proposition evaluates a design choice and its assumed duties. If
readability is required only by the design, an operator can change the
evidentiary design. If a legally necessary field is exempt from Article
17 under Article 17(3)(b), there is no Article 17 deadline for that
field in this model. If an independent ceiling still reaches that very
field and no lawful projection preserves the required evidence, the same
contradiction persists. This case exposes an issue of legal scope or
responsibility that a storage mechanism alone cannot decide.

## 3.3 Accountability-preserving verification

In the second semantics, an auditor can verify the recorded access from
a purpose-specific set of surviving evidence. This means that the
necessary accessor and event facts are authenticated, a hiding and
binding commitment fixes the original payload, and any required loss of
recoverability is recorded as an authorised invalidation. A patient link
must also remain usable whenever the accountability function requires it
and the link can be kept lawfully. After a link or payload is removed,
checking the surviving evidence gives an audit of the event and the
invalidation. The commitment can no longer be opened to establish the
erased content once its opening is destroyed.

**Proposition 2.** Suppose the audit function can be discharged by
lawfully retainable evidence and a verifiable record of changes to the
unavailable fields. Suppose the relevant copies and recovery paths can
be made unavailable at their binding deadlines. Then the model has a
feasible trajectory for any sequence of relevant request and expiry
dates and any applicable floor.

**Proof.** Record the event and commit to each erasable component at
creation. Preserve the evidence required for $V$ throughout $W$. For
each erasable component, schedule invalidation at or before the earliest
applicable deadline, provided any necessary short-lived processing has
finished, and record the authorised change. Do the same independently
for the patient link when a duty reaches it. This makes each affected
field unavailable from its deadline onward. Because the retained
evidence and the invalidation entries meet the defined audit function,
$V = 1$ throughout the floor. If there is no deadline on a field, the
model permits its immediate or later removal once its purpose ends. If
the field is indispensable to $V$ at its deadline, the first premise
fails and Proposition 1 supplies the conflict test.

The propositions specify the facts an operator must establish. They do
not determine what the law regards as an identifiable log, when
irrecoverability qualifies as deletion, or whether a particular event
can be reconstructed from the surviving proof. Each of those questions
has to be answered for the intended audit and the environment in which
the remaining data can be combined.

Table 2 applies this to one investigation, from permit to release.
Each row names the evidence that must exist when the operation runs
and what it still establishes once payloads and openings are gone. The
two queries of Section 1 are distinguishable only through the execution
record in the third row. The last row is where Proposition 1 applies: if
the finding requires the patient-level value itself, no surviving
commitment supplies it. A selection rule kept as a formula, which Article 68(12) allows at the user's request, or a digest of a non-personal output is not patient-level data and can stay comparable after erasure; a hiding commitment whose opening is destroyed cannot be compared with anything.

Table: **Table 2.** What an auditor can establish after erasure in one permit investigation. "After erasure" means patient-level payloads, patient links and the openings of their commitments are unavailable while the listed evidence is retained. The table is a design specification; the sandbox in Section 5 does not model approval, execution or release records.

| **Audit question** | **Evidence created at the time** | **Still established after erasure** | **Not established after erasure** |
|:-------------------|:---------------------------------|:------------------------------------|:----------------------------------|
| Who acted, under which permit, with what outcome? | Authenticated actor, permit reference, time, operation type, outcome | The actor, the authority relied on and the recorded outcome | Which data the actor saw |
| Who approved the result? | Approval entry with approver role and policy version | That an approval under a stated policy was recorded | That the approved filter actually ran |
| Which filter ran? | Execution record binding query category, policy and dataset versions to the selection rule as executed, kept as a formula or as a digest comparable with the approved rule | Whether the executed rule matches the approved rule | Which patients the rule selected |
| Was the released output the approved one? | Release record binding a digest of the non-personal output to its approval entry | That the released output equals the approved output | The content of the output |
| Why was a particular patient included? | Patient-level selection result or retained patient link | Only while that evidence is lawfully retained | After its removal, nothing; the question becomes unanswerable |

# 4 Crypto-erasure by invalidation

## 4.1 What survives each transition

The mechanism separates audit evidence from the data whose
recoverability may have to end. At creation the logger authenticates an
access event, records the necessary accessor and policy facts, and binds
the erasable components to separate commitments. The original payload is
encrypted under a dedicated data-encryption key. A patient link, when
required, is held separately from the event evidence so its removal need
not change the logged accessor facts. The accessor's identity, relevant
permission, time and outcome can remain available to authorised auditors
throughout the applicable retention period. What counts as relevant must
follow the audit specification for the operation.

A binding deadline triggers invalidation of the affected component. The
system removes the component and its recovery material from the
designated boundary and appends a record of the transition (Fig. 2). The
invalidation record references the affected audit event, specifies what
component was invalidated, identifies the authorising role and states
the time and applicable basis. Only evidence necessary to establish the
lifecycle event belongs in that entry. A stable patient identifier, a
raw query or a copied decision text can undo the separation if
reintroduced through the invalidation record itself. An erasure request
can take the payload out of service while a legally necessary patient
link persists. A later, applicable ceiling can remove that link
independently.

![**Fig. 2.** Crypto-erasure by invalidation for one audit record. At creation the event and accessor evidence $A$ are authenticated and logged, and the payload $P$ and patient link $J$ are bound to separate commitments. At a binding deadline the affected component and its recovery material are removed and an invalidation entry is appended to the Merkle log. Retained accessor evidence, commitments and invalidation entries keep $V = 1$ across the retention window $W$, while $x(t) = 0$ from the deadline onward.](Figures/Figure_2.png){#fig2 width=100%}

The use of a hiding commitment matters for structured health data. A
bare digest of a name, a date or a small set of outcomes can be tested
against guesses. The design therefore requires independent, secret
high-entropy openings and a canonical representation of the committed
data. A retained commitment can evidence that a particular value was
fixed when the entry was logged. Once the opening is destroyed, an
auditor can verify inclusion of the commitment and the invalidation
entry. Establishing whether an erased value equals a later candidate
falls outside that evidence. The checker uses deterministic salts and
simulated keys to make runs reproducible. A production deployment would
require cryptographic randomness, assured custody and an assessment of
its commitment construction.

The final transition applies when identifiable audit evidence has served
its purpose and no further lawfully defined retention duty applies. It
covers accessor identity, links, object references and invalidation
details capable of restoring a personal association. A practical design
can keep erasable field values outside immutable log leaves and commit
to them, or partition log storage into segments with explicit retention
and retirement rules. With segment retirement, the operator must avoid
retaining historical proofs, manifests or checkpoints that would
establish a relationship the retirement was meant to remove. Readability
requirements, verification after retirement and personally identifying
content have to be determined before choosing the append-only boundary.

## 4.2 What log integrity and key handling establish

A Merkle log supplies inclusion proofs for event and invalidation
entries against a given root. Changes to committed entries cause checks
against that root to fail. The checker verifies against a root
maintained within its own process. To make a production claim about
append-only history, an auditor needs a trusted checkpoint outside the
writer's control, continuity evidence across successive checkpoints and
an agreed time source. A signed or independently witnessed root helps
detect a rewritten history after commitment. It does not establish that
no events were omitted before logging, that an actor claim was accurate,
or that the writer recorded the real execution time of a deletion.
Authentication of event sources and reconciliation against the access
control system serve those distinct purposes [26,27].

An invalidation entry provides attributable evidence of a process step.
Whether a payload remains recoverable depends on the handling of data
keys, wrapping keys, backups, replicas, recovery systems and cached or exported plaintext [28,29]. In envelope encryption, recoverability remains if a
wrapped copy of the data key survives alongside a usable wrapping key. A
deletion job therefore needs an inventory of recovery paths and
completion evidence that can be reconciled with the log. If key
retirement is interrupted, the system should distinguish a recorded
request or attempt from completion and prevent a restored backup from
silently reviving access. This assurance relies on evidence about
administrative authority, key management and restore behaviour as well
as on cryptographic assumptions. Media sanitisation guidance informs
this engineering assessment [30]. The legal classification of remaining
data also depends on the threat model and the information held by the
relevant parties.

An auditor can ask three separate questions. First, does the
authenticated event evidence identify the required operation? Second,
does the invalidation history show a duly authorised and recorded
transition by the relevant deadline? Third, is there a documented basis
to conclude that relevant recovery paths are closed? The sandbox checks that its recorded actor, event and invalidation entries agree with its local log. The authorising role is a label supplied by the program. Checking that the role holder approved this particular operation would require separate evidence of identity, authority and approval. The third question requires evidence from the systems that manage the data and keys.

## 4.3 Residual personal data and accountability

Retaining the accessor's identity leaves personal data about the
accessor. Its retention needs a purpose, lawful basis, access
restrictions and a schedule. Meanwhile, a residual event might still
identify a patient through a rare operation, a precise timestamp, a
permit reference or correlated information retained by the same controller or another participant [19,31]. Whether the patient link field has
been removed is only one part of that assessment. Reconstructing this
association might require very little outside information in a SPE
processing a small, named cohort. The same fields can have a different
risk profile in a large dataset with many transactions per time
interval.

GDPR recital 26 directs attention to means reasonably likely to be used for identification [2]. *Breyer* illustrates the relevance of additional information available through lawful means [32]. The EDPB’s blockchain guidelines discuss planning for erasure and caution against retaining personal data on a chain, including in encrypted or hashed form [33]. Although the proposed Merkle log can be centrally operated, the caution is relevant where values placed in an append-only record cannot later be withdrawn. The same guidelines treat commitments with off-chain storage of the underlying data as a protective measure [33], and erasable values can likewise be kept outside the log. Any surviving commitments, event identifiers and invalidation entries still require a contextual assessment.

In *EDPS v SRB*, the Court of Justice examined identifiability of pseudonymised material transmitted to a recipient, taking into account the means available to that recipient, under Regulation (EU) 2018/1725 [34]. For the information duty at issue, the Court assessed identifiability at collection from the controller’s perspective. A controller holding recovery keys or a link table has different means from an auditor who receives only a restricted view. An operator must specify whose means it has assessed before drawing conclusions about the residual data. Even if individuals cannot reasonably be identified, Article 68(12) still requires a separate assessment of whether the material is electronic health data within the environment [1].


# 5 Reproducible demonstration

## 5.1 Experimental design

The Python sandbox generates 100 cross-border records and 100 SPE
access-log records at seed 20260915. For each primary-use record it
draws a creation month uniformly from 0 through 11. It generates a
request with probability 0.40 and, where present, places it at a
uniformly drawn offset of 1 to 130 months. The reference run uses a
120-month primary-use retention floor. Secondary-use records use the
same creation range, a 12-month floor and a uniformly drawn expiry
offset from 1 through 12 months. Each secondary-use record receives a
request with probability 0.25, with an offset from 1 to 18 months. Draws
are from a fixed pseudorandom generator. Each record is one access
event with its own expiry draw. The generator assigns secondary-use
records to 17 permit labels by record identifier, and every label
carries between four and six different expiry months, so a label does
not represent one permit. The model therefore cannot say how many real
permits would be affected or how a patient-level request would
propagate across a controller's systems. Every generated request is
treated as applicable to the payload, an upper bound given the
identification condition in Section 2.1. The reference run applies the
six-month ceiling to each simulated SPE entry and models the removal of
its patient link at the ceiling.

The checker reports whether each deadline overlaps the retention window.
A violation is a record-constraint pair, so a record can violate both
the modelled erasure and ceiling constraints. The constructed trajectory
schedules payload invalidation for the earlier deadline and checks that
event evidence and invalidations verify against its Merkle log (Algorithm 1). In this
implementation, payload accessibility is defined from the scheduled
invalidation. The deadline checks thus validate the coded trajectory and
rely on it for accessibility after invalidation. The checker applies scheduled transitions before examining the months in a record’s window. It derives payload readability from the scheduled month and tests the resulting record against its log. It does not replay successive historical storage states. When a deletion deadline falls beyond the floor, the corresponding deadline loop executes no checks. Several integrity
checks can independently reject a modified record relative to the stored
root. The repository's brute-force routine separately checks the
plaintext result for three small conflict cases and one control. The
underlying study used Anthropic Claude to assist with research, source
checking and Python development, Parallel AI for source retrieval, Archify for diagrams and K-Dense skill instructions within Claude.
The reported checker outputs can be reproduced directly from the
deterministic code. The output labels follow a longer formal treatment of
the model: its "Proposition 1" and "Proposition 2" are Propositions 1
and 2 here, "Corollary 1.2" counts the no-request ceiling collisions
reported in Section 5.2, and "Proposition 3" in the output of z3_check.py
is the anchor condition discussed after Proposition 1 in Section 3.2.

::: {.algorithm}
**Algorithm 1.** Verification under accountability-preserving semantics. Faithful transcription of the function V_II in trf_checker.py (lines 305 to 318) of the supplied code archive. Here $a$ is the record rec, $s$ is rec.t_a, $x(t)$ is alpha(rec, t), $c(P)$ is rec.c, $\iota$ is rec.iota, $\iota_J$ is rec.iota_subj, $S$ is SUBJECT_FIELDS, $\rho$ is integrity_result, and $\bot$ stands for None. Integrity is the function integrity(rec) of the archive and is not expanded here.

```{.alg}
H | **Input:** record $a$ with metadata $m$, creation month $s$, payload commitment $c(P)$, invalidation entries $\iota$ and $\iota_J$; month $t$; optional integrity result $\rho$ | 305-308
H | **Output:** a pair (verdict, reason) | 305-308
0 | (*ok*, *why*) $\leftarrow \rho$ if $\rho$ is given, else Integrity($a$) | 309
if | $\neg$ *ok* | 310
1 | **return** (false, *why*) | 311
if | $c(P)$ is absent | 312
1 | **return** (false, "commitment missing") | 313
if | $x(t) = 0$ and $t \geq s$ and $\iota = \bot$ | 314
1 | **return** (false, "payload inaccessible but no invalidation entry") | 315
if | no field of $S$ is in $m$ and $\iota_J = \bot$ | 316
1 | **return** (false, "subject fields removed without a logged entry") | 317
0 | **return** (true, “”) | 318
```
:::

The reference checker and its bundled Synthea comparison were executed
using Python 3.12. The Synthea comparison replaces the constructed input
with FHIR R4 payloads drawn from eight synthetic bundles. The
substitution changes the payloads and commitments. It leaves the event
times, triggering conditions and violation counts unchanged. Synthea
payloads are used to exercise data shape. The sampled resources do not
establish Norwegian clinical representativeness. The data concern no
real individuals [35].

The sensitivity analysis keeps the same generated records, including all
request times and the secondary-use floor. It sets the primary-use floor
to 120, 72 or 36 months and reruns each case with the ceiling active for
the SPE entries, then with it disabled for those entries. The latter
case represents the contextual reading of Article 68(12). In the
checker, an infinite ceiling deadline suppresses C3 without changing the
generated requests. The 36-month setting illustrates the timing effect
of a shorter window. Its legal relevance to a repository depends on that
repository's role under Article 9. The script sensitivity.py in the code
archive supplied as supplementary material (anonymised for review) reproduces the six rows of
Table 3. A second script, sensitivity_secondary.py, reproduces the
secondary-use counts, the five-year floor and the endpoint comparison
reported in Section 5.2.

## 5.2 Results

The secondary-use records isolate the effect relevant to an SPE. Of 100 records, nine had a request-related conflict and 49 had a permit-ceiling conflict. Five had both, giving 53 affected records and 58 record–constraint pairs. With the ceiling excluded, only the nine request-related conflicts remained.

Raising the SPE floor to the five years recommended in TEHDAS2 OPR-18 [21] made all 100 events conflict under the broad reading, with 122 record–constraint pairs, and left 22 conflicts with the ceiling excluded. The first figure follows from the parameters, not from any pattern in the draws. Every simulated permit ceiling falls within 18 months of access, because the expiry offset is at most 12 months and the ceiling adds six, so any floor of 18 months or more contains it. The result shows how directly the chosen permit durations drive the conflict count.

Across the full cohort of 200 records, the reference run reproduced 95 plaintext violations across 90 records.
Thirty-seven cross-border and 53 SPE records incurred at least one.
Forty-one records incurred a request-related violation alone, 44
incurred a ceiling violation alone and five incurred both. Thirty-nine
SPE records had a ceiling collision in the absence of a request. Those
39 are a subset of the 44 ceiling-only violations, because a request can
exist and still have a deadline outside the floor. Under the second
semantics, the checker reported zero violations and verified all 200
records against its log. It scheduled 138 payload invalidations,
attributing 52 to erasure requests and 86 to the permit ceiling. For the illustrated record the program cleared the payload and its simulated recovery material from the record object.

Table: **Table 3.** Fixed cohort of 200 records with a 12-month SPE floor. "Excluded" removes the ceiling from audit entries. A violation is a record-constraint pair.

| **Primary floor** | **SPE ceiling** | **Plaintext records with a violation** | **Plaintext violations** | **Accountability-preserving violations** |
|:--------|:--------|--------:|--------:|--------:|
| 120 months | Applies | 90 | 95 | 0 |
| 120 months | Excluded | 46 | 46 | 0 |
| 72 months | Applies | 78 | 83 | 0 |
| 72 months | Excluded | 34 | 34 | 0 |
| 36 months | Applies | 61 | 66 | 0 |
| 36 months | Excluded | 17 | 17 | 0 |

The 37 affected records outside the secondary-use subset came from the primary-use comparison, to which the permit ceiling never applies.

The treatment of equality also matters. Keeping the generated dates fixed, we counted a conflict for each applicable deadline strictly earlier than the access month plus the floor, then counted distinct records with at least one such deadline. This half-open convention gives 86 pairs across 83 records, compared with 95 across 90 on the closed grid. Within the SPE subset the permit-ceiling count falls from 49 to 41. Thus eight of the 49 SPE ceiling conflicts depend on whether deletion at the retention endpoint is permitted. The remaining 41 persist under either convention.

Removing the ceiling from the log rules reduces the baseline by 49
violations. For five of the affected records, a request-related
violation remains, which is why the number of violating records drops by
44. Reducing the primary-use floor to 72 or 36 months decreases the
number of request overlaps in that class. With the ceiling enabled, all
49 ceiling violations remain because the sensitivity analysis changes
only the primary-use floor. Extending the response parameter from one to
three months in the reference scenario changes the plaintext result to
94 violations across 89 records. The 39 no-request witnesses persist,
and the second semantics again produces zero violations. These
variations expose which assumptions drive the effects in this particular
cohort. Fig. 3 plots the six scenarios of Table 3 together with the number of scheduled invalidations.

![**Fig. 3.** Sensitivity of the fixed cohort to the primary-use floor (120, 72 or 36 months) and to whether the Article 68(12) ceiling applies to SPE audit entries. Panels show plaintext records with a violation, plaintext violations (record-constraint pairs), accountability-preserving violations and scheduled payload invalidations. All values are parsed from the recorded output of sensitivity.py. The records are synthetic, generated at a fixed seed; the counts are not estimates of how often conflicts occur.](Figures/Figure_3.png){#fig3 width=100%}

The brute-force check found no feasible readability assignment for the
three small conflict scenarios and found one for the control. In the
main run, tampering with the stored accessor, the stated invalidation
ground or the patient link caused the corresponding verification checks
to fail. Restoring those values restored verification. These tests
exercise checks against the stored log rather than a fully independent
log witness. The synthetic scenarios contain no observations on
operational requests or permit durations and support no estimate of
conflict prevalence. The analytical criterion in Proposition 1
establishes when an overlap matters. The demonstration shows whether the
code behaves accordingly.

# 6 Discussion

## 6.1 Designing the audit requirement before choosing storage

The field-level test suggests an order of decisions for an SPE operator.
First, identify the operations a later audit must check and the minimum
evidence for each. An access investigation may require identity, time
and permit. An export investigation may also require the release
decision, the check applied to the output and evidence that the version
released was approved. Article 73(2) allows health data users to
download only non-personal electronic health data from the
environment [1], so the released object in such an investigation is an
aggregate or other non-personal output, not a set of patient rows. A misuse investigation may depend on the exact
command or query parameters. Second, classify each evidentiary field for
its relation to the accessor, the patient and the permitted dataset.
Third, assign separate lifetimes to the readable values and the
verification evidence. Those decisions define what the floor protects
and which components a permission expiry or an erasure decision can
remove.

A simple example concerns an approved cohort query. To establish that an
accredited researcher executed a query against the dataset and policy
version specified by the permit, it may be sufficient to preserve
authenticated identity, the policy decision, the query category and the
time. To establish that the researcher selected only a subset authorised
by the permit, the audit may require the identified subset or a record
of how the selection was checked. A system that has to answer both
questions can retain a structured, purpose-specific policy decision
outside the erasable query field. Whether it suffices depends on what
was checked at the time and on the evidence available to contest an
incorrect or incomplete decision. The commitment alone cannot replace
that reasoning. An operation-specific audit test is a stronger
requirement than a general promise that the logs will remain verifiable.

The same distinction applies when multiple obligations attach to
different persons in the same record. An accessor's identity may remain
necessary during the audit window even after a patient has established
an applicable erasure right. The assessor should examine the accessor's
own rights if a request concerns that identity. An authority-specific
retention duty, where it applies, can justify necessary fields while
lawful purposes persist. A longer retention period adopted as an
internal policy calls for its own legal assessment. For both types of
person, a change in purpose, the closure of an investigation or the
expiry of the applicable period can change which fields must remain
identifiable.

A repository that stores only necessary evidence at creation can avoid
accumulating an erasable payload. That approach is preferable where an
auditor's questions can already be answered with those fields. The
invalidation design matters where a separate, time-limited purpose
justifies temporary access to more detailed data. Simple deletion of an
entire log entry loses the necessary event evidence if the floor is
still open. Moving a full log to another system changes the location
tested by a location-specific ceiling. A lawful move also requires an
appropriate basis, safeguards and an allocation of controller
responsibilities. If a valid erasure obligation applies to the same
readable fields in the receiving repository, relocation leaves the
Article 17 issue unresolved. The status of a copy needs assessment at
each controller, including any notification of recipients required by
Article 19 GDPR.

## 6.2 Implementation implications for Norway

For a national contact point supporting primary use, the proposed
boundary is the audit repository. A gateway can continue to emit audit
events under its applicable profile [36,37]. A repository adapter can place
permitted short-lived demographic query content under separate custody
and preserve a patient link for as long as an applicable
access-information duty requires it. The operator needs to verify the
contract about the audit record, including whether the profile
prescribes storage of specific fields or only their transmission, and
whether the event must support access by a patient or evidence exchange
with a partner authority. The Norwegian pilot establishes the
setting for asking these questions. The model does not require a common
cross-border repository or one retention value for all jurisdictions.
Commission Implementing Regulation (EU) 2026/2083 concerns MyHealth@EU
and provides a separate regulatory reference for that pathway [38].

In Norway, the Norwegian Institute of Public Health is the designated coordinating health data access body, and the Directorate of Health's gap analysis found no approved secure processing environment with solutions for control and activity logging as of 11 April 2025 [39,40].

Article 74(1) gives the allocation of these decisions a legal starting point [1]. The health data holder acts as controller when making the requested personal electronic health data available to the access body. The body generally acts as controller for its own statutory tasks. In providing data in the secure environment for processing under a permit, it acts as processor for the health data user, who acts as controller for that processing. For a log spanning both activities, the operator should identify the purpose and controller for each retained field. A user’s instruction to delete the research workspace cannot by itself settle what evidence the access body needs to discharge its own audit task. Equally, the existence of that task cannot alone justify keeping the user’s full research output.

For secondary use, a corresponding attachment point is the SPE
activity-monitoring component. It can obtain permit identifiers and
expiry information from the permit authority and preserve the accessor
evidence needed to audit the environment. Permit expiry must be tied to
the actual permit version, including lawful extension or changes to
access status. Logging governed operations at dataset level can reduce
the amount of patient-linked data accumulated, provided the required
audit remains possible. Any retained patient-level fields need a
specific account of the audit question they answer and a rule governing
their disposition at the applicable ceiling. Where several bodies
control different parts of the flow, each needs a clear responsibility
for originating events, authorising changes, maintaining key custody,
receiving proof of invalidation and handling recoverable copies.

Article 73(3) provides for regular audits of the environment, which may be carried out by third parties [1]. Two acceptance tests follow from Table 2. For cohort selection, an independent reviewer would be asked to distinguish two queries that returned the same aggregate when one of them omitted a condition in the permit. A retained approval flag records what the system decided. To test whether that decision was correct, the reviewer needs the execution record connecting the policy version to the selection rule actually executed. For output release, the reviewer would be asked to show that the non-personal output that left the environment was the version approved, which needs the release record binding the two. If either pair leaves indistinguishable evidence, that audit question fails after erasure. A practical test of the design would have auditors attempt concrete
access, permit and export investigations using pre-erasure and
post-erasure evidence. The assessor could record which audit questions
remain answerable, what a reviewer can link back to a patient and where
missing evidence prevents a decision. A technical evaluation would then
exercise copy inventories, failed or delayed invalidations, restores and
independent checks of log history. It could measure deadline completion,
storage and key-management overhead, and the time needed to obtain the
evidence for a review. A deletion workflow that reports completion when
its backups can still restore a field would fail this evaluation even if
the log entries match the sandbox results.

## 6.3 Limits and regulatory implications

The analytical result depends on scope and adequacy of evidence.
Treating a patient-linked log field as covered by Article 68(12)
produces the no-request conflict only if its deadline falls within the
retention window. Some activities can be audited using accessor and
operation evidence alone. Others require patient-level information. The
contextual, broad and harmonising readings make different assumptions
about when the ceiling reaches such information. Binding guidance on the
interaction between Articles 68(12) and 73(1)(e), and on the evidence
needed for different operations, would let operators test their designs
against a more determinate requirement.

The synthetic records illustrate a limit of measuring link removal as a change to a named field. Their patient pseudonyms are derived from the record identifier, and that identifier remains in the event evidence. The generator can therefore reproduce the synthetic association after the subject field has been removed. The tests establish removal of the designated field in the simulated record. They provide no evidence that a surviving production record would be anonymous. An implementation would need to test the combinations available to each relevant holder, including information held outside the log.

A second question is when cryptographic unrecoverability can constitute
erasure for copies that survive in some form [18,20,33]. The model represents
erasure through observable state and assumes recovery paths are closed.
The checker simulates key destruction and maintains a local log root. It
also treats the timing of valid erasure requests and permit expiry as
generated inputs. It therefore provides a deterministic implementation
check under stated assumptions. A conclusion about compliance would
additionally require a lawful basis for the surviving evidence, an
assessment of its identifiability, and verified key and copy handling in
the relevant organisation. The same issues matter if the original
content is physically deleted and identifying information survives
elsewhere in the event trail.

The minimum guidance needed from implementing authorities is concrete. A
specification can identify required audit facts by operation, state
which patient-linked fields should be excluded or removed when a permit
ends, and describe how to document exceptions for fields required by
another duty. Guidance can also address how an operator should
demonstrate that ordinary restoration cannot recover invalidated data.
Clear requirements at these boundaries would let controllers compare
different storage designs against the same accountability outcomes.

# 7 Conclusion

The EHDS retention and deletion periods can collide only where they act
on the same readable field and their clocks overlap. The TRF model gives
the exact overlap criterion and shows how the result changes when the
floor is defined in terms of the audit evidence required. Crypto-erasure
by invalidation gives a constructive design in which the payload and
patient link can expire independently and an authenticated trail can
still account for the operation. The synthetic results establish how often the assumed deadlines intersect in the fixed cohort and whether the recorded transitions pass the checker. For an operator choosing a retention policy, the decisive question is which post-erasure finding an independent auditor could still substantiate. Its applicability depends on the sufficiency and lawful
retention of the surviving evidence, the scope of the ceiling and the
ability to make the erased information irrecoverable within the relevant
custody boundary.

# Data and code availability

The TRF reproducibility materials contain the deterministic scenario
generator, the reference checker outputs and eight Synthea FHIR R4
bundles. The baseline can be reproduced by running the file
trf_checker.py with Python 3.12, and the payload comparison by running
synthea_layer.py from the same package. Section 5.1 specifies the
variation of inputs used for the fixed-cohort sensitivity analysis. The synthetic data and code are archived in a public repository (link
withheld for anonymised review; given on the title page). For review, an anonymised copy of the code and synthetic data is
supplied as supplementary material.

# Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work the authors used ChatGPT (OpenAI) to
assist with drafting, language editing, pre-submission critical review, checks of legal sources and the interpretation of simulation outputs, Claude (Anthropic) to assist
with drafting, source verification, code review and reproduction of the
numerical results, and Parallel AI for web research support. Open-source
scientific-writing skill instructions (K-Dense) were used within Claude.
After using these tools/services, the authors reviewed and edited the
content as needed and take full responsibility for the content of the
published article. The use of AI during the underlying research and
prototype development is described in Section 5.1.

# References

::: {.references}
[1] Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space, OJ L 2025/327, arts 2, 9, 14, 61, 66, 68, 71, 73, 74 and 105, 5.3.2025. <https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng> (accessed 26 November 2026).

[2] Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (General Data Protection Regulation), OJ L 119/1, 4.5.2016, recital 26 and arts 4(15), 5, 11, 12 and 17-19. <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng> (accessed 26 November 2026).

[3] R. Rak, Anonymisation, Pseudonymisation and Secure Processing Environments Relating to the Secondary Use of Electronic Health Data in the European Health Data Space (EHDS), Eur. J. Risk Regul. 15 (4) (2024) 928-938. <https://doi.org/10.1017/err.2024.67>.

[4] V.L. Raposo, Can personal data be recycled? The reuse and repurposing of data under the EHDS, Int. J. Law Inf. Technol. 33 (2025) eaae016. <https://doi.org/10.1093/ijlit/eaae016>.

[5] P.R. Trigo Kramcsák, Í. de Miguel Beriain, The opt-out right for secondary uses of personal data in the European Health Data Space: Legal basis, scope, and interplay with the GDPR, Comput. Law Secur. Rev. 62 (2026) 106367. <https://doi.org/10.1016/j.clsr.2026.106367>.

[6] A. Martani, L. Skovgaard, J.J. Neubert, G. Richter, L. Marelli, The 2025 European health data space regulation: implementation challenges in harmonising opt-out rules for reusing health data, Health Policy 174 (2026) 105764. <https://doi.org/10.1016/j.healthpol.2026.105764>.

[7] B. Schneier, J. Kelsey, Secure audit logs to support computer forensics, ACM Trans. Inf. Syst. Secur. 2 (2) (1999) 159-176. <https://doi.org/10.1145/317087.317089>.

[8] S.A. Crosby, D.S. Wallach, Efficient data structures for tamper-evident logging, in: Proc. 18th USENIX Secur. Symp., USENIX Association, 2009, pp. 317-334. <https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/efficient-data-structures-tamper-evident> (accessed 26 November 2026).

[9] M. Finck, Blockchain and the General Data Protection Regulation: Can Distributed Ledgers Be Squared with European Data Protection Law?, PE 634.445, European Parliamentary Research Service, Scientific Foresight Unit (STOA), 24 July 2019. <https://www.europarl.europa.eu/thinktank/en/document/EPRS_STU%282019%29634445> (accessed 26 November 2026).

[10] M. Finck, Blockchains and data protection in the European Union, Eur. Data Prot. Law Rev. 4 (1) (2018) 17-35. <https://doi.org/10.21552/edpl/2018/1/6>.

[11] E. Politou, F. Casino, E. Alepis, C. Patsakis, Blockchain mutability: challenges and proposed solutions, IEEE Trans. Emerg. Top. Comput. 9 (4) (2021) 1972-1986. <https://doi.org/10.1109/TETC.2019.2949510>.

[12] G. Ateniese, B. Magri, D. Venturi, E. Andrade, Redactable blockchain - or - rewriting history in Bitcoin and friends, in: 2017 IEEE Eur. Symp. Secur. Priv. (EuroS&P), IEEE, 2017, pp. 111-126. <https://doi.org/10.1109/EuroSP.2017.37>.

[13] G. Ateniese, D.H. Chou, B. de Medeiros, G. Tsudik, Sanitizable signatures, in: S. de Capitani di Vimercati, P. Syverson, D. Gollmann (Eds.), Computer Security - ESORICS 2005, Lect. Notes Comput. Sci. 3679, Springer, 2005, pp. 159-177. <https://doi.org/10.1007/11555827_10>.

[14] R. Johnson, D. Molnar, D. Song, D. Wagner, Homomorphic signature schemes, in: B. Preneel (Ed.), Topics in Cryptology - CT-RSA 2002, Lect. Notes Comput. Sci. 2271, Springer, 2002, pp. 244-262. <https://doi.org/10.1007/3-540-45760-7_17>.

[15] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Q. 28 (1) (2004) 75-105. <https://doi.org/10.2307/25148625>.

[16] N. Feng, L. Marsso, M. Sabetzadeh, M. Chechik, Early verification of legal compliance via bounded satisfiability checking, in: Computer Aided Verification (CAV 2023), Lect. Notes Comput. Sci. 13966, Springer, 2023, pp. 374-396. <https://doi.org/10.1007/978-3-031-37709-9_18>.

[17] T. Petročnik, Secondary use of health data in the EHDS: public interest and the role of HDABs, in: S. Slokenberga, K. Ó Cathaoir, M. Shabani (Eds.), The European Health Data Space: Examining a New Era in Data Protection, Routledge, 2025, pp. 181-206. <https://doi.org/10.4324/9781003544111-12>.

[18] European Data Protection Board, Coordinated Enforcement Action 2025: Implementation of the right to erasure by controllers, report adopted 10 February 2026, sections 4.2.4, 4.2.6 and 4.2.7. <https://www.edpb.europa.eu/system/files/2026-02/edpb_cef-report_2025_right-to-erasure_en.pdf> (accessed 26 November 2026).

[19] Article 29 Data Protection Working Party, Opinion 05/2014 on Anonymisation Techniques, WP 216, adopted 10 April 2014. <https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf> (accessed 26 November 2026).

[20] European Data Protection Board, Guidelines 02/2026 on Anonymisation, version 1.0 (adopted 7 July 2026, version for public consultation), paras 26 and 29. <https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202602_anonymisation_v1_en_0.pdf> (accessed 26 November 2026).

[21] TEHDAS2 Joint Action, Technical Specification for Health Data Access Bodies on the Implementation of Secure Processing Environments, Deliverable D7.4, 2026, tables 5.1 and 5.4, especially OPR-17 and OPR-18 (the one-year minimum and the recommended five years are in OPR-18; the corresponding requirement EHDSR-8 is in table 5.1). <https://tehdas.eu/wp-content/uploads/2026/06/d7.4-technical-specification-for-health-data-access-bodies-on-the-implementation-of-secure-processing-environments.pdf> (accessed 26 November 2026).

[22] IHE International, IT Infrastructure Technical Framework, vol. 2, Cross Gateway Patient Discovery \[ITI-55\], sections 3.55.4.1.2.1 and 3.55.5.1. <https://profiles.ihe.net/ITI/TF/Volume2/ITI-55.html> (accessed 26 November 2026).

[23] Helsedirektoratet, MyHealth@EU: Nasjonalt kontaktpunkt og visning av helseopplysninger om europeiske borgere, project description, <https://www.helsedirektoratet.no/om-oss/internasjonalt-samarbeid/myhealth-eu-nasjonalt-kontaktpunkt-og-visning-av-helseopplysninger-om-europeiske-borgere>; and Veikart for nasjonal e-helsestrategi 2025-2031, delmål 4C, national roadmap, <https://www.helsedirektoratet.no/digitalisering-og-e-helse/veikart-for-nasjonal-e-helsestrategi/4c> (accessed 26 November 2026).

[24] European Free Trade Association, EEA-Lex factsheet 32025R0327: Regulation (EU) 2025/327, legal status "under scrutiny for incorporation into the EEA Agreement by Iceland, Liechtenstein and Norway". <https://www.efta.int/eea-lex/32025r0327> (accessed 26 November 2026).

[25] Helsedirektoratet, Personopplysninger om helsepersonell, section "MyHealth@EU – søk og visningsmodul", privacy notice, last revised 30 June 2026. <https://www.helsedirektoratet.no/om-oss/om-nettstedet/personvernerklaering/nar-behandler-vi-personopplysninger/personopplysninger-om-helsepersonell> (accessed 27 November 2026).

[26] B. Laurie, A. Langley, E. Kasper, Certificate Transparency, RFC 6962, 2013, section 2.1. The prototype uses its Merkle hashing convention. RFC 6962 is obsoleted by RFC 9162. <https://www.rfc-editor.org/rfc/rfc6962> (accessed 26 November 2026).

[27] B. Laurie, E. Messeri, R. Stradling, Certificate Transparency Version 2.0, RFC 9162, 2021. <https://www.rfc-editor.org/rfc/rfc9162.html> (accessed 26 November 2026).

[28] J. Reardon, D. Basin, S. Capkun, SoK: Secure data deletion, in: 2013 IEEE Symp. Secur. Priv., IEEE, 2013, pp. 301-315. <https://doi.org/10.1109/SP.2013.28>.

[29] D. Boneh, R.J. Lipton, A revocable backup system, in: Proc. 6th USENIX Secur. Symp., USENIX Association, 1996, pp. 91-96. <https://www.usenix.org/conference/6th-usenix-security-symposium/revocable-backup-system> (accessed 26 November 2026).

[30] National Institute of Standards and Technology, Guidelines for Media Sanitization, NIST SP 800-88 Rev. 2, 2025. <https://doi.org/10.6028/NIST.SP.800-88r2>.

[31] European Data Protection Board, Guidelines 01/2025 on Pseudonymisation, adopted 16 January 2025 (version for public consultation), para 22. <https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf> (accessed 26 November 2026).

[32] Case C-582/14, Patrick Breyer v Bundesrepublik Deutschland, judgment of the Court (Second Chamber) of 19 October 2016, ECLI:EU:C:2016:779. <https://op.europa.eu/sv/publication-detail/-/publication/84400959-c5cf-11e6-a6db-01aa75ed71a1/language-en> (accessed 26 November 2026).

[33] European Data Protection Board, Guidelines 02/2025 on Processing of Personal Data through Blockchain Technologies, version 2 (adopted 7 July 2026), paras 32-34 and 102-104. <https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf> (accessed 26 November 2026).

[34] Case C-413/23 P, European Data Protection Supervisor v Single Resolution Board, judgment of 4 September 2025, ECLI:EU:C:2025:645, paras 74-86 and 110-112. <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62023CJ0413> (accessed 26 November 2026).

[35] J. Walonoski, et al., Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record, J. Am. Med. Inform. Assoc. 25 (3) (2018) 230-238. <https://doi.org/10.1093/jamia/ocx079>.

[36] IHE International, IT Infrastructure Technical Framework, vol. 1, section 9, Audit Trail and Node Authentication (ATNA) Profile, rev. 20.0 (4 August 2023). <https://profiles.ihe.net/ITI/TF/Volume1/ch-9.html> (accessed 26 November 2026).

[37] International Organization for Standardization, ISO 27789:2021, Health informatics - Audit trails for electronic health records, 2nd ed., 2021. <https://www.iso.org/standard/75313.html> (accessed 26 November 2026).

[38] Commission Implementing Regulation (EU) 2026/2083 of 18 September 2026 on MyHealth@EU, OJ L, 2026/2083, 21.9.2026. <https://eur-lex.europa.eu/eli/reg_impl/2026/2083/oj/eng/pdf> (accessed 26 November 2026).

[39] Helsedirektoratet, EHDS konsekvensvurdering - gapanalyse pr. 11. april 2025, chapter 5, Sekundærbruk av helsedata. <https://www.helsedirektoratet.no/rapporter/ehds-konsekvensvurdering--gapanalyse-pr.11.april-2025/sekundaerbruk-av-helsedata> (accessed 26 November 2026).

[40] Folkehelseinstituttet, FHIs rolle og oppdrag i EHDS, 19 October 2026. <https://www.fhi.no/hd/det-europeiske-helsedataomradet/fhis-rolle-og-oppdrag-i-ehds/> (accessed 26 November 2026).
:::
