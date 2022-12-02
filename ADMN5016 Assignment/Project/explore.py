import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def show_explore_page():

    df = pd.read_csv("MobilePrice.csv")
    st.title("Explore the Dataset")

    st.dataframe(df)
