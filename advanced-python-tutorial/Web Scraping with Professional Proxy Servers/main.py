# https://books.toscrape.com/
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import statistics

BASE_URL = "https://books.toscrape.com/"

url = BASE_URL + "catalogue/category/books/philosophy_7/index.html"

username, password = open('creds.txt').read().splitlines()

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")

def proxy_request(url):
    payload = {
        "source": "universal",
        "url": url,
        "geo_location": "Germany"
    }

    response = requests.request(
        "POST", "https://realtime.oxylabs.io/v1/queries",
        auth=(username, password),
        json=payload
    )

    response_html = response.json()['results'][0]['content']
    return BeautifulSoup(response_html, "lxml")

soup = proxy_request(url)
price_tags = soup.find_all("p", {"class": "price_color"})

prices = [float(price.text[1:]) for price in price_tags]
print(prices)
print(statistics.mean(prices))

cat = "catalogue/category/books/fiction_10/"
url = BASE_URL + cat + "index.html"

prices = []
next_link = True

while next_link:
    soup = proxy_request(url)

    price_tags = soup.find_all("p", {"class": "price_color"})
    page_prices = [float(price.text[1:]) for price in price_tags]
    prices += page_prices
    link = soup.body.find("a", text="next")
    if link:
        url = BASE_URL + cat + link['href']
    else:
        next_link = False

print(prices)
print(statistics.mean(prices))

url = BASE_URL + "catalogue/category/books/psychology_26/index.html"

soup = proxy_request(url)

books = soup.find_all("article", {"class": "product_pod"})
book_links = [book.find("a")['href'] for book in books]
book_names = [book.find("h3").text for book in books]
print(book_names)

for i in range(len(book_links)):
    url = BASE_URL + "catalogue/category/books/psychology_26/" + book_links[i]
    soup = proxy_request(url)
    availability = soup.find("p", {"class": "instock availability"})
    print(f"{book_names[i]}: {availability.text.strip()[10:12].strip()}")