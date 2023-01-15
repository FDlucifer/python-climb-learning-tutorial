# pip install httpx

import asyncio
import httpx
import time

async def fetch():
    urls = ["https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html",
            "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html",
            ]

    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)
    
    print(results)

start = time.perf_counter()
asyncio.run(fetch())
end = time.perf_counter()

print("used time: ", end - start)
