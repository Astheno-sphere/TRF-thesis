#!/usr/bin/env python3
"""Keep Appendix A's source listings and console outputs equal to the files they reproduce.

Usage: python3 handoff_tools/appendix_sync.py          report blocks that differ (exit 1 if any)
       from appendix_sync import BLOCKS, block_edits     used by patches to build exact edits

Added 3 Oct 2026 with the code wave (P12/P13). A.17 (full 98-bundle cohort; A.11 before the renumbering of 4 Oct, B-36) is a historical
record that cannot be re-run without the cohort; it is checked against its own recorded file.
"""
import os, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
APPENDIX = "code_artefacts/README_Appendix_A.md"
BLOCKS = {
    "## A.10 Source listing": "demo_app/trf_checker.py",
    "## A.11 Source listing": "demo_app/synthea_layer.py",
    "## A.12 Source listing": "demo_app/norwegian_layer.py",
    "## A.13 Source listing": "demo_app/cross_sector_check.py",
    "## A.14 Source listing": "demo_app/app.py",
    "## A.15 Source listing": "demo_app/crypto_envelope.py",
    "## A.16 Console output": "repro_package/results/trf_output.txt",
    "## A.17 Console output": "repro_package/results/synthea_comparison_full_cohort_output.txt",
    "## A.21 Console output": "repro_package/results/synthea_comparison_subset_output.txt",
    "## A.18 Console output": "repro_package/results/expected_delta_witness_output.txt",
    "## A.19 Console output": "repro_package/results/expected_norwegian_output.txt",
    "## A.20 Console output": "repro_package/results/expected_cross_sector_output.txt",
    "## A.22 Console output": "repro_package/results/crypto_envelope_output.txt",
    "## A.23 Source listing": "demo_app/z3_check.py",
    "## A.24 Console output": "repro_package/results/z3_check_output.txt",
}


def block(text, heading):
    i = text.index(heading)
    j = text.index("```", i); j = text.index("\n", j) + 1
    k = text.index("\n```", j)
    return text[j:k + 1]


def block_edits_text(text, read_new, prefix):
    """Edits that turn each listing block in `text` into read_new(file). Anchored from the
    section heading to the end of its block, because A.16's output occurs verbatim inside A.18's (A.10 and A.12 before 4 Oct)."""
    edits = []
    for n, (h, f) in enumerate(BLOCKS.items(), 1):
        i = text.index(h)
        j = text.index("```", i); j = text.index("\n", j) + 1
        k = text.index("\n```", j) + 1
        new_block = read_new(f)
        new_block = new_block if new_block.endswith("\n") else new_block + "\n"
        if text[j:k] != new_block:
            old = text[i:k]
            assert text.count(old) == 1, f"{h}: anchor not unique"
            edits.append(dict(id=f"{prefix}{n:02d}", file=APPENDIX, old=old, new=text[i:j] + new_block,
                              why=f"Appendix A {h[3:].split(' ')[0]} synced to {f}"))
    return edits


def block_edits(prefix):
    text = (ROOT / APPENDIX).read_text(encoding="utf-8")
    return block_edits_text(text, lambda f: (ROOT / f).read_text(encoding="utf-8"), prefix)


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
