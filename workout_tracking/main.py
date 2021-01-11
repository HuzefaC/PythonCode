import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Loading .env
load_dotenv()

# Api keys and endpoints
x_app_id = os.getenv("APP_ID")
x_app_key = os.getenv("APP_KEY")
api_endpoint = os.getenv("API_ENDPOINT")
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

# Headers for nutritionix api
headers = {
    "x-app-id": x_app_id,
    "x-app-key": x_app_key,
    "Content-Type": "application/json",
}

# header for sheety
sheety_header = {
    "Authorization": os.getenv("SHEETY_AUTH")
}

# User input
query = input("Enter query: ")

body = {
    "query": query
}

# Nutritionix get request
response = requests.post(api_endpoint, json=body, headers=headers)
data = response.json()

# Data from response
duration = str(data["exercises"][0]["duration_min"])
exercise = str(data["exercises"][0]["name"]).title()
calories = str(data["exercises"][0]["nf_calories"]).title()

# Getting current date time
date = str(datetime.now().date())
time = str(datetime.now().time().strftime("%H:%M:%S"))

# Data to add to google sheet
sheety_body = {
    "workout": {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
    }
}
sheety_response = requests.post(sheety_endpoint, json=sheety_body, headers=sheety_header)
