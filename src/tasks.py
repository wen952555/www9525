import schedule
from datetime import datetime
from functions.news_utils import fetch_daily_news

def job_daily_news():
    news = fetch_daily_news()
    print(f"Daily News at {datetime.now()}:\n{news}")

def schedule_jobs():
    schedule.every().day.at("08:00").do(job_daily_news)