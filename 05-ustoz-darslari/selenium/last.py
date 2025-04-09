
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://shaxzodbek.com/")
    print("Successfully opened the website.")
except Exception as e:
    print("Error while opening the page:", e)
    driver.quit()
    exit()

# Navigate to the "Projects" section
try:
    projects_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Projects')]"))
    )
    projects_button.click()
    print("Successfully clicked on the Projects button.")
    time.sleep(2)  # Allow time for the page to load
except Exception as e:
    print("Error while clicking the projects button:", e)
    driver.quit()
    exit()

try:
    element = driver.find_element(By.XPATH, "/html/body/main/section/div[2]/a[1]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)
except Exception as e:
    print("Error while scrolling to element:", e)

try:
    login_button3 = WebDriverWait(driver, 0).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[2]/a[1]")))
    login_button3.click()
    # time.sleep(2)
except Exception as e:
    print("Error while clicking the login button:", e)


try:
    job_portal_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//h3/a[contains(text(), 'Job Portal System')]"))
    )
    job_portal_link.click()
    print("Successfully navigated to the Job Portal System page.")
    time.sleep(2)
except Exception as e:
    print("Error while navigating to the Job Portal System page:", e)
    driver.quit()
    exit()

# Extract data from the page
try:
    # 1. Header
    header = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text
    print(f"Header: {header}")

    # 2. Date
    project_date = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "project-meta"))
    ).text
    print(f"Date: {project_date}")

    # 3. Image URL
    try:
        image_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/img"))
        )
        image_url = image_element.get_attribute("src")
        print(f"Image URL: {image_url}")
    except Exception as e:
        print("Error extracting main image URL:", e)
        image_url = "Not found"

    # 4. Extract sections dynamically
    section_headings = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'project-body')]//h2"))
    )

    for heading in section_headings:
        title = heading.text.strip()
        if not title:
            continue
        try:
            content_div = heading.find_element(By.XPATH, "./following-sibling::div[1]")

            # Check for technology images
            tech_images = content_div.find_elements(By.TAG_NAME, "img")
            if tech_images:
                technologies = [img.get_attribute('alt').strip() for img in tech_images if img.get_attribute('alt')]
                print(f"{title}: {', '.join(technologies)}")
                continue

            # Check for links
            links = content_div.find_elements(By.TAG_NAME, "a")
            if links:
                for link in links:
                    link_text = link.text.strip()
                    link_url = link.get_attribute('href')
                    if link_text and link_url:
                        print(f"{link_text}: {link_url}")
                continue

            # Default to text content
            content = content_div.text.strip()
            if content:
                print(f"{title}: {content}")
        except Exception as e:
            print(f"Error processing section '{title}': {e}")

except Exception as e:
    print("Error while extracting data from the page:", e)

# Close the driver
try:
    driver.quit()
    print("Driver closed successfully.")
except Exception as e:
    print("Error while closing the driver:", e)