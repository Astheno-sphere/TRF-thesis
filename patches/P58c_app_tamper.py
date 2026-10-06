# P58c — viewer: third tamper test (patient link) on the Thesis run page, included in its self-check.
F = "demo_app/app.py"
EDITS = [
 dict(id="P58c-01", file=F,
  old='        ok_r = trf.V_II(demo, demo.t_a)[0]\n        i1, i2, i3 = st.columns(3)',
  new='        xb = next(r for r in records if r.sigma == "primary" and r.iota is not None)\n'
      '        saved_p = xb.m["patient_pseudonym"]\n'
      '        xb.m["patient_pseudonym"] = "PSN-9999"\n'
      '        ok_p, why_p = trf.V_II(xb, xb.t_a)\n'
      '        xb.m["patient_pseudonym"] = saved_p\n'
      '        ok_r = trf.V_II(demo, demo.t_a)[0] and trf.V_II(xb, xb.t_a)[0]\n'
      '        i1, i2, i3, i4 = st.columns(4)', why="third tamper test"),
 dict(id="P58c-02", file=F,
  old='        i3.metric("Tamper: ground altered", "fails" if not ok_g else "PASSES")',
  new='        i3.metric("Tamper: ground altered", "fails" if not ok_g else "PASSES")\n'
      '        i4.metric("Tamper: patient link altered", "fails" if not ok_p else "PASSES")', why="metric"),
 dict(id="P58c-03", file=F,
  old='            f"after restoring both          : V_II={ok_r}",',
  new='            f"rid={xb.rid} patient link altered  : V_II={ok_p}  ({why_p})\\n"\n'
      '            f"after restoring all three     : V_II={ok_r}",', why="console line"),
 dict(id="P58c-04", file=F,
  old='and n_ok == len(records) and not ok_t and not ok_g and ok_r):',
  new='and n_ok == len(records) and not ok_t and not ok_g and not ok_p and ok_r):', why="self-check"),
 dict(id="P58c-05", file=F,
  old='Semantics II, 200/200 records verifying, both tamper tests failing."',
  new='Semantics II, 200/200 records verifying, all three tamper tests failing."', why="banner"),
]
LOST_OK = []
