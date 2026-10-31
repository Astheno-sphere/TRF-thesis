# RT2: Consistency and citation audit (read-only)

**Scope.** I audited the chapter source files and the assembled `VERA-SNARK_Thesis_SUBMISSION.md`. The bodies are line-identical: the only differences are the per-chapter reference lists, which the assembly replaces with the consolidated References. Locations below use the source-file names. No file was edited.

**Artefact check.** I ran all seven modules in `/home/claude/trf`. Each output diffs clean against its `docs/expected_*.txt` file. The Appendix A source listings A.10–A.13, A.15 and A.23 are byte-identical to the code, and the console outputs A.16–A.24 are byte-identical to the recorded files.

**Headline numbers agree everywhere** (abstract, Ch5, Ch6, Ch7, Table 4.1, A.8, Appendix C script):

| Result | Value |
|---|---|
| Records, violations | 200 records, 95 violations, 90 records with a violation |
| Split by class | 37 cross-border / 53 SPE |
| Violation decomposition | 41 C2-only / 44 C3-only / 5 both |
| Corollary 1.2 witnesses | 39 of the 78 SPE records with no request |
| Invalidations | 138 in all: 52 on Art 17, 86 on Art 68(12) |
| Semantics II | 0 violations |
| δ = 1 vs δ = 3 | 90/95 vs 89/94 |
| Audit log | 200/200 records verify |
| AES module | 138 refused / 62 still decrypt |
| Z3 | 9/9 checks |
| Exhaustive search | 2^14 = 16,384 assignments per case; 65,536 over four cases |
| Floors | 12 and 120 months |
| Dates | 26 Mar 2027 / 2029 / 2031 |

Other checks that passed:
- The line counts in Table 5.1 and A.2 match release v1.0.1.
- 430 of the checker's lines are non-blank, non-comment.
- The DOI 10.5281/zenodo.23819275 and version 1.0.1 agree across the abstract, A.1, `CITATION.cff` and `README.md`. The DOI could not be resolved externally because Zenodo has not indexed it yet.
- The citation cross-match found **no orphans in either direction**. Every reference-list entry is cited in the text, and every author–year citation in the text has an entry. The H. L. Larsen personal communication is correctly kept out of the list.

Findings follow, most severe first.

---

## MAJOR

**M1. The EDPB "corridor" is not in EDPB Guidelines 02/2025 v2.0 (MISMATCH, and the thesis builds on it).**
- **Where it appears:**
  - Ch1 §1.4: "accept, for the first time at Union level, that where physical deletion is not technically possible, deleting the decryption key can render personal data unintelligible and so serve the erasure obligation"
  - Ch2 §2.3, same claim, followed by "these positions define the legal corridor"
  - Ch4 §4.9 "Why the mechanism is nonetheless defensible"
  - Ch6 §6.2 "Second, the direction of regulatory travel favours the argument"
  - Statement of Contribution #3 and §7.2: "designed to the corridor that the European Data Protection Board's finalised Guidelines 02/2025 establish"
  - Table 4.1, row "Key deletion may serve erasure where physical deletion is not possible"
  - Table 2.1, own row: "within the EDPB 02/2025 corridor"
- **What v2.0 actually says** (adopted 7 July 2026; edpb.europa.eu PDF, read via WebFetch):
  - Para 51: "upon deletion of this decryption key, the encrypted data will be unintelligible, at least until the algorithm is broken". The same paragraph adds that "encrypted personal data is still personal data and encryption does not remove the need for GDPR compliance".
  - Para 50: "technical impossibility cannot be invoked to justify non-compliance".
  - Para 103: personal data on the chain must be able to be "effectively rendered anonymous if an erasure request or objection is received".
  - Recommendation 16 (para 125): on an Article 17 request, personal data "needs to be erased or rendered anonymous".
  - No passage ties key deletion to discharging Article 17.
- **What does match:** the "until the algorithm is broken" wording, and the point that encrypted or hashed data may remain personal data.
- **Why it matters:** the sentence the thesis repeats is the anchor of contribution 3, of the legal defensibility of the residue, and of §6.2's "direction of travel" argument. On the actual text the EDPB sets the bar at erasure or anonymisation. §4.9 itself concludes that the residue is not anonymous.
- **Fix:**
  1. Re-read paras 50–52, 103–104 and 125 yourself (my reading went through a summarising fetch tool).
  2. Restate the claim as: the Board describes key deletion as rendering ciphertext unintelligible, while holding that encrypted data remain personal data and that erasure requires deletion or anonymisation.
  3. Present the mechanism's reliance on key deletion as a third interpretive step without authority. Add it to §3.7 (sixth limitation), §6.2, §7.4 and the "What is not claimed" paragraph.
  4. Drop "for the first time at Union level" and "finalised … establish".

**M2. The TEHDAS2 D7.4 Annex 7 quotation is taken out of context.**
- The words match the PDF's printed p. 96: "This raises open questions about how accountability and anonymisation obligations intersect. Further guidance will be needed on retention of project-level collaborative metadata."
- But the passage concerns the **project logbook**, a collaborative record-keeping tool for researchers. The sentence before it reads: "the project logbook is a good example of the privacy problems … It allows project members … use freely identifying pseudonyms in their data. The accountability of their work depends on the accuracy of their log keeping."
- The thesis uses it as the Joint Action naming the retention conflict:
  - Ch7 §7.1: "the Joint Action's specification names their interaction as needing further guidance (TEHDAS2, 2026b, Annex 7, p. 96)"
  - Ch1 §1.4: "in its expert commentary names 'open questions…'"
  - Ch2 §2.4, final paragraph: "The contribution of this thesis is positioned at that named gap"
  - Ch2 §2.9: "log keeping 'raises open questions…' … The body drafting the requirements names the question"
  - Ch6 §6.2 and §6.8
- **Fix:** say that Annex 7 raises an analogous accountability-versus-anonymisation tension for researchers' project logbooks. Rest the "asks for the balance" point on OPR-6 (p. 43) alone, which does say it. Delete "names their interaction" in §7.1 and "positioned at that named gap" in §2.4.

**M3. The Helsedirektoratet reply of 19 October has not been carried through the thesis.**
- Ch2 §2.3 (correctly, and matching `sources/helsedir_retention_correspondence_2026-10.md`): no eHDSI specification fixes a period; the pilot uses 6 years; "The reported ten-year figure is therefore not an established requirement".
- Text that still treats ten years as a reported, merely unconfirmed deployment baseline:
  - Abstract: "on a reported but unverified deployment baseline, ten years for MyHealth@EU audit repositories"
  - Sammendrag: "etter en rapportert, men ikke verifisert, eHDSI-baseline, ti år"
  - Ch1 §1.1: "a figure this thesis could not confirm in a primary document"
  - Ch1 §1.2: "retained for the period its deployment binding sets (ten years as reported, Section 1.1)"
  - Ch1 §1.3 / RQ gloss, Ch3 §3.4 Step 2, Ch4 §4.3 ($F$ = 120), Ch5 Table 5.2 ("eHDSI baseline as reported"), Ch7 §7.1 ("ten years as reported under the eHDSI deployment baseline")
- Ch2 §2.4, closing synthesis: "eHDSI-mandated audit retention". This now contradicts §2.3 outright.
- Ch4 §4.2 and §4.8 keep the cross-border patient link "for the rest of the floor on the strength of the deployment binding", which the operator says does not exist.
- **Fix:** one phrase per location, along the lines of "a long cross-border floor, illustrated at ten years; the Norwegian operator reports that no eHDSI specification fixes a period and that the pilot uses six years (§2.3)". Change "eHDSI-mandated" in §2.4. The model needs no change, because Corollary 2.2 makes the results floor-independent.

**M4. Appendix A.1 describes a viewer that does not exist in the release it cites.**
- A.1: "The archived release is the citable artefact: version 1.0.1 … is the exact code whose outputs this thesis reports". The next paragraph: "The demonstration has eleven pages. *Start here* … *The four propositions* … *Claim ledger* …".
- Release v1.0.1 (commits 0ad3865 and 627654d) has `app.py` at 825 lines with **8** pages.
- The 11-page app, at 1,108 lines, exists only in the later commit 46a3fcd ("App: examiner's walk", 30 Oct). That is what the live Streamlit app and the default branch now serve.
- Inside the thesis this contradicts A.2 ("Eight-page demonstration viewer … 825 + 133"), A.14 ("`app.py` (825 lines)") and Ch5 §5.2 / Table 5.1 ("eight-page viewer"). The repository's own HEAD `README.md` also still says "Eight pages", and its `docs/Appendix_A.md` at 627654d says "eight pages".
- **Fix:** state which is which. For example: "Release 1.0.1 contains the eight-page viewer (A.2); the live demonstration runs a later version of `app.py` (11 pages, no result module changed)." Alternatively, cut release 1.0.2 including 46a3fcd and update the DOI, the line counts and "eight-page" everywhere.

**M5. "Seven Python modules" in A.1 contradicts the rest of the thesis.**
- A.1: "It contains seven Python modules".
- Ch5 §5.2: "Seven further modules accompany it, bringing the artefact to eight Python files in all". Table 5.1 and A.2 list eight `.py` files, with `app.py` and `ui.py` sharing a row.
- **Fix:** "eight Python files (the checker and seven further modules; the viewer is split across `app.py` and `ui.py`)".

**M6. The runtime claims are false as stated and contradict two "no timing" statements.**
- A.5: "Runtime measured at 0.019 s".
- Ch5 §5.8: "completes in under one-twentieth of a second on ordinary hardware".
- Ch7 §7.6: "Every number in it was produced by code that runs in under a twentieth of a second".
- **Measured here:** about 0.45 s in-process and 0.7 s wall for `trf_checker.py`. The machine is ordinary: a 10-million-iteration Python loop takes 0.57 s. Profiling shows the Merkle-log hashing (`_mth`, 1.1 million calls) dominates, so the 0.019 s figure predates the audit log. `z3_check.py` and `synthea_layer.py` take about 2.6–2.7 s, and figures such as 764 controllers are not code outputs at all.
- **Self-contradiction:** Ch3 §3.6 says "It does not measure execution time … and no such measurements are reported anywhere in this thesis", and Ch5 §5.8 says "no statement about execution time … appears anywhere in this thesis".
- **Fix:** delete the three runtime statements, or replace them with "runs in about a second". In §7.6 write "Every reported result of the demonstration was produced by code any reader can execute".

**M7. Chapter 7 does not explicitly answer SQ1–SQ3.**
- §7.1 answers the primary question ("The answer to the research question is therefore…"). None of SQ1, SQ2 or SQ3 (Ch1 §1.3) is named or answered anywhere in Chapter 7. Examiners check for this.
- **Fix:** add one short paragraph to §7.1:
  - SQ1: Propositions 1 and 3, Corollary 1.2, conditional on the broad reading.
  - SQ2: Proposition 2 and Corollary 2.2, with Chapter 5. Add that it holds only within the model and subject to the authority questions of §7.4.
  - SQ3: §4.11 and Table 4.1, as compatibility rather than deployment.

**M8. Ch1 misstates Proposition 3.**
- Ch1 §1.3: "a deletion ceiling collides with a retention floor exactly when it is no longer than the floor".
- Proposition 3 makes $L \le F$ **necessary**, and sufficient only when the ceiling is anchored to the same event (case (i)). With an external anchor, a collision happens only for records with $e - t \le F - L$.
- The abstract, §4.12 and §7.1 correctly say "only if". Ch6 §6.10 has a smaller slip: "its ceiling is shorter than the floor, which any collision requires" should read "no longer than".
- **Fix:** in §1.3, "collides with a retention floor only if it is no longer than the floor, and its anchor decides…".

**M9. The residue "threshold" requirement contradicts §4.9.**
- Ch2 §2.9, fourth gap: the residue "must itself be shown to sit on the lawful side of that threshold … a contribution requirement … that Chapter 4 discharges". "That threshold" is the high Norwegian anonymity threshold.
- Ch4 §4.9 concludes: "The residue therefore does not meet the strict Norwegian anonymisation threshold".
- **Fix:** "must itself be assessed against that threshold, and its status (pseudonymised, not anonymous) stated; Chapter 4 does so". Pair this with the M1 revision.

**M10. The abstract's list of contributions differs from the Statement of Contribution and §7.2.**
- Abstract: "a formal characterisation of the conflict, a minimal semantic move that dissolves it, an executable witness, and an integration analysis". This omits the mechanism specification and residue analysis (contribution 3) and adds a "semantic move" item.
- Statement of Contribution and §7.2 give four different contributions: the model; feasibility results with witness; the mechanism with its residue; the integration analysis.
- Ch1 §1.4 and Ch2 §2.10 describe a three-part "novelty claim" instead.
- **Fix:** align the abstract's last sentence (and the Sammendrag's) to the four contributions of §7.2. In §1.4, add "set out as four contributions in the Statement of Contribution".

**M11. §7.1 states the answer without the authority caveat.**
- §7.1: "the three regimes can be reconciled, that the reconciliation requires no amendment to any instrument".
- §6.2 and §7.4 concede that this rests on an interpretive step without authority. §6.2 says that if it fails, "Proposition 2 remains mathematically true and becomes practically inert".
- **Fix:** "can be reconciled within the model, and in law if the verifiability step of §7.4 is accepted".

---

## MINOR

**m1. EDPB Guidelines 02/2026 is a consultation draft, and the thesis does not say so.**
- The PDF reads "Version 1.0, adopted on 07 July 2026, for public consultation".
- The reference entry reads "(Version 1.0, adopted 7 July 2026)", and §4.9 says "adopted on 7 July 2026, set the same bar at Union level".
- §4.9 also says data "count as anonymous only where they resist record isolation, linkage and inference". The Guidelines say data meeting the three criteria "may be regarded as anonymous" (para 52), and that failing one "does not necessarily" make data personal. Para 91 on encryption and para 90 on access measures MATCH.
- **Fix:** add "[draft for public consultation]" to the entry and change "only where" to "where".

**m2. Two sources are cited for claims they do not make.**
- Ch2 §2.3: "The data controller bears an independent obligation to erase … irrespective of whether the data subject has formally exercised the right (European Data Protection Board, 2026a)". The CEF report does not say this. Article 17(1) GDPR does ("the controller shall have the obligation to erase … where one of the following grounds applies"). **Fix:** cite Article 17(1).
- CEF dates: the report states adoption on 10 February 2026; the thesis says "published on 18 February 2026". That is probably the publication date and is not an error. 32 supervisory authorities and 764 controllers MATCH.

**m3. Some sources are not labelled as preprints, drafts or non-retrievable.**
- *Gabizon et al. 2019 (PLONK)*: ePrint only, unlabelled.
- *Sharma et al. 2025 (zkFL-Health)*: arXiv, unlabelled in the entry and in the §2.4 text. Table 2.1 does label it.
- *Zhuang et al. 2024 (CBCMS)*: arXiv, unlabelled anywhere. §2.7 calls it part of "a small but technically substantial literature".
- **Fix:** add "[Preprint; not peer-reviewed]" to all three entries and qualify Zhuang in §2.5 and §2.7.
- *SPUHiN (2025)*: the entry concedes "no stable public locator … could be established". This sits uneasily with the inclusion criterion of §2.1.5 ("Every cited source must be retrievable") and the Declaration's "Every factual claim … traceable to a source retrievable". The same applies to the H. L. Larsen personal communication. **Fix:** add a named exception to §2.1.5 and the Declaration.

**m4. Representativeness of the synthetic data is claimed in two places and denied elsewhere.**
- Ch3 §3.5: "matching the Norwegian profile version is what makes the demonstration representative of the Norwegian setting".
- Ch2 §2.9, second gap: "demonstrated against synthetic data representative of Norwegian conditions".
- The next paragraph of §3.5 and A.7 deny any such representativeness ("no claim of Norwegian clinical representativeness").
- **Fix:** "matches the FHIR version the Norwegian profiles constrain" in §3.5, and delete "representative of Norwegian conditions" in §2.9.

**m5. Overclaims beyond what is conceded elsewhere.**
- Ch2 §2.4: "the problem this thesis formalises and resolves". §7.2 and §6.9 say "addresses … in one regulatory setting". **Fix:** use "addresses".
- Ch2 §2.4: the single-author, non-peer-reviewed preprint "demonstrates that the erasure side … now has a rigorous formal treatment". **Fix:** "proposes a formal treatment".
- Ch2 §2.7, Elhub: "the TRF Model transfers to energy-sector data-retention conflicts without modification". This is untested. §6.10 and §7.5 treat transfer as open, and §6.10 shows that floor-against-right cases are "the ordinary bi-lateral conflict". **Fix:** "the model's floor-against-right fragment applies; whether a ceiling collision arises there is untested".
- Ch6 §6.1 and Ch4 §4.10: "Cryptographic invalidation is therefore necessary where a data subject's request meets a retention floor". Rival 4 concedes that for cross-border records "'delete the record and log the deletion' is close to an equivalent design". **Fix:** "relocation cannot substitute for it".
- Ch6 §6.1: "The thesis establishes that the conflict … is not a property of the obligations but of an assumption". **Fix:** add "within the model".

**m6. "Two interpretive steps" against three open questions.**
- The Statement of Contribution, §3.7 and §6.2 say two interpretive steps. §7.4 and Table 4.1 add a third open question, whether auditing needs the subject link after the ceiling, and §7.4's request asks all three.
- **Fix:** in §7.4, call the third a sub-question of the scope step.

**m7. §7.3 misreports the canonical limitations list.**
- §7.3: the limitations "stated canonically in Chapter 3, Section 3.7 … are … the single-seed demonstration, … the US Core profiles". Neither is among §3.7's eight; US Core is in §3.5. §6.11 has the same issue: "These limitations are stated once, in Chapter 3, Section 3.7".
- **Fix:** "§3.5 and §3.7", or add both to §3.7.

**m8. The Norwegian audit stream is described three different ways.**
- Ch1 §1.1: "beginning to be generated in Norwegian production, on live infrastructure, in small numbers". §2.6 has "at presently small volume".
- §2.2: "no relevant patients had yet presented".
- §6.8: "has effectively not begun". §7.6: "barely begun".
- **Fix:** use §2.2's wording throughout.

**m9. Small mismatches in Appendix A and Chapter 5.**
- The table of contents says "A.14 Source listing: `app.py`". The heading is "A.14 The demonstration viewer: `app.py` and `ui.py`" and it contains no listing. **Fix:** align the TOC entry.
- A.1 says "a recorded console run for every command", but the A.2 table omits `expected_z3_check_output.txt`, `expected_crypto_envelope_output.txt` and the full-cohort re-run file. **Fix:** add them to A.2.
- A.5 item 1 says the checker "produces every figure in Chapter 5, Sections 5.3–5.7", but §5.6 needs `--delta-witness`. **Fix:** "5.3–5.5 and 5.7".
- Ch5 §5.2's import list omits `sys`. A.4 omits `sys` and lists `glob`, which is used by the Synthea layer. **Fix:** align both lists with the code.

**m10. The Sammendrag drops one substantive sentence from the abstract.**
- It omits: "The formal results are deliberately elementary … The weight lies in the legal necessity analysis and the mechanism design, not in the proofs." This is a self-limitation, so it belongs in both versions. Everything else matches.
- Within the abstract, "Proposition 1 … carries the argument" sits awkwardly beside "The weight lies … not in the proofs". **Fix:** "carries the formal argument".

**m11. Cross-reference and wording slips.**
- Ch4 §4.10: "The partition of Section 4.7 meets the ceiling". The partition is defined in §4.3. **Fix:** "Section 4.3".
- Ch6 §6.10: "The first of those three contributions". §6.9 lists three *implications* of four contributions. **Fix:** "The first of those implications".
- Ch6 §6.2: "Third, the question is decidable by asking. Chapter 7 proposes…". The Datatilsynet enquiry had already been sent on 23 September (§7.4). **Fix:** add "an enquiry to Datatilsynet was sent on 23 September 2026 (§7.4)".
- Ch5 §5.2: "One hundred records of each class … matching the population scale fixed in Chapter 3, Section 3.5". §3.5 fixes about 100 *patients*, not 100 records per class. **Fix:** reword to say what §3.5 actually fixes.
- Ch3 §3.6: the realism layer constructs "metadata from the actual encounter events". The code sets only `doc_category` from the bundle. **Fix:** "sets the document category from the bundle".

---

## Task B(2): quotation sample (30 items)

EUR-Lex returned 403 through the proxy. I verified EHDS text through streamlex.eu, a mirror of the Official Journal text, and through D7.4 Annex 9, which reproduces Article 73(1) verbatim. GDPR text came from gdpr-info.eu. D7.4 page numbers were checked against the local PDF; printed page = PDF index − 1.

| # | Quotation (location) | Result |
|---|---|---|
| 1 | Art 68(12) "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit" (§1.1, §2.3, §4.4, §4.6) | MATCH |
| 2 | Art 68(12) "a storage system with reduced capabilities" (§4.6) | MATCH |
| 3 | Art 68(12) "the formula for the creation of the requested dataset" (§4.6) | MATCH |
| 4 | Permits of up to 10 years (§5.4) | MATCH (Art 68(12)) |
| 5 | Art 73(1)(e) "the keeping of identifiable logs … at least one year" (§1.1, §2.3) | MATCH (D7.4 Annex 9, Fig. 6) |
| 6 | Art 73(1)(a) "authorised natural persons listed in the data permit" (§4.6) | MATCH (D7.4 Annex 9, Fig. 2) |
| 7 | Art 73(1)(c) "authorised identifiable individuals" (§4.6) | MATCH (D7.4 Annex 9, Fig. 4) |
| 8 | Art 9 "information on the healthcare provider or other individuals who accessed…", "the date and time of access", "which personal electronic health data were accessed", "for at least three years from each date of access to the data" (§4.2) | MATCH; all are in para 2, and para 1 names the "health professional access service" |
| 9 | Art 2(2)(a)/(c) "data concerning health and genetic data, processed in an electronic form" (§4.6) | MATCH; the quoted words are (a), and (c) is "personal or non-personal" |
| 10 | GDPR 17(1) right "without undue delay" (§1.1, §2.3) | MATCH |
| 11 | GDPR 17(3)(b) legal-obligation exemption (paraphrase, §1.2, §4.2) | MATCH |
| 12 | GDPR 17(3)(c) "(h) and (i) of Article 9(2) as well as Article 9(3)" (§2.3) | MATCH |
| 13 | GDPR 17(3)(d) "scientific or historical research purposes … objectives of that processing" (§4.4) | MATCH; the quote starts mid-clause after "archiving purposes in the public interest," |
| 14 | GDPR 12(3): one month, extendable by two further months, inform within the first month (§4.4) | MATCH |
| 15 | GDPR 5(1)(c) "adequate, relevant, and limited to what is necessary" (§4.2) | Close paraphrase of the known text; not fetched |
| 16 | NIST SP 800-88r2: cryptographic erase as purge (§2.3, §2.4) | MATCH (NIST r2 FAQ Q9, "an approved purge method", with conditions). The thesis quotes **no** 800-88 definition of "destroy"; the only destruction definition quoted is from SP 800-57 (next row) |
| 17 | SP 800-57 Pt1 r5 "all traces of a cryptographic key so that it cannot be recovered by either physical or electronic means" (§4.8) | MATCH (NIST glossary, "Key destruction") |
| 18 | SP 800-57 "its previous existence may be recorded (e.g., in metadata or audit logs)" (§4.8) | MATCH (glossary, "Destroyed state"; the cited section 7.6 is plausible but not checked) |
| 19 | EDPB 02/2025 v2.0: key deletion "serve[s] the erasure obligation" (§1.4, §2.3, §4.9, §6.2) | **MISMATCH**, see M1 |
| 20 | EDPB 02/2025: unintelligible "at least until the algorithm is broken"; encrypted and hashed data may remain personal data; metadata and content may be personal data (§2.3, §4.9) | MATCH (paras 51, 52, 26, 29; fn 12) |
| 21 | EDPB 02/2026 paras 90 and 91 (§4.9, paraphrase; paragraphs not cited) | MATCH (para 91: encryption "is, by its very nature, intended to be reversible and differs from anonymisation"). "Only where they resist…" is overstated (m1). Para 35 is not used by the thesis |
| 22 | D7.4 Table 5.2, OPR-6, p. 43: "MUST be deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies"; "while ensuring compliance … where relevant"; "The deletion and retention policy should balance these obligations" | MATCH; page 43 correct |
| 23 | D7.4 Annex 7, p. 96: "open questions about how accountability and anonymisation obligations intersect"; "further guidance will be needed on retention of project-level collaborative metadata" | Wording MATCH, page correct; **context MISREPRESENTED** (M2) |
| 24 | D7.4 Table 5.1, p. 31: EHDSR-7 "All SPE logs MUST identify the actor"; EHDSR-8 "All SPE logs MUST be kept at least for one year"; EHDSR-6 | MATCH |
| 25 | D7.4 Table 5.4, p. 51: OPR-17 "access to electronic health data", "Data import, export, or release of outputs", "proportionate, risk-based, and technically feasible", "avoid unnecessary collection of detailed user behaviour not required for auditability or misuse detection"; OPR-18 "longer retention (5 years) is recommended" | MATCH; OPR-8 is on p. 46, also correct |
| 26 | D7.4 Figure 5.13, p. 60 | MATCH (page) |
| 27 | Implementing Decision 2019/1765 Art 7: Commission "shall not have access to patients' personal data"; Member States allocate responsibilities (§4.2) | MATCH (Art 7(2) and 7(1)) |
| 28 | Union Customs Code Art 51 "for at least three years"; Art 197 "may require goods which have been presented to customs to be destroyed" (§2.7) | MATCH (local OJ text) |
| 29 | Aikebaier (2026): five open problems; the 4th is "composition with ZKP selective disclosure" and the 5th is multi-regime retention conflict; Destruction-IND; EDPB equivalence (§2.4, §2.9, §7.5) | MATCH (eprint.iacr.org abstract; preprint correctly labelled) |
| 30 | Rak (2024): the EHDS "has been drafted ambiguously", which "could lead to inconsistent data management practices" (§2.3) | MATCH in substance; p. 928 not confirmable from the reader view |

**UNVERIFIABLE** (sites blocked or nothing indexed):
- Politiregisterloven §17 sentence (lovdata). Lovvedtak 80 (2025–2026) confirms that §17 was not amended.
- Datatilsynet n.d.-b "anonymisering likestilles med sletting av personopplysninger" and Datatilsynet 2015: no indexed match.
- SPUHiN 2024, p. 4 quotation, and requirements P13/P14/P24/P31: helsedata.no not reachable.
- eHealth Network 2017, clause II.4.2: health.ec.europa.eu not reachable.
- TEHDAS2 D6.3, Section 7.2: not local and not reachable.
- CSCMP logistics definition: not fetched, though the wording matches widely reproduced text.
- EHDS Art 73(5), Art 105 and Art 71: not fetched directly.

**Recommended pinpoint additions.** Cite EDPB 02/2025 v2.0 paras 50–52, 103 and 125, and EDPB 02/2026 paras 52, 90 and 91.

---

## Sources consulted (web)
- [EDPB Guidelines 02/2025 v2.0 (blockchain)](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf)
- [EDPB Guidelines 02/2026 v1.0 (anonymisation, public consultation)](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf)
- [EDPB CEF 2025 report on the right to erasure](https://www.edpb.europa.eu/system/files/2026-02/edpb_cef-report_2025_right-to-erasure_en.pdf)
- [EHDS Art 68 (streamlex)](https://streamlex.eu/articles/ehds-en-art-68/), [Art 9](https://streamlex.eu/articles/ehds-en-art-9/), [Art 2](https://streamlex.eu/articles/ehds-en-art-2/)
- [GDPR Art 17](https://gdpr-info.eu/art-17-gdpr/), [GDPR Art 12](https://gdpr-info.eu/art-12-gdpr/)
- [NIST SP 800-88r2](https://csrc.nist.gov/pubs/sp/800/88/r2/final), [SP 800-88r2 FAQ](https://csrc.nist.gov/files/pubs/sp/800/88/r2/final/docs/sp800-88r2-faq.pdf)
- [NIST glossary: key destruction](https://csrc.nist.gov/glossary/term/key_destruction), [destroyed state](https://csrc.nist.gov/glossary/term/destroyed_state)
- [Implementing Decision 2019/1765, consolidated text (legislation.gov.uk)](https://www.legislation.gov.uk/eudn/2019/1765/pdfs/eudn_20191765_2020-07-17_en.pdf)
- [Aikebaier, ePrint 2026/1109](https://eprint.iacr.org/2026/1109)
- [Rak (2024), Cambridge core reader](https://core-prod.cambridgecore.org/core/product/1A05C6D0FB24313674C33037A3E98164/core-reader)
- [Stortinget lovvedtak 80 (2025–2026)](https://stortinget.no/no/Saker-og-publikasjoner/Vedtak/Beslutninger/Lovvedtak/2025-2026/vedtak-202526-080/)
- Local: `sources/TEHDAS2_D7.4_v1.2.pdf`, `sources/UCC_Regulation_952_2013_OJ_text.md`, `sources/helsedir_retention_correspondence_2026-10.md`
