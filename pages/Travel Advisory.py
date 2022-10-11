# pandas for data processing
import pandas as pd

# streamlit for gui
import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":airplane:", layout="wide")
st.title("Travel Advisory")

# convert csv to df
df_file = pd.read_csv("test_data.csv")  # ** change input file


# country_list=[]
# for i in range(len(df_file)):
    # print(df_file.iloc[i,0].split(','))
    # raw_country_list = df_file.iloc[i, 0].split(',')
    #print(raw_country_list)

    # country_list.append(df_file.iloc[i, 0])
#destination_country=df_file.apply(lambda row: row["country"], axis=1))
# print(country_list)


# # Option 1: User to search country and display all data from specified country
# user_input_country = st.text_input("Which country do you want to search for?")
#
# df_file.loc[df_file['country'] == user_input_country]


# Option 2: User to select origin and destination to be displayed
origin, destination = st.columns(2)
with origin:
    user_origin_country = st.selectbox(
        "I am travelling from",
        options=df_file['country'].unique(),
    )
with destination:
    user_destination_country = st.selectbox(
        "I am travelling to",
        options=df_file['country'].unique(),
    )


# Setting country names as index in dataframe
df_file.set_index("country", inplace=True)
st.markdown("---")
st.header(f"Travelling to {user_destination_country} | Pre-requisites and Regulations")


# function to locate destination country's data from country name index
def destination_advisory(column_name):
    return st.markdown(df_file.loc[user_destination_country][column_name], unsafe_allow_html=False)


# function to locate origin country's data from country name index
def origin_advisory(column_name):
    return st.markdown(df_file.loc[user_origin_country][column_name], unsafe_allow_html=False)


# function to display logo image
def logo(image):
    st.image(image, width=70)


# TRAVELLING TO 1st ROW: divide into 3 columns to display data
testing, quarantine, masks = st.columns(3, gap="medium")
with testing:
    logo('images/testing_logo.png')
    st.subheader("Covid-19 Testing Requirements")
    destination_advisory("testing")
with quarantine:
    logo('images/quarantine_logo.png')
    st.subheader("Quarantine Requirements")
    destination_advisory("quarantine")
with masks:
    logo('images/mask_logo.png')
    st.subheader("Mask Wearing Requirements")
    destination_advisory("masks")

# TRAVELLING TO 2nd ROW: divide into 3 columns to display data
vaccination, forms, insurance = st.columns(3, gap="medium")
with vaccination:
    logo('images/vaccine_logo.png')
    st.subheader("Vaccination Requirements")
    destination_advisory("vaccination")
with forms:
    logo('images/forms_logo.png')
    st.subheader("Forms/ Visas Requirements")
    destination_advisory("forms")
with insurance:
    logo('images/insurance_logo.png')
    st.subheader("Insurance Requirements")
    destination_advisory("insurance")

st.markdown("---")

# RETURNING TO 1st ROW: divide into 3 columns to display data
st.header(f"Returning to {user_origin_country} | Pre-requisites and Regulations")
testing, quarantine, masks = st.columns(3, gap="medium")
with testing:
    logo('images/testing_logo.png')
    st.subheader("Covid-19 Testing Requirements")
    origin_advisory("testing")
with quarantine:
    logo('images/quarantine_logo.png')
    st.subheader("Quarantine Requirements")
    origin_advisory("quarantine")
with masks:
    logo('images/mask_logo.png')
    st.subheader("Mask Wearing Requirements")
    origin_advisory("masks")

# RETURNING TO 2nd ROW: divide into 3 columns to display data
vaccination, forms, insurance = st.columns(3, gap="medium")
with vaccination:
    logo('images/vaccine_logo.png')
    st.subheader("Vaccination Requirements")
    origin_advisory("vaccination")
with forms:
    logo('images/forms_logo.png')
    st.subheader("Forms/ Visas Requirements")
    origin_advisory("forms")
with insurance:
    logo('images/insurance_logo.png')
    st.subheader("Insurance Requirements")
    origin_advisory("insurance")

st.markdown("---")


# locate the rows of destination and origin countries and create one dataframe to prepare for export
download_df = df_file.loc[[user_destination_country, user_origin_country]]


# if st.button("Download travel advisory as csv"):
#     download_df = df_file.loc[[user_destination_country, user_origin_country]]
#     download_df.to_csv(f"{user_destination_country} and {user_origin_country} travel advisory.csv", header=True, index=False)

# function to convert download_df into csv for exporting
@st.cache
def convert_to_csv(df):
    return df.to_csv(header=True, index=True).encode('utf-8')


download_csv = convert_to_csv(download_df)


# download csv file for specified destination and origin countries
st.download_button(
    label="Download current travel advisory as .csv",
    data=download_csv,
    file_name=f"{user_destination_country} and {user_origin_country} travel advisory.csv",
    mime="text/csv",
    key='download-csv'
)


# st.download_button(
#     label=f"Download travel advisory as csv",
#     data=download_df,
#     file_name=f"{user_destination_country} and {user_origin_country} travel advisory.csv",
#     mime="text/csv"
# )









# # checkboxes for user to select what data they want to export
# data_options=["data1", "data2"]
# data_checkboxes=[st.checkbox(data) for data in data_options]
#
# # combining selected data
# checked_data_options=[data for data, checked in zip(data_options, data_checkboxes) if checked]
# user_download_file={"col1": ['a,b,c'], "col2": ['a,b,c']}
# df_user_download_file = pd.DataFrame(data=user_download_file)
# csv_export = df_user_download_file.to_csv(df_user_download_file, encoding='utf-8')
#
# # user_download_file = {
# #     df_data1 header: data
# #     df_data2 header: data
# # }
#
# # if data_1:
# #     user_download_file.append(data_1)
# #
# # if data_2:
# #     user_download_file.append(data_2)
#
# # for users to export data
# st.download_button(
#     label="Download selected data as CSV",
#     data=output1.scv,
#     file_name="Covid-19 regulation for [country]",
#     mime="text/csv"
#     )
