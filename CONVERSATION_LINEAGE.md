# Conversation Lineage

Where the work happened, so a future session can be pointed at the right transcript rather
than guessing.

---

## Sessions

| # | When | Surface | Identifier | What happened |
|---|---|---|---|---|
| 1 | 25 May 2026 | claude.ai chat | `conversation_history/2026-05-25-23-16-30-vera-snark-thesis-build.txt` | Original VERA-SNARK build. Produced the draft later abandoned for fabricated citations |
| 2 | 29 May 2026 | claude.ai chat | `conversation_history/2026-05-29-18-12-42-vera-snark-thesis-build.txt` | Verification and correction round |
| 3 | 15 Sept 2026 | claude.ai chat | `conversation_history/2026-09-15-02-29-25-vera-snark-thesis-resume-retrofit.txt` | Resumption; retrofit of Ch1–Ch2 |
| 4 | 15 Sept 2026 | claude.ai chat | `conversation_history/2026-09-15-02-42-38-trf-thesis-sheet-patch-ch3-unblock.txt` | Substrate patch; Ch3 unblocked |
| 5 | 15–21 Sept 2026 | claude.ai chat | `conversation_history/SESSION_LOG_15-21_Sept_2026.md` — **no transcript exists** | Ch3–Ch7 written, theorems penned, checker built, migration package prepared. The log is the only record |
| 6 | 21 Sept 2026 | claude.ai chat | *(transcript not captured)* | Migration handoff prepared. **Wrote the D-05, A-04, A3-l, P8-03 and H-01 trail entries that were never applied** |
| 7 | 28–30 Sept 2026 | **Claude Code / this session** | **`session_01FPbdSPsPKYDLpxAt9wbLiy`**<br>`https://claude.ai/code/session_01FPbdSPsPKYDLpxAt9wbLiy` | Synthea subset to GitHub; repository repair; citation link pass; em-dash pass; Word formatting; table rules; viva notes; this handoff |

**Session 7 is the current one and holds the most detail.** A future session can be told to
consult it by that identifier for anything this handoff summarises too tightly.

---

## What session 7 did, in order

Useful because several findings only make sense with their sequence.

1. **Synthea subset pushed to GitHub.** 8 untrimmed bundles at `data/synthea_subset/`.
   Discovered the 23 Sept web upload had flattened directories and silently dropped
   `requirements.txt`, `docs/expected_trf_output.txt` and `norwegian_docs/HOW_TO_RUN.md`.
2. **Found the repository was *ahead* of the working set.** Four trail entries (D-05, A-04,
   A3-l, P8-03) existed only in the pushed copy. Resynced — and in doing so propagated the
   salt line that João's M3 later flagged.
3. **Repaired the reproducibility package.** It could not run its own realism layer.
4. **Added app Tab 5** — the exhaustive cross-check and δ witness had no viewer anywhere.
5. **Citation link pass.** 68 entries with 41 locators → 67 with 67. Removed two entries as
   documents that do not exist as cited. Corrected six citations on year, title or author.
   Added Appendix B Round 5.
6. **Em-dash pass.** 230 → 110. Found a surviving corruption in Appendix B.
7. **Word formatting.** Built `thesis_reference.docx`; discovered page size was unset;
   applied booktabs table rules after rendering to PDF and looking at it; discovered
   LibreOffice renders no OMML equations.
8. **Appendix C §C.1a** provisionality statement; **Appendix A** provenance entry.
9. **Found H-01 was never applied** — the unsourced superlative was still the opening
   sentence of the thesis. Applied it.
10. **Wrote `Viva_Preparation_Notes.md`** — now partly superseded by João's eight questions.
11. **Received João's peer review** (30 Sept) and built this handoff.

---

## Artefacts outside this workspace

| What | Where |
|---|---|
| Public repository | `github.com/Astheno-sphere/TRF` — 6 commits, latest `dba9c56`. **Cite a tag, not `main`** |
| Live demonstration | `trfhimolde.streamlit.app` — 5 tabs. Unreachable from the container; the candidate confirms it |
| Research substrate | Google Sheet `1TLb5UWXQXMIxyf5QgRZQhtXv-wtE3HE6rO732nkmx1Q`, 17+ subsheets |
| Substrate patches | `Substrate_FINAL_PATCH.xlsx` (16 Sept) and `Substrate_ARTEFACT_PATCH_28Sept.xlsx`, the latter also uploaded to the same Drive folder |
| EUR-Lex primary text | `http://data.europa.eu/eli/reg/2025/327/oj` — the candidate has read it directly |

---

## How to reference this lineage from a future conversation

Tell the new session:

> The prior work is Claude Code session `session_01FPbdSPsPKYDLpxAt9wbLiy`
> (`https://claude.ai/code/session_01FPbdSPsPKYDLpxAt9wbLiy`). If something in the handoff is
> too compressed, ask me and I will pull the detail from there. Earlier sessions are in
> `conversation_history/` as raw transcripts; the 15–21 September work has no transcript and
> exists only as `SESSION_LOG_15-21_Sept_2026.md`.

And warn it, because this is the lesson of the whole lineage:

> Trail entries written in sessions 5 and 6 have been wrong five times. Diff against the
> artefact, never against the record.
