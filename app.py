import streamlit as st

st.write("""
# Is Your Number Odd or Even?
""")

st.header('Please Enter A Number Below')

num = st.number_input("Number", min_value=0, step=1)

if num % 2 == 0:
  num = 'Even'
else:
  num = 'Odd'

st.subheader('Your number is ' + num)
