import socket
import struct

first_name = "John"
last_name = "Smith"
age = 35
gender = "m"
occupation = "Programmer"
weight = 80

data = struct.pack("10s 10s i s 15s f", first_name.encode(), last_name.encode(), age, gender.encode(), occupation.encode(), weight)
print(data)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

client.send(data)
client.close()