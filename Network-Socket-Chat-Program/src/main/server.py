"""Docstring goes here. """

import socket


class Server:
    """docstring for Server"""
    def __init__(self, host, port):
        self.recv_socket = create_socket(host, port)
        self.send_socket = create_socket(host, port)
        pass

    def accept_connections(self):
        pass


def create_socket(host: str, port: int) -> socket:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((host, port))
    return new_socket


if __name__ == '__main__':
    server = Server()
    server.accept_connections()
