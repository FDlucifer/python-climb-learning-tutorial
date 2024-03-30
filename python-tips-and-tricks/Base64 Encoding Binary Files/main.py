import base64

my_text = "fdvoid0"

my_text = my_text.encode("ascii")
my_text_b64 = base64.b64encode(my_text)

print(my_text_b64)
print(base64.b64decode(my_text_b64))

with open("image.jpg", "rb") as f:
    data = f.read()

print(base64.b64encode(data))
