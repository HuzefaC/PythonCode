from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
y_c_news = response.text
soup = BeautifulSoup(y_c_news, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
all_upvotes = []

for article in articles:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)

subtexts = soup.find_all(name="td", class_="subtext")

for subtext in subtexts:
    if not subtext.find(name="span", class_="score"):
        all_upvotes.append(0)
    else:
        all_upvotes.append(int(subtext.find(name="span", class_="score").getText().split()[0]))

max_upvotes_index = all_upvotes.index(max(all_upvotes))
print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])
print(all_upvotes[max_upvotes_index])
# with open("website.html", encoding="utf8") as file:
#     data = file.read()
#
# soup = BeautifulSoup(data, "html.parser")
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
