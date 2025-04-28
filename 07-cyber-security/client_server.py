import socket
from cryptography.fernet import Fernet


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    # Serverdan shifrlash kalitini olish
    key = client.recv(1024)
    cipher = Fernet(key)

    print("Serverga ulandi. Xabar yuborish uchun yozing (chiqish uchun 'exit' yozing):")

    while True:
        # Foydalanuvchi xabarini olish
        message = input("> ")
        if message.lower() == 'exit':
            break

        # Xabarni shifrlash va yuborish
        encrypted_message = cipher.encrypt(message.encode())
        client.send(encrypted_message)

        # Serverdan javob olish
        encrypted_response = client.recv(1024)
        response = cipher.decrypt(encrypted_response).decode()
        print(f"Serverdan javob: {response}")

    client.close()
    print("Ulanish yakunlandi.")


if __name__ == "__main__":
    start_client()
