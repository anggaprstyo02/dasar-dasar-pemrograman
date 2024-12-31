import streamlit as st

st.title('Hitung Luas Persegi')

panjang = st.number_input ('Masukkan Nilai Panjang', 0)
lebar = st.number_input ('Masukkan Nilai Lebar', 0)
hitung = st.button('Hitung luas')

if hitung :
    luas = panjang * lebar
    st.write('Luas persegi panjang adalah =', luas)
    st.success(f'Luas persegi panjang adalah = {luas}') 