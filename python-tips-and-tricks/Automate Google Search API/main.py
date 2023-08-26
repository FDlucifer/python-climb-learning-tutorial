# pip install requests

import requests

API_KEY = ""
SEARCH_ENGINE_ID = ""

search_query = "fdvoid0 books"

url = "https://www.googleapis.com/customsearch/v1"
params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
    'searchType': 'image',
    'lr': 'lang_en',
    'gl': 'US'
}

response = requests.get(url, params=params)
results = response.json()['items']

if 'items' in results:
    print(results['items'][0]['link'])

