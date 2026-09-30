# Resume Prompt — paste this into the new conversation

Attach `TRF_Thesis_Migration_Package_30Sept.zip` and paste everything below the line.

---

I am Tiger (Arshad Akhtar Abbasia), MSc Sustainable Energy Logistics at Høgskolen i Molde.
Thesis submission 14 November 2026, defence first week of December. Supervisor Prof. João
Ferreira. We are resuming work that has been running since May 2026.

The attached archive is the complete working set. Unpack it and read these five files
before doing anything else, in this order:

1. **`HANDOFF_READ_FIRST.md`** — orientation, locked decisions, open work
2. **`SUPERVISOR_REVIEW_2026-09-30_Ferreira.md`** — my supervisor's peer review. **This is
   the live work.** Nothing in it has been actioned
3. **`DECISION_RECORD.md`** — what is settled and why, and the ten open decisions
4. **`FAILURE_LEDGER.md`** — every failure mode observed, and the rule from each
5. **`NUANCES.md`** — how I work and what I react badly to

Then `MASTER_MANIFEST.md` for every file, `VERSION_REGISTER.md` for checksums,
`CHANGE_TRAIL.md` for the full change history, and `CONVERSATION_LINEAGE.md` for where the
work happened.

**Verify before you trust.** Run these four and tell me the results:

```bash
cd <unpacked>
python3 -c "import hashlib,re,pathlib; s=pathlib.Path('VERSION_REGISTER.md').read_text(); \
bad=[(m.group(1).strip()) for m in re.finditer(r'^\| [A-Z]+ \| ([^|]+?) \| ([0-9a-f]{12}) \|',s,re.M) \
if not pathlib.Path(m.group(1).strip()).exists() or hashlib.md5(pathlib.Path(m.group(1).strip()).read_bytes()).hexdigest()[:12]!=m.group(2)]; \
print('register mismatches:',len(bad),bad)"
python3 handoff_tools/assemble.py          # byte-identical rebuild is the pass
bash repro_package/run_all.sh              # all five recorded runs must match
git clone --depth 1 https://github.com/Astheno-sphere/TRF /tmp/trf && \
  cd /tmp/trf && python3 trf_checker.py | diff - docs/expected_trf_output.txt && echo OK
```

**The single most important thing to understand about this project:** five entries in the
change trail were marked applied and were not. One of them, H-01, left an unsourced
superlative as the opening sentence of my thesis for nine days after it was recorded as
fixed. **Diff against the artefact, never against the record.** If you tell me something is
done, I will check.

**Second most important:** the submission `.md` is *generated* by `handoff_tools/assemble.py`
from the chapter files. Editing it directly gets wiped on the next rebuild. Edit chapters,
then rebuild.

**Where to start.** João's review has four issues that decide the verdict: M1, M2, M3, M5.
Do not work down his numbered list in order — the dependency runs the other way:

- **M2 is blocking and is my decision, not a research task.** Which reading of Art. 68(12)
  the thesis carries determines what Chapter 4 proves and whether Corollary 1.2 survives.
  Read `DECISION_RECORD.md` O-01, then put the options to me. Every Chapter 4/6/7 edit is
  wasted until this is settled.
- **M1 next** — it may change the model.
- **M3 any time, and early** — it is cheap and the code currently cites the very section it
  contradicts.
- **M5, minor issues, meta-commentary, length** — mechanical, run in parallel.

Six weeks remain.

**How I work:** compressed and direct, no flattery. One question maximum per turn. Push back
rather than agree — if I assert something wrong, show me the evidence. Nothing is done until
it is applied in the chapter file, the assembly, the repository, the register and the change
trail. Anti-drift and anti-hallucination checks on every change; anchor every claim to
something actually retrieved or executed.

**Prior detail.** This work continued in Claude Code session
`session_01FPbdSPsPKYDLpxAt9wbLiy` (`https://claude.ai/code/session_01FPbdSPsPKYDLpxAt9wbLiy`).
If the handoff is too compressed on something, ask me and I will pull the detail from there.
Earlier transcripts are in `conversation_history/`; the 15–21 September work has no
transcript and survives only as its session log.

Start by running the four verifications, then tell me where we stand and put the M2 options
to me.
