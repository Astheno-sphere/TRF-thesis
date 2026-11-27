# SOURCE_CHECK_v0.9.3 (research only; manuscript.md not edited)

Date of check: 27 Nov 2026. Method: WebSearch then WebFetch. The sandbox proxy blocks eur-lex.europa.eu, doi.org, crossref and efta.int from the shell, and WebFetch returns a model-written summary, not raw text. So article wording below is from fetched pages as summarised; re-read the quoted provisions once in the EUR-Lex HTML before relying on a sub-paragraph letter.

Fetch limits worth knowing:
- The EUR-Lex ELI pages returned metadata only (no article text). Regulation (EU) 2025/327 text was read in the OJ PDF copy hosted by the Spanish Ministry of Health: https://vsf-iwsold-pre-portal.sanidad.gob.es/areas/saludDigital/espacioEuropeoDS/docs/OJ_L_202500327_EN_TXT.pdf (file name OJ_L_202500327_EN_TXT.pdf). It is a mirror of the OJ text, not EUR-Lex itself.
- The GDPR Art 11 text was read at legislation.gov.uk (adopted EU text), not EUR-Lex.
- EFTA EEA-Lex pages (efta.int/eea-lex/32025r0327, /32026r2083, /node/295856) failed on every attempt. Status of [24] is NOT verified.
- The CELEX URL in [33] was not fetchable (not on allowlist); the judgment was read in the University of Bamberg copy of the judgment PDF (ECLI confirmed there).

## Part A. Legal propositions

### A1. Regulation (EU) 2025/327

| # | Manuscript lines | Claim | Verdict | Source provision | Fix |
|---|---|---|---|---|---|
| 1 | 34-36, 82-84, 113, 167 | Art 73(1)(e): identifiable logs of access and activity for as long as needed to verify and audit; access logs kept at least one year | CORRECT | Art 73(1)(e): "logs of access shall be kept for at least one year" | none |
| 2 | 36, 86, 115, 692 | Art 68(12): data in the SPE deleted within six months of permit expiry | CORRECT | Art 68(12): data in the SPE "shall be deleted within six months of the expiry of the data permit" | none |
| 3 | 159 | Final sentence of Art 68(12): at the user's request the access body may keep the formula used to create the requested dataset | CORRECT | Art 68(12) last sentence: at the request of the health data user, "the formula for the creation of the requested dataset may be stored by the health data access body" | none |
| 4 | 178-181 | Art 9: individuals informed of access via health professional access service; info available at least three years from each access | CORRECT | Art 9(1) (right to information on access via the health professional access service, incl. Art 11(5) access); Art 9(2) ("available for at least three years from each date of access"; who, when, which data) | Optionally cite Art 9(2) |
| 5 | 181 | Art 105 phases Art 9: March 2029 for Art 14(1)(a)-(c), March 2031 for (d)-(f) | CORRECT | Art 105: Arts 3-15 (with other listed articles) apply from 26 Mar 2029 for categories in Art 14(1)(a)-(c) and 26 Mar 2031 for (d)-(f) | none |
| 6 | 34, 90 | Chapter IV generally applies from 26 March 2029 | CORRECT | Art 105: Chapter IV applies from 26 Mar 2029, with exceptions (Arts 55(6), 70, 73(5), 75(1) and (12), 77(4), 78(6) from 26 Mar 2027; some Art 51(1) points from 26 Mar 2031; Art 75(5) from 26 Mar 2035) | none; "subject to the exceptions" at line 90 is right |
| 7 | 89 | Implementing acts on SPE requirements under Art 73(5) by 26 March 2027 | CORRECT | Art 73(5): "By 26 March 2027, the Commission shall, by means of implementing acts" (examination procedure, Art 98(2)) | none |
| 8 | 661 | Art 74(1): holder is controller when making data available to the HDAB; HDAB controller for own tasks; HDAB processor for the user when providing data in the SPE under a permit | CORRECT | Art 74(1) first subpara (holder controller, making data available under Art 60(1)); second (HDAB controller for its tasks); third (HDAB processor for the user, who is controller, when providing data in the SPE under a permit or processing for a response to an approved request) | none. Line 661 omits the "approved health data request" limb; harmless |
| 9 | 677 | Art 73(3): regular audits of the environment incl. third-party audits | CORRECT | Art 73(3): bodies "shall" arrange regular audits, which may be by third parties, and correct shortcomings, risks or vulnerabilities found | none |
| 10 | 148 | Art 2(2) includes personal and non-personal electronic health data | CORRECT | Art 2(2)(a)-(c): personal, non-personal and (c) electronic health data as either | none |

### A2. Provisions the co-author says should be ADDED (exact content)

| Provision | What it says | Relevance / caution |
|---|---|---|
| EHDS Art 61(3) | Health data users shall not re-identify, or attempt to re-identify, the natural persons to whom the electronic health data obtained under a data permit, a health data request or an access approval from an authorised participant in HealthData@EU relate. | Yes, a re-identification prohibition on users. It binds users, not the HDAB or SPE operator, so it does not itself license the HDAB to retain patient links. |
| EHDS Art 66(3) | Where the user has shown the purpose cannot be met with anonymised data (Art 68(1)(c)), the HDAB provides pseudonymised data; the information needed to reverse the pseudonymisation is available only to the HDAB or an entity acting as trusted third party under national law. | Yes, it concerns the pseudonymisation key. Useful for "whose means" analysis (line 448): the user has no key; the HDAB or trusted third party has it. |
| EHDS Art 73(2) | HDABs ensure holders can upload data and users can access it in the SPE; users may download only non-personal electronic health data (incl. anonymised statistical format), and download requests are reviewed by the HDAB. | Yes, output/download control. It supports the line 677 export-audit scenario. Check the exact verb on download review in the EUR-Lex HTML (my text is a summary). |
| GDPR Art 11 | 11(1): if the purposes do not or no longer require identification of the data subject, the controller need not keep, acquire or process additional information just to identify them for the sole purpose of complying with the GDPR. 11(2): where the controller can demonstrate it cannot identify the data subject it informs them if possible, and Arts 15 to 20 do not apply unless the data subject supplies additional information enabling identification. | Limits Art 17: if the post-erasure log truly no longer identifies a person, the controller need not re-link to honour an erasure request, but the data subject can defeat this by supplying identifying information. Art 11 is conditional on the controller being unable to identify; it does not apply where the controller keeps the link table. |

### A3. Case law

| Item | Manuscript lines | Verdict | Finding |
|---|---|---|---|
| C-413/23 P EDPS v SRB, 4 Sept 2025, ECLI:EU:C:2025:645 | 448, ref [33] | CORRECT (one nuance) | ECLI and date confirmed in the judgment PDF. Paras 74-86: pseudonymised data are not always personal data for every person; the test looks at means reasonably likely to be used by the controller or another person; for Deloitte the comments may not be personal data if it cannot reverse the measures (paras 77, 85-86); the SRB as key holder still has personal data (para 76). Paras 110-112: for the Art 15(1)(d) information duty (Reg 2018/1725) identifiability is assessed at collection and from the controller's perspective, before transfer. Manuscript matches. Nuance: the Court does not adopt "recipient perspective" as a fixed rule; it is relative to the person holding the means. Line 448's "from the perspective of a recipient" could read "taking into account the means of the recipient". |
| C-582/14 Breyer, 19 Oct 2016 (Second Chamber) | 446, ref [31] | CORRECT | Paras 43-49: information need not all be in one person's hands (para 43); means are not "reasonably likely" if identification is prohibited by law or practically impossible (para 46); legal channels via the competent authority (paras 47-48); dynamic IP is personal data for the media provider with legal means to obtain the ISP's data (para 49). "Additional information available through lawful means" is a fair use. Ref [31] gives no ECLI; ECLI:EU:C:2016:779 (not shown on the fetched pages, add from EUR-Lex). Source read: op.europa.eu record (case, chamber, date) and a DPA copy of the judgment text. |

### A4. EDPB documents

| Item | Manuscript | Verdict | Finding |
|---|---|---|---|
| Guidelines 02/2025 blockchain v2.0, adopted 7 July 2026 | 446, 705, ref [32] | IMPRECISE | Version and date confirmed. Paras 102-104: erasure and objection must be implemented by design (102); real deletion may be technically impracticable on chain, so plan at design stage so data can be rendered anonymous (103); "not advisable" to register personal data in clear, encrypted or hashed form on a blockchain (104). Paras 32-34 are on-chain security measures: encryption (32), key-derived functions/HMAC outputs with data off-chain (33), cryptographic commitments with data off-chain (34). Line 446 states only the 102-104 caution while the reference pins 32-34 as well. Para 34 supports the manuscript's own design (commitments, data off-chain) and should be named. Fix: in line 446 add "and describe commitments with off-chain data as an integrity measure (para 34)". |
| Guidelines 02/2026 anonymisation v1.0, adopted 7 July 2026, for public consultation | 142, 705, ref [20] | CORRECT | Version, date, consultation status confirmed. Para 26: the CJEU defined "means reasonably likely to be used" by what rules them out (impossible, disproportionate time/cost/effort, prohibited by law); cites C-413/23 P and C-479/22 P. Para 29: objective factors (a)-(e), including that a legal means of obtaining additional information is a means reasonably likely to be used. No consultation closing date on the fetched page. |
| Guidelines 01/2025 pseudonymisation, adopted 16 Jan 2025, consultation version | 439, ref [30] | CORRECT | Para 22 (section 2.1): pseudonymised data remain personal data where additional information could be combined; erasing the pseudonymising controller's additional information does not by itself make data anonymous. Document is the consultation version. Whether a final version exists was not checked. |
| CEF 2025 right-to-erasure report, adopted 10 Feb 2026 | 98, 705, ref [18] | CORRECT | Date confirmed. 4.2.4 misuse of Art 17(3) exceptions (anonymisation or restriction as safeguards); 4.2.6 erasure in backups; 4.2.7 difficulties with anonymisation as a response to erasure. No mention of logs. Line 98 cites [18] for Art 17(3)(c)/(d) exceptions: 4.2.4 is about misapplication of exceptions generally, so the cite supports "require their own analysis" but not the specific limbs (c)/(d). Soften if a reviewer pushes. |

### A5. Norway and the Commission

| Item | Manuscript | Verdict | Finding |
|---|---|---|---|
| Helsedirektoratet privacy notice "personopplysninger om helsepersonell", section "MyHealth@EU - søk og visningsmodul" | not cited in v0.9.3 (line 208-211 relies on the study's six-year figure and [23]) | NEW SOURCE (usable) | Fields: name, HPR number, role, type of healthcare institution, place of treatment, time of the lookup. Retention: six years (stored as part of the log). Legal basis: GDPR Art 6(1)(c) with pasientjournalloven section 22. Controller: Helsedirektoratet (dataansvarlig). Processor: Norsk helsenett (NHN), operates and maintains the solution. Page date: last professional change 30 June 2026. This independently supports the six-year figure at line 210-211. |
| FHI "FHIs rolle og oppdrag i EHDS" | 659, ref [39] | CORRECT | Page dated "Publisert 19.10.2026". States FHI is designated by the Ministry of Health and Care Services as national coordinating HDAB. The page also says it is not settled how many HDABs Norway will have. |
| Helsedirektoratet gap analysis 11 April 2025, ch. 5 | 659, ref [38] | CORRECT, with a dating caution | Ch. 5 "Sekundærbruk av helsedata" says approved SPEs that the HDAB can require, with the necessary solutions for control and activity logging, are missing. The chapter does not name FHI; it names Helsedataservice as the closest fit and says a coordinating HDAB is still to be designated. So [38] supports only the SPE finding and [39] only the FHI designation, and line 659 should keep the "as of 11 April 2025" date attached to the SPE finding only (it does). The finding is 19 months old; say so or check for a later one. |
| Reg (EU) 2026/2083 | 656-657, ref [37] | CORRECT | EUR-Lex PDF: "Commission Implementing Regulation (EU) 2026/2083 ... on MyHealth@EU", signed Brussels 18 September 2026, L-series headers 21.9.2026, legal basis Art 23(4) and (8) of Reg 2025/327, enters into force on the 20th day after publication, applies from 26 March 2027. A Danish legal portal dated 21 Sep 2026 corroborates the OJ date. |
| EFTA EEA-Lex 32025R0327 | 208, ref [24] | NOT VERIFIED | Page failed to load in all attempts from this environment. The open_comments.md log says the factsheet was read by hand on 26 Nov 2026. Re-open once before submission. |
| [23] Helsedirektoratet MyHealth@EU page | 204-208 | CORRECT | Project 2023 to end 2025; Norwegian healthcare personnel receive patient summaries for visiting EU/EEA citizens; pilot at emergency primary care in Bodo and Stjordal receiving from Finland, Czechia, Portugal; last professional update 15 Dec 2025. Roadmap page 4C "Samhandling pa tvers av landegrenser i EU": last updated 4 Nov 2026, describes MyHealth@EU as the infrastructure for primary use. Note the project ends at end 2025; the "pilot" wording at line 204 is now past-tense territory. |

### A6. TEHDAS2 D7.4 (ref [21])

| Claim | Verdict | Finding |
|---|---|---|
| OPR-17 and OPR-18, one-year minimum, five years recommended | CORRECT | OPR-17 (Table 5.4, Monitoring, Mandatory): identifiable logs of security- and compliance-relevant activities, tamper protection, kept as long as needed for audit. OPR-18 (Table 5.4, mandatory): secure storage of logs of user access with minimum one year; text says longer retention (5 years) is recommended. Rationale cites Art 73(1)(e). |
| EHDSR-8 in table 5.1 | CORRECT | Table 5.1: "All SPE logs MUST be kept at least for one year" (Mandatory, SPE Operator, source Art 73(1)(e)); linked from the OPR-18 row. Ref [21] wording "tables 5.1 and 5.4" is right. |

## Part B. All 39 references

Legend: OK = confirmed on a page fetched this session; OK* = confirmed except for the flagged detail; NV = not verified.

| Ref | Result | Evidence and flags |
|---|---|---|
| [1] Reg 2025/327 | OK* | Text read in OJ PDF mirror (sanidad.gob.es). EUR-Lex ELI page returned metadata only (title, date 11 Feb 2025). OJ date 5.3.2025 not re-confirmed from the page text. |
| [2] GDPR | OK | https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng: identifier 32016R0679, publication 2016-05-04, title confirmed. "OJ L 119/1" not shown on the fetched page. Art 11 text read at legislation.gov.uk. |
| [3] Rak, EJRR 15(4) 928-938 (2024) | OK | cambridge.org/core/product/1A05C6D0FB24313674C33037A3E98164: author Richard Rak, vol 15, issue 4, pp 928-938, DOI 10.1017/err.2024.67. |
| [4] Raposo, IJLIT 33 (2025) eaae016 | OK | Crossref record: sole author Vera Lucia Raposo, vol 33, article eaae016, DOI matches. |
| [5] Trigo Kramcsak, de Miguel Beriain, CLSR 62 (2026) 106367 | OK* | researchportal.vub.be: authors "Pablo Trigo Kramcsak and Inigo de Miguel Beriain", CLSR vol 62, art 106367, 2026, DOI matches. Flag: manuscript initials "P.R." are not confirmed (portal gives "Pablo"). Check initials on the ScienceDirect page (S2212473X26001082 returned an error). |
| [6] Martani et al., Health Policy 174 (2026) 105764 | OK | researchprofiles.ku.dk: five authors in the manuscript's order, Health Policy vol 174, art 105764, 2026, DOI matches. |
| [7] Schneier and Kelsey, TISSEC 2(2) 159-176 (1999) | OK* | Authors, title, pages 159-176, 1999 confirmed on schneier.com. Flag: schneier.com prints "v. 1, n. 3" for the journal, which conflicts with 2(2). ACM DL and DOI 10.1145/317087.317089 could not be opened. My recollection is 2(2), May 1999. Open the DOI once (already item 27 in open_comments.md). |
| [8] Crosby and Wallach, USENIX Sec 2009 | OK* | usenix.org page: authors, title, 18th USENIX Security Symposium 2009. Page range 317-334 not shown on the fetched page. |
| [9] Finck, STOA/EPRS PE 634.445 | OK | Uni.lu copy of the EPRS PDF: title as cited, PE 634.445, EPRS Scientific Foresight Unit (STOA), July 2019. 24 July 2019 date per the earlier Think Tank check in open_comments.md. |
| [10] Finck, EDPL 4(1) 17-35 (2018) | OK | edpl.lexxion.eu issue 2018/1: article on pp 17-35, URL path edpl/2018/1/6 matches the DOI suffix. Note [10] and [9] are different works; MPI/SSRN preprint is a different record (31 pp). |
| [11] Politou et al., IEEE TETC 9(4) 1972-1986 (2021) | OK | bib-bvb record: four authors, vol 9, issue 4, pp 1972-1986, 2021, DOI matches. |
| [12] Ateniese et al., EuroS&P 2017 pp 111-126 | OK | researchr/dblp bibtex: four authors, pp 111-126, DOI 10.1109/EuroSP.2017.37. |
| [13] Ateniese et al., Sanitizable signatures | OK | Springer: four authors, ESORICS 2005, LNCS 3679, pp 159-177, DOI matches. Editors not checked. |
| [14] Johnson et al., Homomorphic signature schemes | OK | Springer: four authors, CT-RSA 2002, ed. Preneel, LNCS 2271, pp 244-262, DOI matches. |
| [15] Hevner et al., MISQ 28(1) 75-105 | OK | experts.arizona.edu: four authors, vol 28, issue 1, pp 75-105, 2004, DOI 10.2307/25148625. |
| [16] Feng et al., CAV 2023 | OK | Springer: LNCS 13966, pp 374-396, DOI matches. arXiv 2209.04052 lists exactly four authors, matching the manuscript. (open_comments item 18 about "ten authors" is not borne out.) |
| [17] Petrocnik, Routledge 2025, pp 181-206 | OK | Tilburg record: title, editors Slokenberga, O Cathaoir, Shabani, Routledge 2025, pp 181-206, DOI 10.4324/9781003544111-12. Author's name has a hacek on "c" in the original (Tjasa Petrocnik); manuscript spelling "Petrocnik" with the hacek is correct. |
| [18] EDPB CEF 2025 erasure report | OK | URL fetched; adopted 10 Feb 2026; sections as in A4. |
| [19] WP216 | OK | ec.europa.eu PDF fetched: Opinion 05/2014 on Anonymisation Techniques, WP216, 10 April 2014. |
| [20] EDPB Guidelines 02/2026 | OK | URL fetched; v1.0, 7 July 2026, for consultation. |
| [21] TEHDAS2 D7.4 | OK | URL fetched; title, tables and requirements as in A6. |
| [22] IHE ITI-55 | OK | profiles.ihe.net page fetched. Section 3.55.4.1.2.1 is "Major Components of the Patient Registry Query by Demographics"; 3.55.5.1 audit messages: both Initiating and Responding Gateway carry the base64 query in ParticipantObjectQuery; patient objects only in the Responding Gateway message (0..n). Supports line 188-191 as written. |
| [23] Helsedirektoratet pages | OK | See A5. |
| [24] EEA-Lex | NV | Fetch failed. |
| [25] RFC 6962 | OK | rfc-editor.org: authors Laurie, Langley, Kasper; June 2013; section 2.1 "Merkle Hash Trees"; obsoleted by RFC 9162. |
| [26] RFC 9162 | OK | Authors Laurie, Messeri, Stradling; December 2021; obsoletes RFC 6962. |
| [27] Reardon, Basin, Capkun SoK | OK | ieee-security.org PDF: authors, 2013 IEEE S&P, pp 301-315, DOI 10.1109/SP.2013.28. |
| [28] Boneh and Lipton | OK | usenix.org (authors, 6th USENIX Security Symposium 1996) and Boneh's page (pp 91-96). |
| [29] NIST SP 800-88 Rev 2 | OK | csrc.nist.gov: "Guidelines for Media Sanitization", published September 2025 (final 26 Sept 2025), DOI 10.6028/NIST.SP.800-88r2. |
| [30] EDPB 01/2025 | OK | See A4. Consultation version; check for a final version. |
| [31] Breyer | OK* | op.europa.eu record confirms case, Second Chamber, 19 Oct 2016. No ECLI shown. |
| [32] EDPB 02/2025 v2 | OK* | See A4 (IMPRECISE sentence at line 446). |
| [33] EDPS v SRB | OK* | ECLI and date confirmed in a judgment PDF copy. CELEX URL (62023CJ0413) not fetchable here; the EUR-Lex case page for C-413/23 P loads but showed no details. |
| [34] Walonoski et al., JAMIA 25(3) 230-238 | OK | Crossref: ten authors (manuscript uses "et al."), vol 25 issue 3 pp 230-238; online 2017, print March 2018; DOI matches. |
| [35] IHE ATNA | OK | ch-9.html: "Audit Trail and Node Authentication (ATNA) Profile", Revision 20.0, 4 August 2023. |
| [36] ISO 27789:2021 | OK | iso.org/standard/75313.html: ISO 27789:2021, second edition, published. |
| [37] Reg 2026/2083 | OK | See A5. |
| [38] Gap analysis | OK | See A5. |
| [39] FHI | OK | See A5. |

## Summary of items to act on

1. WRONG: none found among the legal propositions checked.
2. IMPRECISE: line 446 / ref [32] (paras 32-34 vs 102-104; para 34 supports commitments); line 448 ("recipient perspective" is relative, not a fixed rule); line 98 ref [18] pinpoint (4.2.4 is general, not on 17(3)(c)/(d)); line 659 gap analysis finding is 19 months old and does not name FHI; line 204 "pilot" for a project that ended end 2025.
3. Reference flags: [5] initials "P.R."; [7] volume/issue conflict (schneier.com says 1(3), manuscript 2(2)); [8] page range not seen; [31] add ECLI:EU:C:2016:779 from EUR-Lex.
4. Not verified: [24] EEA-Lex status (site not reachable); CELEX URL of [33]; whether a final version of EDPB Guidelines 01/2025 exists.
