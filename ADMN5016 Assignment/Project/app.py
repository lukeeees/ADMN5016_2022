import streamlit as st


from predict_page import show_predict_page
from explore import show_explore_page
#py -m streamlit run app.py

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
path = st.sidebar.camera_input("Discussing Now")

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

st.markdown("---")
st.write("Created by: Luke and Ziyang")

