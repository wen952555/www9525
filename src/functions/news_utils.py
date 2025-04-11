import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_daily_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])[:5]
    return "\n".join([f"- {article['title']}" for article in articles])