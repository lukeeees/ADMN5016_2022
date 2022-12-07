import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


def show_explore_page():

    df = pd.read_csv("MobilePrice.csv")
    st.title("Explore the Dataset")
    st.dataframe(df)
    st.header("Distribution of Price Range")
    chart = df['price_range'].value_counts()
    st.bar_chart(chart)

    

    
    
    



