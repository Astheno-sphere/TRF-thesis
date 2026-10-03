# P39 — Streamlit app brought level with the thesis (Tiger, 4 Oct: "didn't see any changes in the
# app"). Visible changes: (1) Tab 1 shows the audit-log integrity check and both tamper tests
# (Ch5 §5.7); (2) Tab 5 runs the optional AES-256-GCM envelope-encryption module (Ch5 §5.8,
# Appendix A.15) when `cryptography` is installed; (3) new Tab 6, an explorer for Proposition 3
# (where a ceiling is anchored), with Article 68(12) and politiregisterloven § 17 as presets;
# (4) Corollary 1.2 label stated conditionally (the thesis no longer "defends" a reading);
# (5) Tab 5 cross-check label corrected (§5.5, not §5.4); Tab 1 table references precise.
A = "demo_app/app.py"
EDITS = [
    dict(id="P39-01", file=A,
         old="    \"Live demonstration of the executable witness for Propositions 1 and 2. \"",
         new="    \"Live demonstration of the executable witness for Propositions 1 and 2, \"\n    \"with an explorer for Proposition 3. \"",
         why="caption"),
    dict(id="P39-02", file=A,
         old="tab1, tab2, tab3, tab4, tab5 = st.tabs(\n    [\"Thesis run\", \"Exploration — not thesis claims\", \"Synthea realism layer\",\n     \"Norwegian context — illustrative\", \"Robustness and cross-checks\"]\n)",
         new="tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(\n    [\"Thesis run\", \"Exploration — not thesis claims\", \"Synthea realism layer\",\n     \"Norwegian context — illustrative\", \"Robustness and cross-checks\",\n     \"Where the ceiling is anchored\"]\n)",
         why="sixth tab"),
    dict(id="P39-03", file=A,
         old="        \"Executes the checker exactly as reported in Chapter 5, Tables 5.3 to 5.6. \"",
         new="        \"Executes the checker exactly as reported in Chapter 5, Tables 5.3 and 5.6, \"\n        \"and the audit-log integrity check of Section 5.7. \"",
         why="precise references"),
    dict(id="P39-04", file=A,
         old="            \"Article 73(1)(e) and Article 68(12) alone, conditional on the reading \"\n            \"of Article 68(12) defended in Chapter 4, Section 4.6.\"",
         new="            \"Article 73(1)(e) and Article 68(12) alone, on the broad reading of \"\n            \"Article 68(12) and for logs kept at patient-record granularity \"\n            \"(Chapter 4, Section 4.6). On the narrow reading these witnesses lapse.\"",
         why="conditional statement as in the thesis"),
    dict(id="P39-05", file=A,
         old="        if M[\"sem1_total\"] == 95 and M[\"sem2_total\"] == 0 and M[\"cor12\"] == 39:",
         new="        st.markdown(\"**Audit-log integrity — Chapter 5, Section 5.7**\")\n        st.write(\n            \"Every access, invalidation and subject-link removal is a leaf of an \"\n            \"append-only Merkle log (RFC 6962 hashing). A record counts as verifiable \"\n            \"under Semantics II only if each of its entries passes an inclusion proof \"\n            \"against the log root. Leaves hold the accessor fields and the commitment, \"\n            \"never the payload or the patient link, so the log never needs erasing.\"\n        )\n        n_ok = sum(1 for r in records if trf.integrity(r)[0])\n        saved = demo.m[\"actor\"]\n        demo.m[\"actor\"] = \"R-999\"\n        ok_t, why_t = trf.V_II(demo, demo.t_a)\n        demo.m[\"actor\"] = saved\n        saved_g = demo.iota[\"ground\"]\n        demo.iota[\"ground\"] = \"none\"\n        ok_g, why_g = trf.V_II(demo, demo.t_a)\n        demo.iota[\"ground\"] = saved_g\n        ok_r = trf.V_II(demo, demo.t_a)[0]\n        i1, i2, i3 = st.columns(3)\n        i1.metric(\"Records verifying\", f\"{n_ok}/{len(records)}\")\n        i2.metric(\"Tamper: actor altered\", \"fails\" if not ok_t else \"PASSES\")\n        i3.metric(\"Tamper: ground altered\", \"fails\" if not ok_g else \"PASSES\")\n        st.code(\n            f\"rid={demo.rid} actor R-008 -> R-999 : V_II={ok_t}  ({why_t})\\n\"\n            f\"rid={demo.rid} ground -> 'none'    : V_II={ok_g}  ({why_g})\\n\"\n            f\"after restoring both          : V_II={ok_r}\",\n            language=\"text\",\n        )\n\n        if (M[\"sem1_total\"] == 95 and M[\"sem2_total\"] == 0 and M[\"cor12\"] == 39\n                and n_ok == len(records) and not ok_t and not ok_g and ok_r):",
         why="integrity and tamper tests visible; included in the match check"),
    dict(id="P39-06", file=A,
         old="                \"Matches the thesis: 95 violations across 90 records under \"\n                \"Semantics I, 39 Corollary 1.2 witnesses, 0 violations under \"\n                \"Semantics II.\"",
         new="                \"Matches the thesis: 95 violations across 90 records under \"\n                \"Semantics I, 39 Corollary 1.2 witnesses, 0 violations under \"\n                \"Semantics II, 200/200 records verifying, both tamper tests failing.\"",
         why="success message"),
    dict(id="P39-07", file=A,
         old="    st.markdown(\"**Independent exhaustive cross-check — Chapter 5 §5.4**\")",
         new="    st.markdown(\"**Independent exhaustive cross-check — Chapter 5 §5.5**\")",
         why="label was wrong (§5.4 is Corollary 1.2)"),
    dict(id="P39-08", file=A,
         old="# Tab 5 — Robustness and cross-checks (Chapter 5 §5.4 and §5.6)",
         new="# Tab 5 — Robustness and cross-checks (Chapter 5 §5.5, §5.6 and §5.8)",
         why="comment"),
    dict(id="P39-09", file=A,
         old="    st.divider()\n    st.markdown(\"**What this artefact does not do**\")",
         new="    st.divider()\n    st.markdown(\"**Real envelope encryption — optional module, Chapter 5 §5.8**\")\n    st.write(\n        \"The checker models key destruction as removing a reference. This module \"\n        \"repeats the lifecycle with real AES-256-GCM: each record under its own data \"\n        \"key, each data key wrapped under a key-encrypting key, and the wrapped key \"\n        \"destroyed at the record's invalidation month. Keys are random on every run; \"\n        \"the counts are not.\"\n    )\n    if st.button(\"Run envelope encryption\", key=\"run_crypto\"):\n        try:\n            import crypto_envelope as ce\n\n            with st.spinner(\"Encrypting 200 records, destroying keys, decrypting ...\"):\n                recs = trf.generate()\n                custody = ce.Custody()\n                store = {r.rid: ce.encrypt(custody, r.rid, r.payload) for r in recs}\n                inval = [r for r in recs if r.t_invalidation() < trf.INF]\n                for r in inval:\n                    custody.destroy(r.rid)\n                readable = refused = 0\n                for r in recs:\n                    try:\n                        ce.decrypt(custody, r.rid, *store[r.rid])\n                        readable += 1\n                    except KeyError:\n                        refused += 1\n            e1, e2, e3 = st.columns(3)\n            e1.metric(\"Records encrypted\", len(recs))\n            e2.metric(\"Refused after key destruction\", refused)\n            e3.metric(\"Still readable\", readable)\n            if refused == len(inval) == 138 and readable == 62:\n                st.success(\n                    \"Exactly the 138 invalidated records refuse to decrypt and the \"\n                    \"other 62 read, as Appendix A.22 records. Unreadability follows \"\n                    \"from destruction; that destruction happened in hardware is still \"\n                    \"an attestation (Chapter 6, Section 6.3).\",\n                    icon=\"✅\",\n                )\n            else:\n                st.error(\"Counts differ from Appendix A.22. Investigate before citing.\")\n        except ImportError:\n            st.info(\"The `cryptography` package is not installed in this deployment.\")\n\n    st.divider()\n    st.markdown(\"**What this artefact does not do**\")",
         why="optional module visible"),
    dict(id="P39-10", file=A,
         old="        \"zero-knowledge proof system. Key destruction is simulated by removing a \"\n        \"reference in program state: that demonstrates the mechanism's logic and \"\n        \"says nothing about whether destruction can be assured in deployment. \"",
         new="        \"zero-knowledge proof system, and it does not implement the terminal \"\n        \"transition at floor expiry. Key destruction is simulated by removing a \"\n        \"reference in program state, or in the optional module by discarding a \"\n        \"wrapped key in memory: either demonstrates the mechanism's logic and \"\n        \"says nothing about whether destruction can be assured in deployment. \"",
         why="limits stated as in Ch5/Ch6"),
    dict(id="P39-11", file=A,
         old="\nst.divider()\nst.caption(\n    \"This application is a viewer over the verified artefact.",
         new="""

# ----------------------------------------------------------------------
# Tab 6 — Proposition 3: where the ceiling is anchored (Chapter 4, Section 4.6)
# ----------------------------------------------------------------------

with tab6:
    st.subheader("Where the ceiling is anchored — Proposition 3")
    st.write(
        "A retention floor of F months runs from the record's creation t(a). A deletion "
        "ceiling of L months runs from an event e(a) at or after creation. Under plaintext "
        "verifiability the two collide for a record exactly when e(a) + L <= t(a) + F. "
        "A collision therefore needs L <= F; where the ceiling is anchored decides "
        "whether the collision can be read from the text or only from each record's history."
    )
    preset = st.radio(
        "Preset",
        ["EHDS Art 73(1)(e) floor, Art 68(12) ceiling", "politiregisterloven § 17",
         "Free"], horizontal=True)
    if preset.startswith("EHDS"):
        F0, L0, same0 = 12, 6, False
    elif preset.startswith("politi"):
        F0, L0, same0 = 12, 36, True
    else:
        F0, L0, same0 = 24, 12, False
    F = st.slider("Floor F (months, from creation)", 1, 120, F0, key=f"F_{preset}")
    L = st.slider("Ceiling L (months, from its anchor)", 1, 120, L0, key=f"L_{preset}")
    same = st.checkbox("Ceiling anchored to creation, the same event as the floor",
                       value=same0, key=f"same_{preset}")
    if same:
        if L > F:
            st.success(f"L = {L} > F = {F}: no record collides. The two limits bound one "
                       "retention window, readable from the text alone.", icon="✅")
        else:
            st.error(f"L = {L} <= F = {F}: every record collides, and the text "
                     "contradicts itself on its face.", icon="🚨")
    else:
        if L > F:
            st.success(f"L = {L} > F = {F}: no record collides, wherever its anchor "
                       "event falls.", icon="✅")
        else:
            gap = F - L
            st.warning(
                f"L = {L} <= F = {F}: a record collides exactly when its anchor event "
                f"falls within {gap} month(s) of creation (e(a) - t(a) <= {gap}). "
                "Nothing in the text says which records those are; each record's "
                "history does.", icon="⚠️")
            offsets = list(range(0, F + 1))
            st.bar_chart(
                {"months of collision": [max(0, (t0 + F) - (t0 + d + L) + 1)
                                         for t0, d in [(0, d) for d in offsets]]},
                x_label="anchor event, months after creation",
                y_label="months in which both apply")
    st.caption(
        "Article 68(12) is of the external-anchor kind: six months from permit expiry "
        "against twelve from the log entry, so logs whose permit expires within six "
        "months of the entry collide (Corollary 1.2). Section 17 of politiregisterloven "
        "measures both limbs from the log entry with the ceiling longer, so it bounds a "
        "window instead (Chapter 6, Section 6.10).")


st.divider()
st.caption(
    "This application is a viewer over the verified artefact.""",
         why="Proposition 3 explorer"),
    dict(id="P39-12", file=A,
         old="    \"of results. Tab 1, Tab 3 and Tab 5 reproduce figures reported in Chapter 5; \"\n    \"Tab 2 is outside the thesis claims, and Tab 4 is illustrative of the \"\n    \"Norwegian setting and not a thesis claim either.",
         new="    \"of results. Tab 1, Tab 3 and Tab 5 reproduce figures reported in Chapter 5; \"\n    \"Tab 2 is outside the thesis claims, Tab 4 is illustrative of the \"\n    \"Norwegian setting and not a thesis claim either, and Tab 6 evaluates the \"\n    \"condition of Proposition 3 for any floor and ceiling you set.",
         why="footer"),
]
