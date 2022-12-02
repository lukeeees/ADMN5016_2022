import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data= load_model()

model_loaded = data['model']

def show_predict_page():
    st.title("CellPhone Price Predictor")
    st.write("""### We need some information to predict the price of Mobile Phone""")

    criteria = {
        "No": 0,
        "Yes": 1
    }

    battery_power = st.slider("Battery Power", 500, 2000, 600)  #1
    blue = st.selectbox("Bluetooth", criteria) #2
    clock_speed = st.slider("Clock Speed", 0,3,1) #3
    dual_sim = st.selectbox("Dual Sim", criteria) #4
    fc = st.slider("Front Camera",0,19,2) #5
    four_g = st.selectbox("4G", criteria) #6 
    int_memory = st.slider("Internal Memory (Gigabytes)", 2,64,5) #7
    m_dep = st.slider("Mobile Depth (cm)", 0.1,1.0,0.2) #8
    mobile_wt = st.slider("Mobile Weight", 80,200,100) #9
    n_cores = st.slider("Core Processor",1,8,2) #10
    pc = st.slider("Back Camera",0,20,10) #11
    px_height = st.slider("Pixel Resolution height",0,1960,100) #12 
    px_width = st.slider("Pixel Resolution width",500,1998,100) #13
    ram = st.slider("RAM",256,3998,1256)    #14
    sc_height = st.slider("Screen height",5,19,12)  #15
    sc_width = st.slider("Screen width",0,18,5) #16
    talk_time = st.slider("Longest time that a single battery charge will last",2,20,11) #17
    touch_screen = st.selectbox("Touch Screen", criteria) #18
    wifi = st.selectbox("Wifi", criteria)



   # if ok:
    X = np.array([[battery_power,conv(blue), clock_speed,conv(dual_sim),fc,conv(four_g),int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_height,sc_width,talk_time,conv(touch_screen),conv(wifi)]])
    #st.write(X)
    pred= model_loaded.predict(X)
    message = "Prediction: The CellPhone is categorized as: "+messages(pred[0])
    st.empty()
    st.info(message,icon="✅")

def conv(x):
    if x :
        flag = 1
    else:
        flag = 0
    return flag

       
def messages(price):
    if(price == 0):
        x = "Low End"
    elif(price == 1):
        x = "Medium Cost"
    elif price == 2:
        x = "High Cost"
    else:
        x = "Very High Cost"
    return x
