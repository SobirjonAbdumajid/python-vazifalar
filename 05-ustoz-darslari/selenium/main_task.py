# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# try:
#     # === Selenium bilan sahifani ochamiz ===
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://shaxzodbek.com/")
# except Exception as e:
#     print("Error while opening the page:", e)
#
# try:
#     # Kirish tugmasini bosamiz
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/nav/ul/li[4]/a")))
#     login_button.click()
# except Exception as e:
#     print("Error while clicking the login button:", e)
#
# try:
#     # Kirish sahifasida scroll qilish
#     login_button2 = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/a[1]")))
#     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", login_button2)
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[2]/a[1]"))).click()
# except Exception as e:
#     print("Error while scrolling and clicking the second login button:", e)
#
# try:
#     # Sertifikat sahifasiga o‘tamiz
#     login_button3 = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[1]/div/div[3]/div[2]/h4/a")))
#     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", login_button3)
#     login_button3.click()
#     time.sleep(2)
# except Exception as e:
#     print("Error while navigating to the certificate page:", e)
#
# try:
#     # === Sahifadagi kerakli ma’lumotlarni avtomatik olish ===
#     title = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".certification-header h3"))).text
#     obtained_date = driver.find_element(By.CLASS_NAME, "certification-date").text.replace("Obtained: ", "")
#     image_url = driver.find_element(By.CSS_SELECTOR, ".certification-image img").get_attribute("src")
#     description = driver.find_element(By.CLASS_NAME, "certification-description").text.strip()
#
#     # === Konsolga chop etish (tekshirish uchun) ===
#     print("Title:", title)
#     print("Obtained Date:", obtained_date)
#     print("Image URL:", image_url)
#     print("Description:", description)
# except Exception as e:
#     print("Error while extracting data from the page:", e)
#
# # Close the driver
# try:
#     driver.quit()
# except Exception as e:
#     print("Error while closing the driver:", e)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # === Selenium bilan sahifani ochamiz ===
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://shaxzodbek.com/")
except Exception as e:
    print("Error while opening the page:", e)



try:
    # Kirish tugmasini bosamiz
    login_button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/nav/ul/li[4]/a")))
    login_button.click()
except Exception as e:
    print("Error while clicking the login button:", e)

try:
    # Kirish sahifasida scroll qilmasdan tugmani bosamiz
    login_button2 = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[2]/a[1]")))
    login_button2.click()
except Exception as e:
    print("Error while clicking the second login button:", e)

try:
    # Sertifikat sahifasiga o‘tamiz
    login_button3 = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[1]/div/div[3]/div[2]/h4/a")))
    login_button3.click()
    time.sleep(2)
except Exception as e:
    print("Error while navigating to the certificate page:", e)

try:
    # === Sahifadagi kerakli ma’lumotlarni avtomatik olish ===
    title = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".certification-header h3"))).text
    obtained_date = driver.find_element(By.CLASS_NAME, "certification-date").text.replace("Obtained: ", "")
    image_url = driver.find_element(By.CSS_SELECTOR, ".certification-image img").get_attribute("src")
    description = driver.find_element(By.CLASS_NAME, "certification-description").text.strip()

    # === Konsolga chop etish (tekshirish uchun) ===
    print("Title:", title)
    print("Obtained Date:", obtained_date)
    print("Image URL:", image_url)
    print("Description:", description)
except Exception as e:
    print("Error while extracting data from the page:", e)

# Close the driver
try:
    driver.quit()
except Exception as e:
    print("Error while closing the driver:", e)