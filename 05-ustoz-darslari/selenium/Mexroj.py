import time
import os
import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def start_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver

def scrape_library_project(driver):
    driver.get("https://shaxzodbek.com")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("🏠 Asosiy sahifa yuklandi.")
    except TimeoutException:
        print("❌ Asosiy sahifa yuklanmadi.")
        return

    # Projects sahifasiga o'tish
    try:
        driver.find_element(By.LINK_TEXT, "Projects").click()
        print("📁 Projects bo‘limiga o‘tildi.")
    except TimeoutException:
        print("❌ Projects havolasi topilmadi.")
        return

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "project-card")))
        projects = driver.find_elements(By.CLASS_NAME, "project-card")

        for project in projects:
            try:
                title = project.find_element(By.TAG_NAME, "h3").text.strip()
                if "Library Management System" in title:
                    print("✅ Library Management System topildi.")

                    # Details havolasini topib, bosamiz
                    detail_link = project.find_element(By.PARTIAL_LINK_TEXT, "Details").get_attribute("href")
                    driver.get(detail_link)
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                    time.sleep(2)

                    # Sahifadagi ma'lumotlarni olish
                    project_title = driver.find_element(By.TAG_NAME, "h1").text.strip()
                    desc = driver.find_element(By.TAG_NAME, "p").text.strip()
                    url = driver.current_url

                    # Faylga yozamiz
                    os.makedirs("../output", exist_ok=True)
                    with codecs.open("../output/library_info.txt", "w", encoding="utf-8") as f:
                        f.write(f"Title: {project_title}\n")
                        f.write(f"Description: {desc}\n")
                        f.write(f"URL: {url}\n")

                    print("📄 Ma’lumotlar faylga yozildi: output/library_info.txt")
                    return
            except Exception as e:
                print(f"⚠️ Ichki xatolik: {e}")

        print("❌ 'Library Management System' topilmadi.")
    except Exception as e:
        print(f"❗ Umumiy xatolik: {e}")

def main():
    driver = start_browser()

    try:
        scrape_library_project(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
