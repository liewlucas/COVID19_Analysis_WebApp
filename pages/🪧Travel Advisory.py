# pandas for data processing
import pandas as pd

# streamlit for gui
import streamlit as st

st.set_page_config(page_title="Travel Advisories", page_icon=":seven:", layout="wide")
st.title("Travel Advisory")


# function to locate destination country's data from country name index
def destination_advisory(column_name):
    return st.markdown(df_travel_adv.loc[user_destination_country][column_name], unsafe_allow_html=False)


# function to locate origin country's data from country name index
def origin_advisory(column_name):
    return st.markdown(df_travel_adv.loc[user_origin_country][column_name], unsafe_allow_html=False)


# function to display logo image
def logo(image):
    st.image(image, width=70)


# function to convert df into csv for exporting
@st.cache
def convert_to_csv(df):
    return df.to_csv(header=True, index=True).encode('utf-8')


# convert csv to df
df_travel_adv = pd.read_csv("processed_output.csv")


# User to select origin and destination to be displayed
origin, destination = st.columns(2)
with origin:
    user_origin_country = st.selectbox(
        "I am travelling from",
        options=df_travel_adv['country'].unique(),
    )
with destination:
    user_destination_country = st.selectbox(
        "I am travelling to",
        options=df_travel_adv['country'].unique(),
    )

st.markdown("---")

# Setting country names as index in dataframe
df_travel_adv.set_index("country", inplace=True)

# Reject input if origin and destination is the same
if user_origin_country == user_destination_country:
    st.error("You are not travelling anywhere. Please change your selection.")
    # st.markdown("Select your origin and destination country to view the latest Covid-19 travel advisory")
    st.header("Travelling Pre-requisites and Regulations")

    # First row to show type of data that will be displayed
    testing, quarantine, masks = st.columns(3)
    with testing:
        logo('testing_logo.png')
        st.subheader("Covid-19 Testing Requirements")
    with quarantine:
        logo('quarantine_logo.png')
        st.subheader("Quarantine Requirements")
    with masks:
        logo('mask_logo.png')
        st.subheader("Mask Wearing Requirements")

    # Second row to show type of data that will be displayed
    vaccination, forms, insurance = st.columns(3)
    with vaccination:
        logo('vaccine_logo.png')
        st.subheader("Vaccination Requirements")
    with forms:
        logo('forms_logo.png')
        st.subheader("Forms Requirements")
    with insurance:
        logo('insurance_logo.png')
        st.subheader("Insurance Requirements")

# accept input and display specified countries' travel advisory
else:
    st.header(f"Travelling to {user_destination_country} | Pre-requisites and Regulations")

    # TRAVELLING TO 1st ROW: divide into 3 columns to display data
    testing, quarantine, masks = st.columns(3)
    with testing:
        logo('testing_logo.png')
        st.subheader("Covid-19 Testing Requirements")
        destination_advisory("Covid_tests")
    with quarantine:
        logo('quarantine_logo.png')
        st.subheader("Quarantine Requirements")
        destination_advisory("Quarantine")
    with masks:
        logo('mask_logo.png')
        st.subheader("Mask Wearing Requirements")
        destination_advisory("Masks")

    # TRAVELLING TO 2nd ROW: divide into 3 columns to display data
    vaccination, forms, insurance = st.columns(3)
    with vaccination:
        logo('vaccine_logo.png')
        st.subheader("Vaccination Requirements")
        destination_advisory("Vaccination")
    with forms:
        logo('forms_logo.png')
        st.subheader("Forms Requirements")
        destination_advisory("Forms")
    with insurance:
        logo('insurance_logo.png')
        st.subheader("Insurance Requirements")
        destination_advisory("Insurance")

    st.markdown("---")

    # RETURNING TO 1st ROW: divide into 3 columns to display data
    st.header(f"Returning to {user_origin_country} | Pre-requisites and Regulations")
    testing, quarantine, masks = st.columns(3)
    with testing:
        logo('testing_logo.png')
        st.subheader("Covid-19 Testing Requirements")
        origin_advisory("Covid_tests")
    with quarantine:
        logo('quarantine_logo.png')
        st.subheader("Quarantine Requirements")
        origin_advisory("Quarantine")
    with masks:
        logo('mask_logo.png')
        st.subheader("Mask Wearing Requirements")
        origin_advisory("Masks")

    # RETURNING TO 2nd ROW: divide into 3 columns to display data
    vaccination, forms, insurance = st.columns(3)
    with vaccination:
        logo('vaccine_logo.png')
        st.subheader("Vaccination Requirements")
        origin_advisory("Vaccination")
    with forms:
        logo('forms_logo.png')
        st.subheader("Forms Requirements")
        origin_advisory("Forms")
    with insurance:
        logo('insurance_logo.png')
        st.subheader("Insurance Requirements")
        origin_advisory("Insurance")

    st.markdown("---")


    # locate the rows of destination and origin countries and create one dataframe to prepare for export
    download_df = df_travel_adv.loc[[user_destination_country, user_origin_country]]
    download_csv = convert_to_csv(download_df)

    # download csv file for specified destination and origin countries
    st.download_button(
        label="Download current travel advisory as .csv",
        data=download_csv,
        file_name=f"{user_destination_country} and {user_origin_country} travel advisory.csv",
        mime="text/csv",
        key='download-csv'
    )
