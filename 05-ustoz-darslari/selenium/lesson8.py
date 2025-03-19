import time
from selenium import webdriver


driver = webdriver.Chrome()


# def click_element():
driver.get("https://google.com")
time.sleep(5000)
driver.back()


driver.close()
