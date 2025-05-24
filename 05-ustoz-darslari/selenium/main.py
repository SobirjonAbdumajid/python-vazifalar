from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from db import get_connection, create_table_if_not_exists
from selenium import webdriver
import time


class JobPortalScraper:
    def __init__(self):
        self.conn = get_connection()
        create_table_if_not_exists()
        self.cursor = self.conn.cursor()
        self.driver = self.init_driver()

    def init_driver(self):
        options = Options()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        return driver

    def open_site(self, url="https://shaxzodbek.com/"):
        self.driver.get(url)

    def go_to_projects_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Projects"))
        ).click()

    def find_and_process_card(self, card_title="Job Portal System"):
        found = False

        while not found:
            time.sleep(2)
            cards = self.driver.find_elements(By.CLASS_NAME, "project-content")

            for card in cards:
                if card_title in card.text:
                    print(f"{card_title} topildi!")
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                    time.sleep(1)
                    card.find_element(By.PARTIAL_LINK_TEXT, card_title).click()
                    time.sleep(2)
                    self.driver.save_screenshot("screenshot.png")

                    self.extract_and_save_data()
                    found = True
                    break

            if not found:
                try:
                    next_btn = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
                    )
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_btn)
                    time.sleep(1)
                    next_btn.click()
                except TimeoutException:
                    print(f"{card_title} topilmadi.")
                    break

    def extract_and_save_data(self):
        try:
            header = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//section//header//h3"))
            ).text

            date = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//section//header//div[contains(@class, 'date')]"))
            ).text

            img = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//section//img"))
            ).get_attribute("src")

            desc = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//section//div[contains(@class,'description')]"))
            ).text

            self.cursor.execute("""
                INSERT INTO projects (header, date, image, description)
                VALUES (%s, %s, %s, %s)
            """, (header, date, img, desc))
            self.conn.commit()

            print("Ma'lumotlar muvaffaqiyatli saqlandi.")
        except Exception as e:
            print("Extract va saqlash jarayonida xatolik:", e)

    def cleanup(self):
        self.cursor.close()
        self.conn.close()
        self.driver.quit()


if __name__ == "__main__":
    scraper = JobPortalScraper()
    try:
        scraper.open_site()
        scraper.go_to_projects_page()
        scraper.find_and_process_card("Job Portal System")
    except Exception as e:
        print("Xatolik yuz berdi:", e)
    finally:
        scraper.cleanup()
