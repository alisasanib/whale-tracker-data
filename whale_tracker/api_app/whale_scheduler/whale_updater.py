from apscheduler.schedulers.background import BackgroundScheduler
from api_app.views import TransactionViews

def start():
  scheduler = BackgroundScheduler()
  transactions = TransactionViews()
  scheduler.add_job(transactions.save_whale_data, "interval", minutes=1,id="whale_001",replace_existing=True)
  scheduler.start()