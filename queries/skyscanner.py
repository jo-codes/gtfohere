from flask import Flask, jsonify, make_response
import requests, json
from api_keys.keys import skyscanner_headers
from city_generator import random_city


origin_airport = "CDG"
dest_airport = str(random_city()["code"]).replace(" ", "")

print(f"{dest_airport}")

# {dest_airport}
# {origin_airport}


def queary_skyscanner(origin, destination):

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/SFO-sky/JFK-sky/2020-09-04"

    querystring = {"inboundpartialdate": "2020-09-18"}

    headers = skyscanner_headers

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# queary_skyscanner(origin_airport, dest_airport)
