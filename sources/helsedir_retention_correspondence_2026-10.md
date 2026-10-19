# Primary source — Helsedirektoratet correspondence on cross-border audit-trail retention

Cited in Chapter 2, §2.3 as a personal communication (APA in-text only; not in the reference list).
Resolves R3-F10 (the ten-year cross-border audit floor had only an unsourced tutorial-article basis,
Simjanoska Misheva et al., 2025).

## Enquiry (sent)
- From: Arshad Akhtar Abbasia <arshad.a.abbasia@himolde.no>
- To: Postmottak (Ekstern post til arkivet) <f-arkivar@helsedir.no>
- Sent: Monday 5 October 2026, 15:48
- Substance: asked for the source and duration of the audit-repository retention requirement for the
  Norwegian NCPeH / MyHealth@EU cross-border audit trail.

## Reply (received)
- From: Hans Löwe Larsen, Avdelingsdirektør, divisjon informasjonsforvaltning og metode, Helsedirektoratet
  (+47 4000 5444; Vitaminveien 4, 0277 Oslo)
- Received: Monday 19 October 2026

Verbatim (Norwegian):

> Hei.
> Takk for din henvendelse, og det er bare hyggelig å kunne være til assistanse.
>
> 1. Jeg finner ingen spesifikk henvisning til lengden på oppbevaring i requirements catalouge eller
>    tilhørende dokumentasjon (Security Services Specification, System Architecture Specifications,
>    NCPeH Architecure Specifications, Audit Trail Profil osv). Det henvises til nasjonal lovgivning,
>    men konkretiserer ikke lagringsmåte eller lagringstid.
>
> 2. Under utprøvingen er det besluttet en lagringstid på 6 år, men en endelig beslutning når det går
>    i full produksjon er ikke tatt. Hdir er dataansvarlig og vil ta den beslutningen.
>
> Håper dette besvarer dine spørsmål, bare ta kontakt dersom du har behov for ytterligere informasjon.
> Med vennlig hilsen
> Hans Löwe Larsen

## What it establishes (for the thesis)
1. The eHDSI requirements catalogue and associated specifications (Security Services, System
   Architecture, NCPeH Architecture, Audit Trail Profile) fix NO retention method or period; they
   defer to national legislation. → The reported "ten years" (Simjanoska Misheva et al., 2025) is not
   an established requirement; it confirms, from the controller, that no catalogue figure exists.
2. For the pilot, Hdir has provisionally set a six-year retention; the full-production figure is
   undecided and reserved to Hdir as data controller (dataansvarlig).
3. "Hdir is controller and decides" corroborates the §4.2 controllership analysis (Commission
   Implementing Decision (EU) 2019/1765, Art 7: the Member-State authority is the controller).

Design consequence: the TRF Model treats the retention floor as a parameter, not a constant; the
demonstration uses F = 120 months (illustrative long floor) and Corollary 2.2 shows no result depends
on the value. The six-year pilot figure is now the live Norwegian data point.
