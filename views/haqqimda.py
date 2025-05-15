import streamlit as st
from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Toğrul Nuruşzadə", anchor=False)
    st.subheader("İT Mütəxəssi & Data Analitik", anchor=False)
    if st.button("✉️ Əlaqə"):
        show_contact_form()


col3, col4, col5, col6, col7 = st.columns(5, gap="small", vertical_alignment="center")
with col3:
    st.markdown('<a href="mailto:toghrul.nur@gmail.com" target="_blank">Gmail</a>', unsafe_allow_html=True)

with col4:
    st.markdown('<a href="https://www.linkedin.com/in/toghrulnurushzade/" target="_blank">LinkedIn</a>', unsafe_allow_html=True)

with col5:
    st.markdown('<a href="https://github.com/ExGashgin" target="_blank">Github</a>', unsafe_allow_html=True)

with col6:
    st.markdown('<a href="https://www.facebook.com/exgashgin/" target="_blank">Facebook</a>', unsafe_allow_html=True)

with col7:
    st.markdown('<a href="https://www.instagram.com/n_togrul_n/" target="_blank">Instagram</a>', unsafe_allow_html=True)


# --- ABOUT ME ---
st.write("\n")
st.subheader("Haqqımda qısa məlumat", anchor=False)
st.write("---")
st.write(
    """
    Təcrübəli İT mütəxəssisi kimi, mən proqramlaşdırma, məlumat bazalarının 
    idarə olunması və biznes analitikası sahəsində güclü bacarıqlara sahibəm. 
    Son illərdə Data Analitik sahəsinə keçid edərək Python, SQL, Power 
    BI və data vizuallaşdırma texnikalarından istifadə edərək dəyərli məlumatlar 
    çıxarmaq və qərar qəbulunu optimallaşdırmaq bacarıqlarımı inkişaf etdirmişəm.
    """
)
st.write(
    """
    Təhsilimi Köln Texniki Universitetində Kompüter Elmləri üzrə magistratura dərəcəsi 
    ilə tamamlamışam. Daha əvvəl Azərbaycan Dövlət Neft və Sənaye Universitetində 
    Kompüter Mühəndisliyi üzrə bakalavr təhsili almışam.
    """
)
st.write(
    """
Peşəkar fəaliyyətim zamanı Almaniyada Eurofins və McZimmervermietung GmbH kimi 
şirkətlərdə çalışaraq data emalı, İT infrastrukturunun optimallaşdırılması və 
təşkilat daxilində effektiv texniki dəstək təmin etmişəm. Məlumat bazalarının 
idarə edilməsi və təşkilatçılıq bacarıqları sayəsində müxtəlif komandalarla uğurla 
əməkdaşlıq etmişəm.
"""
)
st.write(
    """
Problem həll etmə bacarığımı inkişaf etdirərək verilənlərlə işləmə və strukturlaşdırılmış 
analiz sahələrində özümü sübut etmişəm. Hədəfim data yönümlü metodologiyaları tətbiq 
edərək biznes problemlərini həll etmək və strateji inkişafı dəstəkləməkdir.

    """

)