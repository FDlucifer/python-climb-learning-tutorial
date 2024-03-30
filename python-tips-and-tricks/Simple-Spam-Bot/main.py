import pyautogui
import time

time.sleep(2)

spam_text = "this is a spam!"
for _ in range(20):
    pyautogui.typewrite(spam_text)
    pyautogui.press('enter')
    time.sleep(1)