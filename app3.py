import streamlit as st


st.title("basic calculator")

num1 = st.number_input("enter num1")
num2 = st.number_input("enter mum2")

operations = st.selectbox("choose op", ["add","sub","multiply","divide"])


if st.button("calculator"):
    if operations == "add":
        st.write(num1 + num2)
    elif operations == "sub":
        st.write(num1 - num2)
    elif operations == "multiply":
        st.write(num1 * num2)    
    elif operations == "div":
        st.write(num1 / num2)
