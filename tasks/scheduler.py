import schedule
import time
from functions.news_utils import fetch_daily_news

def daily_news_job():
    news = fetch_daily_news()
    print(f"Daily News: {news}")

def start_jobs():
    schedule.every().day.at("08:00").do(daily_news_job)

    while True:
        schedule.run_pending()
        time.sleep(1)