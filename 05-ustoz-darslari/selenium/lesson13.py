import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.fullscreen_window()
driver.get("https://www.axcapital.ae/")

# Find the input field
l = driver.find_element('xpath', "//input[@placeholder='Your name']")

# Scroll the input field into view
driver.execute_script('arguments[0].scrollIntoView();', l)
time.sleep(5)

# Find and hide the logo image
logo_image = driver.find_element('xpath', "//img[@alt='AX CAPITAL Logo']")
driver.execute_script("arguments[0].style.display = 'none';", logo_image)

# Click and fill the input field
l.click()
l.send_keys("Name")

time.sleep(10)
