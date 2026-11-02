# Draft, not sent: correction note to the NORS 2025 audience

*For Tiger to adapt and send, or not, at his discretion. Content matches the nomenclature note in Chapter 1, Section 1.6.*

---

**Subject:** Update on "VERA-SNARK" (NORS 2025): the zero-knowledge design was not needed

At NORS 2025 I presented an early idea, VERA-SNARK, which proposed zero-knowledge succinct arguments (SNARKs) to reconcile audit-log retention with the right to erasure for cross-border health data. That idea was preliminary and underdeveloped, and I no longer stand behind its architecture.

The completed MSc thesis (Høgskolen i Molde, November 2026) reaches a different and simpler result. Once the three obligations (the retention floor, GDPR Article 17, and the six-month deletion ceiling of EHDS Article 68(12)) are written as constraints, the conflict turns on what "verifiable" means. If a record must stay readable, the obligations cannot be met together whenever a deadline falls inside the retention window. If verifiable means accountable (who acted, when, a commitment and a logged invalidation entry), they can always be met. Commitments and a logged invalidation registry suffice; no SNARK is required. The name VERA-SNARK is kept only for continuity.

The results are checked in code on synthetic data, key destruction is attested rather than proven, and the retained residue is pseudonymised, not anonymous.

Thesis: https://github.com/Astheno-sphere/TRF-thesis
Code and archived release: https://doi.org/10.5281/zenodo.23819274
Live demonstration: https://trfhimolde.streamlit.app/

Arshad Akhtar Abbasia, Høgskolen i Molde
