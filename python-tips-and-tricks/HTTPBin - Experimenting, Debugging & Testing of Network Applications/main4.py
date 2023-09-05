# https://httpbin.org
# pip install requests

import requests

BASE_URL = "https://httpbin.org/"


response = requests.get(BASE_URL + f"/redirect-to?url=https://fdlucifer.github.io")

print(response.text)
