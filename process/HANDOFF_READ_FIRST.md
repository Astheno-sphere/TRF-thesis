# HANDOFF — READ THIS FIRST

**Project:** MSc thesis, *Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space*
**Author:** Arshad Akhtar Abbasia ("Tiger"), MSc Sustainable Energy Logistics, Høgskolen i Molde · **Supervisor:** Prof. João Ferreira
**Submission:** 14 November 2026 · **Defence:** first week of December 2026
**This section written 10 October 2026** at the end of Claude Code session `ba27033e` (https://claude.ai/code/session_01NcQq1nsLTRuJVxEX8DbgE6). Older sections (§00 onward, from 21 Sept – 2 Oct) are kept below as history; where they conflict with §000, §000 wins.

---

## 000. STATE ON 10 OCTOBER 2026

### 000.1 Where everything is

| Thing | Location / identifier | State |
|---|---|---|
| Thesis working repo | this folder, git branch `joao-base`, HEAD after commit "B-54" (see `handoff/2026-10-10/VERSION_LOG.md`) | Trail intact (`python3 handoff_tools/trail_check.py --full --remote`) |
| Portable copy of the repo | `TRF_thesis_repo_2026-10-10.bundle` (git bundle, all branches and tags) and `TRF_thesis_workspace_2026-10-10.zip` | Delivered to Tiger 10 Oct; upload to the next chat |
| Public artefact repo | github.com/Astheno-sphere/TRF, `main` at `169c99a` (R-30) | Matches `CHECKSUMS.md` (check 12 passes) |
| Private thesis repo | github.com/Astheno-sphere/trf-thesis | **Still PUBLIC — nothing pushed. Do not push until Tiger makes it private** |
| Live app | https://trfhimolde.streamlit.app/ | Runs the new `app.py` with the OLD `trf_checker` held in memory → Thesis run shows "patient link altered PASSES / does NOT match". **Fix: Tiger reboots the app (Manage app → ⋮ → Reboot)**. Two code fixes proposed, not done (§000.4) |
| Latest delivered documents | `VERA-SNARK_Thesis_SUBMISSION.docx` (sha256 `2ded452d…`), `VERA-SNARK_Thesis_TRACKED_vs_5Oct.docx` (vs commit `1983c11`, the draft João reviewed 5–6 Oct) | No PDF yet — Tiger asked not to make one until the content is final |
| João's latest review | `supervisor_review/review4_JF_2026-10-06.docx` (sha256 `e7239d40…`), extraction `review4_changes.txt`, compact diff `review4_compact.txt` | Merged (P59–P59j); tracker rows R4-* |
| Transcripts | `conversation_history/` (all earlier chats + this session, readable `.md` and raw `.jsonl.gz`) | See `CONVERSATION_LINEAGE.md` |

### 000.2 What the thesis is now (numbers to know)

- Seven chapters + Appendices A (code/reproduction), B (search log), C (evaluation instrument). Body ≈ 48,800 words incl. chapter reference lists (Ch2 12.5k, Ch4 14.0k); submission with appendices ≈ 75,500; abstract 421 words.
- Model: TRF Model; Propositions 1–4, Corollaries 1.1, 1.2 (conditional extension: broad reading of Art 68(12), patient-record granularity), 2.1–2.3. Semantics I (plaintext) vs Semantics II (accountability-preserving: V_II = m_acc ∧ c ∧ (α ∨ ι) ∧ (β ∨ ι_subj)).
- Mechanism: Crypto-Erasure by Invalidation; t_I = min(t_r+δ, t_π+6, t+P(a)) — P(a) (proactive invalidation, João M3) **specified, not implemented** (artefact runs with P = ∞).
- Artefact results (seed 20260915, 200 records): Sem I 95 violations / 90 records (37 cross-border, 53 SPE); 39 Corollary 1.2 witnesses; Sem II 0; 138 invalidated (52 Art 17, 86 Art 68(12)); 200/200 records verify; **three** tamper tests fail (actor, ground — record 100; patient link — record 3); Z3 bounded check 9/9 unsat; envelope encryption 138/138 refuse; Synthea full cohort mean payload **1,002 bytes** (re-run 6 Oct, Synthea commit d9d07a6, `-r 20260916`), subset 891.
- Code: `trf_checker.py` 551 lines (430 code lines), `app.py` 825 + `ui.py` 133 (eight-page viewer), `z3_check.py` 153, `crypto_envelope.py` 118, `synthea_layer.py` 152, `norwegian_layer.py` 135, `cross_sector_check.py` 110.
- Figures: 4.1 (mechanism, §4.8) and 5.1 (artefact modules, §5.2), drawn with Archify; sources `.archify/*/candidate.json`; render with `handoff_tools/render_figure.py`.
- Citations: TEHDAS2 D6.3 v2.0 = **2026a** (Section 7.2, page unverified); D7.4 v1.2 = **2026b**. Helsedataservice (n.d.-a) Priser, (n.d.-b) Vedtak hos HDS. Rak (2024) abstract-only, p. 928.

### 000.3 Open items (as of 10 Oct) — see REVIEW_TRACKER.md for the full list

**Tiger's to answer or do**
1. Datatilsynet enquiry **send date** (Ch7 says "sent; response pending" without a date) — R4-C11.
2. Rak (2024): get the full text through HiMolde library, or keep the abstract-only sentence and tell João — R4-C4.
3. TEHDAS2 D6.3 v2.0: open the PDF (Zenodo 10.5281/zenodo.20199187) and give the page of the "within six months … Article 68(12)" sentence in §7.2 — R4-C12.
4. Reboot the Streamlit app.
5. AI-use declaration confirmed with the coordinator; consider naming Archify — R4-C2, R3-AI.
6. Helsedirektoratet reply on the ten-year floor (email sent 5 Oct) — R3-F10.
7. Last, by Tiger's decision: length (abstract 421; programme limits), release tag + Zenodo DOI cited in A.1, logos — R4-C1, R4-C10, MIN-14, MIN-15, PRES-5, M4d, R3-RS.

**Code (proposed, not done — waiting for Tiger's go)**
- `app.py`: reload `trf_checker` at start of each run (prevents stale-module mismatch).
- `trf_checker.py`/`app.py`: per-run audit log instead of the global `AUDIT_LOG` (race between concurrent sessions can make proofs fail spuriously; log grows without bound on a long-lived server; proof cost O(n)).
- Optional: proactive invalidation as an optional run (`--proactive P`); third trigger in `z3_check.py`.

**Text/consistency (small, known)**
- `repro_package/README.md` line ~94 still says the full cohort is "deterministic and regenerable" (disproved 6 Oct); `repro_package/data/synthea_subset/README.md` line ~76 still says 1,006 for the full cohort.
- No List of Figures; "Figure 4.1/5.1" not hyperlinked (build_docx captions() handles tables only); two Ch2 tables (search rounds, Boolean protocol) uncaptioned.
- ~11 sentences > 60 words in Ch4/Ch6 (one introduced in §4.11 by P53-15, since split by P56-06 — re-check).
- Before any PDF: open in Word, update all fields (contents now carry cached page numbers from a LibreOffice render; Word recomputes).

### 000.4 How to resume in a new chat (exact)

1. Upload: the git bundle (or the workspace zip), João's newest .docx, and paste `RESUME_PROMPT.md`.
2. Restore: `git clone TRF_thesis_repo_2026-10-10.bundle thesis && cd thesis && git checkout joao-base` (or unzip the workspace).
3. Verify before touching anything: `python3 handoff_tools/trail_check.py --full` → must end `TRAIL INTACT`. Compare `handoff/2026-10-10/CHECKSUMS_SHA256.txt` with `sha256sum -c` (see that file's header).
4. Read in this order: this §000 → `handoff/2026-10-10/AUDIT_STATUS.md` → `REVIEW_TRACKER.md` (rows OPEN/PARTIAL) → `NUANCES.md` (working style) → `DECISION_RECORD.md` → `CONVERSATION_LINEAGE.md` (landmarks + chat links).
5. For a new supervisor docx, follow §000.5.

### 000.5 Procedure for João's next reviewed .docx (Round 5)

1. Save it as `supervisor_review/review5_JF_<date>.docx`; record its sha256 in `CHANGE_TRAIL.md`.
2. Establish which version he reviewed: compare a few of his OLD texts with `git log` commits (`git show <commit>:VERA-SNARK_Thesis_SUBMISSION.md | grep`). Round 4 reviewed commit `1983c11`. Build his tracked comparison later with `build_tracked.py --base <that commit>`.
3. `python3 handoff_tools/extract_review.py supervisor_review/review5_….docx supervisor_review/review5_changes.txt` → read every COMMENT and OLD/NEW.
4. `python3 handoff_tools/locate_edits.py supervisor_review/review5_changes.txt patches/P60_jf_tracked.edits.json` → rename IDs, delete artefacts, wrap as a frozen patch (copy `patches/P59_jf_tracked.py`), declare intended losses in LOST_OK, `--dry`, apply.
5. Place the manual items and answer each comment in a second patch (pattern: `patches/P59b_jf_manual.py`). Code changes go through patches too (pattern: P58 for checker + copies; P57b frozen for whole-file app changes), then re-run `bash repro_package/run_all.sh`, copy reruns to recorded outputs, sync Appendix A with `appendix_sync.block_edits` (pattern: P58b/P59c).
6. Add CHANGE_TRAIL rows (one per ID range; exact IDs), REVIEW_TRACKER rows R5-*, `assemble.py`, `trail_check.py`, commit with one line per patch starting `Pnn:` via `bash handoff_tools/commit.sh`.
7. Independent audit by a fresh agent (prompt pattern in `handoff/2026-10-10/AUDIT_STATUS.md`), fix, rebuild `build_docx.py --pages` and `build_tracked.py --base <reviewed commit>`.
8. Public repo: copy changed code/docs to /home/claude/trf (clone of Astheno-sphere/TRF), add `CHANGE_TRAIL.md` R-row, regenerate CHECKSUMS (script in this session's transcript; see VERSION_LOG), push, copy CHECKSUMS back, `trail_check --remote`.

### 000.6 Rules that hold (do not relearn them)

- Chapter text changes only through `handoff_tools/patch.py` (inspector refuses undeclared loss of citations, numbers, hedges). Never edit chapters by hand.
- Commit only through `handoff_tools/commit.sh` (refuses unless TRAIL INTACT; adds the Co-Authored-By/Claude-Session trailers). Commit identity in the public repo: default `Claude <noreply@anthropic.com>`. Never put Tiger's e-mail in a commit, header or payload.
- Every factual claim verified at the source before it enters the text; if a source cannot be read, narrow the claim and say so (Rak, D6.3 pages, Elhub spelling were handled this way).
- Supervisor's tracked wording is applied verbatim unless it is factually superseded; adaptations are logged.
- An independent agent audits each round before delivery.
- Tiger's style: compressed, direct, no flattery; "don't waste tokens"; decide-and-flag when the cost of a wrong guess is low; ask when it is a judgement only he can make.
- Do not push to `Astheno-sphere/trf-thesis` while it is public.

---

# HISTORY (21 Sept – 2 Oct sections, superseded where §000 differs)

## 00. STATE ON 2 OCTOBER 2026 — the base was reset

**The working copy is now the draft Prof. Ferreira reviewed**, not the 30 Sept migration zip.
The two differed in 29 content edits; the zip also carried the Bodø opening (H-01), added after
the draft was sent. Commit `0438daf`, tag `joao-base-v1`, branch `joao-base`. The returned file
and its text are in `supervisor_review/`. See `DECISION_RECORD.md` D-14 and `FAILURE_LEDGER.md`
F-0.

**What this means for every other section of this handoff.** Sections 3, 8a and 10 were written
about the zip. Where they describe the *text*, check the base with grep before relying on them.
Known differences on the base:
- The opening is the draft's ("the most significant data-governance transformation"). H-01 is
  proposal C-1 in `patches/` on branch `zip-base-superseded`, and its two versions disagree on
  whether Finland is connected: unverified.
- §2.2 still carries the EY "June 2025 / January 2026" dates; Art 68(12) is still paraphrased;
  §4.8 still says the salt is not destroyed; §2.1.4 still says four rounds. These are the
  draft's defects, kept because the review refers to them. Fixes are queued in `PATCHES.md`.
- The base already has five rivals, the accumulator caveats, the F+1 window, the corrected
  witness count, the addressee split and the Norwegian abstract.

**Work already done once and queued.** Patches F1–R1 and AS-01 (branch `zip-base-superseded`,
scripts in `patches/` there) answer much of M1, M2, M3 and M5 and were source-verified on 30
Sept–1 Oct. They are candidates in `PATCHES.md` Wave −1, to be re-run on this base and judged
with the supervisor's own tracked change for each passage.

**Order of work from here.** (1) Control documents and package brought into line with this
base: done 2 Oct, see `CHANGE_TRAIL.md`. (2) The supervisor's feedback, starting with the
three gating decisions DEC-1 to DEC-3 in `PATCHES.md`, with DEC-2's salt part already settled.

---

## 0a. THE LIVE WORK (as written 30 Sept)

**Prof. Ferreira delivered a detailed peer review on 30 September 2026. Nothing in it has
been actioned.** It is captured, verified against the files, and sequenced in
`SUPERVISOR_REVIEW_2026-09-30_Ferreira.md`. Four issues decide the verdict: M1, M2, M3, M5.

**Do not work down his numbered list in order.** M2 — which reading of Art. 68(12) the
thesis carries — is blocking and is the candidate's decision, not a research task. It
determines what Chapter 4 proves and whether Corollary 1.2 survives. Every Chapter 4, 6 and
7 edit is wasted until it is settled. See `DECISION_RECORD.md` O-01.

Two things his review found that none of our automated checks could see, and one that was
our own drift:

- **M2:** the thesis uses the *broad* reading of Art. 68(12) to generate Corollary 1.2 and
  the *narrow* reading to resolve it via Theorem 2. Our checks test code against stated
  model; nothing tested whether the model's halves are consistent under one reading.
- **M1:** the model splits a record into metadata and a clinical payload, and nothing ever
  established that a real audit record contains clinical content.
- **M3:** `trf_checker.py` destroys the salt at invalidation while §4.8 says it is *not*
  destroyed — and the code comment cites §4.8 as its authority. This was introduced on 28
  September by syncing the working set to the repository without checking the prose agreed.

---

## 0b. The document set, and what each is for

| File | Read it when |
|---|---|
| **`SUPERVISOR_REVIEW_2026-09-30_Ferreira.md`** | First. It is the live work |
| **`PATCHES.md`** | To do the work. Seven waves, three gating decisions, and the cascade map |
| **`DECISION_RECORD.md`** | Before reopening anything. Settled decisions with alternatives rejected; ten open decisions |
| **`SUPERVISOR_FEEDBACK_HISTORY.md`** | For what he has asked before and the patterns across rounds |
| **`FAILURE_LEDGER.md`** | Before trusting any claim, including in this file |
| **`NUANCES.md`** | Before the first reply. How Tiger works and what he rejects |
| **`MASTER_MANIFEST.md`** | To find out what a file is or whether a copy is current |
| **`VERSION_REGISTER.md`** | To verify nothing has drifted. It is the contract |
| **`CHANGE_TRAIL.md`** | For the full history — but see the failure ledger first |
| **`CONVERSATION_LINEAGE.md`** | To find which session did what, and how to reference this one |
| **`RESUME_PROMPT.md`** | The paste-ready prompt for a new conversation |
| `Viva_Preparation_Notes.md` | Partly superseded — João supplies eight questions, four of them new |

---

## 0. How to resume in a new conversation

1. Attach this file, `VERSION_REGISTER.md`, and the canonical files it lists.
2. Read sections 1–5 before touching anything. They contain the locked decisions and the corrections that must not be reintroduced.
3. Reconcile against the register: every canonical file carries an md5 checksum. A mismatch means drift — resolve it before editing.
4. Use the tools in `handoff_tools/`. Every rewrite must pass `inspector.py` (section 7).
5. Continue from section 9, which lists open work in priority order.

The rule that governs everything: **every claim is anchored to a verifiable source, and nothing is reported as done unless it was checked.** When a check can't be run, say so.

---

## 1. The thesis in one paragraph

EHDS Regulation (EU) 2025/327 puts cross-border health audit records under three kinds of obligation at once: *retention floors* (ten years for MyHealth@EU audit repositories under the eHDSI baseline; one year for Secure Processing Environment access logs under Art 73(1)(e)), the *GDPR Art 17 erasure right*, and a *deletion ceiling* (Art 68(12): data out of an SPE within six months of permit expiry). The **Tri-Lateral Retention Feasibility (TRF) Model** treats these as constraints over a single binary variable per record — payload accessibility α(a,t) — with the meaning of "verifiable" as an explicit parameter. **Theorem 1:** under plaintext verifiability (verifiable = readable) the system is infeasible whenever a deadline falls inside a retention window. **Theorem 2:** under accountability-preserving verifiability (metadata intact + commitment survives + invalidation logged) it is satisfiable for every arrival pattern and every floor. The mechanism, **Crypto-Erasure by Invalidation**, destroys a per-record key, keeps a hiding commitment and metadata, logs the invalidation as a first-class event, and performs a terminal transition at floor expiry.

**The honest size of the contribution:** it is a *reframing* — the conflict comes from an unstated assumption about what "verifiable" means, and dropping it resolves the conflict. No cryptographic primitive is new; the formal method (Feng et al. 2022) is established; Theorem 2's mathematical content is modest (the thesis says so, §4.7). Theorem 1 carries the load: it shows *some* departure from current practice is unavoidable.

---

## 2. Locked decisions — do not relitigate

| Decision | Where |
|---|---|
| Art 73(1)(e) absorbed as a second *floor instance*; model stays tri-lateral by **constraint type**, not instrument count | Ch1 §1.3, Ch3 §3.4, Ch4 §4.3 |
| Research question generalised to "audit-retention floors" | Ch1 §1.3 |
| Research question (102 words) **not shortened** without Tiger's decision | Ch1 §1.3 |
| Ch4: cross-border case first, SPE case second | Ch4 |
| Evaluation instrument stays **designed, not executed** (supervisor's recommendation, accepted). No Sikt, ethics position unchanged | Ch3 §3.8, Ch6 §6.6, App C |
| Page count over 80 acceptable if work is good | — |
| Corollary 1.2 is **conditional** on the broad reading of Art 68(12); only Cor 1.2 depends on it | Ch4 §4.6 |
| Semantics II is an *argument*, not an authority; stated as the thesis's main vulnerability | Ch6 §6.2 |
| Accumulators are **specified, not implemented** | Ch4 §4.8, Ch6 §6.1 |
| Invalidation entry is an **attestation**, not a proof | Ch4 §4.7, Ch6 §6.3 |
| Literature review is a **structured narrative review**, not systematic. No PRISMA diagram (counts not retained) | Ch2 §2.1 |
| Boolean strings in §2.1.6 are **prospective**, not a record of what ran | Ch2 §2.1.6 |
| VERA-SNARK name retained; thesis contains no SNARK; ZKP returns as future work (Aikebaier open problem 4) | Ch1 §1.6, Ch7 §7.5 |

---

## 3. Corrections already made — never reintroduce

*Facts, not a claim about the base's text: several of these are not yet in the reviewed draft. Grep before relying on one (see §00).*

These were each found, verified and fixed. A future edit that reverses any of them is a regression.

**Facts**
- NIST SP 800-88 Rev 2 is **2025** (26 Sept 2025, Chandramouli & Hibbard), not 2024.
- EHDS: adopted 11 Feb 2025, OJ 5 Mar 2025, **in force 26 Mar 2025**, applies generally **26 Mar 2027**, secondary-use Chapter IV (Arts 68, 73) applies **26 Mar 2029**. SPE implementing acts due **26 Mar 2027** (Art 73(5)).
- Helsedataservice is the **presumptive** HDAB, **not yet formally designated** (Norway had not appointed a coordinating HDAB under Arts 55–59 per the 2025 hearing response). Never "designated".
- SPUHiN D5.2 published checklists **do not address** the retention–erasure question. Never "acknowledge".
- D5.2 title: *Recommendations for minimum requirements for Secure Processing Environments in Norway*, Deliverable D5.2, Milestone M10, project 101128232. João's alternative title was not verified.
- Norwegian NCPeH pilot: live at Bodø and Stjørdal, receiving from Portugal, Czechia and (per the fork; the main line says only Portugal and Czechia; unverified) Finland; **no relevant patients had yet presented**. In 2026 the project began establishing **NCP-A** (outbound contact point). Both claims are sourced to Helsedirektoratet (2026a).
- eHOMB approval date: **12 March, year not recoverable** from the public record. Dateless is final. An earlier inference of "2025" was invalid and has been withdrawn.
- arXiv 2210.04541 is **Belen-Saglam, Altuncu, Lu & Li (2023)**, *Blockchain: Research and Applications* 4(2):100129 — **not** Haque et al.
- Benaloh & de Mare is **1994** (proceedings publication year), not 1993.
- EDPB Guidelines 02/2025 **v2.0 adopted 7 July 2026**. The "documented threat model" condition is **Aikebaier's (2026) interpretation**, not the Board's wording — attributed correctly in Ch1, Ch2, Ch4, Ch6.
- Aikebaier (2026) is a **single-author, industry-affiliated, non-peer-reviewed preprint**; the caveat travels with every use. The gap claim rests on the search rounds and regulatory silence, not on it.
- Closest prior art is the **DePaul research programme** (Scope et al., SSDBM 2022; JDI 2022; US Patent 12,425,209, 2025), not "a patent". It keeps *recoverable* keyed copies — which a ceiling forbids.
- Synthea output conforms to **US Core** profiles with US demographics, not Norwegian basisprofiler. FHIR **R4** matches Norway's version. No Norwegian clinical representativeness claimed.
- Synthetic data is **genuine Synthea output** (see `Data_Provenance_Statement.md`).
- Original May draft: **28 citations, ~14 unverifiable**.

**Structure and prose**
- Every chapter header is clean: no version stamps, no "Word count ≈", no retrofit notes.
- Limitations register is canonical in **§3.7 (eight items)**; §4.12 and §7.3 cross-reference rather than restate.
- A single APA reference list goes at the end in the submission assembly.

---

## 4. My own failure modes in this project — watch for them

Stated so the next conversation guards against the same errors.

1. **Reporting "done" before checking.** Twice I marked items "accepted" and never executed them (scalability, trust assumptions). Always grep for the change.
2. **Trusting the change trail instead of diffing.** On 28 September the public repository turned out to be *ahead* of the working set: four trail entries marked applied (D-05, A-04, A3-l, P8-03) existed only in the pushed copy, so the working set still carried a 362-line checker and an Appendix A repeating a claim D-05 had removed as false. A trail entry marked applied is a claim to check, not a fact. Diff against the repository, not only within the working set.
3. **Narrow detectors, then claiming zero.** I reported "zero dash corruptions remaining" when the detector's window was too narrow and only caught one of three shapes. Widen before claiming absence.
4. **Over-correcting.** I removed a true NCP-A claim as "unverified" because I hadn't read that paragraph of the source. Removing is not automatically safe.
5. **Invalid inference from metadata.** I dated a sentence by its page's age; the page was updated in place. Page age does not date its contents.
6. **Automated passes that corrupt punctuation.** The em-dash reduction broke paired asides into dash-then-colon and comma splices. Word-invariance checks don't catch punctuation damage.
7. **Two alternative edits both firing**, producing a duplicated clause (Ch5 §5.2). When writing alternative `replace()` calls, make them mutually exclusive.
8. **Assuming a file is empty** when the viewer just can't render its format (`.Rmd`). Ship a `.md` twin.
9. **Trusting a reviewer's claim, or dismissing it.** Both happened. Verify either way.
10. **Registering a file's checksum, then editing it.** The register went stale for the handoff itself. Compute checksums only after the final edit.
11. **Prefixing instead of replacing.** Marking an item 'COMPLETE' while leaving its old 'Remaining: …' text produced a self-contradicting entry that a fresh conversation read as still open. Replace status text; never append to it.

---

## 5. Working method Tiger requires

- Anti-drift and anti-hallucination on every change. Every claim traceable.
- Every rewrite gated by `inspector.py`. A rejection that shows only *gains* is a deliberate logged correction; a rejection showing *losses* is a regression.
- The inspector guards citations, numerals, article references, hedges and the reference list. It **cannot** see a changed meaning in plain words ("designated" → "presumptive" passes). So **every sentence is read**, not just checked.
- The inspector counts totals, so an offsetting removal and addition cancel. Check such cases by hand.
- Update `VERSION_REGISTER.md` whenever a file changes.
- Hard rule: never move to the next chapter until the research substrate (Google Sheet) reflects new findings.
- Tone: compressed, direct, no flattery. One question at most per turn. Mutual criticism licensed.

---

## 6. Where everything lives

See `VERSION_REGISTER.md` for checksums. Canonical files:

| File | Contents |
|---|---|
| `VERA-SNARK_Thesis_SUBMISSION.md` | Assembled: front matter, Ch1–7, single bibliography, App A–C |
| `Front_Matter_v1.md` | Title, abstract, contribution, declarations (incl. AI-assistance), nomenclature, TOC |
| `Chapter1_…` to `Chapter7_…` | Seven chapters, each with its own reference list for drafting |
| `code_artefacts/README_Appendix_A.md` | Appendix A: provenance, commands, full source listings, console output |
| `Appendix_B_Search_Log.md` | 59 queries, 4 dated rounds, [R] annotations |
| `Appendix_C_Evaluation_Instrument.md` | Designed, unexecuted evaluation instrument |
| `Consolidated_Bibliography.md` / `.Rmd` | 67 entries; read `.md`, knit `.Rmd` |
| `demo_app/` | **Canonical** `trf_checker.py`, `synthea_layer.py`, `app.py`, `norwegian_layer.py`, `cross_sector_check.py` |
| `repro_package/` | Self-verifying reproduction package. Modules sit at its root, data at `data/synthea_subset/`, bookkeeping scripts in `src/`. `bash run_all.sh` runs all four steps |
| `repo_synthea_subset/` | 8 untrimmed real Synthea bundles. Committed to GitHub 28 Sept; the same 8 now also in `repro_package/data/synthea_subset/` and `code_artefacts/synthea_subset/` |
| `Data_Provenance_Statement.md` | Answer to João's data blocker |
| `thesis_yaml_header.yml` | YAML: breezedark code, Word template hook |
| `handoff_tools/` | Inspector, math converter, assembly and bibliography scripts |
| `MASTER_MANIFEST.md` | **Every file, where it lives, its state and what is going on with it.** Read this when you need to know whether a copy is current |

**External:** repo github.com/Astheno-sphere/TRF · demo trfhimolde.streamlit.app · substrate Google Sheet (ID in memory) · EUR-Lex ELI http://data.europa.eu/eli/reg/2025/327/oj

**Non-canonical, kept for provenance only:** `_superseded_Chapter2_RETROFIT.md`, `_draft_Thesis_FULL_with_chapter_refs.md`.

---

## 7. Tools — in `handoff_tools/`

| Tool | Use |
|---|---|
| `inspector.py OLD NEW LABEL` | Gates a rewrite. Exit 0 = admit. Checks citations (parenthetical + narrative), numerals, article refs, hedges, reference list. Negative-tested against five corruption types. |
| `mathconv.py IN OUT` | Converts `*t*ᵣ(*a*)`-style italic unicode math to LaTeX. Skips headings, tables, code, lines with `$`. **Inspect output before committing**; it does not know about backticks. |
| `assemble.py` | Rebuilds the consolidated bibliography from chapter reference lists and the submission assembly. |

Verify Word conversion with: `pandoc FILE.md -o out.docx` then count `<m:oMath>` in `word/document.xml`. Current state (base, 2 Oct): **176 native equations, zero LaTeX or `$` leaking** (175 before the rebase; the draft adds `$t(a) + F(a) + 1$`).

---

## 8. Verification register

| ID | Item | Status |
|---|---|---|
| F-01 | SPUHiN D5.2 | Title, milestone, project number resolved from document cover |
| F-02 | EDPB CEF full report | Open, not load-bearing; recurring-issue count deliberately removed |
| F-03 | EDPB Guidelines 02/2025 | Closed: v2.0, 7 July 2026 |
| F-04 | Aikebaier SoK | Closed |
| F-05 | Haque venue | Closed as a misattribution: it is Belen-Saglam et al. 2023 |
| F-06 | TEHDAS2 SPE deliverable | Closed: D7.4 |
| F-08 | Implementing acts | Closed: due 26 Mar 2027 |
| F-09 | Walonoski Synthea | Closed |
| F-10 | eHOMB year | **Closed: not recoverable; dateless final** |
| F-11 | EUR-Lex Art 73(1)(e) | **Closed at primary source**: official OJ text retrieved, and Tiger read the page |
| F-12 | In-force vs applies-from | Closed |

---

## 8a. Completed — do NOT redo

Each item below is finished and verified. A fresh conversation must not repeat it.

| Item | Result |
|---|---|
| Sentence pass 1 | Every prose sentence over 55 words resolved. Three deliberate exclusions: the TOC list, the research question, the Semantics II formal definition |
| Sentence pass 2 | **Complete across all chapters.** Every 41–55-word sentence screened; structurally complex ones read in full and 21 split; parallel lists left. Simple sentences screened by structure, not read individually |
| Math to LaTeX | 176 native Word equations (base, 2 Oct), zero LaTeX or `$` leakage (verified via pandoc) |
| Em-dash corruption repair | 48 broken dash pairs and comma splices found and repaired |
| P2E2 source | Read and integrated into Ch2 §2.5 as Chakraborty et al. (2025), PVLDB, peer-reviewed |
| F-10, F-11 | Both closed (see §8) |
| DOIs | Hevner, Finck 2018, Benaloh (and year corrected to 1994), arXiv items, Peffers, EU regulations |
| Supervisor feedback, two rounds | All accepted items applied; evaluation left designed-not-executed by agreement |
| Synthea subset on GitHub | **Done 28 Sept.** Eight untrimmed bundles at `data/synthea_subset/` in `github.com/Astheno-sphere/TRF`, with `requirements.txt`, `docs/expected_trf_output.txt` and `norwegian_docs/HOW_TO_RUN.md`, all of which the 23 Sept web upload had silently dropped. Verified from a fresh clone: checker byte-identical to `docs/expected_trf_output.txt`, layer reads 8 bundles, mean payload 891 bytes, six measures identical, 200/200 commitments differing. Do not regenerate Synthea: these are the files Chapter 5's 891 was measured on |
| Working set resynced to the repository | **Done 28 Sept.** The repository was ahead. `trf_checker.py` 362 → 363 lines with the §4.8 salt destruction, `synthea_layer.py` gains the three-directory fallback, Appendix A corrected in all four copies including the assembled submission. See failure mode 2 |
| App feature audit | **Done 28 Sept.** Two reported results had no viewer anywhere: the independent exhaustive cross-check (Ch5 §5.4) and the δ witness (§5.5a). Both now run from Tab 5 with pass/fail banners. Cross-check agrees with the recorded run on all four cases; δ witness returns 90/95 and 89/94, matching Table 5.2a. `cross_sector_check.py` needed nothing — it has been on GitHub and wired into Tab 4 since 23 Sept |
| Recorded run per command | **Done 28 Sept.** Five files in `docs/`, one per command. Previously only the checker had one, so a reader could not tell a changed file from a changed result for the other four |
| Redundancy sweep | **Done 28 Sept.** The eight bundles existed in three working-set copies plus GitHub; now one working copy plus GitHub. Stray root duplicates of the code, the two stray result files and the stale migration zip removed. 133 MB → 45 MB, 95 → 78 files |
| Assembly reproducibility proven | **Done 28 Sept.** `handoff_tools/assemble.py` rebuilt the submission and the bibliography; both came back **byte-identical**. `handoff_tools/inspector.py` returned **ADMIT** on old-against-rebuilt: citations, numerals, article references, hedges and reference list all identical |
| Reproducibility package repaired | **Done 28 Sept.** Modules moved to the package root so the layer resolves `data/synthea_subset/` and the Norwegian modules can import the checker; `run_all.sh` no longer skips the realism layer; both cohort runs recorded separately. `bash run_all.sh` exits clean |

## 9. Open work, in priority order

**Superseded by the supervisor review.** The authoritative list is now
`SUPERVISOR_REVIEW_2026-09-30_Ferreira.md` with the open decisions in `DECISION_RECORD.md`.
Sequence, which is *not* his numbering:

1. **O-01 / M2 — settle the Art. 68(12) reading.** BLOCKING. Candidate's decision. Put the
   options to him; do not decide it alone.
2. **O-02 / M1 — ground p(a) in a real audit-record format**, or reframe Semantics I.
   Research, then a decision. May change the model.
3. **O-03 / M3 — salt and ciphertext design.** Independent, cheap, embarrassing. Do early.
4. **M5 — primary sources**: the ten-year floor; SPUHiN "finalised" claims; verbatim
   Art. 68(12) and 73(1)(e) from the OJ; the §2.2 EHDS dates.
5. **M4 — propositions, promote §6.9a into Chapter 4, hash-chain integrity in V_II.** The
   V_II tamper test should be done regardless of the renaming decision.
6. **M6 — traceability matrix** against TEHDAS2 D7.4 and the SPUHiN checklist. Reword
   Appendix C item A1; João has released us from our own constraint in writing.
7. **M7 — logistics framing**; state programme fit in §1.5.
8. **Meta-commentary, repetition, length**; move the Version and Change Record to the
   repository; slim Appendix A.
9. **Minor-issues table**; renumber sections and appendices; regenerate the TOC.
10. **Tag the repository and mint a Zenodo DOI.** The thesis cites a moving `main`.

Carried forward and unchanged by the review: two unread arXiv sources (aiAuthZ 2607.05518,
privacy-engineering SLR 2606.23696); two figures (record-state diagram §4.8/§5.6, regulatory
timeline §6.8) — the thesis still has **zero**; the HiMolde template, unobtainable from this
environment; Datatilsynet sounding; Sikt notification if the evaluation is run.

**Closed, do not redo:** the four DOIs; bibliography link coverage (67/67); the Synthea
subset on GitHub; em-dash reduction; the Word conversion toolchain.

---

## 10. Key figures — verified, reproduce exactly

| Result | Value |
|---|---|
| Semantics I: records with violation | 90 / 200 |
| Semantics I: total violations | 95 (41 C2-only, 44 C3-only, 5 both) |
| Corollary 1.2 witnesses (no erasure request) | 39 |
| Semantics II: violations | 0 |
| Records invalidated | 138 (52 Art 17, 86 Art 68(12)) |
| δ = 3 witness | 89 records / 94 violations; Cor 1.2 still 39; Sem II still 0 |
| Synthea payload mean | 1,006 bytes (98-bundle cohort); 891 bytes (8-bundle subset); all six measures identical in both |
| Reference commitment, record 100 | `11087780fd192c8f…` |
| Seed | 20260915 |

`python3 demo_app/trf_checker.py` must reproduce these byte-for-byte.
