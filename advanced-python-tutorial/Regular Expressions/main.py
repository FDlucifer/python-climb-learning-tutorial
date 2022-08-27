import re

pattern = re.compile("^[a-zA-Z\s]+$")

print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))

