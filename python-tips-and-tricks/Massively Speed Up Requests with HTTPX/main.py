# pip install requests

import time
import requests

def fetch():
    urls = ["https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html",
            ]

    results = [requests.get(url) for url in urls]
    print(results)

start = time.perf_counter()
fetch()
end = time.perf_counter()

print("used time: ", end - start)
