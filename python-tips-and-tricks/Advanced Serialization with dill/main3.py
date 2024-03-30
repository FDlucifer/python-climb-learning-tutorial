import dill
import threading

class MyClass:
    def __init__(self, initial_value):
        self.value = initial_value
        self.lock = threading.Lock()

    def increase(self, by):
        self.lock.acquire()
        self.value += by
        self.lock.release()

    def lock_value(self):
        self.lock.acquire()

    def unlock_value(self):
        self.lock.release()

myobj = MyClass(0)
myobj.increase(20)
myobj.lock_value()

with open("myobject2.pkl", "wb") as f:
    dill.dump(myobj, f)

with open("myobject2.pkl", "rb") as f:
    myobj = dill.load(f)

myobj.unlock_value()
myobj.increase(10)

