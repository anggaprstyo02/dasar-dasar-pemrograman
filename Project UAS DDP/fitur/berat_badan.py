import streamlit as st

def hitung_berat_badan_ideal(jenis_kelamin, tinggi_badan) :
    if jenis_kelamin == 'Laki-Laki':
        berat_badan_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.1)
    elif jenis_kelamin == 'Perempuan':
        berat_badan_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)
    else:
        berat_badan_ideal = None
    return berat_badan_ideal

st.title("Mencari Berat Badan Ideal (Broca)")
st.write("Metode Broca adalah cara sederhana dan populer untuk menghitung berat badan ideal berdasarkan tinggi badan. Metode ini diperkenalkan oleh Dr. Pierre Paul Broca, seorang dokter asal Prancis. Rumusnya berbeda untuk pria dan wanita karena perbedaan komposisi tubuh antara keduanya.")

# Input pengguna
jenis_kelamin = st.selectbox("Pilih jenis kelamin:", ["Laki-Laki", "Perempuan"])
tinggi_badan = st.number_input("Masukkan tinggi badan (cm):", min_value=0, max_value=250, step=1)

# Hitung berat badan ideal jika data valid
if st.button("Hitung"):
    if tinggi_badan > 0:
        berat_badan_ideal = hitung_berat_badan_ideal(jenis_kelamin, tinggi_badan)
        if berat_badan_ideal:
            st.success(f"Berat badan ideal untuk {jenis_kelamin} dengan tinggi {tinggi_badan} cm adalah dengan berat badan ideal {berat_badan_ideal} kg")
        else:
            st.error("Mohon untuk melakukan perintah yang benar.")
    else:
        st.warning("Masukkan tinggi badan yang valid.")

st.write("---")
st.write("© 2024 Kelompok 5. Hak cipta dilindungi.")