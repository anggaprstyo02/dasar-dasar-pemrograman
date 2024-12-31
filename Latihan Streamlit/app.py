import streamlit as st


# Sidebar Directory
dashboard = st.Page("./fitur/dashboard.py" , title="Dashboard")
nabung = st.Page("./fitur/nabung.py" , title="Nabung")
penarikan = st.Page("./fitur/penarikan.py" , title="Penarikan")
latihan = st.Page("./fitur/latihan.py" , title="Latihan")

pg = st.navigation({
        "Menu Utama": [dashboard],
        "Fitur": [nabung, penarikan, latihan],
        }
)
if "Jumlah" not in st.session_state:
    st.session_state["Jumlah"] = []
 
# Menjalankan Navigasi
pg.run()

 
