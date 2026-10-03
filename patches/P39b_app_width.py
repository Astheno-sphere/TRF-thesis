# P39b — `use_container_width` is deprecated (removal announced after 2025-12-31) and Streamlit
# Cloud installs the latest release, so the app could break on redeploy. Replaced by width="stretch";
# requirements raised to streamlit>=1.45 (width on st.dataframe) and cryptography>=42 for the
# optional module, matching the public repository's requirements.
A = "demo_app/app.py"
EDITS = [
    dict(id="P39b-01", file=A, old="use_container_width=True", new='width="stretch"', count=3,
         why="deprecated parameter"),
    dict(id="P39b-02", file="demo_app/requirements.txt", old="streamlit>=1.30\n",
         new="streamlit>=1.45\ncryptography>=42\n", why="requirements"),
]
