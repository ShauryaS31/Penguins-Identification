import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info("This is a app that builds the machine learning model!")

with st.expander("Data"): 
  st.write("**Raw Data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/palmer-penguins/master/data/penguins_cleaned.csv")
  df
