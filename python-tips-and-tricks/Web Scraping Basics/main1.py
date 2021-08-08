# pip install beautifulsoup4
# pip install lxml

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/tables"
html_code = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html_code, 'lxml')
headings_2 = soup.find_all("h2")
print(headings_2)
images = soup.find_all("img")
print(images[1]['src'])
print(images[1]['alt'])

first_table = soup.find('table')
rows = first_table.findAll('tr')[1:]
last_names = []
for row in rows:
    last_names.append(row.findAll('td')[2].get_text())
print(last_names)