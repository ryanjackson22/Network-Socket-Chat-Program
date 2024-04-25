import socket

class Connection:
    def __init__(self, username: str,  write_socket: socket.socket):
        self.username = username
        self.write_socket = write_socket
