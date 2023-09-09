import dill


def outer(x):
    def inner(y):
        return x + y

    return inner


add_20 = outer(20)

with open("myobject1.pkl", "wb") as f:
    dill.dump(add_20, f)

with open("myobject1.pkl", "rb") as f:
    add_20 = dill.load(f)

print(add_20(30))
