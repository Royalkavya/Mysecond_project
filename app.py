from flask import Flask, render_template
import json
from scraper import scrape_quotes

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open("data/scraped_data.json", "r") as f:
            quotes = json.load(f)
    except FileNotFoundError:
        quotes = scrape_quotes()

    return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)
