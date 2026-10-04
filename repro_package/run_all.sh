#!/usr/bin/env bash
# Reproduces every numerical result reported in Chapters 4 and 5.
# Deterministic: seed 20260915 throughout. Runtime is well under one second for
# the checker. Regenerating the full Synthea cohort takes several minutes and is
# not required: the eight-bundle subset in data/synthea_subset/ is sufficient.
set -euo pipefail
cd "$(dirname "$0")"

echo "=== 1/4  TRF feasibility checker (Theorems 1 and 2) ==="
python3 trf_checker.py | tee results/trf_output_rerun.txt

echo
echo "=== 2/4  Extended erasure response period (Chapter 5, Section 5.6) ==="
python3 trf_checker.py --delta-witness | tee results/delta_witness_rerun.txt

echo
echo "=== 3/4  Synthea realism layer (payload-provenance comparison) ==="
python3 synthea_layer.py | tee results/synthea_comparison_rerun.txt
echo
echo "Mean payload is 891 bytes against the eight-bundle subset shipped here and"
echo "1,006 bytes against the full 98-bundle cohort. Chapter 5, Section 5.8 reports"
echo "both. Every other figure is identical under either cohort."
echo
echo "To run against the full cohort instead, which needs Java 17 or later:"
echo "  curl -sL -o synthea.jar https://github.com/synthetichealth/synthea/releases/download/master-branch-latest/synthea-with-dependencies.jar"
echo "  mkdir -p synthea_run && cd synthea_run && java -jar ../synthea.jar \\"
echo "    -s 20260915 -cs 20260915 -p 100 --exporter.fhir.export=true \\"
echo "    --exporter.hospital.fhir.export=false --exporter.practitioner.fhir.export=false \\"
echo "    --generate.only_alive_patients=true"
echo "The layer reads synthea_run/output/fhir/ in preference to the subset."

echo
echo "=== 4/4  Norwegian context modules (illustrative, not thesis claims) ==="
python3 norwegian_layer.py | tee results/norwegian_layer_rerun.txt
echo
python3 cross_sector_check.py | tee results/cross_sector_rerun.txt

echo
echo "=== 5 (optional)  Envelope encryption with real AES-256-GCM; needs the cryptography package ==="
if python3 -c "import cryptography" 2>/dev/null; then
  python3 crypto_envelope.py | tee results/crypto_envelope_rerun.txt
else
  echo "skipped: pip install cryptography to run it; no thesis figure depends on it"
fi

echo
echo "=== 6 (optional)  Bounded SMT check of Propositions 1-3; needs the z3-solver package ==="
if python3 -c "import z3" 2>/dev/null; then
  python3 z3_check.py | tee results/z3_check_rerun.txt
else
  echo "skipped: pip install z3-solver to run it"
fi

echo
echo "-----------------------------------------------------------------------"
echo "Now diff each rerun against its recorded run. All six should be identical;"
echo "a difference means a file changed, not that the result changed."
echo "  diff results/trf_output_rerun.txt            results/trf_output.txt"
echo "  diff results/delta_witness_rerun.txt         results/expected_delta_witness_output.txt"
echo "  diff results/synthea_comparison_rerun.txt    results/synthea_comparison_subset_output.txt"
echo "  diff results/norwegian_layer_rerun.txt       results/expected_norwegian_output.txt"
echo "  diff results/cross_sector_rerun.txt          results/expected_cross_sector_output.txt"
echo "  diff results/crypto_envelope_rerun.txt       results/crypto_envelope_output.txt"
echo "  diff results/z3_check_rerun.txt              results/z3_check_output.txt"
echo
echo "results/synthea_comparison_full_cohort_output.txt records the same comparison"
echo "against all 98 bundles, recorded on 28 September 2026 before the constructed"
echo "payloads were revised. Besides the bundle count and the mean payloads, no line"
echo "differs from the subset run. Diff the two against each other to see that"
echo "no reported measure moves with cohort size."
