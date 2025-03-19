import time

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://axcapital.ae/")
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    driver.close()
