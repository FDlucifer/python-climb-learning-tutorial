# pip install dill
import pickle
import dill


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self, years):
        self.age += years

    def __repr__(self):
        return f"{self.name} ({self.age})"


p = Person("mike", 20)
p.get_older(10)

# with open('person.pkl', 'wb') as f:
#     pickle.dump(p, f)

# with open('person.pkl', 'rb') as f:
#     print(pickle.load(f))

with open("person.pkl", "wb") as f:
    dill.dump(p, f)

with open("person.pkl", "rb") as f:
    print(dill.load(f))
