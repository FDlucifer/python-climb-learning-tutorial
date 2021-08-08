def mydecorator(function):

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("i am decorating your function!")

    return wrapper

@mydecorator
def hello(person):
    print(f"Hello {person}!")

hello("Mike")