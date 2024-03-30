from datetime import datetime as dt

now = dt.now()

print(now.isoformat(sep=" "))
print(now.month)
print(now.year)
print(now.strftime("today is %A, %B %d"))
