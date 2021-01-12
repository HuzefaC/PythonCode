import requests
import os
from dotenv import load_dotenv


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.api_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.header = {
            "Authorization": os.getenv("SHEETY_AUTH")
        }

    def get_data(self):
        response = requests.get(self.api_endpoint, headers=self.header)
        response.raise_for_status()
        return response.json()

    def update_iatacode(self, data, index):
        update_data = {
            "price": data
        }
        response = requests.put(self.api_endpoint + f"/{index}", headers=self.header, json=update_data)
        response.raise_for_status()
