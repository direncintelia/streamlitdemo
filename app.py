import streamlit as st
import pandas as pd

st.title('intelia Test App')

# Load a sample dataset
df = pd.read_csv("https://raw.githubusercontent.com/direncintelia/streamlitdemo/main/your%20data.csv")

# Display the dataframe 
st.write(df)


values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

