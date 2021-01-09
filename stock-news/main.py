import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from twilio.rest import Client

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
news_articles = []


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news():
    load_dotenv()
    news_api_key = os.getenv("NEWS_API_KEY")
    news_api_endpoint = os.getenv("NEWS_API_ENDPOINT")
    new_api_parameters = {
        "q": "Tesla",
        "apiKey": news_api_key,
        "sortBy": "publishedAt",
        "language": "en",
    }
    news_api_response = requests.get(news_api_endpoint, params=new_api_parameters)
    news_api_response.raise_for_status()
    api_news_articles = news_api_response.json()["articles"][:3]

    for news in api_news_articles:
        title = news["title"]
        description = news["description"]
        article = {
            "title": title,
            "description": description
        }
        news_articles.append(article)
    return news_articles


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_message(msg):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                         body=msg,
                         from_=os.getenv("TWILIO_NUMBER"),
                         to=os.getenv("MY_NUMBER")
                     )
    return message.status


def create_message(news, chng):
    message = ""
    for n in news:
        message += f"{STOCK}: 🔺{round(chng)}%\n"
        message += f"Headline: {n['title']}\nBrief: {n['description']}\n\n"
    return message


# STEP 1: Use
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_vantage_key = os.getenv("ALPHA_VANTAGE_KEY")
alpha_vantage_endpoint = os.getenv("ALPHA_VANTAGE_ENDPOINT")

alpha_vantage_parameters = {
    "function": "GLOBAL_QUOTE",
    "symbol": STOCK,
    "apikey": alpha_vantage_key,
    "sortBy": "publishedAt",
}
stock_api_response = requests.get(alpha_vantage_endpoint, params=alpha_vantage_parameters)
stock_api_response.raise_for_status()
stock_data = stock_api_response.json()["Global Quote"]

change_percentage = float(stock_data["10. change percent"][:-1])

if abs(change_percentage) > 5:
    news_articles = get_news()
    res = send_message(create_message(news_articles, change_percentage))
    print(res)
else:
    print("No news")


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

