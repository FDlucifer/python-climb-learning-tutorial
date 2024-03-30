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

with open('mike.pickle', 'rb') as f:
    p1 = pickle.load(f)

p1.print_info()