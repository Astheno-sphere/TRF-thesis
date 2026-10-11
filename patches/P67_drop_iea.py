# P67 — Round 5: Jo R5[5]. Drop the defensive IEA energy quote in §1.5; keep the honest scope point
# (no energy saving claimed; the programme fit is information logistics). Remove the now-orphaned
# International Energy Agency (2025) reference from the Chapter 1 list.
EDITS = [
 dict(id='P67-01', file='Chapter1_Introduction_v2.md',
   old=r"""Fourth, it does not measure hardware energy consumption, and no sustainability metrics are claimed beyond conceptual framing. Storage has an energy cost at system scale: data centres used "around 1.5% of the world's electricity consumption in 2024, or 415 terawatt-hours" (International Energy Agency, 2025). The thesis does not estimate what share retained audit records account for, and claims no energy saving for the mechanism. Its place in a programme in Sustainable Energy Logistics is therefore in the logistics of information rather than of energy""",
   new=r"""Fourth, it does not measure hardware energy consumption, and no sustainability metrics are claimed beyond conceptual framing. The thesis claims no energy saving for the mechanism; its place in a programme in Sustainable Energy Logistics is in the logistics of information rather than of energy""",
   why="Jo R5[5]: drop the defensive IEA quote, keep the scope disclaimer and the information-logistics framing"),
 dict(id='P67-02', file='Chapter1_Introduction_v2.md',
   old=r"""International Energy Agency. (2025). *Energy and AI* [Executive summary]. IEA. Retrieved 5 October 2026, from https://www.iea.org/reports/energy-and-ai/executive-summary
""",
   new="", why="Jo R5[5]: remove the now-uncited IEA reference"),
]
LOST_OK = ["citation International Energy Agency, 2025", "number 1.5", "number 2024", "number 415",
           "number 2025", "hedge does not"]
