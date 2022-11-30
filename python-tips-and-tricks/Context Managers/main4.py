import socket
from contextlib import contextmanager

@contextmanager
def server_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    yield s
    s.close()

with server_socket("localhost", 9999) as server:
    client, addr = server.accept()

