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
    element = driver.find_element(By.XPATH, "/html/body/main/section/div[2]/a[1]")  # yoki CLASS_NAME, XPATH, etc.
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)
except Exception as e:
    print("Error while navigating to the certificate page:", e)

try:
    login_button3 = WebDriverWait(driver, 0).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[2]/a[1]")))
    login_button3.click()
    # time.sleep(2)
except Exception as e:
    print("Error while clicking the login button:", e)



# Navigate to the "Job Portal System" project
try:
    job_portal_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//h3/a[contains(text(), 'Job Portal System')]"))
    )
    job_portal_link.click()
    print("Successfully navigated to the Job Portal System page.")
    time.sleep(2)  # Allow time for the page to load
except Exception as e:
    print("Error while navigating to the Job Portal System page:", e)
    driver.quit()
    exit()

# Extract data from the page
try:
    # 1. Header
    try:
        header = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        ).text
        print("Header:", header)
    except Exception as e:
        print("Error extracting header:", e)
        header = "Not found"

    # 2. Date
    try:
        project_date = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "project-meta"))
        ).text
        print("Date:", project_date)
    except Exception as e:
        print("Error extracting date:", e)
        project_date = "Not found"

    # # 3. API Tag
    # try:
    #     api_tag = WebDriverWait(driver, 15).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "project-tag"))
    #     ).text
    #     print("API Tag:", api_tag)
    # except Exception as e:
    #     print("Error extracting API tag:", e)
    #     api_tag = "Not found"





    # 4. Image URL
    try:
        image_url = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/img"))
        ).get_attribute("src")
        print("Image URL:", image_url)
    except Exception as e:
        print("Error extracting image URL:", e)
        image_url = "Not found"

    try:
        image_url = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[2]/div[2]/div[1]/img"))
        ).get_attribute("src")
        print("Image URL:", image_url)
    except Exception as e:
        print("Error extracting image URL:", e)
        image_url = "Not found"


    # # 5. Description
    # try:
    #     description = WebDriverWait(driver, 15).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'project-description')]/p"))
    #     ).text
    #     print("Description:", description)
    # except Exception as e:
    #     print("Error extracting description:", e)
    #     description = "Not found"

    # 6. Technologies Used
    try:
        technologies = []
        tech_elements = driver.find_elements(By.CSS_SELECTOR, ".tech-stack img")
        for tech in tech_elements:
            tech_name = tech.get_attribute("alt")
            if tech_name:
                technologies.append(tech_name)
        print("Technologies Used:", technologies)
    except Exception as e:
        print("Error extracting technologies:", e)
        technologies = ["Not found"]

    # 7. GitHub and Live Demo Links
    try:
        github_link = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'View on GitHub')]"))
        ).get_attribute("href")
        print("GitHub Link:", github_link)
    except Exception as e:
        print("Error extracting GitHub link:", e)
        github_link = "Not found"

    try:
        live_demo_link = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Live Demo')]"))
        ).get_attribute("href")
        print("Live Demo Link:", live_demo_link)
    except Exception as e:
        print("Error extracting Live Demo link:", e)
        live_demo_link = "Not found"

except Exception as e:
    print("Error while extracting data from the page:", e)

# Close the driver
try:
    driver.quit()
    print("Driver closed successfully.")
except Exception as e:
    print("Error while closing the driver:", e)