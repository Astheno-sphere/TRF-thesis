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

**To confirm by opening the PDF yourself:** the D7.4 page numbers above, the OPR-6 wording, and the
absence of a record-level logging requirement. The shell cannot reach tehdas.eu or zenodo.org
(proxy policy), so the PDF could not be read locally.
