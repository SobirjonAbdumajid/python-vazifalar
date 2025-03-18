import time

from selenium import webdriver
from selenium.common import NoSuchElementException

driver = webdriver.Chrome()
try:
    driver.get("https://google.com")
    assert "Google" in driver.title
    time.sleep(30)
except Exception as e:
    print(e)
finally:
    driver.close()
