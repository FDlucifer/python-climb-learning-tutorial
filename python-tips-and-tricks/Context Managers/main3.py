import socket

class ServerSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        return self.server

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.close()

with ServerSocket("localhost", 9999) as server:
    server.accept()

