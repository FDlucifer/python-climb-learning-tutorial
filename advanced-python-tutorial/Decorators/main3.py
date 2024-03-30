def mydecorator(function):

    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("i am decorating your function!")
        return return_value

    return wrapper

@mydecorator
def hello(person):
    print(f"Hello {person}")
    return f"Hello {person}!"

print(hello("Mike"))