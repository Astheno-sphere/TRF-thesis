# INDEXING SCORECARD (INTERNAL, NOT FOR SUBMISSION)

v0.9.2a, 26 Nov 2026. This is our own transparent rubric, not an official metric of Elsevier, Scopus or any index. Purpose: compare before and after the patch and choose keywords. Names the Zenodo record, so it must not ship.

## 1. Rubric and scores

High-value search concept groups (G1 to G8), chosen from the article's own subject and the Zenodo record's generic keywords: G1 EHDS / European Health Data Space; G2 audit log / auditing; G3 erasure / right to erasure; G4 GDPR; G5 secure processing environment; G6 data retention; G7 cryptographic erasure / crypto-shredding; G8 health data. Presence: exact phrase 1, partial (stem or only the long form) 0.5, absent 0.

| Criterion | Max | Before | After | How scored |
|---|---|---|---|---|
| 1 Title term coverage | 15 | 5.6 | 5.6 | Share of G1 to G8 in the title x 15. Title "Auditing After Erasure in the European Health Data Space" covers G1, G2, G3 (3/8). Title unchanged (options below) |
| 2 Abstract coverage | 20 | 12.5 | 20.0 | Sum of presence over G1 to G8, /8 x 20. Before: G1 1, G2 0.5, G3 0.5, G4 0.5, G5 1, G6 0.5, G7 0, G8 1 = 5. After: all eight exact = 8 |
| 3 Keyword quality | 15 | 8.8 | 14.4 | Five checks x 3: (A) 1 to 7 keywords; (B) no duplication with title; (C) single concept, no "and"/"of"; (D) established singular forms; (E) share of the five groups not in the title (G4 to G8) covered. Before: A 3, B 0 ("European Health Data Space" repeats the title), C 3, D 1 (plurals "audit logs", "secure processing environments"), E 1.8 (3/5). After: 3, 3, 3, 3, 2.4 (4/5) |
| 4 Controlled vocabularies (EuroVoc, ACM CCS 2012, MeSH) | 15 | not scored | not scored | A term scores only if its presence was checked on the vocabulary's own page. The session hit its usage limit during these checks. Result: see section 3. Totals are normalised to the 85 scored points |
| 5 Zenodo keyword alignment | 10 | 7.1 | 8.6 | Overlap of article keywords with generic keywords in `.zenodo.json` (read only): EHDS, right to erasure, cryptographic erasure, data retention, secure processing environment match; GDPR (Zenodo: "GDPR Article 17") and audit log (Zenodo: "audit log retention") half. Score = matches/7 x 10 (before: 5/7 of six terms counted as 5.0 of 7; after 6.0 of 7). Coined thesis names are deliberately not used (anonymity) |
| 6 Norwegian / EEA discoverability | 10 | 2 | 3 | Abstract mentions Norway or EEA (4); keyword (3); body sections naming Norwegian authorities and law (3, one per cluster: pilot and EFTA; helseregisterloven and FHI; gap analysis and Helsedirektoratet). Before 2 clusters of 3 scaled to 2; after 3 clusters scaled to 3. Abstract and keywords left alone because the abstract makes no Norway claim |
| 7 Reference-network signal | 15 | 8 | 12 | Five sub-criteria x 3: EHDS scholarship; GDPR authorities (EDPB, WP29, CJEU); security and cryptography venues; health-informatics standards; CLSR's own papers. Before 2, 2, 2, 1, 1. After 3, 3, 3, 2, 1 (only [5] is a CLSR paper; no other relevant CLSR 2024-2026 paper was found on an official page) |
| Total (of 85 scored) | 85 | 44.0 | 63.6 | |
| Normalised to 100 | | **52** | **75** | total / 85 x 100 |

If the three title options below are adopted, criterion 1 rises to about 7.5 to 11.3 and the normalised score to about 77 to 82.

## 2. Keywords

Before (6): European Health Data Space; GDPR; right to erasure; audit logs; secure processing environments; cryptographic erasure.
After (7): EHDS; GDPR; right to erasure; audit log; secure processing environment; cryptographic erasure; data retention.

Reasons: "European Health Data Space" repeats the title, so the acronym "EHDS" (searched on its own) replaces it; singular forms; "data retention" added because the article is about retention floors and was absent from keywords and abstract; each is a single concept; no "and" or "of"; English; GDPR and EHDS are the established abbreviations (both also spelled out in the abstract). Not chosen: "crypto-shredding" (synonym, kept out of the keyword list because "cryptographic erasure" is the precise term used throughout; consider swapping if the editor prefers practitioner wording), "secondary use" (not a main concept of the article), coined model names (anonymity), "Norway" (the abstract makes no Norwegian claim). CLSR guide: 1 to 7 keywords. Count: 7.

Abstract: 157 words (limit 250). Changes: acronyms defined (EHDS, GDPR); "audit logs for secure processing environments"; "under the right to erasure"; "data retention and deletion constraints"; "after cryptographic erasure". All numbers and claims unchanged; gate passes.

## 3. Controlled vocabulary checks (what could and could not be verified)

- MeSH: a search surfaced MeSH records meshb.nlm.nih.gov/record/ui?ui=D057286, D003219, D066275 and D062527 for the query terms Electronic Health Records, Computer Security, Confidentiality, Health Information Exchange. The descriptor names behind each UI were not read before the limit, so which UI is which term is NOT confirmed. To do by hand: confirm "Electronic Health Records", "Computer Security", "Confidentiality", "Health Information Exchange" on meshb.nlm.nih.gov. No MeSH term was added to keywords (CLSR is a law journal; MeSH helps only PubMed-type indexes).
- EuroVoc: a search returned the EuroVoc top-concept page https://op.europa.eu/en/web/eu-vocabularies/th-top-concept-scheme/-/resource/eurovoc/100141 but the page was not read. NOT verified: "data protection", "right to be forgotten" or "health data" as EuroVoc concepts. To do by hand on op.europa.eu/en/web/eu-vocabularies.
- ACM CCS 2012: two searches did not surface dl.acm.org/ccs. NOT verified: "Security and privacy > Privacy protections", "Social and professional topics > Medical information policy", "Applied computing > Health informatics". To do by hand. (Not needed for CLSR, which does not use CCS.)
- Therefore criterion 4 is not scored and totals are normalised.

## 4. Title options (proposed, NOT applied; authors choose)

The current title carries G1, G2, G3. Options add concepts without coined model names. Estimated group coverage in brackets.

1. "Auditing after erasure in the European Health Data Space: audit log retention and the right to erasure" [G1, G2, G3, G6; right to erasure exact; 4 to 5 of 8; criterion 1 about 7.5 to 9.4]
2. "Audit logs, data retention and the right to erasure in the European Health Data Space: a cryptographic erasure design" [G1, G2, G3, G6, G7; 5 to 6 of 8; about 10.3; drops the "Auditing After Erasure" hook]
3. "Auditing after erasure in the European Health Data Space: retention, secure processing environments and the GDPR right to erasure" [G1, G2, G3, G4, G5, G6; 6 of 8; about 11.3; longest, about 20 words]

Trade-off: the present short title is memorable; options 1 and 3 keep its first half, so citations by title fragment still resolve. Option 3 gives the most search coverage; option 1 is the closest to the supervisor's voice. Check the current CLSR Guide for Authors for any title length rule (not read in this session).

## 5. Not done

- No Norway or EEA term was put in the abstract or keywords (would add a claim to the abstract).
- No CLSR-filtered Crossref query could be run (host blocked), so the "CLSR own papers" sub-score is based on WebSearch only.
