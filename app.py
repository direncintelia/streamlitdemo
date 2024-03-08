import streamlit as st
import pandas as pd

st.title('intelia Test App')

# Load a sample dataset
def get_data():
    return pd.read_csv("https://raw.githubusercontent.com/direncintelia/streamlitdemo/main/your%20data.csv")

# Display the dataframe 
df = get_data()

min_year = int(df['price'].min())
max_year = int(df['price'].max())

countries = df['country'].unique()

'## By country'
country = st.selectbox('country', countries)
df[df['country'] == country]


'## By price'
price = st.slider('price', min_price, max_price)
df[df['Price'] == price]

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

