import streamlit as st

def menghitung_kalori(usia, berat_badan, tinggi_badan, jenis_kelamin, tingkat_aktivitas):
    if jenis_kelamin == "Laki-laki":
        bmr = 10 * berat_badan + 6.25 * tinggi_badan - 5 * usia + 5
    else:
        bmr = 10 * berat_badan + 6.25 * tinggi_badan - 5 * usia - 161

    if tingkat_aktivitas == "Sangat rendah (tidak aktif)":
        kalori = bmr * 1.2
    elif tingkat_aktivitas == "Rendah (olahraga ringan)":
        kalori = bmr * 1.375
    elif tingkat_aktivitas == "Sedang (olahraga moderat)":
        kalori = bmr * 1.55
    elif tingkat_aktivitas == "Tinggi (olahraga berat)":
        kalori = bmr * 1.725
    else:
        kalori = bmr * 1.9

    return kalori

# Judul Aplikasi
st.title("Menghitung Kebutuhan Kalori Harian")

# Deskripsi Aplikasi
st.write("Aplikasi ini membantu Anda menghitung kebutuhan kalori harian berdasarkan usia, berat badan, tinggi badan, jenis kelamin, dan tingkat aktivitas.")

# Input Pengguna
st.header("Masukkan Data Anda")
usia = st.number_input("Usia (tahun):", min_value=0, max_value=120, step=1)
berat_badan = st.number_input("Berat Badan (kg):", min_value=1.0, max_value=300.0, step=0.1)
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=50.0, max_value=250.0, step=0.1)
jenis_kelamin = st.selectbox("Jenis Kelamin:", ("Laki-laki", "Perempuan"))
tingkat_aktivitas = st.selectbox(
    "Tingkat Aktivitas:",
    (
        "Sangat rendah (tidak aktif)",
        "Rendah (olahraga ringan)",
        "Sedang (olahraga moderat)",
        "Tinggi (olahraga berat)",
        "Sangat tinggi (aktivitas fisik sangat berat)"
    )
)

# Tombol Hitung
if st.button("Hitung Kebutuhan Kalori"):
    if usia > 0 and berat_badan > 0 and tinggi_badan > 0:
        kalori = menghitung_kalori(usia, berat_badan, tinggi_badan, jenis_kelamin, tingkat_aktivitas)
        st.success(f"Kebutuhan kalori harian Anda adalah {kalori:.2f} kalori.")
    else:
        st.error("Harap masukkan data yang valid.")

st.write("---")
st.write("© 2024 Kelompok 5. Hak cipta dilindungi.")