# Drafts for Tiger — 5 October 2026

Two things João's 4 Oct review asks only you can send or own. Edit freely; nothing here is in the thesis yet.

## 1. Email to Helsedirektoratet (the ten-year floor)

**To:** postmottak@helsedir.no (ask them to forward to the MyHealth@EU / NCPeH team)
**Subject:** Spørsmål om lagringstid for revisjonslogger i MyHealth@EU (masteroppgave, HiMolde)

Hei,

Jeg skriver en masteroppgave ved Høgskolen i Molde om lagring og sletting av revisjonslogger i grensekryssende helsedatautveksling under EHDS, med Norges nasjonale kontaktpunkt for e-helse som case. Veileder er professor João Ferreira.

Oppgaven bruker en minste lagringstid på ti år for revisjonslogger i nasjonale kontaktpunkter, slik den er gjengitt i faglitteraturen som eHDSI-baselinen. Jeg har ikke funnet perioden i et primærdokument. Avtalen mellom nasjonale myndigheter om deltakelse i de grensekryssende tjenestene (eHealth Network, 2017) krever revisjonsspor i klausul II.4.2, men angir ingen periode i hovedteksten, og vedleggene har jeg ikke hatt tilgang til.

Kan dere bekrefte
1. om det finnes et krav i eHDSI-rammeverket (vedlegg til avtalen, sikkerhetspolicy eller tilsvarende) om hvor lenge revisjonslogger skal lagres, og i så fall hvilket dokument og hvilken bestemmelse, og
2. hvilken lagringstid det norske kontaktpunktet faktisk praktiserer for slike logger?

Svaret brukes bare til å angi kilden riktig i oppgaven. Jeg siterer dere ikke uten samtykke.

Med vennlig hilsen
Arshad Akhtar Abbasia
MSc Sustainable Energy Logistics, Høgskolen i Molde

## 2. Programme fit (paragraph for §2.7, to make your own)

The thesis belongs to logistics in the sense the programme uses the word: the planning and control of flows across boundaries under constraints that differ on each side. An audit record is the information flow that accompanies a cross-border health data consignment, and the problem the thesis solves is a retention-scheduling problem for that flow: how long each part of the record must be held, where, and when it must be disposed of, when three authorities set incompatible limits. Two logistics concepts carry over directly. Chain-of-custody records keep the documentation of a consignment after the consignment itself has been delivered or destroyed, which is the separation Semantics II makes between the record of an access and its payload. And disposal is a planned stage of a product's life cycle, with its own documentation, rather than an absence; the invalidation entry is that documentation for information. The energy dimension of the programme is not engaged, and the thesis says so (Chapter 1, Section 1.5).

## 3. Open checks only you can do

- Article 9(1)–(2) EHDS: the quotes in §4.2 were taken from a mirror of the Official Journal text (streamlex.eu). Check them against the OJ PDF: http://data.europa.eu/eli/reg/2025/327/oj
- politiregisterloven § 17: the wording matches the 2009 bill text (Ot.prp. nr. 108 (2008–2009)); lovdata.no could not be read from here. Check the current consolidated § 17 on lovdata.no for later amendments.
- HiMolde's current rules on AI use: confirm the Declaration matches them.

## 4. Sustainable Energy Logistics framing: anchors checked 5 Oct (for §1.5 / §2.7, R3-FIT)

Use what you can defend at the defence. Status: **V** = wording checked at the source today; **C** = known source, check the wording yourself before quoting.

1. **Logistics already includes information and disposal (V).** CSCMP defines logistics management as the part of supply chain management that "plans, implements, and controls the efficient, effective forward and reverse flow and storage of goods, services and related information between the point of origin and the point of consumption" (CSCMP, Supply Chain Management Terms and Glossary; FAQ page read 5 Oct). The thesis is about the *storage* of *related information* and its planned exit, which this definition names.
   Hook: *"Logistics has always moved two things: the goods, and the record of the goods. This thesis is about the second, and about when it must stop."*
2. **Reverse logistics: disposal is a planned flow (C).** Rogers & Tibben-Lembke (1999, *Going Backwards*, Reverse Logistics Executive Council; also J. Business Logistics 22(2), 2001) define reverse logistics as planning and controlling the flow "from the point of consumption to the point of origin for the purpose of recapturing value or proper disposal". Invalidation is "proper disposal" of information, with a disposal record (the invalidation entry).
3. **Perishable inventory: the floor/ceiling is a shelf-life problem (V for the paper, C for the wording).** Nahmias (1982), "Perishable inventory theory: a review", *Operations Research* 30(4), 680–708, doi:10.1287/opre.30.4.680. An item with a minimum holding duty and a maximum life is perishable stock. Proposition 3 restated in that language: if the expiry clock starts at a different event from the holding clock, whether an item can be held long enough depends on each item's history, not on the rulebook. Strongest theory hook you have; it puts Proposition 3 in operations-research terms your examiners know.
4. **Time windows (C).** Solomon (1987), *Operations Research* 35(2), 254–265: vehicle routing with time windows. A delivery is infeasible when its window is empty. Proposition 1 is the empty-window case: the floor demands availability until t+F, the deadline demands absence from t_r+δ, and the window [t_r+δ, t+F] is where they cannot both be met.
5. **Chain of custody (C).** ISO 22095:2020, *Chain of custody: general terminology and models*. Already your customs analogy (§2.7); ISO gives it a neutral, standards-grade anchor instead of customs alone.
6. **Energy, stated honestly (V).** IEA (2025), *Energy and AI*, executive summary: data centres used "around 1.5% of the world's electricity consumption in 2024, or 415 terawatt-hours (TWh)", set to "more than double to around 945 TWh by 2030". Storage limitation is an obligation to *stop* storing. Do **not** claim audit-log erasure saves meaningful energy; claim only that retention rules are also storage rules, and that the thesis makes no energy estimate (keep the line in §1.5).
7. **An energy-sector test of Proposition 3 (V, operator source).** Elhub, Norway's electricity data hub, states in its privacy statement that consumption values are kept "3 år og 41 dager, med mindre du aktivt har bestilt lagring i 10 år" (Elhub, Personvernerklæring, read 5 Oct). Both periods run from the recording of the value, one anchor, so by Proposition 3(i) no floor/ceiling collision can arise from the text, exactly like politiregisterloven § 17. The legal source is forskrift om måling, avregning … (1999-03-11-301) kapittel 6; Lovdata blocks automated reading, so check the paragraph yourself. Possible use: one paragraph in §6.10 ("the same diagnostic run on Norway's energy data hub"), which ties the model to the programme's own sector without overclaiming. Not yet in the thesis.

Recommended: 1 + 3 + 7 in §2.7 (one paragraph each, max), 6 as one sentence in §1.5. Skip 2, 4, 5 unless you want more.
