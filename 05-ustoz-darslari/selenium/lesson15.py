from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--incognito')
# options.add_argument('--ignore-certificate-errors')
# options.page_load_strategy = 'eager' # no

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://axmap.ae/')

print(driver.title)