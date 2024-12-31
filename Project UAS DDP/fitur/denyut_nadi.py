import streamlit as st

class KalkulatorDenyutNadi:
    def __init__(self, usia,):
        self.usia = usia
        self.denyut_nadi_maks = 220 - usia

    def get_denyut_nadi_istirahat(self):
        # Rentang denyut nadi istirahat ideal (perkiraan umum berdasarkan usia)
        if self.usia < 30:
            return 60, 100
        elif self.usia < 50:
            return 65, 105
        else:
            return 70, 110

    def get_denyut_nadi_aktivitas(self, intensitas):
        if intensitas == "ringan":
            return 0.5 * self.denyut_nadi_maks, 0.69 * self.denyut_nadi_maks
        elif intensitas == "sedang":
            return 0.5 * self.denyut_nadi_maks, 0.69 * self.denyut_nadi_maks
        elif intensitas == "berat":
            return 0.7 * self.denyut_nadi_maks, 0.85 * self.denyut_nadi_maks
        else:
            return 0, 0  # Intensitas tidak dikenal
# Antarmuka Streamlit
st.title("Kalkulator Mencari Denyut Nadi Normal")
st.write("Denyut nadi normal adalah jumlah denyutan jantung per menit atau biasa disebut BPM (Beats Per Minute) yang bervariasi berdasarkan usia dan aktivitas fisik. Denyut nadi memberikan gambaran tentang seberapa baik jantung memompa darah ke seluruh tubuh.")

# Input usia pengguna
usia = st.number_input("Masukkan usia Anda:", min_value=0, max_value=120, step=0)
aktivitas = st.selectbox(
        "Pilih tingkat aktivitas Anda:",
        ("Istirahat", "Aktivitas Ringan", "Aktivitas Sedang", "Aktivitas Berat")
    )
if st.button("Hitung Denyut Nadi"):
    if usia:
        kalkulator = KalkulatorDenyutNadi(usia)

        st.write(f"Denyut Nadi Maksimum Anda pada umur {usia} tahun adalah {kalkulator.denyut_nadi_maks} bpm")

        # Denyut nadi istirahat
        istirahat_min, istirahat_maks = kalkulator.get_denyut_nadi_istirahat()

        # Pilihan aktivitas
        

        if aktivitas == "Istirahat":
            st.write(f"dan ketika anda sedang {aktivitas} adalah {istirahat_min:.0f} - {istirahat_maks:.0f} bpm")
        else:
            mapping_intensitas = {
                "Aktivitas Ringan": "ringan",
                "Aktivitas Sedang": "sedang",
                "Aktivitas Berat": "berat",
            }
            intensitas = mapping_intensitas.get(aktivitas, "tidak dikenal")
            min_dn, maks_dn = kalkulator.get_denyut_nadi_aktivitas(intensitas)
            st.write(f"dan ketika anda sedang {aktivitas} adalah {min_dn:.0f} - {maks_dn:.0f} bpm")
    else:
        st.error("Masukkan Usia Terlebih Dahulu!")

st.write("---")
st.write("© 2024 Kelompok 5. Hak cipta dilindungi.")