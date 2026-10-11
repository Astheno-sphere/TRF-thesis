# P66 — Round 5 legal (Jo R5[9], authorised by Tiger to add if it strengthens):
#  P66-01  Two short paragraphs added to the end of 4.2:
#          (1) the accessor fields are the professionals'/researchers' own personal data; their Art 17
#              right does not empty the log because Art 17(3)(b) covers retention necessary for the audit
#              obligation, and what necessity does not protect goes at the terminal transition.
#          (2) which controller bears the erasure duty: Commission Implementing Decision (EU) 2019/1765
#              Art 7 makes the Member States' national authorities the controllers and the Commission a
#              processor with no access to patients' data; so the duty lands on the NCPeH's national authority.
#  P66-02  Bibliography entry for the Decision added to the Chapter 4 reference list (assemble.py propagates
#          it to the consolidated bibliography). OJ L 270 and the ELI are certain; the exact page range is to
#          be confirmed by Tiger at EUR-Lex (primary not reachable this session) — start page given, verifiable
#          via the ELI link.
EDITS = [
 dict(id='P66-01', file='Chapter4_TRF_Model_v1.md',
   old=r"""The residue left by the mechanism must therefore be analysed against that threshold rather than assumed to clear it, which is the work of Section 4.9.""",
   new=r"""The residue left by the mechanism must therefore be analysed against that threshold rather than assumed to clear it, which is the work of Section 4.9.

*The accessor's own rights.* The accessor fields are themselves personal data of the health professional or researcher who acted, and those persons hold their own Article 17 right in respect of them. That right does not empty the audit log, for the same reason the payload analysis turns on necessity: retaining the accessor's identity, the time, the legal basis and the outcome is necessary for compliance with the audit-retention obligation of Article 73(1)(e) and the eHDSI baseline, so Article 17(3)(b) GDPR exempts that retention for the length of the floor. What necessity does not protect is not kept: the accessor fields are destroyed at the terminal transition once the retention obligation lapses (Section 4.8).

*Which controller bears the duty.* The erasure duty falls on a definite controller, and the cross-border architecture names it. Commission Implementing Decision (EU) 2019/1765, which lays down the rules for the eHealth Digital Service Infrastructure and is incorporated into the EEA Agreement, makes the participating Member States, through their national authorities or designated bodies, the controllers of the personal data they process through the infrastructure, and requires them to allocate responsibilities between themselves; the Commission is a processor only and "shall not have access to patients' personal data" (European Commission, 2019, Article 7). The controller of a given National Contact Point's audit repository is therefore that point's own national authority, not the Commission, and it is that authority on which an Article 17 request lands and on which the Article 17(3)(b) necessity analysis of this section operates. For a Norwegian-held cross-border audit record that authority is the operator of the Norwegian NCPeH (Section 4.11).""",
   why="Jo R5[9](1) accessor rights via Art 17(3)(b); (2) controller identified via Implementing Decision 2019/1765 Art 7"),

 dict(id='P66-02', file='Chapter4_TRF_Model_v1.md',
   old=r"""European Data Protection Board. (2026b). *Guidelines 02/2025 on processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB. https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf""",
   new=r"""European Commission. (2019). *Commission Implementing Decision (EU) 2019/1765 of 22 October 2019 laying down the rules for the establishment, management and functioning of the network of national authorities responsible for eHealth, and repealing Implementing Decision (EU) 2015/1302*. Official Journal of the European Union, L 270, 83. http://data.europa.eu/eli/dec_impl/2019/1765/oj

European Data Protection Board. (2026b). *Guidelines 02/2025 on processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB. https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf""",
   why="bibliography entry for 2019/1765 (Ch4 list; assemble propagates to consolidated)"),
]
LOST_OK = []
