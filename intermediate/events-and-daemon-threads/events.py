import threading

event = threading.Event()

def myfunction():
    print ("waiting for event to trigger...\n")
    event.wait()
    print ("performing action evil now...")

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("do you want to trigger the event? (y/n)\n")
if x == "y":
    event.set()