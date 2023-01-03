import dis

def hello_world():
    msg = "hello world!"
    return msg

print(dis.dis(hello_world))

def add1(x,y):
    return x + y

print(dis.dis(add1))

def list_fct1():
    results = []
    for x in range(10):
        results.append(x)
    return results

print(dis.dis(list_fct1))

def list_fct2():
    return [x for x in range(10)]

print(dis.dis(list_fct2))

def comp_floats():
    return 0.1 + 0.2 == 0.3

dis.dis(comp_floats)

def fct(x):
    if x == 5:
        return True
    else:
        return False

dis.dis(fct)

def myfct():
    for x in range(20000000):
        y = x ** 2

dis.dis(myfct)

