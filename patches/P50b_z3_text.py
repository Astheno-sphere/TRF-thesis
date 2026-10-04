# P50b — A.24 note corrected: Z3 version as installed (5.1.0), and the sanity check returns a satisfying
# trajectory, not a counterexample.
EDITS = [dict(id="P50b-01", file="code_artefacts/README_Appendix_A.md",
              old="(Z3 4.15). Nine checks find no counterexample; the sanity check and the mutation check return counterexamples, as they must.",
              new="(Z3 5.1.0). Nine checks find no counterexample; the sanity check finds a satisfying trajectory and the mutation check finds counterexamples, as they must.",
              why="accuracy")]
LOST_OK = ["number 4.15"]
