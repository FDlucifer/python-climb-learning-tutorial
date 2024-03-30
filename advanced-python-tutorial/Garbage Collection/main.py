import sys
import gc

a = "hello world"
print(sys.getrefcount(a))

mylist = []
mylist.append(a)
print(sys.getrefcount(a))

gc.get_referents(a)
print(gc.get_threshold())
print(gc.set_threshold(1000, 20, 30))
print(gc.get_threshold())
print(gc.get_count())
