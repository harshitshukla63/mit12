import streamlit as st

st.title("kindly sdd city and age")
age = st.slider("select your age" , 1,100)
city = st.selectbox("select your city :", ["delhi","mumbai","pune"])

if st.button("submit"):
    st.write("age" , age)
    st.write("city" , city)