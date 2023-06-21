class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Mike", 30)
print(p.name)
print(p.age)

choice = input("whitch attribute do you want to access: ")
print(getattr(p, choice, "Non-existent"))
