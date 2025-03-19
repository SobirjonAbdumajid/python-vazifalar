from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.shaxzodbek.com/")


def tap_nav_links(links, _driver):
    for link in links:
        try:
            element = WebDriverWait(_driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, link))
            )
            actions = ActionChains(_driver)
            actions.move_to_element(element).pause(1).click().perform()
            old_title = _driver.title
            print(f"🌟 Clicked '{link}', refreshed the page! Moved from '{old_title}' to '{_driver.title}' 🎯")
            time.sleep(3)
            _driver.refresh()
            WebDriverWait(_driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            time.sleep(3)
        except Exception as e:
            print(f"Error clicking {link}: {e}")


try:
    tap_nav_links(["fab fa-github", "Projects", "Certifications", "About Me"], driver)
    tap_nav_links(["Home"], driver)
except Exception as e:
    print(f"Script error: {e}")
finally:
    driver.quit()
