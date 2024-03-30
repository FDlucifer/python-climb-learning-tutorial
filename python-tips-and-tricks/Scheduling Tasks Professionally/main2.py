# pip install schedule

import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime


def break_reminder():
    print("take a break! you have been working for 30 minutes!")

schedule.every().day.at("10:00").do(break_reminder)

while True:
    schedule.run_pending()
    tm.sleep(1)

