# https://httpbin.org
# pip install requests

import requests

BASE_URL = "https://httpbin.org/"

response = requests.get(BASE_URL + "/delay/5", timeout=2)
response = response.json()
del response["origin"]

print(response)
