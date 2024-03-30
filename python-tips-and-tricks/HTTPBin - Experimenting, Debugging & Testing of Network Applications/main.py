# https://httpbin.org
# pip install requests

import requests

BASE_URL = "https://httpbin.org/"

response = requests.get(
    BASE_URL + "/get?test=hello&other=world", headers={"User-Agent": "something else"}
)
response = response.json()
del response["origin"]

print(response)
