import datetime as dt
import pytz

datetime_string = "2022-01-01 12:21:33"
datetime_newyork = dt.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")

current_timezone = pytz.timezone("US/Eastern")
target_timezone = pytz.timezone("Europe/Vienna")

print(datetime_newyork)
localized_newyork = current_timezone.localize(datetime_newyork)
print(localized_newyork)

datetime_vienna = localized_newyork.astimezone(target_timezone)
print(datetime_vienna)

print(datetime_vienna.replace(tzinfo=None))
print(datetime_vienna.timetz())

print(pytz.all_timezones)
print(pytz.common_timezones)
print(pytz.country_timezones["US"])

print(localized_newyork.tzname())
print(localized_newyork.utcoffset())
print(localized_newyork.dst())