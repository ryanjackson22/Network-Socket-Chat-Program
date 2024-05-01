import socket


class Connection:
    def __init__(self, username: str, connection_socket: socket):
        self.username = username
        self.connection_socket = connection_socket
