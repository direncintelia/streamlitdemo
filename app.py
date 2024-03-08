import streamlit as st
import pandas as pd

st.title('My First Streamlit App')

# Load a sample dataset
df = pd.read_csv("https://github.com/direncintelia/streamlitdemo/blob/main/your%20data.csv")

# Display the dataframe 
st.write(df)

