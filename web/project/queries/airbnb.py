import requests
from keys import airbnb_headers

url = "https://airbnb-com.p.rapidapi.com/listings/nearby/37.788719679657554/-122.40057774847898"

querystring = {
    "min_bathrooms": "0",
    "check_out": "2021-02-26",
    "hotel_room": "false",
    "max_guests": "1",
    "check_in": "2021-02-25",
    "private_room": "false",
    "min_bedrooms": "0",
    "offset": "0",
    "entire_home": "false",
    "min_price": "0",
    "max_price": "5000",
    "min_beds": "0",
    "radius": "5",
    "shared_room": "false",
}

headers = airbnb_headers

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
