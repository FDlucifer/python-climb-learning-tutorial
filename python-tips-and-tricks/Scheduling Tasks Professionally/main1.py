# pip install schedule

import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime

@repeat(every(5).seconds, message="lucifer11")
@repeat(every(2).seconds, message="hey")
def job(message):
    print("hello the message is:", message)

schedule.every().second.do(job, message="HELLO")

while True:
    schedule.run_pending()
    tm.sleep(1)

