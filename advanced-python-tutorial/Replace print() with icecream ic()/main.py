# pip install icecream

from icecream import ic


def add(x, y):
    return x + y


ic(add(10, 20))
ic(add(40, 20))
ic(add(30, 70))
ic(add(10, 60))
ic(add(10, 10))
ic(add(20, 20))

data = {"data": [1, 2, 3, 4, 5], "labels": ["a", "b", "c", "d", "e"]}

print(data["data"][2])
ic(data["data"][2])

def myfunction(value):
    if value % 2 == 0:
        ic()
        return True
    else:
        return False

ic.disable()
print(myfunction(10))
ic.enable()
ic(myfunction(10))

def output_to_file(text):
    with open('debug_log.txt', 'a') as f:
        f.write(text + '\n')

ic.configureOutput(prefix='Debug| ', outputFunction=output_to_file, includeContext=True)

ic(add(40, 20))
