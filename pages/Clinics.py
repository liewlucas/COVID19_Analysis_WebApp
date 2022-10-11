import streamlit as st
import pandas as pd

st.title("Approved Test Centres")

st.subheader("Approved Covid19 Pre Departure ART Clinics")


with st.container():
    data = pd.read_csv('Approved-Test-Clinics.csv')
    st.dataframe(data)

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader ('')

    with col2:
        st.write(" ")

    with col3:
        st.write(' ')
