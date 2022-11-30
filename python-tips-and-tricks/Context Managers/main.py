with open("file.txt", "w") as file:
    file.write("hello world")

print(file.closed)

file = open("file.txt", "w")
file.write("hello world")
print(file.closed)