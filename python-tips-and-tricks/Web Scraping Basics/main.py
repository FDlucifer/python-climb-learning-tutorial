# https://webscraper.io/test-sites/tables

from urllib.request import urlopen

url = "https://webscraper.io/test-sites/tables"
html_code = urlopen(url).read().decode("utf-8")
#print(html_code)
start = html_code.find("<h1>") + len("<h1>")
end = html_code.find("</h1>")

print(html_code[start:end])