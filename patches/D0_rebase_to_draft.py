# D0: rebase the working copy onto the draft Joao reviewed (Master_thesis_Abbasia_tracked_JF.docx, tracked changes rejected).
# Content differences only. Not ported (Word/template rendering, not content): title page and TOC layout, chapter reference-list variants
# (the draft carries one consolidated bibliography), maths spacing, Appendix A code-listing line wrapping and comment rendering.
EDITS = [{'file': 'Front_Matter_v1.md',
  'id': 'D0-01',
  'new': 'The European Health Data Space Regulation (EU) 2025/327 subjects cross-border health data audit records to three retention obligations at once: audit-retention floors (ten years for MyHealth@EU audit '
         'repositories under the eHDSI deployment baseline, and one year for Secure Processing Environment access logs under Article 73(1)(e)), the right to erasure under Article 17 GDPR, and the six-month deletion '
         'ceiling of Article 68(12). No instrument reconciles them, and the implementing acts that must specify Secure Processing Environment requirements are not due until 26 March 2027.\n'
         '\n'
         'The thesis develops the Tri-Lateral Retention Feasibility (TRF) Model, a constraint-satisfaction formulation in which the semantics of audit verifiability is an explicit parameter. Under '
         'plaintext-verifiability semantics the constraints are infeasible whenever an erasure or deletion deadline falls inside a retention window (Theorem 1). Under accountability-preserving semantics they are '
         'jointly satisfiable for every arrival pattern of erasure requests and permit expiries and for every retention floor (Theorem 2). The witnessing mechanism, Crypto-Erasure by Invalidation, destroys a per-record '
         'payload key while retaining event metadata, a hiding commitment and a logged invalidation entry.\n'
         '\n'
         'Both results are demonstrated in a Python sandbox over two hundred records with Synthea-generated FHIR R4 payloads: ninety-five violations across ninety records under plaintext semantics, and none under '
         'accountability-preserving semantics. Thirty-nine of the violations arise in access-log records that received no erasure request, but only on a contestable reading of Article 68(12).\n'
         '\n'
         'The contribution is bounded: no novel cryptographic primitive or formal method, informal proofs, simulated key destruction, and two interpretive steps without regulatory authority. The thesis offers a formal '
         'characterisation of the conflict, a minimal semantic move that dissolves it, an executable witness, and an integration analysis against Norwegian infrastructure.\n'
         '\n'
         '*Keywords:* European Health Data Space; GDPR Article 17; cryptographic erasure; audit trail; data retention; design science research; Secure Processing Environment; MyHealth@EU; information logistics; Norway\n'
         '\n'
         'Supervisor: Prof. João Ferreira. Artefact: https://github.com/Astheno-sphere/TRF. Demonstration: https://trfhimolde.streamlit.app/\n'
         '\n'
         '---\n'
         '\n'
         '## Sammendrag\n'
         '\n'
         'Forordning (EU) 2025/327 om det europeiske helsedataområdet (EHDS) underlegger revisjonsspor for grensekryssende helsedata tre lagringsplikter samtidig: minstekrav til lagring av revisjonslogger (ti år for '
         'MyHealth@EU under eHDSI-baselinen og ett år for tilgangslogger i sikre analyserom etter artikkel 73(1)(e)), retten til sletting etter GDPR artikkel 17, og en sletteplikt på seks måneder etter artikkel 68(12). '
         'Ingen rettsakt forener disse, og gjennomføringsrettsaktene som skal fastsette kravene til sikre analyserom skal ikke foreligge før 26. mars 2027.\n'
         '\n'
         'Oppgaven utvikler Tri-Lateral Retention Feasibility (TRF)-modellen, en betingelsesbasert formulering der semantikken for revisjonsverifiserbarhet er en eksplisitt parameter. Under semantikk der en post er '
         'verifiserbar bare så lenge innholdet er lesbart i klartekst, er kravene uforenlige så snart en slettefrist eller en sletteplikt faller innenfor lagringsperioden (teorem 1). Under semantikk som bevarer '
         'etterrettelighet, kan kravene tilfredsstilles samtidig for alle tidspunkter for slettebegjæringer og utløp av tillatelser og for alle lagringsminimum (teorem 2). Mekanismen som viser dette, Crypto-Erasure by '
         'Invalidation, ødelegger nøkkelen til innholdet i hver enkelt post, samtidig som hendelsesmetadata, en skjulende forpliktelse (commitment) og en logget ugyldiggjøringspost beholdes.\n'
         '\n'
         'Begge resultatene demonstreres i en Python-sandkasse med to hundre poster og syntetiske FHIR R4-data generert med Synthea: nittifem brudd fordelt på nitti poster under klartekstsemantikk, og ingen under '
         'semantikk som bevarer etterrettelighet. Trettini av bruddene oppstår i tilgangslogger uten noen slettebegjæring, men bare under en omstridt lesing av artikkel 68(12).\n'
         '\n'
         'Bidraget er avgrenset: ingen nye kryptografiske primitiver eller formelle metoder, uformelle bevis, simulert nøkkelødeleggelse og to tolkningssteg uten støtte i rettskilder. Oppgaven gir en formell '
         'beskrivelse av konflikten, et minimalt semantisk grep som løser den, et kjørbart vitnebyrd og en analyse av hvordan mekanismen kan integreres i norsk infrastruktur.\n'
         '\n'
         '*Nøkkelord:* europeisk helsedataområde; GDPR artikkel 17; kryptografisk sletting; revisjonsspor; lagringstid; design science-forskning; sikkert analyserom; MyHealth@EU; informasjonslogistikk; Norge',
  'old': 'The European Health Data Space Regulation (EU) 2025/327 places cross-border health data audit records under three kinds of retention obligation simultaneously. Audit-retention floors require records to remain '
         'verifiable for fixed periods: ten years for MyHealth@EU audit repositories under the eHDSI deployment baseline, one year for Secure Processing Environment access logs under Article 73(1)(e). The right to '
         'erasure under Article 17 GDPR may be exercised at any point within those periods. And Article 68(12) EHDS requires data to be deleted from a Secure Processing Environment within six months of the expiry of a '
         'data permit. No instrument reconciles the three, the guidance drafted to implement them does not address their interaction, and the Commission implementing acts that must specify Secure Processing Environment '
         'requirements are not due until 26 March 2027.\n'
         '\n'
         'This thesis formalises that conflict and resolves it by design. It develops the Tri-Lateral Retention Feasibility (TRF) Model, a constraint-satisfaction formulation in which each audit record is decomposed '
         'into event metadata and a committed personal-data payload, the three obligations are expressed as constraints over discretised time, and the semantics of *verifiability* is made an explicit parameter rather '
         'than an inherited assumption. Two results follow. Under plaintext-verifiability semantics, a record is verifiable while its payload remains readable, the constraint system is infeasible whenever an erasure '
         'deadline or a deletion-ceiling deadline falls inside a retention window. Under accountability-preserving semantics, a record is verifiable while its metadata is intact, its commitment survives, and any loss '
         'of payload accessibility is itself logged, grounded, and attributed. Under those semantics the system is jointly satisfiable for every arrival pattern of erasure requests and permit expiries and for every '
         'retention floor.\n'
         '\n'
         'The mechanism that the feasibility proof exhibits, termed Crypto-Erasure by Invalidation, applies the cryptographic-erase technique recognised in NIST SP 800-88 Rev. 2 at the audit-trail boundary. The '
         'per-record key binding a record to its payload is destroyed, while hiding commitments and event metadata are retained. The invalidation is appended to the audit trail as a first-class witnessed event, and a '
         'terminal transition at floor expiry discharges the storage-limitation obligation on the metadata itself.\n'
         '\n'
         'Both results are demonstrated in a Python sandbox over two hundred records drawn from Synthea-generated FHIR R4 data. Under plaintext semantics the demonstration produces ninety-five constraint violations '
         'across ninety records; under accountability-preserving semantics it produces none. An independently written exhaustive search over all assignments of payload accessibility confirms that under plaintext '
         'semantics no assignment succeeds. Thirty-nine violations arise in Secure Processing Environment records that received no erasure request at all, through the interaction of Article 73(1)(e) with Article '
         '68(12), a collision internal to a single regulation. That specific result is conditional on a reading of Article 68(12) that the thesis defends at length and marks as contestable; the remaining results, '
         'including the infeasibility theorem itself, do not depend on it.\n'
         '\n'
         'The contribution is bounded. No cryptographic primitive is novel, and the general method of treating legal compliance as a satisfiability problem is established. The proofs are informal rather than '
         'machine-checked, and key destruction is simulated and attested rather than proven. Two interpretive steps at the centre of the argument rest on reasoning rather than on regulatory authority. What the thesis '
         'offers is the formal characterisation of a conflict that the most recent systematisation of the cryptographic-erasure literature names as an open problem, a minimal and principled semantic move that dissolves '
         'it, an executable witness of both results, and an integration analysis against Norwegian infrastructure verified as it currently operates.\n'
         '\n'
         '*Keywords:* European Health Data Space; GDPR Article 17; cryptographic erasure; audit trail; data retention; design science research; Secure Processing Environment; MyHealth@EU; information logistics; '
         'Norway.\n'
         '\n'
         '*(Approx. 520 words.)*',
  'why': 'Abstract as in the draft sent to Joao (shorter rewrite); Norwegian abstract (Sammendrag) and supervisor/artefact line added; "(Approx. 520 words.)" note dropped'},
 {'file': 'Chapter1_Introduction_v2.md',
  'id': 'D0-02',
  'new': "The European Union's health sector is undergoing the most significant data-governance transformation in its history. Regulation (EU) 2025/327",
  'old': "At the emergency clinics in Bodø and Stjørdal, Norway's gateway to European health data exchange has been in production since 2025, connected to Portugal and Czechia. It has served almost no one: the "
         "Directorate of Health's own portfolio reporting notes that no relevant patients had yet presented for the solution to be used in practice (Helsedirektoratet, 2026). That near-empty gateway is where this "
         'thesis starts, because the obligations attaching to each record it will eventually write are already in conflict with one another, and the conflict is easier to see before the volume arrives than after. '
         'Regulation (EU) 2025/327',
  'why': 'Opening as in the draft Joao reviewed. The Bodo/Stjordal hook (H-01) was applied after the draft was sent and is now a proposal (conflict C-1)'},
 {'file': 'Chapter2_LitReview_v2_FINAL.md',
  'id': 'D0-03',
  'new': 'Every query in rounds 1 to 4 is reproduced verbatim, by round, in Appendix B. A fifth round, on 28 September 2026, contained no discovery queries: it verified locators and source standing for entries already '
         'in the bibliography, and is described by target in Appendix B.',
  'old': 'Every query in rounds 1 to 4 is reproduced verbatim, by round, in Appendix B.',
  'why': 'Draft: round 5 (28 Sept) mentioned in s2.1.4'},
 {'file': 'Chapter2_LitReview_v2_FINAL.md',
  'id': 'D0-04',
  'new': 'with hiding commitments and the invalidation registry supplying the verifiability that the practitioner crypto-shredding pattern lacks (accumulator witnesses being a specified but unimplemented optional '
         'layer).',
  'old': 'with hiding commitments and accumulator witnesses supplying the verifiability that the practitioner crypto-shredding pattern lacks.',
  'why': 'Draft: accumulator not implemented'},
 {'file': 'Chapter4_TRF_Model_v1.md',
  'id': 'D0-05',
  'new': "at or before the sixth month of the record's retention window",
  'old': "at or before the eleventh month of the record's retention window",
  'why': 'Draft: Corollary 1.2 month'},
 {'file': 'Chapter4_TRF_Model_v1.md',
  'id': 'D0-06',
  'new': 'Hence $V^{II}(a,t) = 1$ throughout the window. The terminal transition of Section 4.8 takes place after the window and is not part of this trajectory.',
  'old': 'Hence $V^{II}(a,t) = 1$ throughout the window.',
  'why': 'Draft: terminal transition outside the C1 trajectory'},
 {'file': 'Chapter4_TRF_Model_v1.md',
  'id': 'D0-07',
  'new': 'Theorem 2 holds if validity is established by linear scan of the registry, and the accumulator makes that check succinct. The accumulator is specified but not implemented in the artefact (Section 6.1). '
         'Dynamic accumulators of the Camenisch and Lysyanskaya type also require a trusted accumulator manager holding a trapdoor, which adds a trust assumption stated in Section 4.9.',
  'old': 'Theorem 2 holds if validity is established by linear scan of the registry, and the accumulator makes that check succinct.',
  'why': 'Draft: accumulator caveat'},
 {'file': 'Chapter4_TRF_Model_v1.md',
  'id': 'D0-08',
  'new': 'which follows from the accumulator witness where that layer is used, and otherwise from a scan of the registry. What the auditor cannot do',
  'old': 'which follows from the accumulator witness. What the auditor cannot do',
  'why': 'Draft: auditor view without accumulator'},
 {'file': 'Chapter4_TRF_Model_v1.md',
  'id': 'D0-09',
  'new': 'After $t = t(a) + F(a)$, the last month of the closed window on which C1 is defined, the retention obligation lapses',
  'old': 'At $t = t(a) + F(a)$ the retention obligation lapses',
  'why': 'Draft: F+1 window (closed interval spans F+1 months)'},
 {'file': 'Chapter4_TRF_Model_v1.md',
  'id': 'D0-10',
  'new': 'In the first month after the window, $t(a) + F(a) + 1$, the record undergoes a second invalidation',
  'old': 'At floor expiry the record undergoes a second invalidation',
  'why': 'Same'},
 {'file': 'Chapter4_TRF_Model_v1.md',
  'id': 'D0-11',
  'new': 'which the append-only construction makes detectable but not impossible. Where the optional accumulator layer is used, its manager is also trusted, since a party holding the accumulator trapdoor can forge '
         'validity witnesses. And the cryptographic assumption',
  'old': 'which the append-only construction makes detectable but not impossible. And the cryptographic assumption',
  'why': 'Draft: accumulator manager trust'},
 {'file': 'Chapter4_TRF_Model_v1.md', 'id': 'D0-12', 'new': 'Five are treated here', 'old': 'Four are treated here', 'why': 'Draft: five rivals'},
 {'file': 'Chapter4_TRF_Model_v1.md', 'id': 'D0-13', 'new': 'Five rival designs were considered', 'old': 'Four rival designs were considered', 'why': 'Draft: five rivals'},
 {'file': 'Chapter5_Demonstration_v1.md',
  'id': 'D0-14',
  'new': 'reduce to the nine records in this population whose erasure requests fall inside the retention window (four that collide with C2 only and five that also collide with C3; twenty-two records received requests '
         'in all);',
  'old': 'reduce to the twenty-two records in this population that received erasure requests;',
  'why': 'Draft: corrected witness count under the narrow reading'},
 {'file': 'Chapter5_Demonstration_v1.md',
  'id': 'D0-15',
  'new': 'a second, separately written procedure',
  'old': 'a second, independently written procedure',
  'why': 'Draft wording (source of the "an separately" typo Joao flagged)'},
 {'file': 'Chapter5_Demonstration_v1.md',
  'id': 'D0-16',
  'new': 'confirming that the search is capable of returning True and that the infeasibility results are not an artefact of a procedure that never succeeds.\n'
         '\n'
         'This cross-check is separate code, not independent evidence in a stronger sense. It was written in the same AI-assisted process as the main checker and encodes the same constraint definitions from Section '
         '4.4, so it guards against implementation error in the checker and not against error in the model.',
  'old': 'confirming that the search is capable of returning True and that the infeasibility results are not an artefact of a procedure that never succeeds.',
  'why': 'Draft: new paragraph after the cross-check result'},
 {'file': 'Chapter5_Demonstration_v1.md', 'id': 'D0-17', 'new': 'survive an separately written exhaustive search', 'old': 'survive an independently written exhaustive search', 'why': 'Draft wording'},
 {'file': 'Chapter5_Demonstration_v1.md',
  'id': 'D0-18',
  'new': '*How the tables should be read.* The Semantics II result of Table 5.3 holds by construction: the checker derives payload accessibility from the same invalidation month that the trajectory of Theorem 2 '
         'prescribes, so zero violations is the expected outcome, and a failure would expose an implementation error and not a modelling error. The violation rates of Table 5.1 are functions of the generator parameters '
         'in Table 5.0 and are not estimates of real frequency.\n'
         '\n'
         '*Payload provenance, tested rather than assumed.*',
  'old': '*Payload provenance, tested rather than assumed.*',
  'why': 'Draft: new paragraph "How the tables should be read"'},
 {'file': 'Chapter5_Demonstration_v1.md',
  'id': 'D0-19',
  'new': '',
  'old': '---\n'
         '\n'
         '## Appendix A. Checker source and run output\n'
         '\n'
         'The complete source of `trf_checker.py` and the verbatim console output of the run reported in this chapter are reproduced in Appendix A of the thesis. The run is reproduced by executing `python '
         'trf_checker.py` with no arguments; seed 20260915 is set in the module header, and the output is byte-identical across runs.\n'
         '\n'
         '\n',
  'why': 'Draft drops the chapter-level Appendix A stub'},
 {'file': 'Chapter6_Discussion_v1.md', 'id': 'D0-20', 'new': 'and an separately written exhaustive search confirms', 'old': 'and an independently written exhaustive search confirms', 'why': 'Draft wording'},
 {'file': 'Chapter6_Discussion_v1.md',
  'id': 'D0-21',
  'new': 'Two clarifications of status belong here. The terminal transition of Section 4.8 is likewise specified but not implemented in the checker.',
  'old': 'Two clarifications of status belong here.',
  'why': 'Draft: terminal transition not implemented'},
 {'file': 'Chapter6_Discussion_v1.md',
  'id': 'D0-22',
  'new': 'which is textual and, on the narrow reading of Article 68(12), survives in its erasure-driven form, and would still',
  'old': 'which is textual and survives any reading, and would still',
  'why': 'Draft: narrow-reading hedge'},
 {'file': 'Chapter6_Discussion_v1.md',
  'id': 'D0-23',
  'new': 'seeking an opinion on whether accountability-preserving verifiability discharges the retention obligation in Article 73(1)(e). Datatilsynet is the natural addressee for the GDPR-side questions; because '
         'Articles 68 and 73 are provisions of the EHDS Regulation, the Norwegian authorities responsible for its incorporation (Helsedirektoratet and the Ministry of Health and Care Services) and the Commission are '
         'the more appropriate addressees for those.',
  'old': 'seeking an opinion from Datatilsynet on whether accountability-preserving verifiability discharges the retention obligation in Article 73(1)(e).',
  'why': 'Draft: Datatilsynet for GDPR side; EHDS authorities for Arts 68/73'},
 {'file': 'Chapter6_Discussion_v1.md',
  'id': 'D0-24',
  'new': 'The same request, addressed to the authorities responsible for EHDS incorporation, could reasonably carry this one alongside it.',
  'old': 'A request to Datatilsynet on the verifiability question could reasonably carry this one alongside it.',
  'why': 'Same'},
 {'file': 'Chapter6_Discussion_v1.md',
  'id': 'D0-25',
  'new': 'the collision is textual and, on the narrow reading of Article 68(12), survives in its erasure-driven form;',
  'old': 'the collision is textual and survives any reading;',
  'why': 'Draft: narrow-reading hedge'},
 {'file': 'Chapter6_Discussion_v1.md',
  'id': 'D0-26',
  'new': 'The first version of this project, abandoned in May 2026, made broader claims than it could support, as the Declaration of Originality records. The breadth of those claims was what made them fragile: a claim '
         'to have done six things fails if any one of them fails.',
  'old': 'The first version of this project, abandoned in May 2026, claimed six original contributions, a first-ever framework, institutional review board approval that had not been obtained, and a zero-knowledge '
         'architecture that was never built. Its bibliography contained a series of citations to works that do not exist, identified during the audit that led to the rebuild. None of those claims could survive a '
         'determined reader, and the breadth of the claims was precisely what made them fragile: a claim to have done six things fails if any one of them fails.',
  'why': 'Draft: shorter first-version paragraph'},
 {'file': 'Chapter7_Conclusion_v1.md', 'id': 'D0-27', 'new': 'with an separately written exhaustive search confirming', 'old': 'with an independently written exhaustive search confirming', 'why': 'Draft wording'},
 {'file': 'Chapter7_Conclusion_v1.md',
  'id': 'D0-28',
  'new': 'hiding commitments, and, without implementing them, dynamic accumulators) and claims',
  'old': 'hiding commitments, dynamic accumulators) and claims',
  'why': 'Draft: accumulators not implemented'},
 {'file': 'Chapter7_Conclusion_v1.md',
  'id': 'D0-29',
  'new': 'A request to the competent authorities (Datatilsynet on the GDPR side; Helsedirektoratet, the Ministry of Health and Care Services or the Commission on the EHDS side) on whether accountability-preserving '
         'verifiability discharges a retention obligation, and whether Article 68(12) reaches access logs, has a determinate answer.',
  'old': 'A request to Datatilsynet (whether accountability-preserving verifiability discharges a retention obligation, and whether Article 68(12) reaches access logs) has a determinate answer.',
  'why': 'Draft: competent authorities'}]