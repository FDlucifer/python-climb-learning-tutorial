'''
this is my new library

author: fdlucifer
'''

__author__ = "fdlucifer"
__email__ = "mail@mail.mail"
__status__ = "planning"

class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def get_older(self, years):
        self.age += years
        return self.age

p1 = Person(None, None, None)
p1.get_older(12)