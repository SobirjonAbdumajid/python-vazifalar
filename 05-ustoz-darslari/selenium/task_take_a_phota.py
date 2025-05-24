import time
import codecs
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager


def start_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver


def scrape_smart_homes_post(driver):
    driver.get("https://shaxzodbek.com")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "body"))
        )
        print("Bosh sahifa yuklandi.")
    except TimeoutException:
        print("Bosh sahifa yuklanmadi.")
        return None

    try:
        close_popup = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Close')] | //div[contains(@class, 'popup-close')]"))
        )
        driver.execute_script("arguments[0].click();", close_popup)
        print("Pop-up yopildi.")
    except TimeoutException:
        print("Pop-up topilmadi.")

    try:
        post_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Post"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post_link)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", post_link)
        print("'Post' sahifasiga o'tildi: https://shaxzodbek.com/post")
    except (TimeoutException, ElementClickInterceptedException) as e:
        print(f"'Post' havolasi topilmadi yoki bosilmadi: {e}")
        return None

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "body"))
        )
        print("Postlar sahifasi yuklandi.")
    except TimeoutException:
        print("Postlar sahifasi yuklanmadi.")
        return None

    try:
        cards = WebDriverWait(driver, 15).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//article | //div[contains(@class, 'post') or contains(@class, 'article')]"))
        )
        print(f"{len(cards)} ta post topildi.")
    except TimeoutException:
        print("Postlar ro'yxati topilmadi. Iltimos, to'g'ri selektorni tekshiring.")
        return None

    post_links = []
    for card in cards:
        try:
            link = card.find_element(By.TAG_NAME, "a")
            post_url = link.get_attribute("href")
            if post_url and "/post/" in post_url and post_url not in post_links:
                post_links.append(post_url)
        except:
            continue

    print(f"Topilgan noyob post havolalari: {post_links}")

    for post_url in post_links:
        try:
            driver.get(post_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)
            print(f"Post sahifasiga kirdi: {post_url}")

            try:
                header = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//main/section/div/header/h3 | //h1 | //h2"))
                ).text
                if "The Evolution of Smart Homes" in header:
                    print("The Evolution of Smart Homes topildi.")

                    data = {
                        "title": header,
                        "publish_date": "",
                        "image": "",
                        "text": "",
                        "link": driver.current_url
                    }

                    try:
                        data["publish_date"] = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,
                                                            "//time | //span[contains(@class, 'date') or contains(@class, 'post-date') or contains(text(), '2025')] | //div[contains(@class, 'date')]"))
                        ).text
                    except TimeoutException:
                        print("Publish Date topilmadi, 'Topilmadi' yoziladi.")
                        data["publish_date"] = "Topilmadi"

                    try:
                        data["image"] = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,
                                                            "//main/section/div/div[1]/div[1]/img | //img[contains(@class, 'post-image')]"))
                        ).get_attribute("src")
                    except TimeoutException:
                        print("Image topilmadi, bo'sh qoldirildi.")
                        data["image"] = "Topilmadi"

                    try:
                        data["text"] = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,
                                                            "//main/section/div/div[1]/div[2] | //div[contains(@class, 'content') or contains(@class, 'post-body')]"))
                        ).text
                    except TimeoutException:
                        print("Text topilmadi, bo'sh qoldirildi.")
                        data["text"] = "Topilmadi"

                    filename = "smart_homes_data.txt"
                    output_dir = "output"

                    try:
                        os.makedirs(output_dir, exist_ok=True)
                        filename = os.path.join(output_dir, filename)
                    except Exception as e:
                        print(f"Output papkasi yaratishda xato: {e}")
                        return None

                    # Ma'lumotlarni txt faylga saqlash
                    try:
                        with codecs.open(filename, 'w', encoding='utf-8') as file:
                            file.write(f"Title: {data['title']}\n")
                            file.write(f"Text: {data['text']}\n")
                            file.write(f"Image: {data['image']}\n")
                            file.write(f"Publish Date: {data['publish_date']}\n")
                            file.write(f"Link: {data['link']}\n")
                        print(f"Ma'lumotlar '{filename}' fayliga saqlandi!")
                    except Exception as e:
                        print(f"Faylga saqlashda xato: {e}")
                        return None

                    return data
                else:
                    print(f"Bu post 'The Evolution of Smart Homes' emas: {header}")
            except TimeoutException as e:
                print(f"Post sahifasida ma'lumot topilmadi: {post_url}, Xato: {e}")
        except Exception as e:
            print(f"Post URLiga kirishda xato: {post_url}, Xato: {e}")

        # Postlar sahifasiga qaytish
        driver.get("https://shaxzodbek.com/post")
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)
        except TimeoutException:
            print("Postlar sahifasiga qaytishda xato.")
            return None

    print("The Evolution of Smart Homes postlar sahifasida topilmadi.")
    return None


def main():
    driver = start_browser()

    try:
        data = scrape_smart_homes_post(driver)
        if not data:
            print("Ma'lumot topilmadi.")
    except Exception as e:
        print(f"Umumiy xatolik yuz berdi: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()