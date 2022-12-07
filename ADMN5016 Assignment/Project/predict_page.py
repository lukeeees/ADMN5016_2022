import streamlit as st
import pickle
import numpy as np
import time


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data= load_model()

model_loaded = data['model']

def show_predict_page():
    st.title("CellPhone Price Predictor")
    st.write("""#### We need some information to predict the price of Mobile Phone""")
    st.markdown("---")
    col1, col2 ,col3= st.columns(3)
    criteria = {
        "Yes": 1,
        "No": 0
    }

    battery_power = col1.slider("Battery Power", 500, 2000, 600)  #1
    blue = col1.selectbox("Bluetooth", criteria) #2
    clock_speed = col1.slider("Clock Speed", 0,3,1) #3
    dual_sim = col1.selectbox("Dual Sim", criteria) #4
    fc = col1.slider("Front Camera",0,19,2) #5
    four_g = col1.selectbox("4G", criteria) #6 
    int_memory = col1.slider("Internal Memory (Gigabytes)", 2,64,5) #7
    m_dep = col2.slider("Mobile Depth (cm)", 0.1,1.0,0.2) #8
    mobile_wt = col2.slider("Mobile Weight", 80,200,100) #9
    n_cores = col2.slider("Core Processor",1,8,2) #10
    pc = col2.slider("Back Camera",0,20,10) #11
    px_height = col2.slider("Pixel Resolution height",0,1960,1000) #12 
    px_width = col2.slider("Pixel Resolution width",500,1998,1000) #13
    ram = col2.slider("RAM",256,3998,1256)    #14
    sc_height = col3.slider("Screen height",5,19,12)  #15
    sc_width = col3.slider("Screen width",0,18,5) #16
    talk_time = col3.slider("Longest time that a single battery charge will last",2,20,11) #17
    touch_screen = col3.selectbox("Touch Screen", criteria) #18
    wifi = col3.selectbox("Wifi", criteria) #19

    X = np.array([[battery_power,conv(blue), clock_speed,conv(dual_sim),fc,conv(four_g),int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_height,sc_width,talk_time,conv(touch_screen),conv(wifi)]])
    pred= model_loaded.predict(X)

    progress_bar = col3.progress(0)
    for perc_completed in range(100):
        time.sleep(0.010)
        progress_bar.progress(perc_completed+1)
    
    message = "Prediction: "+messages(pred[0])
    col3.info(message,icon="✅")

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
