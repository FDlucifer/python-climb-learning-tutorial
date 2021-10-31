import requests

proxies = {
    'https': 'https://140.227.69.170:6000'
}

response = requests.get("https://ipinfo.io/json", proxies=proxies)

print(response.json()['country'])
print(response.json()['region'])