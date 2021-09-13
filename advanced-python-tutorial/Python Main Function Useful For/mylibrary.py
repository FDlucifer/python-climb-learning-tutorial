def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def hello():
    print("hello world")

def main():
    hello()
    print(add(10,20))
    print(sub(10,20))
    myvalue = 10

print("TEST")
print(__name__)

if __name__ == 'mylibrary':
    print("fucked")
    main()