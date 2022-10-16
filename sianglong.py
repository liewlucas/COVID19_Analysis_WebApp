import requests
import pandas as pd
# api-endpoint
import urllib
from urllib.request import urlopen

#url = 'https://data.gov.sg/api/action/datastore_search?resource_id=9de30d8d-3c0d-48ab-8c1b-4a7dc03d687a&limit=5&q=title:jones'
url = "https://data.gov.sg/api/action/datastore_search?resource_id=9de30d8d-3c0d-48ab-8c1b-4a7dc03d687a&limit=5"
#url = 'https://data.gov.sg/api/action/datastore_search?resource_id=9de30d8d-3c0d-48ab-8c1b-4a7dc03d687a&limit=5&q=title:jones'
with urllib.request.urlopen(url) as fileobj:
    fileobj = urllib.urlopen(url)
    # st.table(fileobj)
    #s = url.read()
    #st.write(s)
    print(fileobj)