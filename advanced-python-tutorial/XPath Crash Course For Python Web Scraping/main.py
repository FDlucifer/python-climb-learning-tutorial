# pip install selenium webdriver-manager

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = "https://books.toscrape.com/"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url)
driver.maximize_window()

xpath_query = "//article[p[@class='star-rating One']]//h3/a | //article[p[@class='star-rating One']]//p[@class='price_color']"

results = driver.find_elements("xpath", xpath_query)

for result in results:
    if result.tag_name == "a":
        print(result.get_attribute("title"))
    else:
        print(result.get_attribute("innerHTML"))

