# https://httpbin.org
# pip install requests

import requests

BASE_URL = "https://httpbin.org/"

data = {"data1": "hello", "data2": "world"}

response = requests.post(BASE_URL + "/post", data=data)
response = response.json()
del response["origin"]

print(response)
