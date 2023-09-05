# https://httpbin.org
# pip install requests

import requests

BASE_URL = "https://httpbin.org/"

TOKEN = "whatever this is my token"

headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(BASE_URL + "/bearer", headers=headers)

if response.status_code == 200:
    response = response.json()
    print(response)
else:
    print("Auth failed!")
