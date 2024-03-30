import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("6.tcp.ngrok.io", 15933))

print(client.recv(1024).decode())
client.send("Hey Server".encode())