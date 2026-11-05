# Code Review: Findings and Resolutions

*Supplement to Appendix A. Two review passes over the artefact, 6 November 2026, and what was done about each finding.*

| | |
|---|---|
| Pass 1 | External review in the style of CodeRabbit, on a fresh clone of branch `joao-base` at `9d69d7c` (2 Nov). Three readers: core logic; demo app and reproducibility; tooling and hygiene. |
| Pass 2 | A deeper read-only hunt for what pass 1 missed, run against `main` while the pass-1 fixes were being made, so it also caught a flaw in one of those fixes. |
| Rule applied | Every finding was reproduced or checked against the code before anything changed. A finding that did not hold is marked as such. No result-producing number was allowed to move. |
| Code repository | https://github.com/Astheno-sphere/TRF, commits `fb2650e`, `dc9d4c0`, `067baec`, `8f785e3` (CHANGE_TRAIL rows R-33 to R-36); release 1.3.0 |
| Thesis repository | patches P115 (code and packaging sync), P116 (Appendix A listings), P117 (thesis text), P118 (checksums), P119 (viewer), P120 (release 1.3.0 cited); CHANGE_TRAIL rows P115 to P120 |

## 1. Verdict

Both passes confirm the result itself. A fresh run reproduces every reported figure byte for byte: Semantics I 95 violations across 90 of 200 records, 39 Corollary 1.2 witnesses, 138 invalidations (52 under Article 17, 86 under Article 68(12)), Semantics II 0 violations, 200 of 200 records verifying against the audit log, and all three tamper tests detected. The modules shared by `code_artefacts/`, `demo_app/` and `repro_package/` were and remain byte-identical.

What was broken was the verification story around those numbers: a reproduction README whose first check gave the wrong value, tests the thesis repository did not contain, commands that did not run from the folder they were written for, two guarantees worded more strongly than the code supports, an ungated Word build, and an inspector that could not pass on any machine but the author's. All of that is fixed. After the fixes:

- **All eight recorded runs are byte-identical** to fresh runs, except two lines reworded on purpose (Section 4); `repro_package/run_all.sh` diffs clean on all seven of its comparisons.
- **56 automated tests pass**, in the code repository and now also from `demo_app/` in this repository.
- **The trail inspector passes every check** (`handoff_tools/trail_check.py`: TRAIL INTACT), including check 14, the full replay, which had failed since October. That failure was a flaw in how the check replayed files, not an unlogged edit; Section 5 explains.

## 2. Pass 1 findings

### Critical

| # | Finding | Verified | Resolution |
|---|---|---|---|
| C1 | `repro_package/README.md` gave the reference commitment of record 100 as `11087780fd192c8f…`; the run prints `678ade47c1e6dc03…`. An examiner following the README's first check would conclude a correct reproduction had failed. | Yes. The same stale value was also in the code repository's `norwegian_docs/HOW_TO_RUN.md` (pass 2). | Corrected in both. The README's integrity table was rebuilt from `results/trf_output.txt` and Chapter 5, row by row. |

### Major

| # | Finding | Verified | Resolution |
|---|---|---|---|
| M1 | The 54 tests the README and Appendix A cite were not in this repository. | Yes | `demo_app/` now carries `tests/` and the recorded runs in `docs/`; `cd demo_app && python3 -m pytest -q tests/` passes 56 tests, including the two verbatim-quote tests, which now find the thesis one folder up. |
| M2 | Appendix A.5 commands failed from `code_artefacts/`. | Yes | A.5 now says where the commands run: the release root, `repro_package/` or `demo_app/`, all of which match the release layout. `code_artefacts/` is for reading beside the appendix; `DATA_LOCATION.md` says so. The realism layer also finds the subset at `../repro_package/data/synthea_subset/`. |
| M3 | The Merkle log detects divergence between a record and its log, not a rewrite of the log. | Yes | Stated in the code (`MerkleLog` docstring) and in Chapter 5, Section 5.7: a rewrite needs a root published outside the log, which Chapter 6, Section 6.1 specifies and the code does not implement. |
| M4 | Semantics II: C2 and C3 hold by construction; only the integrity check can fail. | Yes | Stated in the `check_semantics_II` docstring and in Section 5.7, which now names the integrity check as the falsifiable part of the result. |
| M5 | `brute_force_semantics_I` answered wrongly when the horizon left retention months unexamined. | Yes, outside the thesis's own calls | Now raises `ValueError` on such a horizon; precondition documented; new test. The checker also compares the cross-check with itself on its four cases and fails on a disagreement. |
| M6 | Repro README pointed at `src/trf_checker.py`. | Yes | Paths corrected; every command in the README and `run_all.sh` run from a clean state. |
| M7 | `demo_app/` could not find the Synthea subset. | Yes | Solved without a second 40 MB copy: the layer's search path includes the repository's one copy. |
| M8 | The global audit log grew with every rerun of the hosted app. | Yes (4,380 leaves after ten runs) | See Section 3, item P2-C1: the first fix was itself flawed. Each population now has its own log, bound to each record when it is created. Ten runs leave 438 leaves; the test suite runs in 13 s instead of 22 s. |
| M9 | `demo_app/README.md`: stale figures (35, 940) and table numbers. | Yes | Rewritten from Chapter 5: 43 / 891 / 1,002 bytes; Tables 5.3, 5.6, 5.7. |
| M10 | Repro README cited Tables 5.1 and 5.2 for results in Tables 5.3 and 5.4. | Yes | Corrected in the rebuilt table. |
| M11 | `demo_app/README_repo.md` was a stale copy of an older README. | Yes | Replaced by a two-line pointer to the code repository's README. |
| M12 | `trail_check.py` constants (`main`, `joao-base-v1`) did not match the reviewed clone. | Partly | The reviewer cloned branch `joao-base`, which lags `main`; on `main` the branch constant is right. The tag `joao-base-v1` had never been pushed, so no other machine could run checks 2 and 14: now pushed. `sh()` now fails loudly on a non-zero exit instead of returning empty output. |
| M13 | `trail_check.py` crashed without pandoc; check 4 could not read "P107-P111:" commit lines; HEAD was committed past a failing check 14. | Yes | pandoc is checked with a clear message (also in `verify_base.py`); check 4 reads patch ranges; check 14 was redesigned (Section 5) and now passes. |
| M14 | The submission `.docx` was ungated: `#` page numbers in a plain build, unchecked LibreOffice failures, non-atomic overwrite, no content assertions. | Yes | `build_docx.py` now runs the page-number pass by default (85 of 90 entries filled; Word fills the rest on opening), fails if LibreOffice or pdftotext fail or no page number is found, refuses to write a build with no tables, contents or links, and writes to a temporary file that passes a CRC check before replacing the submission. New trail check 15 confirms the `.docx` exists, is newer than the assembled text and carries its headings, tables and page references. |
| M15 | `CHECKSUMS.md` in this repository described the code repository. | Yes | Now lists this repository's own code copies (44 files); the code repository keeps its own. Trail check 12 now reads the code repository's `CHECKSUMS.md` instead of this one. |
| M16 | `concordance.py --check` passed vacuously from another directory. | Yes | Paths anchored to the repository; missing files or zero references now fail. |

### Minor and nits (pass 1)

| Finding | Resolution |
|---|---|
| `key_id_commitment` is an unsalted digest of a predictable toy key | Documented in the code as a key-identifier digest, not a hiding commitment. Changing it would change the printed log root; the toy keys are themselves predictable. |
| Derived salts repeat with period 256 | Documented; the 200-record run stays inside one period. |
| `crypto_envelope` crashed on `InvalidTag` | Counted as refused, in the module and at both decrypt sites in the app. |
| Z3: accountability conjuncts instantiated true; no timeout; full model printed on SAT | Comment added; 120 s timeout per check (unknown counts as failure); a verdict line instead of the model. Chapter 5, Section 5.5 already disclosed the first point. |
| `integrity()` weaker than `V_II`; delta-witness not in the exit code | The delta witness now fails the exit status on any Semantics II violation; the reported 200/200 is the integrity check by design, and Semantics II itself is reported through `V_II`. |
| Pseudonyms `PSN-{rid % 100}` collide | Documented: 100 synthetic patients, so records share patients as real logs do; no figure depends on uniqueness. Changing it would change the log root. |
| `run_all.sh` header "1/4" with six sections; footer "six" with seven diffs; 1,006 | Fixed: 1/6 to 6/6, seven, 1,002 (with both cohorts named in the provenance statement). |
| Repro README called `requirements.txt` empty; pins differed between copies | Rewritten; the same pins (`cryptography==50.0.1`, `z3-solver==5.3.3.0`) everywhere. |
| No Python version stated | Appendix A.4 and both READMEs: tested on Python 3.11 to 3.13; CI now runs all three. |
| Google Fonts versus "no network required" | `demo_app/README.md` now says fonts load from Google Fonts online and fall back offline. |
| Licence "add one before making public" | Already MIT in the code repository; the stale line is gone. |
| `.gitignore` one line | Now ignores `*.pyc`, `.pytest_cache/`, a regenerated `synthea_run/` and `synthea.jar`. |
| Tooling nits in `build_docx.py`, `build_tracked.py`, `trim_inspector.py`, `assemble.py` (duplicate imports, dead code, weak error messages) | Not changed: none affects an output, and the tools are frozen for submission. Listed here so they are not mistaken for unknown. |
| Archive holds two raw session transcripts (`archive/conversation_history/`) | Not changed; the author decides before sharing the repository. No credentials were found in the reviewed scope. |

## 3. Pass 2 findings (what pass 1 missed)

| # | Finding | Verified | Resolution |
|---|---|---|---|
| P2-C1 | **The first audit-log fix was flawed.** Records were attached to a log only when first invalidated, so two populations generated before invalidation shared one log, and records built directly (Norwegian and cross-sector modules, Explore page) wrote into whichever log was current, on the server possibly the cached thesis population's. A first attempt that cleared the log on every rerun crashed the cached population. | Yes (438 leaves became 933 after one Norwegian and one cross-sector run) | `Record(..., log=)` binds the log at creation; `generate()`, the Norwegian and cross-sector builds and the Explore page each start their own log and pass it explicitly, so concurrent sessions cannot swap it under a population. New test: an earlier population's log is untouched by later runs and still verifies. |
| P2-M1 | Line counts in Table 5.1, §5.2 and Appendix A disagreed with the files and each other. | Yes | Regenerated with `wc -l` at the final code (P117); the non-comment count is 466. |
| P2-M2 | §5.2 said payloads are drawn from Synthea; the reported run uses constructed payloads (43 bytes). | Yes | §5.2 now says so; Synthea serves the comparison of §5.8 only. |
| P2-M3 | Two Synthea cohorts were conflated (16 September, without `-r`, which gave the subset and 1,006 bytes; 6 October, with `-r 20260916`, which gave Table 5.7's 1,002 bytes). | Yes | `Data_Provenance_Statement.md`, the subset README and `HOW_TO_RUN.md` now name both, in both repositories. |
| P2-M4 | The cross-sector "no violations" under Semantics II does not test the whole log entry the § 17 limit reaches. | Yes | Chapter 6, Section 6.10 now says the zero is narrower: the accessor fields outlive the three years unchecked; the module's docstring says the records reuse the health model's grounds and field names. |
| P2-M5 | Personal and process material is public (supervisor review files, the Helsedirektoratet correspondence, a hash map naming commit rewrites). | Yes | Not changed. The author has decided the repositories stay public until he makes them private; Appendix D is reproduced with the sender's permission. |
| Minor | "Shows a failure notice rather than results" was false: the page shows results, then the notice. | Yes | Thesis text (§5.8, Appendix A) now says "beside the results". |
| Minor | The Semantics II row of the record life strip was drawn, not computed. | Yes | Computed from `V_II` per month; a failing month shows as "fails its check". |
| Minor | App: verdict said "Semantics II holds" even on failure; Explore caption gave 6/π (600% at π = 1); record horizon capped at 130 although a floor can end at 131. | Yes | Fixed: conditional verdict, min(6, π)/π, horizon to 134. |
| Minor | Exit status ignored undetected tampering, failed proofs and cross-check disagreement; the realism layer exited 0 on divergence. | Yes | The checker now fails on any of them; the realism layer exits 1 on divergence. |
| Minor | Ties in the invalidation ground were broken silently. | Yes (4 records) | Documented: on a tie the data subject's request names the ground. |
| Minor | Overclaims: "real FHIR", "proved against the root", `del dek` "only the wrapped copy survives", an always-true "metadata intact" flag. | Yes | Reworded to synthetic, "checked by inclusion proof", no erasure claim, and a printed log-integrity result. |
| Minor | CI tested Python 3.12 only; README said 54 tests. | Yes | CI matrix 3.11 to 3.13; 56 tests. |

## 4. What changed in the recorded outputs

Two printed lines changed on purpose, and both recorded runs were re-recorded:

- `norwegian_layer.py`: "metadata intact=True" (always true) became "log integrity=True" (computed).
- `synthea_layer.py`: "IDENTICAL under real FHIR payloads" became "IDENTICAL under Synthea FHIR payloads".

No other line of any recorded run changed. No figure in the thesis changed.

## 5. Why check 14 failed, and why it passes now

Check 14 replays every logged patch from the tag `joao-base-v1` and compares the result with the files on disk. It skipped the D0 rebase that P01 is written against, and it started every file from its tag state, although many files gained content outside the patch log before their first patch: files created later (Appendix D) and code synced from the code repository. The replay therefore failed by construction for those files, and a genuine unlogged edit would have produced the same symptom, so the failure proved nothing either way.

The check now includes D0 and starts each file from the state its first logged patch began from: the tag's copy when the checksums agree, otherwise the committed version whose checksum equals that first logged "before" value. A file with no such committed state fails the check by name. Every one of the 48 files now replays exactly, so the patch log fully accounts for every change it took over.

## 6. Left as they are, deliberately

- **No anchored log root.** Publishing the root outside the log is specified (Chapter 6, Section 6.1), not built.
- **Constructed toy keys and derived salts.** For reproducibility; `--random-salts` exists; destruction is attested, not proven.
- **Tooling nits** that affect no output (Section 2, last rows).
- **Public process material** (P2-M5): the author's decision.

## 7. Release

The reviewed code, with the viewer design pass that followed it, is release 1.3.0 (https://doi.org/10.5281/zenodo.23989242, code repository commit `8f785e3`), which the thesis now cites in the abstract footer and Appendix A.1. It produces the same figures as releases 1.0.1 to 1.2.0.

## 8. How to check this yourself

```bash
cd repro_package && ./run_all.sh          # then the seven diffs it prints: all empty
cd ../demo_app && python3 -m pytest -q tests/   # 56 passed
cd .. && python3 handoff_tools/trail_check.py    # TRAIL INTACT (needs pandoc)
```

Regenerate `CHECKSUMS.md` after a change:

```bash
python3 - <<'EOF'
import pathlib, hashlib
fs = sorted(p for d in ("code_artefacts", "demo_app", "repro_package") for p in pathlib.Path(d).rglob("*")
            if p.is_file() and p.suffix in (".py", ".txt", ".sh", ".md")
            and "synthea_subset" not in str(p) and "__pycache__" not in str(p) and "results/" not in str(p))
for p in fs:
    b = p.read_bytes(); print(f"| `{p}` | {hashlib.md5(b).hexdigest()[:12]} | {b.count(b'\n')} |")
EOF
```

## 9. After the review: viewer design pass (release 1.3.0)

A presentation-only pass on the viewer, so that it reads as one walk rather than a list of pages: navigation grouped into the seven numbered steps of the walk, then full runs, then context that is not a thesis claim; the selected page marked by a rule instead of a radio dot; a brand mark of three bands in the diagram palette (retention floor, deadline, accountable); fact cards ruled in the colour of what each quantity is in the model; alerts in the palette instead of the framework's blue; a progress strip for the walk that names the next step; the framework's deploy toolbar hidden. No computation changed, and the 56 tests pass. Code repository commit `8f785e3`, thesis patches P119 and P121.
