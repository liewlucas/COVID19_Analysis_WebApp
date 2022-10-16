import requests

def travel_spider():
    count_list = []
    respobj = requests.get("https://www.trip.com/restapi/soa2/19676/getSearchCountry")
    if respobj.status_code != 200:
        print("Unable to access")
        return
    jsondict = respobj.json()
    countrylist = jsondict.get('countryList')
    url = "https://www.trip.com/travel-restrictions-covid-19/singapore-to-"
    for countrydict in countrylist:
        count_list.append(url + countrydict.get('formatName'))
    return count_list
