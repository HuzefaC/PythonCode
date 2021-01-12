import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

api_location_endpoint = os.getenv("TEQUILA_LOCATION_ENDPOINT")
api_location_key = os.getenv("TEQUILA_LOCATION_KEY")
api_search_key = os.getenv("TEQUILA_SEARCH_KEY")
api_search_endpoint = os.getenv("TEQUILA_SEARCH_ENDPOINT")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()

    def get_iata_code(self, country_name):
        params = {
            "apikey": api_location_key,
            "term": country_name,
        }
        response = requests.get(api_location_endpoint, params=params)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def get_data(self, city):
        date_from = datetime.now()+timedelta(days=1)
        date_from = date_from.strftime("%d/%m/%Y")

        date_to = datetime.now() + timedelta(days=180)
        date_to = date_to.strftime("%d/%m/%Y")

        params = {
            "apikey": api_location_key,
            "fly_from": "LON",
            "fly_to": city,
            "date_from": f"{date_from}",
            "date_to": f"{date_to}",
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        response = requests.get(url=api_search_endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        return data



