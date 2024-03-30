# pip install schedule

import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime


def job():
    print("i am lUc1f3r11!")

j = schedule.every(1).to(5).seconds.do(job)

counter = 0

while True:
    schedule.run_pending()
    tm.sleep(1)
    counter += 1
    if counter == 10:
        schedule.cancel_job()

