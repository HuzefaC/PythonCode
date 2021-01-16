import requests
from bs4 import BeautifulSoup

# Budget in rupees
BUDGET = 15000

# URL for the HyperX Mechanical Keyboard
URL = "https://www.amazon.in/HyperX-Mechanical-Keyboard-HX-KB4RD1-US-R2/dp/B076BYZJFT/" \
      "ref=sr_1_1_sspa?crid=C9ELJTBYWHFS&dchild=1&keywords=hyperx+mechanical+keyboard&" \
      "qid=1610536110&s=electronics&sprefix=hyperx+me%2Celectronics%2C306&sr=1-1-spons&psc=1&" \
      "spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOERNSlBTTDJZWDRXJmVuY3J5cHRlZElkPUEwNTIwMTAyM1ZEVkFZS1VX" \
      "VU1MMCZlbmNyeXB0ZWRBZElkPUEwODc4NjI3MTkzUTAxWDI2NlcxOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y" \
      "2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
}

continue_loop = True

# Continue sending request until you get a response

while continue_loop:
    response = requests.get(url=URL, headers=headers)

    response.raise_for_status()

    amazon_website = response.text

    soup = BeautifulSoup(amazon_website, "html.parser")

    span_tag = soup.find(name="span", id="priceblock_ourprice")
    if span_tag is not None:
        continue_loop = False
        price = float(span_tag.text.split()[1].replace(",", ""))
        if price < BUDGET:
            print(f"Go buy now the price is {price}")
        else:
            print(f"Still expensive the price is {price}")
