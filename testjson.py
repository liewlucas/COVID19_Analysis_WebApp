import requests

def travel_spider():
    count_list = []
    # The get() method returns a requests.Response object.
    # The requests.Response() Object contains the server's response to the HTTP request.
    respobj = requests.get("https://www.trip.com/restapi/soa2/19676/getSearchCountry")
    # Returns a number that indicates the status (200 is OK, 404 is Not Found)
    if respobj.status_code != 200:
        print("Unable to access")
        return
    # Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
    jsondict = respobj.json()
    countrylist = jsondict.get('countryList')
    # print(dict)
    # print(countrylist)
    url = "https://www.trip.com/travel-restrictions-covid-19/singapore-to-"
    for countrydict in countrylist:
        # print(url + countrydict.get('formatName'))
        count_list.append(url + countrydict.get('formatName'))
    return count_list

# travel_spider()