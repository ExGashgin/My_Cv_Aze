import streamlit as st

# --- PAGE SETUP ---


haqqimda = st.Page(
    "views/haqqimda.py",
    title="Haqqımda",
    icon=":material/account_circle:",
    default=True,
)

bacariqlar = st.Page(
    "views/bacariqlar.py",
    title="Bacarıqlar",
    icon=":material/star:",
)
tehsil = st.Page(
    "views/tehsil.py",
    title= "Təhsil",
    icon=":material/school:",
)
ish_tecrubesi = st.Page(
    "views/ish_tecrubesi.py",
    title="Iş Təcrübəsi",
    icon=":material/work_history:",
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Məlumatlar": [haqqimda, bacariqlar],
        "Təhsil və İş təcrübəsi": [tehsil, ish_tecrubesi],
    }
)


# --- SHARED ON ALL PAGES ---

# --- RUN NAVIGATION ---
pg.run()