# pip install pytz

import datetime as dt
import pytz

dt1 = dt.datetime.now()
print(dt1)

dt2 = dt.datetime.now(pytz.utc)
print(dt2)

dt3 = dt.datetime.now(pytz.timezone("Europe/Vienna"))
print(dt3)