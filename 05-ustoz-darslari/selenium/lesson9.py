import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/login/ru")
# driver.find_element('id', "username").send_keys("SomeEmail")
time.sleep(3)
# driver.find_element('id', "password").send_keys("SomePassword")
# time.sleep(2)
driver.find_element('class name', "alternate-signin__btn--google").submit()
# print(driver.page_source)
print(driver.current_url)
time.sleep(10)


# print(driver.title)
# print(driver.page_source)
# assert driver.current_url == "https://www.linkedin.com/login/ru"
# print(driver.current_url)
# except Exception as e:
#     print(e)
