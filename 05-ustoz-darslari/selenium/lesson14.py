import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.axcapital.ae/")
driver.find_element('xpath', '//*[@id="ax"]/div/div[2]/div/div/div[2]/div/a').click()
time.sleep(10)
