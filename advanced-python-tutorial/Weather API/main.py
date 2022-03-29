# https://home.openweathermap.org/api_keys

import datetime as dt
from pydoc import describe
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = "Shenzhen"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"temperature in {CITY}: {temp_celsius:.2f}℃  or {temp_fahrenheit:.2f}℉")
print(f"temperature in {CITY} feels like: {feels_like_celsius:.2f}℃  or {feels_like_fahrenheit:.2f}℉")
print(f"humidity in {CITY}: {humidity}%")
print(f"wind speed in {CITY}: {wind_speed}m/s")
print(f"general weather in {CITY}: {description}")
print(f"sunrise in {CITY} at {sunrise_time} local time.")
print(f"sunset in {CITY} at {sunset_time} local time.")