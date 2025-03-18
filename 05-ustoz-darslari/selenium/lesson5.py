from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Chrome settings to avoid bot detection
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124")

# Start Chrome browser
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://openbudget.uz/boards/initiatives")
time.sleep(5)  # Wait for the page to load fully

# Open a text file to save the data
with open("initiatives.txt", "w", encoding="utf-8") as file:
    try:
        # Find all initiative elements (adjust class name based on inspection)
        initiatives = driver.find_elements(By.CLASS_NAME, "initiative-item")  # Hypothetical class name
        if not initiatives:
            print("No initiatives found. Check the class name or HTML structure.")
            file.write("No initiatives found.\n")
        else:
            for index, initiative in enumerate(initiatives, 1):
                # Extract title (adjust based on actual tag or class)
                try:
                    title = initiative.find_element(By.TAG_NAME, "h3").text  # Assuming title is in <h3>
                except:
                    title = "Title not found"

                # Write to file
                file.write(f"{index}. {title}\n")
                print(f"{index}. {title}")  # Also print to console
    except Exception as e:
        print(f"Error occurred: {e}")
        file.write(f"Error occurred: {e}\n")

# Close the browser
driver.quit()
