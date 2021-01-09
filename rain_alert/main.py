import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client


load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
weather_api_url = os.getenv("WEATHER_API_URL")

twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")

parameters = {
    "appid": weather_api_key,
    "lat": 15.849695,
    "lon": 74.497673,
    "exclude": "currently,minutely,daily"
}

carry_umbrella = False

response = requests.get(weather_api_url, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data['hourly'][:12]

for data in hourly_data:
    weather_id = data['weather'][0]['id']
    if int(weather_id) < 700:
        carry_umbrella = True
        break

if carry_umbrella:
    print("Please carry a umbrella")
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
        body="Carry an umbrella, It might rain today!!",
        from_='+12055258874',
        to='+918411037244'
    )
else:
    print("No umbrella needed")
