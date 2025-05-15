import streamlit as st

st.title("Təhsil")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/th_koeln.png", width=150)

with col2:
    st.header("Köln Texniki Univeristeti", anchor=False)
    st.subheader("Magistr", anchor=False)
    st.write(
        "Oktyabr 2018 - Avqust 2024",
    )


col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
with col3:
    st.image("./assets/aztu.png", width=150)

with col4:
    st.header("Azərbaycan Texniki Universiteti", anchor=False)
    st.subheader("Magistr", anchor=False)
    st.write(
        "Sentyabr 2016 - İyul 2018",
    )

col5, col6 = st.columns(2, gap="small", vertical_alignment="center")
with col5:
    st.image("./assets/esgerlik.png", width=150)
with col6:
    st.header("Azərbaycan Müdafiə Nazirliyi", anchor=False)
    st.subheader("Hərbi Xirmət", anchor=False)
    st.write(
        "İyul 2014 - İyun 2016",
    )

col5, col6 = st.columns(2, gap="small", vertical_alignment="center")
with col5:
    st.image("./assets/adnsu.png", width=150)
with col6:
    st.header("Azərbaycan Dövlət Neft və Sənaye Universiteti", anchor=False)
    st.subheader("Bakalavr", anchor=False)
    st.write(
        "Sentyabr 2010 - İyul 2014",
    )