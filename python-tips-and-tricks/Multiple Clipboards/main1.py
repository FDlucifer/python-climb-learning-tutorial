import win32clipboard
import time
import threading

counter = 0
clips = ['', '', '', '', '']

def process_input():
    while True:
        choice = int(input())
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(clips[choice], win32clipboard.CF_TEXT)
        win32clipboard.CloseClipboard()

t = threading.Thread(target=process_input)
t.start()

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if data not in clips:
        clips[counter] = data
        counter += 1
        counter %= 5
        print(clips)
    time.sleep(0.5)