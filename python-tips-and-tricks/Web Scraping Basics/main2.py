from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
html_code = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html_code, 'lxml')

type_table = soup.find(class_="wikitable")
body = type_table.find("tbody")
rows = body.find_all("tr")[1:]

mutable_types = []
immutable_types = []

for row in rows:
    data = row.find_all("td")
    if data[1].get_text() == "mutable\n":
        mutable_types.append(data[0].get_text())
    else:
        immutable_types.append(data[0].get_text())
print(f"mutable types: {mutable_types}")
print(f"immutable types: {immutable_types}")

thumb_box = soup.find(class_="thumb")
thumb_img_src = thumb_box.find("img")['src']
print(f"thumb img src: {thumb_img_src}")

toc = soup.find(class_="toc")
toc_text = [a.get_text() for a in toc.find_all("a")]
print(f"toc text: {toc_text}")