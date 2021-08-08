# python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 55555))
s.listen()

while True:
    client, address = s.accept()
    print("connected to {}".format(address))
    client.send("you are connected!".encode())
    client.close()