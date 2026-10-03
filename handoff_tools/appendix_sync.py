#!/usr/bin/env python3
"""Keep Appendix A's source listings and console outputs equal to the files they reproduce.

Usage: python3 handoff_tools/appendix_sync.py          report blocks that differ (exit 1 if any)
       from appendix_sync import BLOCKS, block_edits     used by patches to build exact edits

Added 3 Oct 2026 with the code wave (P12/P13). A.11 (full 98-bundle cohort) is a historical
record that cannot be re-run without the cohort; it is checked against its own recorded file.
"""
import os, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
APPENDIX = "code_artefacts/README_Appendix_A.md"
BLOCKS = {
    "## A.8 Source listing": "demo_app/trf_checker.py",
    "## A.9 Source listing": "demo_app/synthea_layer.py",
    "## A.9b Source listing": "demo_app/norwegian_layer.py",
    "## A.9c Source listing": "demo_app/cross_sector_check.py",
    "## A.9d Source listing": "demo_app/app.py",
    "## A.10 Console output": "repro_package/results/trf_output.txt",
    "## A.11 Console output": "repro_package/results/synthea_comparison_full_cohort_output.txt",
    "## A.11b Console output": "repro_package/results/synthea_comparison_subset_output.txt",
    "## A.12 Console output": "repro_package/results/expected_delta_witness_output.txt",
    "## A.13 Console output": "repro_package/results/expected_norwegian_output.txt",
    "## A.14 Console output": "repro_package/results/expected_cross_sector_output.txt",
}


def block(text, heading):
    i = text.index(heading)
    j = text.index("```", i); j = text.index("\n", j) + 1
    k = text.index("\n```", j)
    return text[j:k + 1]


def block_edits(prefix):
    """One patch edit per listing whose block differs from its file. Each edit is anchored
    from the section heading to the end of its block, because one console output (A.10)
    occurs verbatim inside another (A.12)."""
    text = (ROOT / APPENDIX).read_text(encoding="utf-8")
    edits = []
    for n, (h, f) in enumerate(BLOCKS.items(), 1):
        i = text.index(h)
        j = text.index("```", i); j = text.index("\n", j) + 1
        k = text.index("\n```", j) + 1
        new_block = (ROOT / f).read_text(encoding="utf-8")
        new_block = new_block if new_block.endswith("\n") else new_block + "\n"
        if text[j:k] != new_block:
            old = text[i:k]
            assert text.count(old) == 1, f"{h}: anchor not unique"
            edits.append(dict(id=f"{prefix}{n:02d}", file=APPENDIX, old=old,
                              new=text[i:j] + new_block,
                              why=f"Appendix A {h[3:].split(' ')[0]} synced to {f}"))
    return edits


def main():
    os.chdir(ROOT)
    text = pathlib.Path(APPENDIX).read_text(encoding="utf-8")
    bad = []
    for h, f in BLOCKS.items():
        new = pathlib.Path(f).read_text(encoding="utf-8")
        if block(text, h).strip() != new.strip():
            bad.append(f"{h[3:]} differs from {f}")
    print(f"Appendix A listings: {len(BLOCKS) - len(bad)}/{len(BLOCKS)} equal to their files")
    for b in bad:
        print("  " + b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
