import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Browser sozlamalari
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

# Veb-sahifani ochish
driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")

try:
    # Birinchi forma: Popup "Download Brochure in One Click"
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popupModal"]/div/div/div')))
    print("Popup paydo bo'ldi!")

    # Formani to'ldirish
    name_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[1]/input')
    email_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[2]/input')
    phone_field = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/div[3]/div/input')
    download_button = driver.find_element(By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')

    name_field.send_keys("Sobirjon")
    email_field.send_keys("sobirjon@example.com")
    phone_field.send_keys("998901234567")
    print("Birinchi forma to'ldirildi!")

    # Yuklab olish tugmasini bosing
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/div/div[1]/form/button')))
    download_button.click()
    print("Yuklab olish tugmasi bosildi!")

    # Birinchi forma uchun skrinshot olish
    driver.get_screenshot_as_file("Sobirjon_Form1.png")
    print("Birinchi forma uchun screenshot olindi!")

    # SweetAlert2 tasdiqlash popup'ini boshqarish (agar paydo bo'lsa)
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swal2-container")))
        print("SweetAlert2 confirmation popup paydo bo'ldi!")
        ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "swal2-confirm")]')))
        ok_button.click()
        print("SweetAlert2 OK tugmasi bosildi!")
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))
        print("SweetAlert2 yopildi!")
    except Exception as e:
        print(f"SweetAlert2 ni boshqarishda xatolik: {e}. Davom etamiz...")

    # Asosiy popup'ni yopish
    x_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/button')))
    x_button.click()
    print("Popup yopildi!")

    # Dinamik kontentni yuklash uchun scroll qilish
    print("Scrolling to load dynamic content...")
    for i in range(500, 5000, 500):  # Sahifaning butun qismini qamrab olish uchun kengaytirildi
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Debug: Scroll'dan keyin sahifa skrinshotini olish
    driver.get_screenshot_as_file("Debug_After_Scroll.png")
    print("Debug screenshot olindi: Debug_After_Scroll.png")

    # Ikkinchi forma (Footer "Request a Call") ni topish va to'ldirish
    try:
        # Aniq tanlovchi yordamida formani topish
        second_form = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//form[contains(@class, "footer-request-a-call__form")] | //h5[contains(text(), "Request a call")]/ancestor::form')
        ))
        driver.execute_script("arguments[0].scrollIntoView(true);", second_form)
        time.sleep(1)

        print("Ikkinchi forma topildi!")

        # Ikkinchi formani to'ldirish
        name_field_2 = second_form.find_element(By.XPATH, './/input[@name="name"]')
        email_field_2 = second_form.find_element(By.XPATH, './/input[@name="email"]')
        phone_field_2 = second_form.find_element(By.XPATH, './/input[@name="phone"]')

        name_field_2.send_keys("Sobirjon")
        email_field_2.send_keys("sobirjon@example.com")
        phone_field_2.send_keys("998901234567")
        print("Ikkinchi forma to'ldirildi!")

        # Ikkinchi forma uchun skrinshot olish
        driver.get_screenshot_as_file("Sobirjon_Form2.png")
        print("Ikkinchi forma uchun screenshot olindi!")

        # Ikkinchi forma uchun yuborish tugmasini bosing
        send_button_2 = second_form.find_element(By.XPATH, './/button[@type="submit"] | .//button[contains(@class, "footer-request-a-call__btn")]')
        send_button_2.click()
        print("Ikkinchi forma yuborildi!")

    except Exception as e:
        print(f"Ikkinchi formani topishda xatolik: {e}")
        driver.get_screenshot_as_file("Debug_Form2_Failure.png")
        print("Debug screenshot olindi: Debug_Form2_Failure.png")

    # Uchinchi forma qidirilmaydi (foydalanuvchi ko'rsatmasi bo'yicha)
    print("Uchinchi forma qidirilmaydi, chunki ikkinchi rasm birinchi bilan bir xil (footer forma).")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

finally:
    time.sleep(5)
    driver.quit()