import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Brauzer sozlamalari
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

# Saytni ochish
driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")

try:
    # Popup paydo bo'lishini kutish
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popupModal"]/div/div/div')))
    print("Popup paydo bo'ldi!")

    # Formani topish
    name_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[1]/input')
    email_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[2]/input')
    phone_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[3]/div/input')
    download_button = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')

    # Formani to'ldirish
    name_field.send_keys("Sobirjon")
    email_field.send_keys("sobirjon@example.com")
    phone_field.send_keys("998901234567")
    print("Forma to'ldirildi!")

    # Yuklab olish tugmasini bosish
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')))
    download_button.click()
    print("Yuklab olish tugmasi bosildi!")

    # "OK" tugmasini kutish va bosish (agar bo'lsa)
    try:
        ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "OK")]')))
        ok_button.click()
        print("OK tugmasi bosildi!")
    except:
        print("OK tugmasi topilmadi yoki paydo bo'lmadi. Davom etamiz...")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

finally:
    time.sleep(5)
    driver.quit()