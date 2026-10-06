# P58d — viewer text: leaves also hold a salted commitment to the patient link.
EDITS = [dict(id="P58d-01", file="demo_app/app.py",
 old='"against the log root. Leaves hold the accessor fields and the commitment, "\n            "never the payload or the patient link, so the log never needs erasing."',
 new='"against the log root. Leaves hold the accessor fields, the payload commitment "\n            "and a salted commitment to the patient link, never the payload or the link "\n            "itself, so the log never needs erasing and a changed link is still caught."',
 why="M2")]
LOST_OK = []
