from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.add_argument('--incognito')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Navigate to the website
    driver.get('https://axmap.ae/')
    print("Page Title:", driver.title)

    # Wait for the elements with class="content_link" to be present (up to 10 seconds)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "content_link"))
    )

    # Find all <a> tags with class="content_link"
    content_links = driver.find_elements(By.CLASS_NAME, "content_link")

    # Extract and print the text (names) from each <a> tag
    if content_links:
        print("\nNames found in <a> tags with class='content_link':")
        for link in content_links:
            name = link.text.strip()  # Get the text and remove any leading/trailing whitespace
            if name:  # Only print if the text is not empty
                print(name)
    else:
        print("No <a> tags with class='content_link' were found on the page.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()