import streamlit as st
import joblib

model = joblib.load("clean_mail.pkl")
vector = joblib.load("vector.pkl")

st.title('Spam Email Checker')

st.write("Copy And Paste Your Email Here And ML Model Will Check Is It Spam Or Not.")

email_text = st.text_area('Copy And Paste Your Email Here')

check_button = st.button('Check')

if(check_button):
    v_mail = vector.transform([email_text])
    res = model.predict(v_mail)
    st.subheader(f'It is {res[0]}.')