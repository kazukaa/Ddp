import streamlit as st 

st.write("Oi Oi Oi")

with st.form("Nabung"):
    nama = st.text_input("Masukkan Nama: ")
    nominal = st.number_input ("Masukkan Nominal: ")
    submit = st.form_submit_button("Simpan")
    
    if submit:
        st.write(nama)
        st.session_state["Nabung"].append({
            "Nama" : nama,
            "Nominal" : nominal,
        })
        st.success("Berhasil Menabung")