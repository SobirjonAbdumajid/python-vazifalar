# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Initialize the driver
# try:
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://shaxzodbek.com/")
#     print("Successfully opened the website.")
# except Exception as e:
#     print("Error while opening the page:", e)
#     exit()
#
# # Click on "Projects"
# try:
#     projects_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Projects')]"))
#     )
#     projects_button.click()
#     print("Successfully clicked on the Projects button.")
#     time.sleep(2)
# except Exception as e:
#     print("Error while clicking the projects button:", e)
#     driver.quit()
#     exit()
#
# # Scroll to and click the certificate/project link
# try:
#     project_entry = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[2]/a[1]"))
#     )
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", project_entry)
#     time.sleep(1)
#     project_entry.click()
# except Exception as e:
#     print("Error while accessing the project:", e)
#     driver.quit()
#     exit()
#
# # Navigate to specific project (Job Portal System)
# try:
#     job_portal_link = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//h3/a[contains(text(), 'Job Portal System')]"))
#     )
#     job_portal_link.click()
#     print("Navigated to Job Portal System page.")
#     time.sleep(2)
# except Exception as e:
#     print("Error while navigating to Job Portal System:", e)
#     driver.quit()
#     exit()
#
# # --- Extract Content from Project Page ---
# try:
#     # Header (h1)
#     header = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.TAG_NAME, "h1"))
#     ).text
#     print(header)
#
#     # Date or metadata (usually .project-meta)
#     meta_info = driver.find_element(By.CLASS_NAME, "project-meta").text
#     print(meta_info)
#
#     # H2 sections (like API, Features, etc.)
#     h2_elements = driver.find_elements(By.XPATH, "//div[@class='project-body']//h2")
#     for h2 in h2_elements:
#         print(h2.text)
#
#     # Description
#     description_blocks = driver.find_elements(By.XPATH, "//div[@class='project-body']/p")
#     for block in description_blocks:
#         print(block.text)
#
#     # Images
#     images = driver.find_elements(By.XPATH, "//main//img")
#     for img in images:
#         src = img.get_attribute("src")
#         if src:
#             print(src)
#
#     # Technologies
#     tech_icons = driver.find_elements(By.XPATH, "//div[@class='technology-item']/img")
#     for icon in tech_icons:
#         tech_name = icon.get_attribute("alt")
#         if tech_name:
#             print(tech_name)
#
#     # GitHub and Live Demo Links
#     links = driver.find_elements(By.XPATH, "//a[contains(@href, 'http')]")
#     for link in links:
#         href = link.get_attribute("href")
#         if "github" in href.lower() or "demo" in href.lower():
#             print(href)
#
# except Exception as e:
#     print("Error extracting project content:", e)
#
# # Close browser
# try:
#     driver.quit()
#     print("Driver closed successfully.")
# except Exception as e:
#     print("Error while closing driver:", e)
