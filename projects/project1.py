import pyautogui
import time

message = "salom"
n = 100
print("boshlandi")

count = 5

while(count !=5):
    time.sleep(1)
    count -= 1

print('tugab qoldi')

for i in range(0, int(n)):
    pyautogui.typewrite(message + '\n')