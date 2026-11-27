"""Every recorded console run in docs/ reproduces byte for byte.

Run: python3 -m pytest -q tests/
"""
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUNS = [
    (["trf_checker.py"], "expected_trf_output.txt"),
    (["trf_checker.py", "--delta-witness"], "expected_delta_witness_output.txt"),
    (["sensitivity.py"], "expected_sensitivity_output.txt"),
    (["cross_sector_check.py"], "expected_cross_sector_output.txt"),
    (["norwegian_layer.py"], "expected_norwegian_output.txt"),
    (["synthea_layer.py"], "expected_synthea_subset_output.txt"),
    (["crypto_envelope.py"], "expected_crypto_envelope_output.txt"),
    (["z3_check.py"], "expected_z3_check_output.txt"),
]


@pytest.mark.parametrize("cmd,expected", RUNS, ids=[" ".join(c) for c, _ in RUNS])
def test_recorded_output_reproduces(cmd, expected):
    out = subprocess.run([sys.executable, *cmd], cwd=ROOT, capture_output=True, text=True).stdout
    assert out == (ROOT / "docs" / expected).read_text(encoding="utf-8")
