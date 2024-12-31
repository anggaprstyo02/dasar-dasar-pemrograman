import streamlit as st

st.title("Halaman Dashboard")

# Fungsi untuk Menghitung dan Menyimpan Total Nabung
def total():
    total_nabung = sum(t["Jumlah"] for t in st.session_state ["Jumlah"] if t["Tipe"] == "Menabung")

    return f"Total Anda Menabung sejumlah {total_nabung}"

st.write(total())
