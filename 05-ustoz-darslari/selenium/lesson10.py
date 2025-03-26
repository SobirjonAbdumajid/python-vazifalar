import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.axcapital.ae/buy/dubai/properties-for-sale")
time.sleep(1)
cards = len(driver.find_elements("class name", "property-card"))


try:
    for i in range(cards):
        time.sleep(3)
        driver.find_elements("class name", "property-card")[i].click()
        print(driver.current_url)
        time.sleep(3)
        driver.back()
        time.sleep(3)
except Exception as e:
    print(e)
