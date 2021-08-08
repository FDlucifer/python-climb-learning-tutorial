def mydecorator(function):

    def wrapper():
        function()
        print("i am decorating your function!")

    return wrapper

def hello_world():
    print("Hello World!")

mydecorator(hello_world)()