import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
selenium_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=selenium_options)

driver.get("https://www.ilovepdf.com/word_to_pdf/")
upload_file = driver.find_element('xpath', '//input[@type="file"]')
time.sleep(2)
upload_file.send_keys(f'{os.getcwd()}/downloads/Muxtorov_Shaxzodbek_cv.docx')
time.sleep(2)
