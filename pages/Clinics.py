import numpy as np
import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie

#---- FUNCTIONS--------

def loadlottie(url):
    #get url
    r = requests.get(url)

    # if returns error code 200, return none, else return json/ animation file
    if r.status_code != 200:
        return None

    return r.json()





#_---- MAIN CODE ----

#page config
st.set_page_config(page_title="Pre Departure Testing", page_icon=":tada:", layout="wide")

with st.container():
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.title("Pre Departure ART Testing ✈️")
        st.write("_Singapore has finally opened its borders for travelling! However there are new regulations before travelling."
                 "Here is everything you need to know!_ ")

    with col2:
        animation = loadlottie("https://assets8.lottiefiles.com/packages/lf20_tCIUzD.json")
        st_lottie(animation, height=150)
    st.write("---")


with st.container():
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.subheader("Travelling Overseas?")
        st.markdown("Most destinations require you to produce a negative Covid-19 test result prior to entry.  \n"
                 "Learn where you can book your pre-departure Antigen Rapid Test (ART) or Polymerase Chain Reaction (PCR) test in Singapore!")

    with col2:
        animation2 = loadlottie("https://assets7.lottiefiles.com/packages/lf20_ptdtk2up.json")

        st_lottie(animation2, height=200)

    st.write("***")


with st.container():
    st.subheader("🏥🧪    List of Approved Providers for Antigen Rapid Testing for COVID-19 ")
    st.write("""  _NOTE: The fees published in this list are as per Healthcare Instituitions’ declaration and may be subject to change by the HCI from time to time.
         Please call the clinic to ensure that they are able to offer private-paid ART swabs._""")
    st.write("###")

with st.container():
    #reading csv file
    df = pd.read_csv('Approved-Test-Clinics.csv')

    #search box for user input
    #st.markdown(".stTextInput > label {font-size:105%; font-weight:bold; color:blue;}")
    message = "Please Enter Clinical Information to start searching for your Preferred Clinic:"
    filterbox = st.text_input(message, placeholder="Type Here...")

    #converts all to upper frame, matching dataset
    searchtext = filterbox.upper()

    #renaming columns
    df.columns = ["Clinic Name", "Clinic Address", "Operating Hours", "Age Group", "Contact Number", "Approximate Price", "7", "8"]

    #removing unnecessary Data from dataset
    df.drop(['7','8'], axis=1, inplace=True)
    df.drop(labels=797, axis=0, inplace=True)

    #changing dataset based on user input
    mask = np.column_stack([df[col].str.contains(searchtext, na=False) for col in df])
    df.loc[mask.any(axis=1)]


