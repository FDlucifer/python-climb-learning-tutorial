import pickle

class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.weight)
    
    def get_older(self, years):
        self.age += years

p1 = Person('Mike', 25, 89)
p1.print_info()
p1.get_older(6)
p1.print_info()

with open('mike.pickle', 'wb') as f:
    pickle.dump(p1, f)