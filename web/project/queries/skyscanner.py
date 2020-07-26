import requests
from keys import skyscanner_headers
from city_generator import random_city

destination = random_city()
origin_airport = "SFO"
dest_airport = "LAX"
# destination["code"]

# print(dest_airport)
# print(test_dest_city)


def queary_skyscanner(origin, destination):

    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{origin_airport}-sky/{dest_airport}-sky/2020-09-01"

    querystring = {"inboundpartialdate": "2020-12-01"}

    headers = skyscanner_headers

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


queary_skyscanner(origin_airport, dest_airport)
