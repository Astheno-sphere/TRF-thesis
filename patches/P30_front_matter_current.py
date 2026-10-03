# P30 — front matter brought level with the body after P01–P29. Sammendrag "teorem" -> "proposisjon"
# (D-18 renamed the theorems); Abstract, Sammendrag and Statement of Contribution now carry
# Propositions 3-4, the accessor/patient-link partition (D-16), the tamper-evident log, and the
# conditional statement of Corollary 1.2 (broad reading, patient-record granularity).
FM = "Front_Matter_v1.md"
EDITS = [
    # ---- Abstract
    dict(id="P30-01", file=FM,
         old="for every arrival pattern of erasure requests and permit expiries and for every retention floor (Proposition 2). The witnessing mechanism, Crypto-Erasure by Invalidation, destroys a per-record payload key while retaining event metadata, a hiding commitment and a logged invalidation entry.",
         new="for every arrival pattern of erasure requests and permit expiries and for every retention floor (Proposition 2). Two further results locate the conflict: a ceiling collides with a floor only if it is no longer than the floor, and the event the ceiling is anchored to decides whether the collision is visible in the text or only in each record's history (Proposition 3); moving a record out of the regulated environment satisfies the ceiling but not the right to erasure (Proposition 4). The witnessing mechanism, Crypto-Erasure by Invalidation, destroys a per-record payload key and removes the record's link to the patient, while retaining the accessor's identity, event metadata, a hiding commitment and a logged invalidation entry in a tamper-evident log.",
         why="PRES-4/MIN: abstract level with Ch4 (Props 3-4, D-16 partition, Merkle log)"),
    dict(id="P30-02", file=FM,
         old="Thirty-nine of the violations arise in access-log records that received no erasure request, but only on a contestable reading of Article 68(12).",
         new="Thirty-nine of the violations arise in access-log records that received no erasure request, but only on a contestable reading of Article 68(12), the broad reading, and only for logs kept at patient-record granularity.",
         why="Corollary 1.2 stated with both of its conditions (D-16)"),
    # ---- Sammendrag
    dict(id="P30-03", file=FM,
         old="så snart en slettefrist eller en sletteplikt faller innenfor lagringsperioden (teorem 1).",
         new="så snart en slettefrist eller en sletteplikt faller innenfor lagringsperioden (proposisjon 1).",
         why="D-18 rename carried into the Norwegian summary"),
    dict(id="P30-04", file=FM,
         old="for alle tidspunkter for slettebegjæringer og utløp av tillatelser og for alle lagringsminimum (teorem 2). Mekanismen som viser dette, Crypto-Erasure by Invalidation, ødelegger nøkkelen til innholdet i hver enkelt post, samtidig som hendelsesmetadata, en skjulende forpliktelse (commitment) og en logget ugyldiggjøringspost beholdes.",
         new="for alle tidspunkter for slettebegjæringer og utløp av tillatelser og for alle lagringsminimum (proposisjon 2). To resultater til avgrenser konflikten: en øvre grense kolliderer med et lagringsminimum bare når den ikke er lengre enn minimumet, og hendelsen grensen regnes fra avgjør om kollisjonen kan ses i teksten eller bare i den enkelte postens historikk (proposisjon 3); å flytte en post ut av det regulerte miljøet oppfyller sletteplikten, men ikke retten til sletting (proposisjon 4). Mekanismen som viser dette, Crypto-Erasure by Invalidation, ødelegger nøkkelen til innholdet i hver enkelt post og fjerner postens kobling til pasienten, samtidig som identiteten til den som ga seg tilgang, hendelsesmetadata, en skjulende forpliktelse (commitment) og en logget ugyldiggjøringspost beholdes i en manipulasjonssikker logg.",
         why="D-18 rename; Sammendrag level with the Abstract"),
    dict(id="P30-05", file=FM,
         old="Trettini av bruddene oppstår i tilgangslogger uten noen slettebegjæring, men bare under en omstridt lesing av artikkel 68(12).",
         new="Trettini av bruddene oppstår i tilgangslogger uten noen slettebegjæring, men bare under en omstridt, vid lesing av artikkel 68(12), og bare for logger som føres på nivå med den enkelte pasientjournal.",
         why="Corollary 1.2 conditions, Norwegian"),
    # ---- Statement of Contribution
    dict(id="P30-06", file=FM,
         old="*2. Two feasibility results with an executable witness.* Proposition 1 establishes infeasibility under the semantics implicit in current audit practice. Proposition 2 establishes satisfiability under an alternative and exhibits the trajectory achieving it. Both are proved informally and demonstrated executably, with an independent exhaustive cross-check.",
         new="*2. Feasibility results with an executable witness.* Proposition 1 establishes infeasibility under the semantics implicit in current audit practice. Proposition 2 establishes satisfiability under an alternative and exhibits the trajectory achieving it. Both are proved informally and demonstrated executably, with an independent exhaustive cross-check. Proposition 3 states the exact condition under which a ceiling collides with a floor and shows that the ceiling's anchor decides whether the collision can be read from the text; Proposition 4 shows why relocating a record, the rival that removes it from the environment, does not dissolve the conflict.",
         why="Props 3-4 claimed at the level Ch4 defends them"),
    dict(id="P30-07", file=FM,
         old="*3. A mechanism specification with its residue analysed against the applicable legal threshold.* Crypto-Erasure by Invalidation is specified in implementable detail.",
         new="*3. A mechanism specification with its residue analysed against the applicable legal threshold.* Crypto-Erasure by Invalidation is specified in implementable detail, with each record's metadata partitioned into the accessor's fields, which accountability requires and the mechanism retains, and the link to the patient, which it removes, and with entries committed to a tamper-evident log whose inclusion proofs the demonstration checks.",
         why="D-16 partition and Merkle log in the contribution statement"),
]
