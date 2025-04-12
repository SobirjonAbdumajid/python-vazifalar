import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

# Setup
fake = Faker()
fake_ru = Faker('ru_RU')
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

# Open site
driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")

try:
    # Wait for the popup to appear
    popup = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popupModal"]/div/div/div')))
    print("Popup appeared!")

    # Locate form fields
    name_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[1]/input')
    email_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[2]/input')
    phone_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[3]/div/input')
    download_button = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')


    # Function to fill field using JavaScript if direct interaction fails
    def fill_field(element, value):
        try:
            # Check if the element is visible and enabled
            if not element.is_displayed() or not element.is_enabled():
                print(
                    f"Field {element.get_attribute('name') or 'unknown'} is not interactable (not visible or disabled).")
                return False
            element.clear()
            element.send_keys(value)
            print(f"Filled field {element.get_attribute('name') or 'unknown'} with value: {value}")
            return True
        except ElementNotInteractableException:
            print(f"Direct interaction failed for {element.get_attribute('name') or 'unknown'}. Trying JavaScript...")
            driver.execute_script("arguments[0].value = arguments[1];", element, value)
            print(f"Filled field {element.get_attribute('name') or 'unknown'} with value: {value} using JavaScript")
            return True


    # Fill the form
    fill_field(name_field, fake.name())
    fill_field(email_field, fake.email())
    phone_number = fake_ru.phone_number().replace('+', '').replace(' ', '')  # Clean phone number
    fill_field(phone_field, phone_number)

    # Click the download button
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')))
    download_button.click()
    print("Download button clicked.")

    # Wait for a potential confirmation dialog and locate the "OK" button
    try:
        ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "OK")]')))
        ok_button.click()
        print("OK button clicked.")
    except TimeoutException:
        print("No 'OK' button found or it didn't appear in time. Continuing...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait to view the result before quitting
    time.sleep(5)
    driver.quit()
# driver.quit()