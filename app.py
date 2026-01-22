import streamlit as st

st.title("few more")
name = st.text_input("enter name")

if st.button("submit"):
    st.write("hello")
