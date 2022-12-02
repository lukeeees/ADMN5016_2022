import streamlit as st
from predict_page import show_predict_page
from explore import show_explore_page
#py -m streamlit run app.py
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()