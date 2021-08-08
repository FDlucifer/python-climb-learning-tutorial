class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed!")

p = Person("Mike", 25)