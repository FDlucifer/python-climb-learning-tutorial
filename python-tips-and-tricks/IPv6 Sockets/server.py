import socket

# print(socket.getaddrinfo(socket.gethostbyname(), 9999, socket.AF_INET6)[0][4][0])

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server.bind(("::1", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send("hello from server!")