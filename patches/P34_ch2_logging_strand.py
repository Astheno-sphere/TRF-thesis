# P34 — Chapter 2 §2.4 gains the strand the artefact now builds on: tamper-evident audit logging
# (Schneier & Kelsey 1999; Merkle 1988; Crosby & Wallach 2009; RFC 6962; Laurie 2014), placed
# against KONFIDO's unresolved immutability-vs-erasure tension and pointed forward to Ch4 §4.8.
# The secure-deletion paragraph gains the origin of the cryptographic-erasure idea (Boneh & Lipton
# 1996). A stray duplicated URL line in the reference list is removed.
C2 = "Chapter2_LitReview_v2_FINAL.md"
EDITS = [
    dict(id="P34-01", file=C2,
         old="Ren (2022) surveys the field, covering applications ranging from anonymous credentials and certificate revocation through to blockchain-based audit systems.",
         new="Ren (2022) surveys the field, covering applications ranging from anonymous credentials and certificate revocation through to blockchain-based audit systems.\n\nThe integrity of the audit trail itself has an older literature of its own. Schneier and Kelsey (1999) designed audit logs in which entries written before an attacker compromises the logging machine can be neither read nor altered without detection, by chaining each entry to its predecessor under evolving keys. Crosby and Wallach (2009) replaced the chain with a Merkle tree (Merkle, 1988), so that the presence of a single entry, and the consistency of an earlier version of the log with a later one, can each be checked with a proof logarithmic in the size of the log. Certificate Transparency standardised that construction for public append-only logs (Laurie, Langley, & Kasper, 2013), and has operated it at the scale of the web's certificate infrastructure (Laurie, 2014). These designs make a log immutable in the sense accountability needs. None was designed for a log that must also lose content on request, and a log that records personal data in its entries, as KONFIDO's blockchain component did, reproduces the immutability-against-erasure tension described above. Chapter 4, Section 4.8 keeps the construction and resolves the tension by deciding what an entry may contain.",
         why="tamper-evident logging strand; link to KONFIDO and Ch4 §4.8"),
    dict(id="P34-02", file=C2,
         old="Cryptographic erasure is the limiting case of this observation: it operates entirely above the medium,",
         new="Cryptographic erasure is the limiting case of this observation, and an old one: Boneh and Lipton (1996) proposed making files removable from backups by encrypting them and later forgetting the key. It operates entirely above the medium,",
         why="origin of the technique (Boneh & Lipton 1996)"),
    dict(id="P34-03", file=C2,
         old="Benaloh, J., & de Mare, M. (1994).",
         new="Boneh, D., & Lipton, R. J. (1996). A revocable backup system. In *Proceedings of the 6th USENIX Security Symposium* (pp. 91–96). USENIX Association. https://www.usenix.org/legacy/publications/library/proceedings/sec96/boneh.html\n\nBenaloh, J., & de Mare, M. (1994).",
         why="reference (consolidated list is sorted by assemble.py)"),
    dict(id="P34-04", file=C2,
         old="Camenisch, J., & Lysyanskaya, A. (2002). Dynamic a",
         new="Crosby, S. A., & Wallach, D. S. (2009). Efficient data structures for tamper-evident logging. In *Proceedings of the 18th USENIX Security Symposium* (pp. 317–334). USENIX Association. https://www.usenix.org/legacy/events/sec09/tech/full_papers/crosby.pdf\n\nCamenisch, J., & Lysyanskaya, A. (2002). Dynamic a",
         why="reference"),
    dict(id="P34-05", file=C2,
         old="Matheson. (2026).",
         new="Laurie, B. (2014). Certificate transparency. *Communications of the ACM, 57*(10), 40–46. https://doi.org/10.1145/2659897\n\nLaurie, B., Langley, A., & Kasper, E. (2013). *Certificate Transparency* (RFC 6962). RFC Editor. https://doi.org/10.17487/RFC6962\n\nMatheson. (2026).",
         why="references"),
    dict(id="P34-06", file=C2,
         old="National Institute of Standards and Technology. (2025).",
         new="Merkle, R. C. (1988). A digital signature based on a conventional encryption function. In C. Pomerance (Ed.), *Advances in Cryptology — CRYPTO '87* (LNCS 293, pp. 369–378). Springer. https://doi.org/10.1007/3-540-48184-2_32\n\nNational Institute of Standards and Technology. (2025).",
         why="reference"),
    dict(id="P34-07", file=C2,
         old="Sharma, S., Petrovic, G., & Kaushik, S. (2025).",
         new="Schneier, B., & Kelsey, J. (1999). Secure audit logs to support computer forensics. *ACM Transactions on Information and System Security, 2*(2), 159–176. https://doi.org/10.1145/317087.317089\n\nSharma, S., Petrovic, G., & Kaushik, S. (2025).",
         why="reference"),
    dict(id="P34-08", file=C2,
         old="\n\n https://www.helsedirektoratet.no/digitalisering-og-e-helse/nasjonal-e-helseportefolje/tiltak-i-nasjonal-e-helseportefolje/myhealth-eu-norsk-helsenett\n",
         new="\n",
         why="stray duplicated URL line"),
]
