# Research log, October 2026 (candidate round for Appendix B)

Every lookup made while answering the 30 Sept review. Appendix B's round structure will be
re-judged together with the fork's rounds (Wave −1, R1) before any of this enters the appendix;
until then this file is the record. "Fetch" = WebFetch (page converted to text and read by a
summarising model); anything quoted from a fetch of a long PDF was cross-checked by a second
fetch and is flagged where the fetches disagreed.

## 3 October 2026

| # | Kind | Query or URL | Outcome | Used in |
|---|---|---|---|---|
| 1 | search | EHDS Article 68(12) secure processing environment deletion six months Article 73 logs one year conflict | No source treating the collision. Regulation text, TEHDAS D7.1, law-firm series only | gap check |
| 2 | search | crypto-shredding audit log verifiable erasure retention conflict GDPR 2026 arXiv | Practitioner crypto-shredding only (VeritasChain, blogs) | gap check |
| 3 | search | "crypto-erasure" OR "cryptographic erasure" health data audit trail retention floor erasure ceiling formal model | Aikebaier SoK (ePrint 2026/1109), practitioner material | gap check |
| 4 | search | EHDS implementing act secure processing environment Article 73(5) draft consultation 2026 | D7.4 (Zenodo 20266473); Sidley Apr 2026; EDPS formal comments Jan 2026. No SPE implementing act found | currency |
| 5 | search | TEHDAS2 D7.4 secure processing environment logging requirements retention access logs | M7.4 draft (Sept 2025) PDF; D7.3 | M1, D-16 |
| 6 | search | eHDSI MyHealth@EU audit trail retention 10 years NCPeH security policy audit log | No primary eHDSI document reached (M5a still open) | M5a |
| 7 | fetch | zenodo.org/records/20266473 | D7.4 metadata: v1, 24 Feb 2026, 17 contributors | bibliography check |
| 8 | fetch | goodlifesci.sidley.com 2026/04/14 EHDS–GDPR part 2 | Does not discuss 68(12), 73(1)(e) or log retention | gap check |
| 9 | search | arXiv 2026 European Health Data Space audit logs erasure right retention verifiable deletion SPE | Nothing on point | gap check |
| 10 | fetch | eprint.iacr.org/2026/1109 | Aikebaier, single author (Nexum Ledger), submitted 30 May 2026, preprint; open problem 5 "erasure under multi-regime retention conflict" | Ch1 corroboration |
| 11 | fetch | streamlex.eu EHDS Art 2 | Art 2(2)(a), (c) verbatim | D-16, P04 |
| 12 | fetch | streamlex.eu EHDS Art 73 | Art 73(1) chapeau, (a), (c), (e) verbatim | D-16, P04 |
| 13 | fetch | streamlex.eu EHDS Art 68 | Art 68(12) verbatim, whole paragraph | D-16, P04 |
| 14 | fetch | streamlex.eu EHDS Art 19 | Art 19(1); inform Commission by 26 March 2027 | P03 |
| 15 | fetch | streamlex.eu EHDS Art 105 | Application dates 2027 / 2029 / 2031; Chapter IV 2029 | P03 |
| 16 | fetch | profiles.ihe.net ITI TF-2 ITI-55 | Rev 20.1, 12 Dec 2024. §3.55.4.1.2.1 name and birth time required unless LivingSubjectId; §3.55.5.1 ParticipantObjectQuery = QueryByParameter, base64 | M1, P04 |
| 17 | fetch | profiles.ihe.net ITI-38, ITI-39 | Audit by reference to ITI-18 / ITI-43; field content not in the fetched text. Not used | — |
| 18 | search | tehdas.eu D7.4 technical specification … pdf | TEHDAS news item, 5 June 2026, with the final PDF link | D7.4 |
| 19 | fetch | tehdas.eu M7.4 draft (2025/09) PDF | Draft: EHDSR-6/7/8; OPR-5 deletion "or rendered unrecoverable … including any backups"; OPR-16 log every access, processing, viewing and output; OPR-17 one year minimum, five years recommended | context only |
| 20 | fetch ×4 | tehdas.eu D7.4 final (2026/06) PDF | v1.2 final, 24 Feb 2026. EHDSR-7 "All SPE logs MUST identify the actor" (Table 5.1, p. 31); EHDSR-8 one year (p. 31); OPR-6 "deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies" (Table 5.2, p. 43; two fetches agree, a third gave a different OPR-6 text); Annex 7 / p. 19 "User action logs are seen to be covered by user privacy…" (two fetches agree). No record-level logging requirement found and no five-year recommendation, per the fetches: a negative from a summariser, so worded "in the version inspected" | P06 |
| 21 | search | "made available under the data permit" OR "made available pursuant to the data permit" regulation 2025/327 | No instance found; EUR-Lex HTML listed but not searched in full. The claim in Ch6/Ch7 was removed rather than kept unverified | P07 |
| 22 | search | eHDSI audit trail retention "10 years" NCPeH security policy MyHealth@EU eHMSEG | eHMSEG minutes, eHealth Network governance, CBeHIS slides; no primary text stating ten years | M5a |
| 23 | fetch | ihe-europe.net CBeHIS Security Requirements and Impact (Jiráková) | Auditability required of all NCPs; no retention period | M5a |
| 24 | search | "NCPeH" audit logs retained "ten years" … agreement security | 2017 NCPeH agreement (health.ec.europa.eu ev_20170509_co06) | M5a |
| 25 | fetch | health.ec.europa.eu/system/files/2017-07/ev_20170509_co06_en_0.pdf | Agreement adopted 9 May 2017; clause II.4.2 "Each Contracting Party shall ensure the compliance of its NCPeH with the requirements for logs, audit trails, non-repudiation"; no period in the main text; annexes not reached | M5a, P09 |
| 26 | fetch | jmir.org/2025/1/e81184 (Simjanoska Misheva et al.) | Page returned no text; their source for ten years not identified | M5a |
| 27 | search | Feng 2022 arXiv formalising legal compliance satisfiability GDPR SMT peer-reviewed | CAV 2023 chapter found | M5e |
| 28 | fetch | link.springer.com/chapter/10.1007/978-3-031-37709-9_18 | Feng, Marsso, Sabetzadeh, Chechik, "Early verification of legal compliance via bounded satisfiability checking", CAV 2023, LNCS 13966, 374–396; cites arXiv 2209.04052 as its extended version | M5e, P09 |
| 29 | search | SPUHiN D5.2 anbefalinger minimumskrav sikre behandlingsmiljøer endelig versjon 2025 | Helsedirektoratet SPUHiN project page; helsedata.no gap report; Legeforeningen hearing response 3 Oct 2025. Final version not yet located | M5b (open) |
| 30 | search | Union Customs Code Article 51 … destruction of goods | UCC 952/2013 on EUR-Lex; Finnish Customs destruction page. Not yet read | M7a (open) |
| 31 | fetch | helsedirektoratet.no … fair-secure-provision-and-use-of-health-data-in-norway-spuhin | Criteria "were on hearing July–October 2025" and are "included in SPUHiN-rapport D5.2"; D5.2 via EU Funding & Tenders portal; adaptation to the implementing act depends on the Commission. No final national publication date given | M5b, P10 |
| 32 | fetch | legeforeningen.no hearing response 3 Oct 2025 | Responds to "Høring – Oversikt over kriterier til sikre analyserom …" (Helsedirektoratet); no mention of logging, retention or deletion | M5b |
| 33 | fetch | eur-lex.europa.eu CELEX:02013R0952-20221212 (HTML) | Returned the Delegated Regulation 2015/2446 instead; not used | — |
| 34 | fetch | legislation.gov.uk/eur/2013/952/article/51/adopted | UCC Art 51 verbatim as adopted: "at least three years", start of period by procedure; 51(2) extensions for corrections, appeals, court proceedings | M7a, P11 |
| 35 | fetch | legislation.gov.uk/eur/2013/952/article/197/adopted | UCC Art 197 verbatim as adopted: customs "may require goods which have been presented to customs to be destroyed" | M7a, P11 |
| 36 | file (Tiger) | TEHDAS2 D7.4 v1.2, 24 Feb 2026, full text supplied by Tiger as Markdown (`sources/TEHDAS2_D7.4_v1.2_2026-02-24.md`) | Read in full. **Corrects rows 19–20:** EHDSR-6/7/8 are on p. 32, not 31; the "User action logs" sentence is on p. 20 (with the typo "coved"), not 19; OPR-18 (p. 52) **keeps** the five-year recommendation, which the fetches said the final had dropped. New: OPR-6 (p. 43) continues "while ensuring compliance with applicable legal obligations and traceability or reproducibility requirements where relevant", rationale "the deletion and retention policy should balance these obligations"; OPR-8 (p. 47) logs "protected against tampering"; OPR-17 (p. 52) proportionate logging, "access to electronic health data", "avoid unnecessary collection of detailed user behaviour"; Annex 7 (p. 97) "open questions about how accountability and anonymisation obligations intersect … Further guidance will be needed on retention of project-level collaborative metadata"; p. 19 footnote on the 2025 CJEU ruling on pseudonymised data. No log-granularity requirement anywhere | P24 |
| 37 | file (Tiger) | Regulation (EU) No 952/2013, OJ L 269 text from EUR-Lex, supplied by Tiger (`sources/UCC_Regulation_952_2013_OJ_text.md`) | Art 51 and Art 197 match the quotations in §2.7 word for word. The page states a consolidated version of 12 Dec 2022 exists; that version was not supplied, so an amendment to either article after 2013 is not excluded | P11 confirmed |
| 38 | fetch, search | streamlex.eu ehds-de-art-68 (404); search for the German wording; data.consilium.europa.eu PE-76-2024-INIT/de (truncated) | German text of Art 68(12) not obtained | T-10 open |

**Done 3 Oct (rows 36–37), formerly to confirm:** the UCC citations were read on legislation.gov.uk's "as adopted" text, because EUR-Lex returned another act; checking Arts 51 and 197 on EUR-Lex is advisable. Also: the D7.4 page numbers above, the OPR-6 wording, and the
absence of a record-level logging requirement. The shell cannot reach tehdas.eu or zenodo.org
(proxy policy), so the PDF could not be read locally.
