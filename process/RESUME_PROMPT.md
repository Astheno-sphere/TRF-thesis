# Resume prompt — paste this into the new chat (updated 10 Oct 2026)

I am Tiger (Arshad Akhtar Abbasia), MSc Sustainable Energy Logistics, HiMolde. We are finishing my thesis "Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space" (TRF Model / VERA-SNARK), supervisor Prof. João Ferreira, submission 14 Nov 2026.

Attached: (1) `TRF_thesis_repo_2026-10-10.bundle` (git bundle of the full working repo; or the workspace zip), (2) João's newest reviewed .docx (if any), (3) this prompt.

Do this, in order, before changing anything:
1. Restore the repo: `git clone TRF_thesis_repo_2026-10-10.bundle thesis && cd thesis && git checkout joao-base` (or unzip the workspace). Clone the public artefact repo too: github.com/Astheno-sphere/TRF (needed for the viewer and for trail check 12).
2. Run `python3 handoff_tools/trail_check.py --full` (must end TRAIL INTACT) and `sha256sum -c handoff/2026-10-10/CHECKSUMS_SHA256.txt` (from the repo root; report any FAILED lines).
3. Read `HANDOFF_READ_FIRST.md` §000 (state, open items, rules, Round 5 procedure), then `handoff/2026-10-10/AUDIT_STATUS.md`, `REVIEW_TRACKER.md` (OPEN/PARTIAL rows), `NUANCES.md`, `DECISION_RECORD.md`, `CONVERSATION_LINEAGE.md` (landmarks and links to every earlier chat; transcripts in `conversation_history/`).
4. If João's .docx is attached: follow §000.5 (extract → locate → patch → comments → audit → rebuild). Tell me first which version he reviewed and what he asked, before applying.
5. Report back briefly: what you verified, what is open, what you propose — then wait for my go.

Rules: chapter text changes only via `handoff_tools/patch.py`; commits only via `handoff_tools/commit.sh`; verify every source before it enters the text; independent audit before delivery; never push to `Astheno-sphere/trf-thesis` while it is public; my style is compressed and direct, no padding.
