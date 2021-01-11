import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
pixela_endpoint = os.getenv("PIXELA_ENDPOINTS")
token = os.getenv("PIXELA_TOKEN")
username = os.getenv("PIXELA_USERNAME")
terms_of_service = os.getenv("AGREE_TERMS_OF_SERVICE")
not_minor = os.getenv("NOT_MINOR")

graph_endpoint = os.getenv("GRAPH_ENDPOINT")
graph_id = "graph1"
graph_name = "Coding Graph"
unit_measure = "Hours"
unit_type = "float"
color = "ajisai"

add_pixel_endpoint = os.getenv("ADD_PIXEL_ENDPOINT")

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": terms_of_service,
    "notMinor": not_minor
}

# Create a user on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": graph_id,
    "name": graph_name,
    "unit": unit_measure,
    "type": unit_type,
    "color": color
}

headers = {
    "X-USER-TOKEN": token,
}

# Gets today's date using datetime.now() and formats it to YYYYMMDD (20210111)format
today = datetime(2021, 1, 11).strftime("%Y%m%d")

add_pixel_params = {
    "date": today,
    "quantity": "6",
}

# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add a pixel to graph
response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)

update_params = {
    "quantity": "2",
}
update_endpoint = add_pixel_endpoint + "/" + today

# Update graph
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_endpoint = add_pixel_endpoint + "/" + today
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
