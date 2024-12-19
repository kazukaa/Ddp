import streamlit as st

st.write("OI OI OI")
st.session_state["Nabung"]

jumlah = 0
for session in st.session_state["Nabung"]:
    jumlah += session["Nominal"]
    
st.write("Total tabungan: ", jumlah)