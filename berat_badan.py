import streamlit as st

def hitung_berat_badan_ideal(jenis_kelamin, tinggi_badan):
    if jenis_kelamin == "Pria":
        berat_badan_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.1)
    elif jenis_kelamin == "Wanita":
        berat_badan_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)
    else:
        berat_badan_ideal = None
    return berat_badan_ideal

st.title("Kalkulator Berat Badan Ideal (Rumus Broca)")

# Input pengguna
jenis_kelamin = st.selectbox("Pilih jenis kelamin:", ["Pria", "Wanita"])
tinggi_badan = st.number_input("Masukkan tinggi badan (cm):", min_value=100, max_value=250, step=1)

# Hitung berat badan ideal jika data valid
if tinggi_badan > 0:
    berat_badan_ideal = hitung_berat_badan_ideal(jenis_kelamin, tinggi_badan)
    if berat_badan_ideal:
        st.success(f"Berat badan ideal untuk {jenis_kelamin} dengan tinggi {tinggi_badan} cm adalah {berat_badan_ideal:.2f} kg.")
        st.success("Harus tetap menjaga pola makan")
    else:
        st.error("Jenis kelamin tidak valid.")
else:
    st.warning("Masukkan tinggi badan yang valid.")
