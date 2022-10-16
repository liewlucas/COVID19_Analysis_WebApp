# pandas for data processing
import pandas as pd


# function to return blank values with "Not available".
def replace_blanks(data_list):
    data_list=["No restrictions" if info == '' else info for info in data_list]
    return data_list


# read json file
df_file = pd.read_json("scraper_output.json")


# convert each column into a list to remove nested values
country_og_list = df_file["bartitle"].values.tolist()

headers_data = df_file["title"].values.tolist()
headers_og_list = [header[0] for header in headers_data]

info_data = df_file["info"].values.tolist()
info_og_list = [info[0] for info in info_data]


# create new data frame
data = {
    'country': country_og_list,
    'headers': headers_og_list,
    'info': info_og_list
}
df_sorted = pd.DataFrame(data, columns=['country','headers','info'])
# download as CSV to view in excel (change path directory and leave output_file_name.csv at the back)
# df_sorted.to_csv("amended_output.csv")


# sort new data frame by country then headers
df_sorted.sort_values(by=['country','headers'], inplace=True)
df_sorted.to_csv("Test_output2.csv")


# create new lists for sorted dataframe
country_list = df_sorted["country"].values.tolist()
headers_list = df_sorted["headers"].values.tolist()
info_list = df_sorted["info"].values.tolist()


# extract country names, remove nested lists, remove duplicates, keep output as list, sort according to ASCII
country_nested_names = [data.split(" ", 2)[2:] for data in country_list]
country_names = list(set([country[0] for country in country_nested_names]))
# add US back due to 2 different US data and sort according to ASCII
country_names += ["United States"]
country_names = sorted(country_names)


# separate info data according to type, remove Singapore data (duplicated and misnamed)
quarantine_data = info_list[0::6]
vaccination_data = info_list[1::6]
covid_testing_data = info_list[2::6]
forms_data = info_list[3::6]
insurance_data = info_list[4::6]
masks_data = info_list[5::6]


# add Singapore data back to lists
country_names += ["Singapore"]
covid_testing_data.append("Unvaccinated travelers authorized to enter Singapore must carry proof of \
a negative result for COVID-19 issued no more than 2 days prior to departure using a PCR test, a \
professionally-administered Antigen Rapid Test (ART), or a self-administered ART that is remotely \
supervised by an ART provider in Singapore.")
forms_data.append("All travelers authorized to enter Singapore must submit a  with an electronic \
health declaration no more than 3 days prior to departure.")
masks_data.append("Masks are not required except in certain public venues such as healthcare facilities.")
quarantine_data.append("Not required")
insurance_data.append("Unvaccinated and partially vaccinated short-term visitors authorized to enter \
Singapore must have proof of medical insurance valid for use in Singapore for the entire duration of \
their stay with a minimum coverage amount of at least S$30,000.")
vaccination_data.append("Travelers who carry proof they have completed a full vaccination regimen using \
a COVID-19 vaccine approved for use by the World Health Organization (WHO) are exempt from the ban on entry\
 and from pre-departure testing, quarantine, and insurance requirements.")


# replace all blank values with "No restrictions"
covid_testing_data = replace_blanks(covid_testing_data)
forms_data = replace_blanks(forms_data)
masks_data = replace_blanks(masks_data)
quarantine_data = replace_blanks(quarantine_data)
insurance_data = replace_blanks(insurance_data)
vaccination_data = replace_blanks(vaccination_data)


# create new dataset
new_data = {
    'country': country_names,
    'Covid_tests': covid_testing_data,
    'Forms': forms_data,
    'Masks': masks_data,
    'Quarantine': quarantine_data,
    'Insurance': insurance_data,
    'Vaccination': vaccination_data
}
df_new = pd.DataFrame(new_data, columns=['country','Covid_tests','Forms','Masks','Quarantine','Insurance','Vaccination'])
# sort to account for addition of Singapore's data
df_new.sort_values(by=['country'], inplace=True)
# download as CSV to view in excel (change path directory and leave output_file_name.csv at the back)
df_new.to_csv("processed_output.csv")
