# Defence walkthrough: where the app and Zenodo come in

Talk: slides 1 to 16 (15:00, notes run 14:40). Slide 17 is the break into questions. Slides 18 to 31 are backup.

## Before the day
- Rehearse on the live URL the day before. Screenshot the Claim ledger page as the fallback.
- On the day, open `trfhimolde.streamlit.app` in a tab ten minutes before you start. It sleeps when idle; waking takes up to a minute.
- Open a second tab on the Zenodo record: `doi.org/10.5281/zenodo.23989242` (release 1.3.0, the one the thesis cites).
- Both apps run the same code, release 1.3.2 (DOI 10.5281/zenodo.24399784). Use `trfhimolde.streamlit.app`, the one on the close slide.

## During the talk (one live stop, slide 13)
| Slide | Where | What you click | What you say |
|---|---|---|---|
| 3, 4 | none, deck only | | "This is record 3 of the run; you will see it again, live." |
| 13 demo, stop 1 | App, sidebar: **Witness a record** | Record box: "Cross-border record with an erasure request, record 3". Drag the Month slider to **116**. | "Under the first reading, the collision; under the second, the invalidation." |
| 13 demo, stop 2 | App, sidebar: **Claim ledger** | Wait for it to recompute. Point at 90, 95, 39, 138, 0. | "Each matches the thesis." If the Synthea row says bundles not deployed: "that row needs the bundles", move on. |
| 13 fallback | Ledger screenshot, then Figure 5.2 | | Network failed: show the screenshot and carry on. |
| 16 close | Point at the bottom three lines | Do not click | "The repository, the archived code and the app. Everything I showed you can be rerun." |

Time box for slide 13: 75 seconds. Then back to the deck.

## During questions (only if asked)
| Question | Backup slide | Live stop |
|---|---|---|
| "Show me the research log with no request" | research (5) and q-permits (23) | App, **Witness a record**, preset "Research log, no erasure request (Corollary 1.2)". Slide month to 16. |
| "Do the propositions really hold? Break them." | q-proofs (24), q-props34 (30) | App, **The four propositions**: Z3 refutes the deliberately broken variants. |
| "How is the mechanism built?" | mechanism (10) | App, **How it is built**. |
| "Can I rerun it myself?" | close (16) | Zenodo tab: show the record, the DOI, the zip. Say: `python3 trf_checker.py` prints 95 violations across 90 records and 0; the commitment of record 100 starts `678ade47c1e6dc03`. |
| "Which version is the thesis?" | | 1.3.0 is cited and counted in Appendix A. 1.3.1 and 1.3.2 change the viewer wording and metadata only; the six result modules are byte-identical. |
| "Operator rewrites the log" | q-roots (29) | none. Say: specified, not built. |

## Words to hold
Attested, not proven. Pseudonymised, not anonymous. In the model. Synthetic, not frequency estimates. Propositions 1 to 3 proved informally and checked in code; Proposition 4 argued from a premise.
