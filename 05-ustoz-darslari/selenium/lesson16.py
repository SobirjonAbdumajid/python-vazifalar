from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.add_argument('--incognito')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get('https://www.axcapital.ae/')

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "content_link"))
    )

    content_links = driver.find_elements(By.CLASS_NAME, "content_link")

    if content_links:
        for link in content_links:
            name = link.text.strip()
            print(name)
    else:
        print("No <a> tags with class='content_link' were found on the page.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
