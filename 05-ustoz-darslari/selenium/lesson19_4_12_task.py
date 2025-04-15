# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# # Brauzer sozlamalari
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# wait = WebDriverWait(driver, 30)
#
# # Saytni ochish
# driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")
#
# try:
#     # Popup paydo bo'lishini kutish
#     wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popupModal"]/div/div/div')))
#     print("Popup paydo bo'ldi!")
#
#     # Formani topish
#     name_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[1]/input')
#     email_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[2]/input')
#     phone_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[3]/div/input')
#     download_button = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')
#
#     # Formani to'ldirish
#     name_field.send_keys("Sobirjon")
#     email_field.send_keys("sobirjon@example.com")
#     phone_field.send_keys("998901234567")
#     print("Forma to'ldirildi!")
#
#     # Yuklab olish tugmasini bosish
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')))
#     download_button.click()
#     print("Yuklab olish tugmasi bosildi!")
#
#     # "OK" tugmasini kutish va bosish (agar bo'lsa)
#     try:
#         ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "OK")]')))
#         ok_button.click()
#         driver.get_screenshot_as_file("Sobirjon.png")
#         print("OK tugmasi bosildi!")
#         x_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/button')))
#
#     except:
#         print("OK tugmasi topilmadi yoki paydo bo'lmadi. Davom etamiz...")
#
# except Exception as e:
#     print(f"Xatolik yuz berdi: {e}")
#
# finally:
#     time.sleep(5)
#     driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Browser settings
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

# Open the website
driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")

try:
    # First Form: Popup "Download Brochure in One Click"
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popupModal"]/div/div/div')))
    print("Popup paydo bo'ldi!")

    # Fill the form
    name_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[1]/input')
    email_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[2]/input')
    phone_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[3]/div/input')
    download_button = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')

    name_field.send_keys("Sobirjon")
    email_field.send_keys("sobirjon@example.com")
    phone_field.send_keys("998901234567")
    print("Birinchi forma to'ldirildi!")

    # Click the download button
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')))
    download_button.click()
    print("Yuklab olish tugmasi bosildi!")

    # Take screenshot after filling the first form
    driver.get_screenshot_as_file("Sobirjon_Form1.png")
    print("Birinchi forma uchun screenshot olindi!")

    # Handle SweetAlert2 confirmation popup (if it appears)
    try:
        # Wait for the SweetAlert2 modal to appear
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swal2-container")))
        print("SweetAlert2 confirmation popup paydo bo'ldi!")

        # Find and click the "OK" button in the SweetAlert2 modal
        ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "swal2-confirm")]')))
        ok_button.click()
        print("SweetAlert2 OK tugmasi bosildi!")

        # Wait for the SweetAlert2 modal to disappear
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))
        print("SweetAlert2 yopildi!")

    except Exception as e:
        print(f"SweetAlert2 ni boshqarishda xatolik: {e}. Davom etamiz...")

    # Now click the 'X' button to close the main popup
    x_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/button')))
    x_button.click()
    print("Popup yopildi!")

    # Second Form: "Request a Call" (First instance)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-request-a-call_form-box-gs-anim")))
    print("Ikkinchi forma topildi!")

    # Fill the second form
    name_field_2 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//input)[1]')
    email_field_2 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//input)[2]')
    phone_field_2 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//input)[3]')
    send_button_2 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//button)[1]')

    name_field_2.send_keys("Sobirjon")
    email_field_2.send_keys("sobirjon@example.com")
    phone_field_2.send_keys("998901234567")
    print("Ikkinchi forma to'ldirildi!")

    # Take screenshot after filling the second form
    driver.get_screenshot_as_file("Sobirjon_Form2.png")
    print("Ikkinchi forma uchun screenshot olindi!")

    # Click the send button for the second form
    send_button_2.click()
    print("Ikkinchi forma yuborildi!")

    # Third Form: Another "Request a Call" (Further down)
    # Scroll down to the third form
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the scroll to complete

    wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")])[2]')))
    print("Uchinchi forma topildi!")

    # Fill the third form
    name_field_3 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//input)[4]')
    email_field_3 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//input)[5]')
    phone_field_3 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//input)[6]')
    send_button_3 = driver.find_element(By.XPATH, '(//div[contains(@class, "footer-request-a-call_form-box-gs-anim")]//button)[2]')

    name_field_3.send_keys("Sobirjon")
    email_field_3.send_keys("sobirjon@example.com")
    phone_field_3.send_keys("998901234567")
    print("Uchinchi forma to'ldirildi!")

    # Take screenshot after filling the third form
    driver.get_screenshot_as_file("Sobirjon_Form3.png")
    print("Uchinchi forma uchun screenshot olindi!")

    # Click the send button for the third form
    send_button_3.click()
    print("Uchinchi forma yuborildi!")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

finally:
    time.sleep(5)
    driver.quit()