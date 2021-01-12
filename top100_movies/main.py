import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)

empire_online = response.text

soup = BeautifulSoup(empire_online, "html.parser")

title_list = soup.find_all(name="h3", class_="title")

list_of_movies = []

for title in title_list:
    movie = title.getText()
    list_of_movies.append(movie)

list_of_movies.reverse()

with open("100_Greatest_Movies.txt", mode="w", encoding="ISO-8859-1") as file:
    for movie in list_of_movies:
        file.write(movie+"\n")
