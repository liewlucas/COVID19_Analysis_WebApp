import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie


# functions to retrieve the following numbers
def total_cases(country):
    return int(df_covid_cases.loc[country]["total_cases"])


def total_cases_per_mil(country):
    return int(df_covid_cases.loc[country]["total_cases_per_million"])


def new_cases(country):
    return int(df_covid_cases.loc[country]["new_cases"])


def new_cases_per_mil(country):
    return int(df_covid_cases.loc[country]["new_cases_per_million"])


def new_cases_7d(country):
    return int(df_covid_cases.loc[country]["new_cases_smoothed"])


def last_updated(country):
    return df_covid_cases.loc[country]["last_updated_date"]


# function to load animation
def loadlottie(url):
    # get url
    r = requests.get(url)

    # if returns error code 200, return none, else return json/ animation file
    if r.status_code != 200:
        return None
    return r.json()


def risk_scoring(country):
    # -- FACTOR 1: VACCINATION COVERAGE RISK --
    # remove last row (Not Vaccinated) from calculation and find the average efficacy of all vaccines combined
    df_vax_efficacy_values = df_vax_efficacy_summary.copy()[:-1]
    vax_avg_efficacy = df_vax_efficacy_values.mean().mean()

    # recommended vaccination coverage based on vaccine efficacy
    # to eliminate peak, 100% coverage for 60% efficacy, 75% coverage for 70% efficacy and 60% coverage and 80% efficacy
    if vax_avg_efficacy >= 70:
        vax_efficacy_coefficient = (75 - 60) / (80 - 70)
        rec_vax_coverage = round(vax_efficacy_coefficient * (vax_avg_efficacy - 70) + 70)
    elif vax_avg_efficacy >= 60:
        vax_efficacy_coefficient =  (100 - 75) / (70 - 60)
        rec_vax_coverage = round(vax_efficacy_coefficient * (vax_avg_efficacy - 60) + 60)
    else:
        # vaccine efficacy too low, vaccination will not be able to do much, exclude from calculations
        rec_vax_coverage = 0

    # convert NaN values to 0 so that it will be excluded from calculation
    # df_covid_cases["people_fully_vaccinated_per_hundred"] = df_covid_cases["people_fully_vaccinated_per_hundred"].fillna(0)
    # vaccination coverage in specified country
    country_vax_coverage = int(df_covid_cases.loc[country]["people_fully_vaccinated_per_hundred"])

    # check country's vaccination coverage against recommended coverage and assign a coverage risk score
    if country_vax_coverage > rec_vax_coverage:
        coverage_risk = 1
    elif country_vax_coverage == rec_vax_coverage:
        coverage_risk = 3
    else:
        coverage_risk = 5

    # -- FACTOR 2: NEW CASES PER ONE MILLION RISK --
    # using 100 and 60 new cases per million as benchmark, assign a new case risk score
    if int(new_cases_per_mil(country)) > 100:
        new_case_risk = 5
    elif int(new_cases_per_mil(country)) >= 60:
        new_case_risk = 3
    else:
        new_case_risk = 1

    # -- FACTOR 3: USER VACCINATION RISK --
    # assign a risk score based on user's specified vaccine efficacy against the country's vaccination coverage
    df_indv_vax_eff_avg = df_vax_efficacy_summary.mean(axis=1)
    user_vaccine_efficacy = df_indv_vax_eff_avg.loc[user_vaccine]

    # recommended vaccination efficacy based on vaccine coverage
    # to eliminate peak, 100% coverage for 60% efficacy, 75% coverage for 70% efficacy and 60% coverage and 80% efficacy
    if country_vax_coverage > 75:
        vax_coverage_coefficient = (70 - 60) / (100 - 75)
        rec_vax_efficacy = vax_coverage_coefficient * (country_vax_coverage - 75) + 75
    elif country_vax_coverage >= 60:
        vax_coverage_coefficient = (80 - 70) / (75 - 60)
        rec_vax_efficacy = vax_coverage_coefficient * (country_vax_coverage - 60) + 60
    else:
        # coverage too low, vaccination will not be able to help much, exclude from calculations
        rec_vax_efficacy = 0

    # check country's vaccination coverage against recommended coverage and assign a coverage risk score
    if user_vaccine_efficacy == "Not Vaccinated":
        vax_efficacy_risk = 5
    elif user_vaccine_efficacy > rec_vax_efficacy:
        vax_efficacy_risk = 1
    elif user_vaccine_efficacy == rec_vax_efficacy:
        vax_efficacy_risk = 3
    else:
        vax_efficacy_risk = 5

    # risk score
    if rec_vax_coverage == 0 and rec_vax_efficacy == 0:
        risk_score = round(new_case_risk, 2)
    elif rec_vax_coverage == 0 or rec_vax_efficacy == 0:
        risk_score = round((new_case_risk + coverage_risk + vax_efficacy_risk) / 2, 2)
    else:
        risk_score = round((new_case_risk + coverage_risk + vax_efficacy_risk) / 3, 2)

    return risk_score


# stable url for latest data in csv format
covid_cases_url = "https://covid.ourworldindata.org/data/latest/owid-covid-latest.csv"

# vaccine data
df_vax_efficacy_summary = pd.read_csv("vaccine_efficacy_summary.csv", skiprows=1)
df_vax_efficacy_summary.loc[len(df_vax_efficacy_summary.index)] = ["Not Vaccinated", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vaccine_types = df_vax_efficacy_summary["Vaccine"].values.tolist()
df_vax_efficacy_summary.set_index("Vaccine", inplace=True)

# create dataframes for data to be used
df_covid_cases = pd.read_csv(covid_cases_url)
df_covid_cases = df_covid_cases.fillna(0)
df_country = df_covid_cases["location"]

# Setting country names as index in dataframe
df_covid_cases.set_index("location", inplace=True)

# page start
st.set_page_config(page_title="My Webpage", page_icon=":seven:", layout="wide")
title, animation = st.columns(2, gap="medium")
with title:
    st.title("Current Covid-19 Situation")
    st.markdown("_We all want to enjoy our holidays, don't we? \
    View the current Covid-19 situation in your destination country before planning your next holiday trip._")
with animation:
    animation2 = loadlottie("https://assets8.lottiefiles.com/packages/lf20_8axjdnts.json")
    st_lottie(animation2, height=280)

# user to select country and vaccine they took as input
country, vaccine = st.columns(2)
with country:
    covid_country = st.selectbox(
        "Select a country to view the current Covid-19 situation there",
        options=df_country,
    )
with vaccine:
    user_vaccine = st.selectbox(
        "Please indicate the vaccine that you took. If unvaccinated, select \"Not Vaccinated\".",
        options=vaccine_types
    )

st.markdown("---")

data, new_case = st.columns([2, 1], gap="large")
with data:
    st.header(f"Covid-19 in {covid_country}")
    st.markdown(
        f"""
        {covid_country} has a total of {total_cases(covid_country):,} cases.\n
        As population varies across countries, it can be insightful to compare the number as \"per million people\".\
        There are approximately {total_cases_per_mil(covid_country):,} total cases per one million people and
        {new_cases_per_mil(covid_country):,} new cases per one million people. \n
        The 7-day average is also a good reference number to account for sudden spikes in cases. The 7-day average \
        of new cases in {covid_country} is {new_cases_7d(covid_country):,}.
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
        {new_cases(covid_country):,}</b>""",
        unsafe_allow_html=True
    )
    st.markdown(
        f"""<p style="font-size:50px;line-height:0px;">
        new cases</p>""",
        unsafe_allow_html=True
    )

st.markdown("---")


df_analysis = df_covid_cases[["new_cases_per_million","people_fully_vaccinated_per_hundred"]]
risk_list = []
for i in df_analysis.index:
    r_score = risk_scoring(i)
    risk_list.append(r_score)

risk_col = {'risk_score': risk_list}
df_risk_score = pd.DataFrame.from_dict(risk_col)
df_risk_score.index = list(df_country)
df_risk_analysis = df_analysis.join(df_risk_score)

# plotting results to graphs
plt.rcParams["font.size"] = "30"
df_risk_analysis[0:41].plot.bar(figsize=(28, 12), subplots=True,legend=None)
# plt.savefig("risk_analysis_1",bbox_inches='tight',pad_inches = 0)
df_risk_analysis[40:81].plot.bar(figsize=(28, 12), subplots=True,legend=None)
# plt.savefig("risk_analysis_2",bbox_inches='tight',pad_inches = 0)
df_risk_analysis[80:121].plot.bar(figsize=(28, 12), subplots=True,legend=None)
# plt.savefig("risk_analysis_3",bbox_inches='tight',pad_inches = 0)
df_risk_analysis[120:161].plot.bar(figsize=(28, 12), subplots=True,legend=None)
# plt.savefig("risk_analysis_4",bbox_inches='tight',pad_inches = 0)
df_risk_analysis[160:201].plot.bar(figsize=(28, 12), subplots=True,legend=None)
# plt.savefig("risk_analysis_5",bbox_inches='tight',pad_inches = 0)
df_risk_analysis[200:241].plot.bar(figsize=(28, 15), subplots=True,legend=None)
# plt.savefig("risk_analysis_6",bbox_inches='tight',pad_inches = 0)
# plt.show()

# determine risk level:
if risk_scoring(covid_country) > 10:
    risk_level = "High"
elif risk_scoring(covid_country) > 5:
    risk_level = "Some"
else:
    risk_level = "Low"

risk, info = st.columns([1, 2], gap="large")
with risk:
    st.markdown(
        f"""<b right style="font-size:130px;text-align: right;">
        {risk_level}</b>""",
        unsafe_allow_html=True
    )
    st.markdown(
        f"""<p style="font-size:50px;line-height:0px;">
        risks</p>""",
        unsafe_allow_html=True
    )

with info:
    st.header(f"Covid-19 risks")
    st.markdown(
        f"""
        It is good to understand one's risk of travelling, especially during the pandemic. We have analysed and \
        categorised each country to different risk levels (i.e. Low risk, Some risks, High risks) . \n 

        Our risk analysis is based on on 3 factors - Vaccination coverage, New cases per one million people, and the \
        Efficacy of your vaccine. Each factor is given equal weightage and a final score is computed. The score is \
        then compared against a scale of \'1\' to \'15\' with \'1\' being the lowest risk and \'15\' being the highest \
        risk. Our risk score for you travelling to {covid_country} is currently at {risk_scoring(covid_country)}.
        """
    )
    st.markdown(
        f"""<p style="font-size:12px;">
        *All calculations provided are just an estimate for your reference. Factors where we do not have data are \
        excluded from our calculations.</p>""",
        unsafe_allow_html=True
    )
