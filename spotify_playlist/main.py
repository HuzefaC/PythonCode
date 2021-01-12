import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(URL)
response.raise_for_status()

website = response.text

soup = BeautifulSoup(website, "html.parser")
song_list = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artist_list = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")

print(song_list[0].getText())
# for song in song_list:
#     song_name = song.getText()
#     artist =
