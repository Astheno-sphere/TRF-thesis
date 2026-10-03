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

The thesis develops the Tri-Lateral Retention Feasibility (TRF) Model, a constraint-satisfaction formulation in which the semantics of audit verifiability is an explicit parameter. Under plaintext-verifiability semantics the constraints are infeasible whenever an erasure or deletion deadline falls inside a retention window (Proposition 1). Under accountability-preserving semantics they are jointly satisfiable for every arrival pattern of erasure requests and permit expiries and for every retention floor (Proposition 2). The witnessing mechanism, Crypto-Erasure by Invalidation, destroys a per-record payload key while retaining event metadata, a hiding commitment and a logged invalidation entry.

Both results are demonstrated in a Python sandbox over two hundred records with Synthea-generated FHIR R4 payloads: ninety-five violations across ninety records under plaintext semantics, and none under accountability-preserving semantics. Thirty-nine of the violations arise in access-log records that received no erasure request, but only on a contestable reading of Article 68(12).

The contribution is bounded: no novel cryptographic primitive or formal method, informal proofs, simulated key destruction, and two interpretive steps without regulatory authority. The thesis offers a formal characterisation of the conflict, a minimal semantic move that dissolves it, an executable witness, and an integration analysis against Norwegian infrastructure.

*Keywords:* European Health Data Space; GDPR Article 17; cryptographic erasure; audit trail; data retention; design science research; Secure Processing Environment; MyHealth@EU; information logistics; Norway

Supervisor: Prof. João Ferreira. Artefact: https://github.com/Astheno-sphere/TRF. Demonstration: https://trfhimolde.streamlit.app/

---

## Sammendrag

Forordning (EU) 2025/327 om det europeiske helsedataområdet (EHDS) underlegger revisjonsspor for grensekryssende helsedata tre lagringsplikter samtidig: minstekrav til lagring av revisjonslogger (ti år slik det er rapportert for MyHealth@EU under eHDSI-baselinen og ett år for tilgangslogger i sikre analyserom etter artikkel 73(1)(e)), retten til sletting etter GDPR artikkel 17, og en sletteplikt på seks måneder etter artikkel 68(12). Ingen rettsakt forener disse, og gjennomføringsrettsaktene som skal fastsette kravene til sikre analyserom skal ikke foreligge før 26. mars 2027.

Oppgaven utvikler Tri-Lateral Retention Feasibility (TRF)-modellen, en betingelsesbasert formulering der semantikken for revisjonsverifiserbarhet er en eksplisitt parameter. Under semantikk der en post er verifiserbar bare så lenge innholdet er lesbart i klartekst, er kravene uforenlige så snart en slettefrist eller en sletteplikt faller innenfor lagringsperioden (teorem 1). Under semantikk som bevarer etterrettelighet, kan kravene tilfredsstilles samtidig for alle tidspunkter for slettebegjæringer og utløp av tillatelser og for alle lagringsminimum (teorem 2). Mekanismen som viser dette, Crypto-Erasure by Invalidation, ødelegger nøkkelen til innholdet i hver enkelt post, samtidig som hendelsesmetadata, en skjulende forpliktelse (commitment) og en logget ugyldiggjøringspost beholdes.

Begge resultatene demonstreres i en Python-sandkasse med to hundre poster og syntetiske FHIR R4-data generert med Synthea: nittifem brudd fordelt på nitti poster under klartekstsemantikk, og ingen under semantikk som bevarer etterrettelighet. Trettini av bruddene oppstår i tilgangslogger uten noen slettebegjæring, men bare under en omstridt lesing av artikkel 68(12).

Bidraget er avgrenset: ingen nye kryptografiske primitiver eller formelle metoder, uformelle bevis, simulert nøkkelødeleggelse og to tolkningssteg uten støtte i rettskilder. Oppgaven gir en formell beskrivelse av konflikten, et minimalt semantisk grep som løser den, et kjørbart vitnebyrd og en analyse av hvordan mekanismen kan integreres i norsk infrastruktur.

*Nøkkelord:* europeisk helsedataområde; GDPR artikkel 17; kryptografisk sletting; revisjonsspor; lagringstid; design science-forskning; sikkert analyserom; MyHealth@EU; informasjonslogistikk; Norge

---

## Statement of Contribution

This thesis makes four contributions, each stated at the level it can be defended.

*1. A formal model of the tri-lateral retention conflict.* The TRF Model expresses audit-retention floors, the erasure right, and the deletion ceiling as constraints over a single binary variable per record, with verifiability semantics as an explicit parameter. The method of formalising legal compliance as satisfiability is established in the literature and is not claimed here; its application to a retention system combining floors, a right, and a ceiling, and the isolation of verifiability as the parameter determining feasibility, are new to the reviewed literature.

*2. Two feasibility results with an executable witness.* Proposition 1 establishes infeasibility under the semantics implicit in current audit practice. Proposition 2 establishes satisfiability under an alternative and exhibits the trajectory achieving it. Both are proved informally and demonstrated executably, with an independent exhaustive cross-check.

*3. A mechanism specification with its residue analysed against the applicable legal threshold.* Crypto-Erasure by Invalidation is specified in implementable detail. Its surviving residue is characterised as pseudonymised rather than anonymous by the Norwegian standard, and designed to the corridor established by the European Data Protection Board's finalised Guidelines 02/2025.

*4. An integration analysis against verified Norwegian infrastructure.* The mechanism is placed at the audit-repository step of the MyHealth@EU flow and the access-logging boundary of a Secure Processing Environment, and requires of the substrate nothing that the national criteria put to public hearing in 2025 do not already demand.

*What is not claimed.* No novel cryptographic primitive or construction. No novel formal method. No first-ever framework for anything. No deployed system, no performance result, no connection to any National Contact Point. No proof that key destruction occurred, as distinct from an attestation that it did. No empirical estimate of how often the conflict arises in practice. No regulatory authority for either of the two interpretive steps the argument depends upon, both of which are identified in Chapter 6 and proposed for resolution in Chapter 7.

---

## Declaration of Originality

This thesis is my own work. Where the work of others is used, it is cited. Where an argument originates in the supervisory relationship or in feedback on drafts, that is noted in the text.

Two declarations are made explicitly because the first version of this project, abandoned in May 2026, failed to make them truthfully.

*Ethics.* This research involved no human participants, no interviews, no surveys, no observation of persons, and no personal data of any kind. All data used are synthetic, generated by Synthea, and describe no real individual. No approval from the Norwegian Agency for Shared Services in Education and Research, from any regional research-ethics committee, or from any institutional review board was required for this work, and none was sought or obtained. Any claim to the contrary appearing in earlier drafts of this project is withdrawn.

*Sources.* Every factual claim in this thesis is traceable to a source retrievable at the time of writing. Where verification of a source remains incomplete, the text says so. An audit conducted in May 2026 identified citations in the earlier draft to works that do not exist; that draft has been discarded in its entirety and every citation in the present work has been checked against a primary or retrievable source.

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

## Version and Change Record

This thesis and its artefact are versioned together. The table records what changed, when, and what verified it, so that a reader comparing the document against the published repository can tell which of the two moved if a figure disagrees. The full trail, with an identifier for every individual change, is maintained alongside the artefact.

*Table F.1. Document and artefact versions*

| Date | Document | Artefact | What changed | Verification |
|---|---|---|---|---|
| 16 Sept 2026 | Chapters 1–7 assembled | `trf_checker.py`, `synthea_layer.py` | First complete draft; the checker and the realism layer written and run | Checker output recorded |
| 18 Sept 2026 | Appendix A written | — | Provenance of the synthetic cohort established by inspecting the bundles rather than by recollection | Six Synthea markers confirmed in every bundle |
| 19 Sept 2026 | §5.5a added | `--delta-witness` added | The erasure response period tested at δ = 3 rather than asserted | Table 5.2a produced by execution |
| 21 Sept 2026 | §4.8 terminal transition; mathematics to LaTeX | Salt destroyed with the key | A reviewer-found gap at the end of the record's life closed; 159 equations converted | Checker output unchanged, byte for byte |
| 23 Sept 2026 | — | Repository published | Code and documents pushed to GitHub; demonstration deployed | — |
| 28 Sept 2026 | §5.2 line counts corrected; §6.9a added; Appendix A extended | Eight-bundle subset committed; Tab 5 added; five recorded runs committed | The dataset the thesis reports on made obtainable; the two robustness results given a viewer; the cross-sector instance carried into the discussion | Verified from a fresh clone: checker byte-identical to its recorded run, realism layer 891 bytes and six identical measures |
| 28 Sept 2026 | Bibliography linked | — | Every entry given a DOI or URL that was fetched; two entries removed as documents that do not exist as cited; six citations corrected on year, title or author | 67 of 67 entries carry a locator |

*Table F.2. The artefact at the date of submission*

| Module | Lines | Reports a thesis figure? |
|---|---|---|
| `trf_checker.py` | 533 | Yes — Tables 5.1, 5.2a, 5.3 |
| `synthea_layer.py` | 152 | Yes — Table 5.4 |
| `norwegian_layer.py` | 135 | No — illustrative |
| `cross_sector_check.py` | 110 | No — illustrative, discussed at §6.9a |
| `app.py` | 526 | No — a viewer, never a source |

Repository: https://github.com/Astheno-sphere/TRF · Demonstration: https://trfhimolde.streamlit.app/

Published commits, most recent first:

```text
  0d855a7  28 Sep 2026  Add Tab 5 robustness checks and a recorded run per command
  88840a6  28 Sep 2026  Record R-09 to R-11 and refresh checksums
  cc0d7f3  28 Sep 2026  Appendix A: drop the norwegian/ path prefix
  d79b96f  28 Sep 2026  Ship the Synthea subset and repair the flattened upload
  03048f2  23 Sep 2026  Add files via upload
```

Two corrections are recorded here because they were made against the thesis's own earlier claims rather than in response to a reviewer. An inference dating a source from the age of its web page was withdrawn, the page being updated in place and its age therefore saying nothing about its contents. And a statement that the artefact's code carried a comment recommending a cryptographically secure random source was removed, no such comment existing; the salt's reproducibility-only status is now stated directly instead.

## Table of Contents

1. *Introduction*: background, problem statement, research questions, significance, scope, methodological approach, structure
2. *Literature Review and Theoretical Foundation*: review strategy; cross-border landscape; the audit-retention versus erasure tension; cryptographic approaches; formal approaches to compliance verification; Norwegian secondary-use infrastructure; information-logistics framing; comparative analysis; research gaps; conceptual positioning
3. *Methodology and Research Design*: design science paradigm; the adopted cycle; specification-and-demonstration with formal modelling; formal-modelling methodology; synthetic data; sandbox approach; validity, reliability and limitations; ethics
4. *The Tri-Lateral Retention Feasibility Model and the Crypto-Erasure by Invalidation Mechanism*: necessity analysis; model and notation; constraints; two semantics; Proposition 1 and corollaries; Proposition 2; mechanism specification; residue analysis; rival designs; Norwegian integration
5. *Demonstration*: implementation; results under each semantics; Corollary 1.2 witnesses; independent cross-check; payload-provenance comparison; what is and is not established
6. *Discussion*: what the thesis establishes; the authority problems; key destruction and assurance; the cost objection; synthetic data; practice and policy; theoretical implications; boundaries as contribution
7. *Conclusion*: problem and answer; contributions; limitations; open questions of authority; future work

*Appendix A*: Code artefacts, reproduction commands, data provenance, integrity record, full source of all five modules and the recorded console run of every command

*Appendix B*: Search query log: 59 queries across four dated search rounds, a fifth round of 18 locator verifications, round purposes and coverage notes

*Appendix C*: Expert evaluation instrument: panel composition, session structure, demonstration script, semi-structured interview guide, closed-response questionnaire, analysis plan
