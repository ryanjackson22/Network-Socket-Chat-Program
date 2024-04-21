"""Docstring goes here. """

import socket


class Server:
    """docstring for Server"""
    def __init__(self: object, host: str, port: int):
        self.recv_socket = create_socket(host, port)
        self.recv_socket.listen(20)
        self.send_socket = create_socket(host, port)

    def accept_connections(self: object):
        pass


def create_socket(host: str, port: int) -> socket:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((host, port))
    return new_socket


if __name__ == '__main__':
    server = Server("localhost", 10000)
    server.accept_connections()
