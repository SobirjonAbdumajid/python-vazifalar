import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

selenium_options = webdriver.ChromeOptions()

default_download_path = {
    'download.default_directory': f'{os.getcwd()}/downloads'
}

selenium_options.add_experimental_option('prefs', default_download_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=selenium_options)
driver.get("https://shaxzodbek.com/")
time.sleep(2)
driver.find_elements('xpath', '//a')[10].click()
time.sleep(2)
