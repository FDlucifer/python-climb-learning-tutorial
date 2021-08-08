import threading

def hello():
    for x in range(50):
        print("hello!!!")

t1 = threading.Thread(target=hello)
t1.start()

t1.join()

print ("another text")