import time
print(time.time())

import datetime
print(datetime.date(year=2021, month=12, day=21))
print(datetime.time(hour=13, minute=25, second=42))

today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

when = datetime.time(now.hour, now.minute, now.second)
print(datetime.datetime.combine(today, when))

then = "12-21-2012 13:25:42"
format_string = "%m-%d-%Y %H:%M:%S"
print(datetime.datetime.strptime(then, format_string))

import dateparser
dateparser.parse("yesterday")
dateparser.parse("morgen")

from datetime import datetime

BAKTUN = datetime(year=2012, month=12, day=21, hour=23, minute=59, second=59)
survived = datetime.now() - BAKTUN

print(f"you have survived {survived} since the Mayan bak'tun")