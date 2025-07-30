import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        quotes_data.append({"quote": text, "author": author})

    os.makedirs("data", exist_ok=True)
    with open("data/scraped_data.json", "w") as file:
        json.dump(quotes_data, file, indent=4)

    return quotes_data
