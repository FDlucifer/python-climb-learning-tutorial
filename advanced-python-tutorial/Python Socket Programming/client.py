import socket

HOST = '192.168.1.107'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("fuck world!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))