# https://httpbin.org
# pip install requests

import requests

BASE_URL = "https://httpbin.org/"

response = requests.get(BASE_URL + "/status/200")


print(response)

username = "testuser"
password = "testuser"

response1 = requests.get(
    BASE_URL + f"/basic-auth/{username}/{password}", auth=(username, password)
)

response1 = response1.json()

print(response1)

cookies = {"cookies_are": "working"}

response2 = requests.get(BASE_URL + "/cookies", cookies=cookies)

response2 = response2.json()

print(response2)

s = requests.session()

response3 = s.get(BASE_URL + "/cookies/set/test/cookie")

response3 = response3.json()

print(response3, s.cookies)
