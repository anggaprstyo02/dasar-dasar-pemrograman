import streamlit as st

# Fungsi untuk menghitung tinggi badan ideal menggunakan while loop
def hitung_tinggi_badan_ideal(berat_badan, bmi_ideal):
    tinggi_badan_ideal = 0.0  # Inisialisasi tinggi badan dalam meter
    iterasi = 0  # Untuk menghitung jumlah iterasi

    # Loop untuk mendekati tinggi badan ideal
    while True:
        tinggi_badan_ideal += 0.01  # Tambah tinggi badan dalam meter
        iterasi += 1
        if (tinggi_badan_ideal ** 2) * bmi_ideal >= berat_badan:
            break

    tinggi_badan_ideal_cm = tinggi_badan_ideal * 100  # Konversi ke cm
    return tinggi_badan_ideal_cm, iterasi

# Judul aplikasi
st.title("Mencari Tinggi Badan Ideal dengan BMI")
st.write("Indeks Massa Tubuh (IMT) atau Body Mass Index (BMI) adalah tinggi badan yang dihitung berdasarkan berat badan dan indeks massa tubuh yang diinginkan. BMI adalah indikator yang digunakan untuk menilai apakah berat badan seseorang berada dalam kategori kurang, normal, berlebih, atau obesitas berdasarkan tinggi badannya.")

# Input berat badan pengguna
berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=0.0, step=0.1)

st.markdown("#### BMI normal adalah antara 18.5 - 24.9")
# Input BMI ideal (default: 22)
bmi_ideal = st.slider("Pilih nilai BMI ideal:", min_value=18.5, max_value=24.9, value=22.0, step=0.1)

# Perhitungan tinggi badan ideal
if st.button("Hitung Tinggi Badan Ideal"):
    if berat_badan > 0:
        tinggi_badan_ideal_cm, iterasi = hitung_tinggi_badan_ideal(berat_badan, bmi_ideal)
        st.success(f"Tinggi badan ideal Anda dengan BMI {bmi_ideal:.2f} adalah {tinggi_badan_ideal_cm:.2f} cm.")
        st.info(f"Perhitungan selesai dalam {iterasi} iterasi.")
    else:
        st.warning("Masukkan berat badan untuk menghitung tinggi badan ideal.")

st.write("---")
st.write("© 2024 Kelompok 5. Hak cipta dilindungi.")