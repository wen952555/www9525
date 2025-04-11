from apscheduler.schedulers.background import BackgroundScheduler

def schedule_tasks():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_subscriptions, trigger="interval", hours=1)
    scheduler.start()

def update_subscriptions():
    print("Subscriptions updated!")