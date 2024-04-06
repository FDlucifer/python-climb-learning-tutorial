# pip install selenium webdriver_manager

import time
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--verbose")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

url = "https://setcookie.net"

driver.get(url)

try:
    with open("cookie.pkl", "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(url)
except FileNotFoundError:
    print("No cookies found.")

    time.sleep(2)

    name_input = driver.find_element('name', 'name')
    value_input = driver.find_element('name', 'value')

    name_input.send_keys('somecookiename')
    value_input.send_keys('somecookievalue')

    submit_button = driver.find_element('xpath', '//input[@type="submit"]')
    submit_button.click()

    time.sleep(2)

with open("cookie.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

driver.get(url)

time.sleep(5)
