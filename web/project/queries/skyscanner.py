import requests
from keys import skyscanner_headers


url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

querystring = {"query": "Stockholm"}

headers = skyscanner_headers

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
