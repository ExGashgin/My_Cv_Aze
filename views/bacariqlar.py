import streamlit as st

st.title("Bacarıqlarım", anchor=False)

st.write("\n")
st.header("Dillər", anchor=False)
col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/azerabiajani.png", width=50)
with col2:
    st.image("./assets/turkish.png", width=50)
with col3:
    st.image("./assets/english.webp", width=50)
with col4:
    st.image("./assets/german.webp", width=50)
with col5:
    st.image("./assets/russian.png", width=50)


st.write("\n")
st.header("Texniki Bacarıqlar", anchor=False)
st.subheader("İT Mütəxəssis bacarıqları", anchor=False)
st.write("---")
st.write(
    """
    - Problem həll etmə və diaqnostika: Avadanlıq və proqram təminatı problemlərini effektiv şəkildə aşkar etmək və həll etmək.
    - Əməliyyat sistemləri üzrə bilik: Windows və macOS platformalarına dair məlumatlılıq.
    - Şəbəkə əsasları: IP konfiqurasiyaları, VPN-lər və bağlantı problemlərini anlamaq.
    - Proqram və avadanlıq dəstəyi: Tətbiqlərin və cihazların quraşdırılması, konfiqurasiya edilməsi və idarə olunması.
    - Uzaqdan giriş alətləri: TeamViewer və AnyDesk kimi alətlərlə istifadəçilərə uzaqdan kömək göstərmək.
    - Sorğu idarəetmə sistemləri: Jira və ServiceNow kimi platformalar vasitəsilə istifadəçi sorğularını izləmək və idarə etmək.
    """
)

st.subheader("Proqramlaşdırma dilləri və bacarıqları", anchor=False)
st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/sql.png", width=100)

with col2:
    st.write(
        """
        - Verilənlərin əldə edilməsi üçün effektiv sorğular yazmaq
        - Birləşdirmələr, funksiyalar və alt sorğular icra etmək
        - Məlumat bazası strukturalarını dizayn etmək və normallaşdırmaq
        - Saxlanılmış prosedurlar və triqqerlər ilə işləmək
        """
    )

st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/python.png", width=100)

with col2:
    st.write(
        """
        - Python sintaksisindən istifadə edərək təmiz və səmərəli kod yazmaq
        - Pandas və NumPy ilə verilənləri manipulyasiya etmək
        - Matplotlib və Seaborn vasitəsilə məlumatları vizuallaşdırmaq
        - Səhvləri aşkar etmək və onları aradan qaldırmaq
        """
    )

st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/html.png", width=100)

with col2:
    st.write(
        """
        - HTML ilə veb səhifələrin qurulması
        - Multimedia elementlərinin (şəkillər, videolar, audio) yerləşdirilməsi
        - Formlar və interaktiv elementlərin tətbiqi
        - CSS vasitəsilə dizayn və tərtibatın minimal tənzimlənmənin aparılması
        """
    )


st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/php.webp", width=100)

with col2:
    st.write(
        """
        - PHP ilə dinamik veb tətbiqlər yazmaq
        - MySQL vasitəsilə məlumat bazasına qoşulmaq
        - Üçüncü tərəf API-lərini inteqrasiya etmək
        - PHP skriptlərini effektiv şəkildə redaktə etmək və səhvləri düzəltmək
        """
    )


st.subheader("Data Analist bacarıqları", anchor=False)
st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/data-visualization.webp", width=100)

with col2:
    st.write(
        """
        - Power BI: İnteraktiv hesabatlar və panellər yaratmaq
        - Tableau: Vizualizasiya və məlumatlar əsasında hekayələr qurmaq
        - Excel: Qrafiklər, filtrlər və KPI-lər vasitəsilə interaktiv hesabatlar hazırlamaq
        """
    )

st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/database.png", width=100)

with col2:
    st.write(
        """
        - PostgreSQL: Ətraflı SQL sorğuları, məlumat modelləşdirilməsi və 
        performansın optimallaşdırılması
        - SQLite: Lokal tətbiqlər üçün yüngül verilənlər bazası idarəetməsi
        - MySQL: Verilənlər bazasının dizaynı, indeksləmə və optimallaşdırma
        - SQL Server: Data bazası, ETL prosesləri və hesabat xidməti
        """
    )
    

st.write("\n")
st.header("Şəxsi keyfiyyətlər", anchor=False)
st.write(
    """
    - Kommunikasiya bacarıqları: Data hekayələşdirmə, aktiv dinləmə, təqdimat bacarıqları
    - Problemlərin həlli və kritik düşüncə: Analitik düşüncə, detallara diqqət
    - Əməkdaşlıq və komanda işi: Şöbələrarası kommunikasiya, uyğunlaşma bacarığı
    - Vaxtın idarə edilməsi və təşkilatçılıq: Prioritetlərin müəyyənləşdirilməsi, eyni 
    anda bir çox iş görmə
      """
)

CERTIFICATES = {
    "🏆 Pytonla verilenlərin analizi": "https://www.codecademy.com/profiles/java3425545538/certificates/a91cf883da2f48e2b977577646801c81",
    "🏆 SQL-lə verilənərin analizi": "https://www.codecademy.com/profiles/java3425545538/certificates/5cafb2d937090210d7df3652",
    "🏆 Power BI-da BI hesabatların hazırlanması": "https://www.codecademy.com/profiles/java3425545538/certificates/1cb76ac48943853ca32c394afeb491c9",
    "🏆 Tableu-da BI hesabatların hazırlanması": "https://www.codecademy.com/profiles/java3425545538/certificates/050d7cf465567fdd0c9abb1fbf20e269",
    "🏆 Data fundamental biliklər": "https://www.credly.com/badges/3391a546-b6eb-45c8-ac5a-6b523366b937/linked_in_profile",
    "🏆 SQL": "https://www.codecademy.com/profiles/java3425545538/certificates/042a4e5884e3eb6ea1f2a12be6abb851",
    "🏆 Python 3": "https://www.codecademy.com/profiles/java3425545538/certificates/6c152bd262967f8c941c9707ed636bda",
    }

st.write('\n')
st.header("Sertifikatlar", anchor=False)
for project, link in CERTIFICATES.items():
    st.write(f"[{project}]({link})")