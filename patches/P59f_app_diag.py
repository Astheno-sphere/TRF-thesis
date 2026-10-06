# P59f — viewer: when the Thesis run disagrees with Chapter 5, say which check failed, and name the one
# known cause (a deployment still running the previous checker module, which cannot see a changed link).
EDITS=[dict(id='P59f-01',file='demo_app/app.py',
 old='''            st.error(
                "This run does NOT match the figures reported in Chapter 5. "
                "Do not present these numbers — investigate the discrepancy first."
            )
''',
 new='''            st.error(
                "This run does NOT match the figures reported in Chapter 5. "
                "Do not present these numbers — investigate the discrepancy first."
            )
            st.dataframe([
                {"check": "Semantics I violations", "expected": 95, "got": M["sem1_total"]},
                {"check": "Semantics II violations", "expected": 0, "got": M["sem2_total"]},
                {"check": "Corollary 1.2 witnesses", "expected": 39, "got": M["cor12"]},
                {"check": "records verifying", "expected": len(records), "got": n_ok},
                {"check": "tamper: actor altered fails", "expected": True, "got": not ok_t},
                {"check": "tamper: ground altered fails", "expected": True, "got": not ok_g},
                {"check": "tamper: patient link altered fails", "expected": True, "got": not ok_p},
                {"check": "all restored verify", "expected": True, "got": ok_r},
            ], hide_index=True)
            if not hasattr(records[0], "c_subj"):
                st.warning("The checker module loaded here predates the patient-link commitment. "
                           "The deployment is running a stale copy of trf_checker.py: reboot the app.")
''',
 why="diagnosis")]
LOST_OK=[]
