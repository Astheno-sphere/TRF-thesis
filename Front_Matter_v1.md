# Front Matter

---

## Title Page

*Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space*

*A Design Science Study of the Tri-Lateral Retention Feasibility Problem in the Norwegian Implementation Context*

Arshad Akhtar Abbasia

Master of Science in Sustainable Energy Logistics
Faculty of Logistics, Høgskolen i Molde, Vitenskapelig høgskole i logistikk

Supervisor: Prof. João Ferreira

Molde, November 2026

---

## Abstract

The European Health Data Space Regulation (EU) 2025/327 subjects cross-border health data audit records to three retention obligations at once: audit-retention floors (ten years as reported for MyHealth@EU audit repositories under the eHDSI deployment baseline, and one year for Secure Processing Environment access logs under Article 73(1)(e)), the right to erasure under Article 17 GDPR, and the six-month deletion ceiling of Article 68(12). No instrument reconciles them, and the implementing acts that must specify Secure Processing Environment requirements are not due until 26 March 2027.

The thesis develops the Tri-Lateral Retention Feasibility (TRF) Model, a constraint-satisfaction formulation in which the semantics of audit verifiability is an explicit parameter. Under plaintext-verifiability semantics the constraints are infeasible whenever an erasure or deletion deadline falls inside a retention window (Proposition 1). Under accountability-preserving semantics they are jointly satisfiable for every arrival pattern of erasure requests and permit expiries and for every retention floor (Proposition 2). Two further results locate the conflict: a ceiling collides with a floor only if it is no longer than the floor, and the event the ceiling is anchored to decides whether the collision is visible in the text or only in each record's history (Proposition 3); moving a record out of the regulated environment satisfies the ceiling but not the right to erasure (Proposition 4). The witnessing mechanism, Crypto-Erasure by Invalidation, destroys a per-record payload key and removes the record's link to the patient, while retaining the accessor's identity, event metadata, a hiding commitment and a logged invalidation entry in a tamper-evident log.

Both results are demonstrated in a Python sandbox over two hundred records with Synthea-generated FHIR R4 payloads: ninety-five violations across ninety records under plaintext semantics, and none under accountability-preserving semantics. Thirty-nine of the violations arise in access-log records that received no erasure request, but only on a contestable reading of Article 68(12), the broad reading, and only for logs kept at patient-record granularity.

The contribution is bounded: no novel cryptographic primitive or formal method, informal proofs, simulated key destruction, and two interpretive steps without regulatory authority. The thesis offers a formal characterisation of the conflict, a minimal semantic move that dissolves it, an executable witness, and an integration analysis against Norwegian infrastructure.

*Keywords:* European Health Data Space; GDPR Article 17; cryptographic erasure; audit trail; data retention; design science research; Secure Processing Environment; MyHealth@EU; information logistics; Norway

Supervisor: Prof. João Ferreira. Artefact: https://github.com/Astheno-sphere/TRF. Demonstration: https://trfhimolde.streamlit.app/

---

## Sammendrag

Forordning (EU) 2025/327 om det europeiske helsedataområdet (EHDS) underlegger revisjonsspor for grensekryssende helsedata tre lagringsplikter samtidig: minstekrav til lagring av revisjonslogger (ti år slik det er rapportert for MyHealth@EU under eHDSI-baselinen og ett år for tilgangslogger i sikre analyserom etter artikkel 73(1)(e)), retten til sletting etter GDPR artikkel 17, og en sletteplikt på seks måneder etter artikkel 68(12). Ingen rettsakt forener disse, og gjennomføringsrettsaktene som skal fastsette kravene til sikre analyserom skal ikke foreligge før 26. mars 2027.

Oppgaven utvikler Tri-Lateral Retention Feasibility (TRF)-modellen, en betingelsesbasert formulering der semantikken for revisjonsverifiserbarhet er en eksplisitt parameter. Under semantikk der en post er verifiserbar bare så lenge innholdet er lesbart i klartekst, er kravene uforenlige så snart en slettefrist eller en sletteplikt faller innenfor lagringsperioden (proposisjon 1). Under semantikk som bevarer etterrettelighet, kan kravene tilfredsstilles samtidig for alle tidspunkter for slettebegjæringer og utløp av tillatelser og for alle lagringsminimum (proposisjon 2). To resultater til avgrenser konflikten: en øvre grense kolliderer med et lagringsminimum bare når den ikke er lengre enn minimumet, og hendelsen grensen regnes fra avgjør om kollisjonen kan ses i teksten eller bare i den enkelte postens historikk (proposisjon 3); å flytte en post ut av det regulerte miljøet oppfyller sletteplikten, men ikke retten til sletting (proposisjon 4). Mekanismen som viser dette, Crypto-Erasure by Invalidation, ødelegger nøkkelen til innholdet i hver enkelt post og fjerner postens kobling til pasienten, samtidig som identiteten til den som ga seg tilgang, hendelsesmetadata, en skjulende forpliktelse (commitment) og en logget ugyldiggjøringspost beholdes i en manipulasjonssikker logg.

Begge resultatene demonstreres i en Python-sandkasse med to hundre poster og syntetiske FHIR R4-data generert med Synthea: nittifem brudd fordelt på nitti poster under klartekstsemantikk, og ingen under semantikk som bevarer etterrettelighet. Trettini av bruddene oppstår i tilgangslogger uten noen slettebegjæring, men bare under en omstridt, vid lesing av artikkel 68(12), og bare for logger som føres på nivå med den enkelte pasientjournal.

Bidraget er avgrenset: ingen nye kryptografiske primitiver eller formelle metoder, uformelle bevis, simulert nøkkelødeleggelse og to tolkningssteg uten støtte i rettskilder. Oppgaven gir en formell beskrivelse av konflikten, et minimalt semantisk grep som løser den, et kjørbart vitnebyrd og en analyse av hvordan mekanismen kan integreres i norsk infrastruktur.

*Nøkkelord:* europeisk helsedataområde; GDPR artikkel 17; kryptografisk sletting; revisjonsspor; lagringstid; design science-forskning; sikkert analyserom; MyHealth@EU; informasjonslogistikk; Norge

---

## Statement of Contribution

This thesis makes four contributions, each stated at the level it can be defended.

*1. A formal model of the tri-lateral retention conflict.* The TRF Model expresses audit-retention floors, the erasure right, and the deletion ceiling as constraints over a single binary variable per record, with verifiability semantics as an explicit parameter. The method of formalising legal compliance as satisfiability is established in the literature and is not claimed here; its application to a retention system combining floors, a right, and a ceiling, and the isolation of verifiability as the parameter determining feasibility, are new to the reviewed literature.

*2. Feasibility results with an executable witness.* Proposition 1 establishes infeasibility under the semantics of an audit log that keeps its payload readable. Proposition 2 establishes satisfiability under an alternative and exhibits the trajectory achieving it. Both are proved informally and demonstrated executably, with an independent exhaustive cross-check. Proposition 3 states the exact condition under which a ceiling collides with a floor and shows that the ceiling's anchor decides whether the collision can be read from the text; Proposition 4 shows why relocating a record, the rival that removes it from the environment, does not dissolve the conflict.

*3. A mechanism specification with its residue analysed against the applicable legal threshold.* Crypto-Erasure by Invalidation is specified in implementable detail, with each record's metadata partitioned into the accessor's fields, which accountability requires and the mechanism retains, and the link to the patient, which it removes, and with entries committed to a tamper-evident log whose inclusion proofs the demonstration checks. Its surviving residue is characterised as pseudonymised rather than anonymous by the Norwegian standard, and designed to the corridor established by the European Data Protection Board's finalised Guidelines 02/2025.

*4. An integration analysis against verified Norwegian infrastructure.* The mechanism is placed at the audit-repository step of the MyHealth@EU flow and the access-logging boundary of a Secure Processing Environment, and requires of the substrate nothing that the national criteria put to public hearing in 2025 do not already demand.

*What is not claimed.* No novel cryptographic primitive or construction. No novel formal method. No first-ever framework for anything. No deployed system, no performance result, no connection to any National Contact Point. No proof that key destruction occurred, as distinct from an attestation that it did. No empirical estimate of how often the conflict arises in practice. No regulatory authority for either of the two interpretive steps the argument depends upon, both of which are identified in Chapter 6 and proposed for resolution in Chapter 7.

---

## Declaration of Originality

This thesis is my own work. Where the work of others is used, it is cited. Where an argument originates in the supervisory relationship or in feedback on drafts, that is noted in the text.

Two declarations are made explicitly.

*Ethics.* This research involved no human participants, no interviews, no surveys, no observation of persons, and no personal data of any kind. All data used are synthetic, generated by Synthea, and describe no real individual. No approval from the Norwegian Agency for Shared Services in Education and Research, from any regional research-ethics committee, or from any institutional review board was required for this work, and none was sought or obtained.

*Sources.* Every factual claim in this thesis is traceable to a source retrievable at the time of writing. Where verification of a source remains incomplete, the text says so. An earlier draft of this project, discarded in May 2026, contained citations to works that do not exist and a statement of ethics approval that was never obtained; every citation in the present work has been checked against a primary or retrievable source.

*Use of AI assistance.* Anthropic's Claude was used throughout this project as a research and drafting assistant: for literature search and source verification, for critique of the author's arguments, for drafting and redrafting prose to the author's direction, and for writing the Python code in Appendix A. All design decisions, the model's formulation, the interpretive legal arguments, and the acceptance or rejection of every suggestion are the author's own, and the author is answerable for the whole. This declaration is made in the form the institution's guidance requires and should be read alongside it.

---

## Nomenclature and Abbreviations

*Model notation*

| Symbol | Meaning |
|---|---|
| *a* | An audit record |
| *m*(*a*) | Event metadata — actor, contact point, patient pseudonym, document category, legal basis, outcome |
| *p*(*a*) | Personal-data payload of the record |
| *c*(*a*) | Hiding commitment to the payload, *c* = Commit(*p*, *r*) |
| *r*(*a*) | Per-record commitment salt |
| *k*(*a*) | Payload key |
| *ι*(*a*) | Invalidation entry — month, legal ground, authorising actor |
| *t*(*a*) | Month in which the access event occurred |
| *F*(*a*) | Retention floor, in months (120 cross-border; 12 for SPE access logs) |
| *σ*(*a*) | Pathway: primary or secondary |
| *t*ᵣ(*a*) | Month an erasure request arrives (∞ if none) |
| *t*π(*a*) | Month a data permit expires (∞ if not applicable) |
| *t*ᴵ(*a*) | Invalidation month, min(*t*ᵣ + δ, *t*π + 6) |
| δ | Erasure response period, in months (GDPR Art. 12(3)) |
| *α*(*a*, *t*) | Payload accessibility at month *t* — 1 if recoverable, 0 otherwise |
| *V*(*a*, *t*) | Whether the record counts as verifiable at month *t* |
| *V*ᴵ, *V*ᴵᴵ | Verifiability under Semantics I (plaintext) and Semantics II (accountability-preserving) |
| C1, C2, C3 | Retention floor, erasure right, and deletion ceiling constraints |

*Abbreviations*

| Term | Expansion |
|---|---|
| ATNA | Audit Trail and Node Authentication (IHE integration profile) |
| CEF | Coordinated Enforcement Framework (EDPB) |
| DSR | Design Science Research |
| EDPB | European Data Protection Board |
| EEA | European Economic Area |
| EEHRxF | European Electronic Health Record Exchange Format |
| eHDSI | eHealth Digital Service Infrastructure |
| eHMSEG | eHealth Member States Expert Group |
| eHOMB | eHealth Operational Management Board |
| EHDS | European Health Data Space |
| FHIR | Fast Healthcare Interoperability Resources (HL7) |
| GDPR | General Data Protection Regulation (EU) 2016/679 |
| HDAB | Health Data Access Body |
| HSM | Hardware Security Module |
| IHE | Integrating the Healthcare Enterprise |
| NCPeH | National Contact Point for eHealth |
| NHN | Norsk Helsenett SF |
| NIST | National Institute of Standards and Technology (US) |
| NORTRE | Norwegian Trusted Research Environments |
| OpenNCP | Open National Contact Point software stack |
| PoSE | Proof of Secure Erasure |
| SoK | Systematization of Knowledge |
| SPE | Secure Processing Environment |
| SPUHiN | Secure Provision and Use of Health Data in Norway (project) |
| TEHDAS2 | Towards European Health Data Space, Joint Action 2 |
| TRF | Tri-Lateral Retention Feasibility (Model) |
| zk-SNARK | Zero-Knowledge Succinct Non-Interactive Argument of Knowledge |

*A note on the project name.* This work has been presented in preliminary form under the name VERA-SNARK, which originates in an earlier design iteration that envisaged zero-knowledge succinct arguments as the enforcement machinery. The design-science process showed that the audit-trail retention problem requires no such machinery, and the mechanism specified here contains none. The name is retained for continuity with that earlier presentation, and the evolution is discussed in Chapter 1, Section 1.6. Chapter 7, Section 7.5 identifies the distinct problem for which zero-knowledge arguments do become necessary.

---

## Table of Contents

**Chapter 1. Introduction**

- 1.1 Background and Context
- 1.2 Problem Statement
- 1.3 Research Objectives and Questions
- 1.4 Significance and Relevance
- 1.5 Scope and Out-of-Scope
- 1.6 Methodological Approach
- 1.7 Thesis Structure

**Chapter 2. Literature Review and Theoretical Foundation**

- 2.1 Review Protocol
- 2.2 The Cross-Border Health Data Exchange Landscape
- 2.3 The Audit-Retention versus Right-to-Erasure Tension
- 2.4 Cryptographic Approaches to Audit Compliance
- 2.5 Formal Approaches to Regulatory-Compliance Verification
- 2.6 Norwegian Secondary-Use Infrastructure
- 2.7 Information Logistics Framing
- 2.8 Comparative Analysis
- 2.9 Identified Research Gaps
- 2.10 Conceptual Positioning of the Thesis

**Chapter 3. Methodology and Research Design**

- 3.1 Research Paradigm
- 3.2 The Design Science Cycle Adopted
- 3.3 The Specification-and-Demonstration Variant, Extended with Formal Modelling
- 3.4 Formal-Modelling Methodology
- 3.5 Synthetic Data
- 3.6 Sandbox Implementation Approach
- 3.7 Validity, Reliability, and Limitations
- 3.8 Evaluation Design for the Next Cycle
- 3.9 Ethical Considerations

**Chapter 4. The Tri-Lateral Retention Feasibility Model and the Crypto-Erasure by Invalidation Mechanism**

- 4.1 Purpose and Structure of the Chapter
- 4.2 What Must Be Retained: The Necessity Analysis
- 4.3 The Model: Objects and Notation
- 4.4 The Three Constraints
- 4.5 Two Semantics of Verifiability
- 4.6 Propositions 1 and 3: Infeasibility, and Where the Ceiling Is Anchored
- 4.7 Proposition 2: Feasibility under Accountability-Preserving Verifiability
- 4.8 The Mechanism: Crypto-Erasure by Invalidation
- 4.9 Residue Analysis
- 4.10 Rival Designs and Proposition 4
- 4.11 Integration with the Norwegian Infrastructure
- 4.12 Summary

**Chapter 5. Demonstration**

- 5.1 Purpose and Claim
- 5.2 Implementation
- 5.3 Results under Semantics I
- 5.4 Corollary 1.2: Infeasibility Without an Erasure Request
- 5.5 Independent Cross-Check
- 5.6 Witness at the Extended Response Period
- 5.7 Results under Semantics II
- 5.8 What the Demonstration Establishes, and What It Does Not

**Chapter 6. Discussion**

- 6.1 What the Thesis Establishes
- 6.2 The Authority Problem
- 6.3 Key Destruction and the Limits of Assurance
- 6.4 The Cost Objection
- 6.5 Scalability
- 6.6 Evaluation Design and the Role of Stakeholder Assessment
- 6.7 Synthetic Data and the Limits of the Demonstration
- 6.8 Implications for Practice and Policy
- 6.9 Theoretical Implications
- 6.10 Where the Ceiling Is Anchored: a Cross-Sector Test
- 6.11 Boundaries as Contribution
- 6.12 Summary

**Chapter 7. Conclusion**

- 7.1 The Problem and the Answer
- 7.2 Contributions
- 7.3 What the Thesis Does Not Establish
- 7.4 The Two Open Questions of Authority
- 7.5 Future Work
- 7.6 Closing

**References**

**Appendix A. Code Artefacts and Reproduction Record**

- A.1 Availability
- A.2 Contents
- A.3 Environment and generation provenance
- A.4 Software environment
- A.5 Exact commands
- A.6 What the code does
- A.7 Data provenance
- A.8 Integrity record
- A.9 Known limitations of the artefact
- A.10 Source listing: `trf_checker.py`
- A.11 Source listing: `synthea_layer.py`
- A.12 Source listing: `norwegian_layer.py`
- A.13 Source listing: `cross_sector_check.py`
- A.14 Source listing: `app.py`
- A.15 Source listing: `crypto_envelope.py`
- A.16 Console output of the reported run
- A.17 Console output of the payload-provenance comparison, full cohort
- A.18 Console output of the erasure-response-period witness
- A.19 Console output of the Norwegian context module
- A.20 Console output of the cross-sector instance
- A.21 Console output of the payload-provenance comparison, committed subset
- A.22 Console output of the envelope-encryption module

**Appendix B. Search Query Log**

**Appendix C. Expert Evaluation Instrument**

- C.1 Purpose and status
- C.2 Panel composition
- C.3 Session structure
- C.4 Demonstration script
- C.5 Semi-structured interview guide
- C.6 Closed-response questionnaire
- C.7 Analysis
- C.8 Data protection, if executed
