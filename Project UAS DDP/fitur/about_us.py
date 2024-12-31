import streamlit as st

st.title("Kelompok 5")

sekilas_kami = "Kelompok 5 adalah sebuah kelompok yang terbentuk untuk membuat projek aplikasi dengan menggunakan *Streamlit*. Kami membuat aplikasi ini dengan bertemakan Aplikasi Kesehatan. Dengan bertujuan supaya memudahkan masyarakat untuk mencari kesehatan jasmani yang tersedia didalam fitur kami."
definisi = "Definisi kelompok kami adalah selalu pantang menyerah, optimis, selalu percaya akan hasil, percaya satu sama lain, dan selalu mengutamakan diskusi walaupun banyak tugas yang selalu menumpuk"
akhir = "Yang membuat solidaritas kami sebagai teman didalam satu kelas menjadi kuat, dan telah selesai untuk menyelesaikan tugas Project ini. Terima kasih semuanya!"

if st.button("Learn more"):
    st.info(f"{sekilas_kami}")
    st.info(f"{definisi}")
    st.info(f"{akhir}")

st.write("---")
st.write("© 2024 Kelompok 5. Hak cipta dilindungi.")