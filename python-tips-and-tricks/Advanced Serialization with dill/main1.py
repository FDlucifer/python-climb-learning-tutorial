import dill

mysquare = lambda x: x**2

with open("myobject.pkl", "wb") as f:
    dill.dump(mysquare, f)

with open("myobject.pkl", "rb") as f:
    mysquare = dill.load(f)

print(mysquare(10))
