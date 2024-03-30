print(f"my value is {155.463:09}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

    def __format__(self, format_spec):
        if format_spec == "name":
            return self.name
        elif format_spec == "age":
            return str(self.age)
        elif format_spec == "both":
            return f"{self.name}, {self.age}"
        else:
            return f"name: {self.name}, age: {self.age}"


p = Person("Mike", 30)
print(f"{p:both}")
