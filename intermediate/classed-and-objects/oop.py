class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return "name: {}, age: {}, height: {}".format(self.name, self.age, self.height)

    def get_older(years):
        self.age += years

person1 = Person("lucifer11", 12312, 2134123)
print (person1)
person2 = Person("satan", 312312, 4353)
print (person2)
del person2
print (Person.amount)