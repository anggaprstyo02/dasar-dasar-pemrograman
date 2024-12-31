import streamlit as st

# Sidebar Directory
home = st.Page("./fitur/home.py" , title="Home")
berat_badan = st.Page("./fitur/berat_badan.py" , title="Kalkulator Berat Badan Ideal")
tinggi_badan = st.Page("./fitur/tinggi_badan.py" , title="Kalkulator Tinggi Badan Ideal")
denyut_nadi = st.Page("./fitur/denyut_nadi.py" , title="Denyut Nadi Normal")
kalori_harian = st.Page("./fitur/kalori_harian.py" , title="Kebutuhan Kalori Harian")
about_us = st.Page("./fitur/about_us.py", title="Kelompok 5")



pg = st.navigation({
        "Menu Utama": [home],
        "Fitur": [berat_badan, tinggi_badan, denyut_nadi, kalori_harian],
        "About Us": [about_us]
        }
)
 
# Menjalankan Navigasi
pg.run()