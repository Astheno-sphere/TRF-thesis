# Round 5 — Combined Revision & Assembly Plan

**11 October 2026. Merges João's final review (7 points), his 20 Round-5 comments + 23 tracked edits (`review5_JF_2026-10-10.docx`), and the adversarial review (`ADVERSARIAL_REVIEW_2026-10-11.md`) into one ordered, de-conflicted, patch-sequenced plan.** Base: branch `joao-base`, HEAD `dfe9dbe` (B-55), TRAIL INTACT. He reviewed the current submission (R5 OLD-texts matched `VERA-SNARK_Thesis_SUBMISSION.md` verbatim). He wants the revised draft back once before submission. Target 14 Nov.

Rules unchanged: chapter text only via `handoff_tools/patch.py`; commit only via `handoff_tools/commit.sh` (gates on TRAIL INTACT); every new source verified before it enters; independent audit before delivery; verify by diffing the artefact, never trust the trail.

---

## A. The fork that sets the schedule — Tiger decides

**Expert pilot (João point 6).** João now ranks it optional ("otherwise submit"). Two branches:
- **PILOT:** file Sikt notification **this week** → 2–3 expert walkthroughs → report as indicative pilot in Ch5/Ch6; rewrite §3.8/§6.6 to "executed, limited." Biggest single A-move; Sikt lead 4–6 wks is the risk against 14 Nov.
- **NO PILOT (default recommendation):** strengthen the deferral justification in §3.8 and §6.6, naming João's own prior endorsement of deferral and the new indicative-pilot suggestion, so the record shows a supervised, revisited choice. Ships on time.

Recommendation: **NO PILOT unless Sikt can be filed in the next 2–3 days**, because the schedule risk outweighs the marginal gain João himself now calls optional. Everything in B–E proceeds regardless of this fork.

---

## B. Work order — by leverage, each section touched once

Each chapter gets ONE coordinated pass that does reframe + legal + comment-resolution + de-duplication together, so no section is edited twice. Length cut is folded into each pass, not bolted on last, EXCEPT the global cross-section de-duplication sweep (W7) which must run last to see the whole.

| Wave | What | João | Adversarial | Patch IDs | Owner |
|---|---|---|---|---|---|
| **W1** | **Reframe the contribution.** Abstract + §1.3/§1.4 + §2.10 + §4.7 + §7.2: lead with "formal characterisation (verifiability as explicit parameter) + derived mechanism"; state Props 1–3 are simple and the weight is the legal analysis + mechanism; present tri-lateral/Cor 1.2 as the *sharpest instance* that **survives as bilateral under the narrow reading**. Front-load the §4.7 concession. | 2 | **A1, A2** (the grade-deciding move) | P60 | Claude |
| **W2** | **Relabel Proposition 4 → Observation 4** (or state its legal premise inside it); fix every cross-ref (abstract, §1.3, §4.10, §6.1, §6.11, §7.1). | 2 | [14] | P61 | Claude |
| **W3** | **Unify contribution labels** (do NOT flatten count): §7.2/Front Matter = 4 deliverables (already identical); rename §6.9 "three contributions" → "three theoretical implications"; §2.10 = "novel core (three)" nested in the four; state 4-gaps→4-contributions mapping once. | 2 | [3] / H-3 | P62 | Claude |
| **W4** | **Close legal gaps.** (a) Controller of the audit repository: add para from **Implementing Decision (EU) 2019/1765 Art 7** — MS national authority = controller, Commission = processor; names who bears the erasure duty (verified). (b) Clinicians'/researchers' own Art 17 rights over accessor fields, covered by Art 17(3)(b). (c) Ten-year floor presented openly as assumption (already hedged; tighten framing to lead with "floors of differing duration"). (d) Datatilsynet enquiry: insert send date + append letter as appendix, or cut the sentence. | 3 | [9], A3, [10], [16] | P63 | Claude + **Tiger** (Datatilsynet date; confirm 2019/1765 wording acceptable) |
| **W5** | **Declaration + AI-use.** Drop the discarded-draft history from the Declaration, keep one forward sentence ("every citation checked against a primary or retrievable source"); AI-use statement reconciled with Ch4 italic note, checked against HiMolde's current generative-AI rules. **Wording agreed with João before submission.** | 4 | [1], [2] | P64 | **Tiger** (HiMolde rule text; agree wording) + Claude |
| **W6** | **Model-integrity + code.** [11] second-disjunct assumption in Prop 1; [13] state the commitment's real value + "delete+logged-deletion" near-equivalence for cross-border; [15] exhaustive search as sanity check (keep independence rationale); [17] module count 8 vs "six further"; [18] `--delta-witness` guard + re-run + re-record; [7]/[34] salt clause & [40] Synthea determinism (accept João verbatim). | 2,3,5 | [11],[13],[15],[17],[18] | P65 (prose) + P66 (code: trf_checker/app + Appendix A sync) | Claude |
| **W7** | **Length cut 48k → 30–35k + abstract/Sammendrag to 250–300.** Global de-duplication: collision stated once in §4.6, cross-ref the other 10 sites; programme-fit full in §2.7 only; drop IEA quote (§1.5); demote "Healthy Europe" (§6). **WHIPLASHER GATE: Proposition 3 (drafting test) and the invalidation-entry takeaway (§6.8) must survive prominent. A cut that removes either is rejected.** | 1 | A5-protect | P67… (per-chapter) | Claude |
| **W8** | **Add "What each reader can reuse"** (fold into §6.8 or a short subsection): Prop 3 diagnostic; invalidation entry; Table 4.1 vs TEHDAS2 IDs. Converts "argument" → "tool." | — | **A5** (goal) | P68 | Claude |

---

## C. Assembly & delivery (after W1–W8, before each handback)

1. `bash repro_package/run_all.sh` → `trail_check --full` check 11 (6/6) if any code changed (W6).
2. `python3 demo_app/trf_checker.py` reproduces Ch5 figures byte-for-byte.
3. `python3 handoff_tools/appendix_sync.py` → 14/14.
4. **Independent audit** (fresh agent, read-only, prompt pattern in `AUDIT_STATUS.md`): every João change present & reading cleanly; every comment addressed; number/citation/cross-ref consistency; **cut-integrity — nothing the argument depends on was removed** (W7's risk).
5. `python3 handoff_tools/build_docx.py --pages` into the **HiMolde template** (now in hand from `review5` — extract its styles.xml); `build_tracked.py --base <commit João reviewed>` for his tracked comparison. Open in Word, update all fields, check contents page numbers (point 5).
6. Hand revised draft to João (his explicit request) **before** final submission.

## D. End-stage (point 7, after content final)
- Tag repo release; mint **Zenodo DOI**; cite it in A.1 (replaces moving `main`).
- Add short **Preface/Acknowledgements** after Sammendrag (HiMolde convention).
- PDF only after fields updated and João's final look.

## E. Push-backs to put in the cover note to João
1. **Contribution count** — refined labels, not one flattened number (true distinction between 4 deliverables / 3 novelty claims / 4 gaps).
2. **Exhaustive search** — reframed as sanity check per your note, but its *independence* rationale kept (it caught a bug Z3's formalism-sharing could not).
3. **Novelty reframe** — the tri-lateral story is now robust to the *narrow* reading of Art 68(12): the contribution no longer bets on the broad reading you (rightly) won't force. Cor 1.2 is presented as the sharpest instance, not the load-bearing claim.

## F. Open inputs needed from Tiger
- Pilot fork (A).
- Datatilsynet enquiry send date (W4d) or agree to cut the sentence.
- HiMolde current generative-AI rule wording (W5).
- Confirm the 2019/1765 Art 7 controller paragraph is acceptable framing before it enters (W4a).
- Rak (2024) full text via HiMolde library, if obtainable (R4-C4) — else the abstract-only sentence stands with a note to João.
