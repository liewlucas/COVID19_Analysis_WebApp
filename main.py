#INF1002 Python Project Group 7

#pandas for data processing
import pandas as pd

#streamlit for gui
import streamlit as st

#streamlit option menu
from streamlit_option_menu import option_menu

#config
st.set_page_config(page_title="Team 7 INF1002", page_icon=":tada:", layout="wide")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.title("COVID19 Updates")

    with col3:
        st.write(' ')



selected = option_menu(
    menu_title=None,
    options=["Main", "Covid19 Data", "Travel Regulations"],
    icons=["house","book","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)



with st.container():

    st.subheader("Welcome to Team 7's Python Project")
    st.write("Group Members: Thaddeus, Lucas, Tommy, Zhi Yin, Siang Long")

with st.container():
    st.write('---')
    left, right = st.columns(2)
    with left:
        # covid daily figures
        data = pd.read_csv('covid-19-daily-figures.csv')
        st.table(data)
    with right:
        st.write("HELLO THIS IS RIGHT COLUMN")


