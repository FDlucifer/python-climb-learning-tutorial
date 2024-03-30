# just a selenium test code for beginner
from selenium import webdriver
import time

url = 'https://outlook.live.com/'

driver = webdriver.Chrome(r'D:\chromedriver')
driver.get(url)

driver.find_element_by_class_name('linkButtonSigninHeader').click()
time.sleep(2)

driver.find_element_by_id('MemberName').send_keys('testusername123')
time.sleep(2)

driver.find_element_by_id('isSignupAction').click()
time.sleep(2)

driver.find_element_by_id('isSignupAction').send_keys('testpassword123')
time.sleep(2)

driver.find_element_by_id('isSignupAction').click()
time.sleep(2)

driver.find_element_by_id('FirstName').send_keys('john')
time.sleep(2)

driver.find_element_by_id('LastName').send_keys('keets')
time.sleep(2)

driver.find_element_by_id('isSignupAction').click()
time.sleep(2)

driver.find_element_by_id('BirthDay').send_keys('11')
time.sleep(2)

driver.find_element_by_id('BirthMonth').send_keys('07')
time.sleep(2)

driver.find_element_by_id('BirthYear').send_keys('1997')
time.sleep(2)

driver.close()