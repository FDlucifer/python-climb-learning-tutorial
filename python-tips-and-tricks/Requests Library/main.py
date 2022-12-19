# pip install requests
# https://httpbin.org/

import requests

params = {
    "name": "Mike",
    "age": 25
}

response = requests.get('https://httpbin.org/get', params=params)
print(response.url)

res_json = response.json()
del res_json['origin']

print(res_json)

payload = {
    "name": "Mike",
    "age": 25
}

response = requests.post('https://httpbin.org/post', data=payload)
print(response.url)
res_json = response.json()
print(res_json)

response = requests.get('https://httpbin.org/status/404')

if response.status_code == requests.codes.not_found:
    print("not found")
else:
    print(response.status_code)

headers = {
    "User-Agent": "lucifer11",
    "Accept": "image/webp"
}

response = requests.get('https://httpbin.org/image', headers=headers)
print(response.status_code)

with open("myimage.webp", "wb") as f:
    f.write(response.content)


response = requests.get('https://httpbin.org/delay/1', timeout=2)
res_json = response.json()
print(res_json)

proxies = {
    "http:": "139.99.237.62:80",
    "https:": "139.99.237.62:80"
}

response = requests.get('https://httpbin.org/get', proxies=proxies)
print(response.text)

