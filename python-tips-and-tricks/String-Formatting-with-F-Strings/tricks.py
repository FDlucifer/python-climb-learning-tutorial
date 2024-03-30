name = "Mike"
age = 24
myfavoritenumber = 19.341453457635673456

print("hello my name is " + name + " and i am " + str(age) + " years old!")
print("hello my name is %s and i am %d years old! My favorite number is %.2f" % (name, age, myfavoritenumber))
print("hello my name is {} and i am {} years old!".format(name, age))
print(f"hello my name is {name} and i am {age if age % 2 == 0 else 7} years old! My favorite number is {myfavoritenumber:.2f}")