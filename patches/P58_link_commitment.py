# P58 — João (6 Oct), comment for Arshad: implement the salted commitment to the patient link in each
# log entry, and a third tamper test (a changed link), which he confirmed fails on the previous code.
# Same edits on demo_app/ and its two copies.
FILES = ["demo_app/trf_checker.py", "repro_package/trf_checker.py", "code_artefacts/trf_checker.py"]
BASE = [
 ("  - V_II tests integrity against an append-only Merkle log (RFC 6962 hashing), with a tamper\n",
  "  - each log leaf also holds a salted commitment to the patient link, so a changed link no longer\n"
  "    opens it, while the leaf still never holds the subject fields themselves\n"
  "  - V_II tests integrity against an append-only Merkle log (RFC 6962 hashing), with a tamper\n",
  "header"),
 ('    return json.dumps({"event": "access", "rid": rec.rid, "t_a": rec.t_a,\n                       "m_acc": m_acc, "c": rec.c}, sort_keys=True).encode()',
  '    return json.dumps({"event": "access", "rid": rec.rid, "t_a": rec.t_a,\n                       "m_acc": m_acc, "c": rec.c, "c_subj": rec.c_subj},\n                      sort_keys=True).encode()',
  "leaf carries c_subj"),
 ('    root = AUDIT_LOG.root()\n    checks = [("access", _creation_entry(rec))]',
  '    if any(f in rec.m for f in SUBJECT_FIELDS):                # the link, while it is held\n'
  '        link = _entry({f: rec.m.get(f) for f in SUBJECT_FIELDS})\n'
  '        if rec.subj_salt is None or commit(link, rec.subj_salt) != rec.c_subj:\n'
  '            return False, "patient link does not open its logged commitment (altered)"\n'
  '    root = AUDIT_LOG.root()\n    checks = [("access", _creation_entry(rec))]',
  "integrity checks the link"),
 ('        self.c = commit(payload, self.salt)   # survives invalidation\n',
  '        self.c = commit(payload, self.salt)   # survives invalidation\n'
  '        # salted commitment to the patient link, logged with the accessor fields (Ch4 s4.8)\n'
  '        self.subj_salt = make_salt(rid + 100000)\n'
  '        self.c_subj = commit(_entry({f: self.m[f] for f in SUBJECT_FIELDS}), self.subj_salt)\n',
  "Record holds c_subj"),
 ('        for f in SUBJECT_FIELDS:          # beta = 0 from the ceiling (Ch4 s4.7, steps 2 and 4)\n            rec.m.pop(f, None)\n',
  '        for f in SUBJECT_FIELDS:          # beta = 0 from the ceiling (Ch4 s4.7, steps 2 and 4)\n            rec.m.pop(f, None)\n'
  '        rec.subj_salt = None              # the link\'s salt goes with the link\n',
  "salt destroyed with the link"),
 ('    print(f"after restoring both       : V_II={V_II(demo, demo.t_a)[0]}")',
  '    xb = next(r for r in prim if r.iota is not None)          # a cross-border record keeps its link\n'
  '    saved_p = xb.m["patient_pseudonym"]\n'
  '    xb.m["patient_pseudonym"] = "PSN-9999"                    # tamper with the patient link\n'
  '    ok_p, why_p = V_II(xb, xb.t_a)\n'
  '    xb.m["patient_pseudonym"] = saved_p\n'
  '    print(f"tamper test, rid={xb.rid} link altered  : V_II={ok_p}  ({why_p})")\n'
  '    print(f"after restoring all three  : V_II={V_II(demo, demo.t_a)[0] and V_II(xb, xb.t_a)[0]}")',
  "third tamper test"),
]
EDITS = [dict(id=f"P58-{i*len(BASE)+j+1:02d}", file=f, old=o, new=n, why=w)
         for i, f in enumerate(FILES) for j, (o, n, w) in enumerate(BASE)]
LOST_OK = []
