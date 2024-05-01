"""Docstring goes here. """

import socket
import threading

active_connections = []


class Server:
    """docstring for Server"""
    def __init__(self, host: str, port: int):
        # One for client sending threads to communicate with (the "reading" socket)
        self.reading_socket = create_socket(host, port)
        # one for client receiving threads to connect to (the "writing" socket)
        self.writing_socket = create_socket(host, port + 1)

        # These sockets will be passed to their own individual threads, which should operate as follows:
        reading_thread = threading.Thread(target=self.accept_connections(self.reading_socket), args=())
        reading_thread.start()

        writing_thread = threading.Thread(target=self.wait_for_start_message(), args=())
        writing_thread.start()

    def accept_connections(self, reading_socket):
        reading_socket.listen(20)
        while True:
            client_socket, address = reading_socket.accept()
            client_connection = threading.Thread(target=self.communication_handler(client_socket), args=())
            client_connection.start()

    def communication_handler(self, client_socket: socket):
        while True:
            data = client_socket.recv(4096)
            if not data:
                continue
            if is_exit(data):
                pass
            if is_broadcast(data):
                pass
            if is_private(data):
                pass

    def wait_for_start_message(self):
        while True:
            message = self.reading_socket.recv(4096).decode('ascii')
            if not message:
                continue
            active_connections.append(self.reading_socket)


def create_socket(host: str, port: int) -> socket:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((host, port))
    return new_socket


def is_exit(data:str):
    return data.__contains__('EXIT')


def is_broadcast(data):
    return data.__contains__('ALL')


def is_private(data):
    pass


if __name__ == '__main__':
    server = Server("localhost", 10000)
