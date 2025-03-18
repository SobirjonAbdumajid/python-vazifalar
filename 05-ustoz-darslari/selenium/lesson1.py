from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
import time

# 2Captcha sozlamasi
solver = TwoCaptcha('YOUR_2CAPTCHA_API_KEY')

# Chrome brauzerini ochish
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# CAPTCHA aniqlansa
try:
    result = solver.recaptcha(sitekey='GOOGLE_SITE_KEY', url='https://www.google.com')
    driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{result["code"]}";')
except:
    print("CAPTCHA hal qilinmadi")

# Qidiruv
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium misol")
search_box.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()