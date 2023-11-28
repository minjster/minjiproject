import pandas as pd
import requests

API_KEY_FILEPATH = "/Users/minji/Desktop/secrets/yelp_api_key.txt"

url = "https://api.yelp.com/v3/businesses/search"
key = open(rf"{API_KEY_FILEPATH}").readlines()[0]
headers = {"Authorization": f"Bearer {key}"}
print(key)

parameters = {
    "location": "12880 Riverplace Court, Jacksonville, FL",
    "categories": "coffee",
    "radius": 10000,
    "limit": 3,
}

response = requests.get(url, headers=headers, params=parameters)

print(response.json()["businesses"])
