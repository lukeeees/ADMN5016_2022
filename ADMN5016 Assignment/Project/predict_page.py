import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

#data= load_model()

#model_loaded = data['model']

def show_predict_page():
    st.title("CellPhone Price Predictor")
    st.write("""### We need some information to predict the price of Mobile Phone""")

    criteria = {
        "No": 0,
        "Yes":1
    }

    battery_power = st.slider("Battery Power", 500, 2000, 600)  
    blue = st.selectbox("Bluetooth", criteria)
    clock_speed = st.slider("Clock Speed", 0,3,1)
    dual_sim = st.selectbox("Dual Sim", criteria)
    fc = st.slider("Front Camera",0,19,2)
    four_g = st.selectbox("4G", criteria)
    int_memory = st.slider("Internal Memory (Gigabytes)", 2,64,5)
    m_dep = st.slider("Mobile Depth (cm)", 0.1,1.0,0.2)
    mobile_wt = st.slider("Mobile Weight", 80,200,100)
    n_cores = st.slider("Core Processor",1,8,2)
    px_height = st.slider("Pixel Resolution height",0,1960,100)
    px_width = st.slider("Pixel Resolution width",500,1998,100)
    sc_height = st.slider("Screen height",5,19,12)
    sc_width = st.slider("Screen width",0,18,5)
    talk_time = st.slider("Longest time that a single battery charge will last",2,20,11)
    touch_screen = st.selectbox("Touch Screen", criteria)
    wifi = st.selectbox("Wifi", criteria)
    ok = st.button("Predict")