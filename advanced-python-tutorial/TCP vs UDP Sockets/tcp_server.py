import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen()

while True:
    client, address = server.accept()
    print(f"connected to {address}")
    print(client.recv(1024).decode('utf-8'))
    client.send("hello client!".encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.send("bye!".encode('utf-8'))
    client.close()