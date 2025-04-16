import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

# l = os.getenv("INSTAGRAM_SESSION")

try:
    driver.get("https://www.instagram.com")
    # driver.delete_all_cookies()
    driver.add_cookie({'name': 'sessionid', 'value': "19545839310%3A8wS3W30qaq1l9S%3A26%3AAYdIvWae9lp6tgyr2dBseD94h8_Uo_ryFd7sfVoK6A"})
    driver.refresh()
    time.sleep(100)
except Exception as e:
    driver.save_screenshot('screenshot.png')
    print(e)