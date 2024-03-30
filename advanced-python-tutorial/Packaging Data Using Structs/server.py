import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

client, addr = server.accept()
data = client.recv(1024)

first, last, age, gender, occupation, weight = struct.unpack("10s 10s i s 15s f", data)

print(first.decode().rstrip("\x00"))
print(last.decode().rstrip("\x00"))
print(age)
print(gender.decode().rstrip("\x00"))
print(occupation.decode().rstrip("\x00"))
print(round(weight, 2))