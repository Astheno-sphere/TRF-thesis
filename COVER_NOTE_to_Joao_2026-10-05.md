Dear João,

Thank you for the review of 4 October. The revised draft is attached, together with a tracked-changes file against the version you reviewed.

What changed:

- Your ten tracked wording changes are in, verbatim. The abstract, the Sammendrag, §5.1, §6.1 and §7.2 now follow your abstract change: the counts are labelled as set by the generator, and Corollary 1.2 is a conditional extension throughout.
- The patient link on the cross-border path is kept, and §4.2 argues why. Article 9 EHDS requires that a person be able to learn who accessed their data, when, and which data, for at least three years from each access. Article 17(3)(b) therefore protects the link for the controller that must provide that information. The section also states the argument's limits: who holds that duty for a foreign NCPeH, the years beyond Article 9's three, and the Secure Processing Environment case.
- The circularity: the payload is now defined by its source (the ITI-55 query; the logged SPE activity), not as "whatever accountability does not need". Necessity is argued per record class, and Corollary 2.3 gives the sensitivity result you asked for. Feasibility survives any part of the payload that auditing needs, unless that part is data concerning health inside an SPE on the broad reading of Article 68(12).
- Semantics I is now anchored in OpenNCP. In the 2017 source, the audit repository stored the whole received audit message readable, refused modification, and had no scheduled retention or purge logic. The schema of the Danish NCPeH's 9.1.0 deployment (2026) keeps the same columns. "Verification" there means the sending gateway signs each message; the repository does not check the signature.
- Your request for an independent check: a bounded SMT check in Z3 (Appendix A.23/A.24; §5.5). It covers Propositions 1–3, including Semantics II for Proposition 2, over every parameter combination within its bounds, with floors up to 120 months. It finds no counterexample, and it does find counterexamples to deliberately broken versions.
- Article 17(3)(d) and the Article 71 opt-out are discussed in §4.4. Redactable signatures and chameleon-hash blockchains (Ateniese et al., 2005, 2017, and later work) are distinguished in §2.4. §4.12 and §7.1 now say plainly that the terminal transition, the nonce, consistency proofs and the accumulator are specified but not implemented.
- Chapter 2 is trimmed where it repeated Chapter 1. The limitations are stated once, in §3.7.

Still open on my side:

- the eHDSI source for the ten-year floor (I have written to Helsedirektoratet);
- the current wording of politiregisterloven § 17 on Lovdata;
- checking the AI-use declaration against HiMolde's current rules;
- the programme-fit paragraph;
- the final length, once I have the programme's guidance.

Best regards,
Arshad
