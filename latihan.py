import streamlit as st
from denyut_nadi import app as denyut_nadi
from persegi import app as persegi

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Latihan", ["Denyut Nadi", " persegi"])

if page == "Denyut Nadi":
    denyut_nadi()
elif page == "Latihan 2":
    persegi()
