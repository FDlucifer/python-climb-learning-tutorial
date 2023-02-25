import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen()

connected_clients = []

def handle_match(c1, c2):
    c1.send("MATCH".encode())
    c2.send("MATCH".encode())

def handle_client(c):
    c.send("enter matching string: ".encode())
    matching_string = client.recv(1024).decode()
    found_match = False
    for i in range(len(connected_clients)):
        if connected_clients[i][1] == matching_string:
            threading.Thread(target=handle_match, args=(c, connected_clients[i][0])).start()
            del connected_clients[i]
            found_match = True
    
    if not found_match:
        connected_clients.append((c, matching_string))

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()

