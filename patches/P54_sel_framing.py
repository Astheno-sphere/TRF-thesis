# P54 — R3-FIT: the Sustainable Energy Logistics framing anchored in checked sources (CSCMP definition,
# Nahmias 1982 via Crossref, Elhub privacy statement of 31 Mar 2026, IEA 2025); R3-PRL: politiregisterloven
# § 17 checked against the consolidated Lovdata text supplied by the author (last amended LOV-2026-06-19-49,
# in force 1 Oct 2026; § 17 carries no amendment note; wording identical to the quotation in §6.10).
C1 = 'Chapter1_Introduction_v2.md'
C2 = 'Chapter2_LitReview_v2_FINAL.md'
C6 = 'Chapter6_Discussion_v1.md'
EDITS = [
 dict(id='P54-01', file=C2,
  old="within a literature on cross-border data movement under regulatory constraint.\n\n",
  new="within a literature on cross-border data movement under regulatory constraint.\n\n"
      "The framing rests on the discipline's own definitions, not on analogy alone. The Council of Supply Chain Management Professionals defines logistics management as the part of supply chain management that \"plans, implements, and controls the efficient, effective forward and reverse flow and storage of goods, services and related information between the point of origin and the point of consumption\" (Council of Supply Chain Management Professionals, n.d.). An audit record is related information in exactly this sense. The thesis concerns its storage and its planned exit: the reverse end of the flow, where a record is retained, reduced or disposed of.\n\n"
      "Operations research supplies the closest formal relative. Perishable inventory theory studies stock that must be held to meet demand but expires after a fixed or random lifetime (Nahmias, 1982). A record under a retention floor and a deletion ceiling is perishable stock with two clocks. Proposition 3 (Chapter 4, Section 4.6) states the condition in that idiom: when the expiry clock starts at a different event from the holding clock, whether an item can be held as long as it must depends on each item's history, not on the rule book.\n\n"
      "The energy sector's own data infrastructure schedules retention in the same terms. Elhub, the Norwegian electricity data hub, keeps a customer's personal data for \"ytterligere 3 år og 41 dager\" after both the supply and the grid contract end, \"for eventuell feilretting og mulighet for å korrigere økonomiske oppgjør\", and keeps metering values for ten years only where the customer asks (Elhub, 2026). That is a retention period per data category, anchored to an event, with an extension the data subject controls: the parameters of the model in Chapter 4, Section 4.3, in a different sector.\n\n",
  why='R3-FIT: SEL anchors'),
 dict(id='P54-02', file=C2, old="\nDatatilsynet. (2015).",
  new="\nCouncil of Supply Chain Management Professionals. (n.d.). *Frequently asked questions* [Includes the CSCMP definition of logistics management]. Retrieved 5 October 2026, from https://cscmp.org/CSCMP/CSCMP/Develop/Starting_Your_Career/Frequently_Asked_Questions.aspx\n\nDatatilsynet. (2015).",
  why='ref'),
 dict(id='P54-03', file=C2, old="\nEuropean Commission. (2025a).",
  new="\nElhub. (2026). *Elhubs personvernerklæring* [Privacy statement; last updated 31 March 2026]. Elhub AS. Retrieved 5 October 2026, from https://elhub.no/personvern-og-sikkerhet/elhubs-personvernerklaering\n\nEuropean Commission. (2025a).",
  why='ref'),
 dict(id='P54-04', file=C2, old="\nNational Institute of Standards and Technology. (2025).",
  new="\nNahmias, S. (1982). Perishable inventory theory: A review. *Operations Research, 30*(4), 680–708. https://doi.org/10.1287/opre.30.4.680\n\nNational Institute of Standards and Technology. (2025).",
  why='ref'),
 dict(id='P54-05', file=C1,
  old="no sustainability metrics are claimed beyond conceptual framing.",
  new="no sustainability metrics are claimed beyond conceptual framing. Storage has an energy cost at system scale: data centres used \"around 1.5% of the world's electricity consumption in 2024, or 415 terawatt-hours\" (International Energy Agency, 2025). The thesis does not estimate what share retained audit records account for, and claims no energy saving for the mechanism.",
  why='R3-FIT: energy stated honestly'),
 dict(id='P54-06', file=C1, old="\nIHE International. (2023).",
  new="\nInternational Energy Agency. (2025). *Energy and AI* [Executive summary]. IEA. Retrieved 5 October 2026, from https://www.iea.org/reports/energy-and-ai/executive-summary\n\nIHE International. (2023).",
  why='ref'),
 dict(id='P54-07', file=C6,
  old="§ 17 Kravet til sporbarhet. Norwegian Ministry of Justice and Public Security. https://lovdata.no/lov/2010-05-28-16",
  new="§ 17 Kravet til sporbarhet [Consolidated text as last amended by LOV-2026-06-19-49, in force 1 October 2026; § 17 unamended; read 5 October 2026]. Norwegian Ministry of Justice and Public Security. https://lovdata.no/lov/2010-05-28-16",
  why='R3-PRL'),
]
LOST_OK = []
