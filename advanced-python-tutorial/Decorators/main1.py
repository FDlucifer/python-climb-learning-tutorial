def mydecorator(function):

    def wrapper():
        function()
        print("i am decorating your function!")

    return wrapper

@mydecorator
def hello_world():
    print("Hello World!")

hello_world()