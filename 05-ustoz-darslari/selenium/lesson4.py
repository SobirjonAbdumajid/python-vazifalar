from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Chrome sozlamalari (bot aniqlanishini kamaytirish)
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124")

# Chrome brauzerini ochish
driver = webdriver.Chrome(options=options)

# Saytga kirish
driver.get("https://openbudget.uz/boards/initiatives")
time.sleep(5)  # Sahifa yuklanishini kutish

# Tashabbuslarni ro‘yxatdan olish (masalan, taklif sarlavhalari)
try:
    # Takliflar ro‘yxatini topish (HTML class yoki ID ga qarab moslashtiring)
    initiatives = driver.find_elements(By.CLASS_NAME, "initiative-item")  # Bu class faqat misol uchun
    for index, initiative in enumerate(initiatives, 1):
        title = initiative.find_element(By.TAG_NAME, "h3").text  # Sarlavhani olish (agar h3 bo‘lsa)
        print(f"{index}. {title}")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# Brauzerni yopish
time.sleep(3)
driver.quit()