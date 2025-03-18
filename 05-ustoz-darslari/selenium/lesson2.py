# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # import time
# #
# # # Chrome brauzerini ishga tushirish uchun WebDriver yo‘lini ko‘rsatamiz
# # driver = webdriver.Chrome()  # ChromeDriver o‘rnatilgan bo‘lishi kerak
# #
# # # Google sahifasini ochamiz
# # driver.get("https://www.google.com")
# #
# # # Qidiruv maydonini topib, so‘rov kiritamiz
# # search_box = driver.find_element(By.NAME, "q")
# # search_box.send_keys("Python Selenium misol")
# #
# # # Enter tugmasini bosamiz
# # search_box.send_keys(Keys.RETURN)
# #
# # # Natijalarni ko‘rish uchun bir oz kutamiz
# # time.sleep(5)
# #
# # # Brauzerni yopamiz
# # driver.quit()
#
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import random
#
# # Chrome brauzerini ochish
# driver = webdriver.Chrome()
#
# # Google sahifasiga kirish
# driver.get("https://www.google.com")
# time.sleep(random.uniform(2, 5))  # Tasodifiy kutish (2-5 soniya)
#
# # Qidiruv maydonini topish
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Python Selenium misol")
# time.sleep(random.uniform(1, 3))  # Yozgandan keyin kutish
#
# # Enter bosish
# search_box.send_keys(Keys.RETURN)
# time.sleep(5)  # Natijalarni ko‘rish uchun kutish
#
# # Brauzerni yopish
# driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Chrome sozlamalari
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # Bot aniqlanishini oldini olish
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Oddiy user-agent

# Chrome brauzerini ochish
driver = webdriver.Chrome(options=options)

# Google sahifasiga kirish
driver.get("https://openbudget.uz/boards/initiatives    ")
time.sleep(2)

# Qidiruv maydonini topish va so‘rov kiritish
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium misol")
search_box.send_keys(Keys.RETURN)

time.sleep(50)
driver.quit()
