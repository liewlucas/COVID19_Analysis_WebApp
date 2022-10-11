#INF1002 Python Project Group 7

#pandas for data processing
import pandas as pd

#streamlit for gui
import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.write("Hello")
st.write('---')

# covid daily figures
df_json = pd.read_json('output1.json')
print(df_json)

st.table(df_json)