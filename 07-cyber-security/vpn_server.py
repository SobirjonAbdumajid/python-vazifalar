import json
import socket
import threading
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
def handle_client(client_socket,address):
    print(f"Yang'i ulanish: {address}")
    client_socket.send(key)
    while True:
        try:
            encrypted_data = client_socket.recv(1024)
            if not encrypted_data:
                break
            data = cipher.decrypt(encrypted_data).decode()
            print(f"Mijozdan {address} : {data}")

            response = f"Serverdan javob: {data}"
            encrypted_response = cipher.encrypt(response.encode())
            client_socket.send(encrypted_response)
        except Exception as e:
            print(f"Xatolik: {e}")
            break
        client_socket.close()
        print(f"Mijoz {address} ulanishi uzildi")
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("Server ishga tushdi, mijozlarni kutmoqda...")
    while True:
        client_socket, address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,address))
        client_thread.start()
if __name__ == "__main__":
    start_server()
