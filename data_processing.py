# pandas for data processing
import pandas as pd


# function to return blank values with "Not available".
def replace_blanks(data_list):
    data_list=["No restrictions" if info == '' else info for info in data_list]
    return data_list


# read json file
df_file = pd.read_json("output.json")


# convert each column into a list to remove nested values
country_og_list = df_file["bartitle"].values.tolist()

headers_data = df_file["title"].values.tolist()
headers_og_list = [header[0] for header in headers_data]

info_og_list = df_file["info"].values.tolist()


# create new data frame
data = {
    'country': country_og_list,
    'headers': headers_og_list,
    'info': info_og_list
}
df_sorted = pd.DataFrame(data, columns=['country','headers','info'])
# download as CSV to view in excel (change path directory and leave output_file_name.csv at the back)
# df_sorted.to_csv(r"C:\Users\thadd\iCloudDrive\SIT\Programming Fundamentals\Python Project\Backup copies\amended_output.csv")


# sort new data frame by country then headers
df_sorted.sort_values(by=['country','headers'], inplace=True)
# df_sorted.to_csv(r"C:\Users\thadd\iCloudDrive\SIT\Programming Fundamentals\Python Project\Backup copies\Test_output2.csv")


# create new lists for sorted dataframe
country_list = df_sorted["country"].values.tolist()
headers_list = df_sorted["headers"].values.tolist()
info_list = df_sorted["info"].values.tolist()


# extract country names, remove nested lists, remove duplicates, keep output as list
country_nested_names = [data.split(" ", 2)[2:] for data in country_list]
country_names = list(set([country[0] for country in country_nested_names]))
# add US back due to 2 different US data and sort according to ASCII
country_names += ["United States"]
country_names = sorted(country_names)


# separate info data according to type, remove Singapore data (duplicated and misnamed)
covid_testing_data = info_list[0::12]
forms_data = info_list[2::12]
masks_data = info_list[4::12]
quarantine_data = info_list[6::12]
insurance_data = info_list[8::12]
vaccination_data = info_list[10::12]


# add Singapore data back to lists
country_names += ["Singapore"]
covid_testing_data.append(info_list[1])
forms_data.append(info_list[3])
masks_data.append(info_list[5])
quarantine_data.append(info_list[7])
insurance_data.append(info_list[9])
vaccination_data.append(info_list[11])


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
