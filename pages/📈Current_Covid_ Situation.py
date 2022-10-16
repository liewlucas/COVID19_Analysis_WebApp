import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie


#functions to retrieve the following numbers and format case numbers with "," as the thousand seperator
def total_cases(country):
    return f'{int(df_covid_cases.loc[country]["total_cases"]):,}'

def total_cases_per_mil(country):
    return f'{int(df_covid_cases.loc[country]["total_cases_per_million"]):,}'

def new_cases(country):
    return f'{int(df_covid_cases.loc[country]["new_cases"]):,}'

def new_cases_per_mil(country):
    return f'{int(df_covid_cases.loc[country]["new_cases_per_million"]):,}'

def last_updated(country):
    return df_covid_cases.loc[country]["last_updated_date"]

# function to load animation
def loadlottie(url):
    #get url
    r = requests.get(url)

    # if returns error code 200, return none, else return json/ animation file
    if r.status_code != 200:
        return None
    return r.json()

# function to convert df into csv for exporting
@st.cache
def convert_to_csv(df):
    return df.to_csv(header=True, index=True).encode('utf-8')


# page start
st.set_page_config(page_title="Covid Statistics", page_icon=":seven:", layout="wide")
title, animation = st.columns(2, gap="medium")
with title:
    st.title("Current Covid-19 Situation")
    st.markdown("_We all want to enjoy our holidays, don't we? \
    View the current Covid-19 situation in your destination country before planning your next holiday trip._")
with animation:
    animation2 = loadlottie("https://assets8.lottiefiles.com/packages/lf20_8axjdnts.json")
    st_lottie(animation2, height=280)


# stable url for latest data in csv format
covid_cases_url = "https://covid.ourworldindata.org/data/latest/owid-covid-latest.csv"


# create dataframes for data to be used
df_covid_cases = pd.read_csv(covid_cases_url)
df_country = df_covid_cases["location"]


# Setting country names as index in dataframe
df_covid_cases.set_index("location", inplace=True)


# user to select country as input
covid_country = st.selectbox(
    "Select a country to view the current Covid-19 situation there",
    options=df_country,
)

st.markdown("---")


data, new_case = st.columns([2,1])
with data:
    st.header(f"Covid-19 in {covid_country}")
    st.markdown(
        f"""
        {covid_country} has a total of {total_cases(covid_country)} cases.\n
        As population varies across countries, it can be insightful to compare the number as \"per million people\".\
        There are approxiamtely {total_cases_per_mil(covid_country)} total cases per one million people and
        {new_cases_per_mil(covid_country)} new cases per one million people.
        """
    )
    st.markdown(
        f"""<p style="font-size:12px;">
        *Data last updated on {last_updated(covid_country)}. Source data from Our World in Data.</p>""",
        unsafe_allow_html=True
    )

with new_case:
    st.markdown(
        f"""<b style="font-size:130px;">
        {new_cases(covid_country)}</b>""",
        unsafe_allow_html=True
    )
    st.markdown(
        f"""<p style="font-size:50px;line-height:0px;">
        new cases</p>""",
        unsafe_allow_html=True
    )

st.markdown("---")
