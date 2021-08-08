import threading
import time

path = "D:\\1.program\\python\\python2\\neuralnine-practise\\intermediate\\5\\text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()