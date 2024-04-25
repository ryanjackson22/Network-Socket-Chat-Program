"""Docstring goes here. """

import socket
from src.main.connection import Connection


class Server:
    """docstring for Server"""
    def __init__(self, host: str, port: int):
        self.active_connections = []
        self.recv_socket = create_socket(host, port)
        self.recv_socket.listen(20)
        self.send_socket = create_socket(host, port + 1)

    def accept_connections(self):
        while True:
            try:
                client_connection, client_address = self.recv_socket.accept()
                username = client_connection.recv(4096)
                self.add_connection(username, client_connection)
                print(f'Connected to {username}')
                # client_connection.sendall(b'Connection Confirmed')

            except ConnectionAbortedError:
                break

    def add_connection(self, username: str, client_socket: socket.socket) -> None:
        self.active_connections.append(Connection(username, client_socket))

    def remove_connection(self):
        pass


def create_socket(host: str, port: int) -> socket:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((host, port))
    return new_socket


if __name__ == '__main__':
    server = Server("localhost", 10000)
    server.accept_connections()
