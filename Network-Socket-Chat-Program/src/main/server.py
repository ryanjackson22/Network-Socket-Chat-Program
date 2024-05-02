"""Docstring goes here. """

import socket
import threading
from src.main.connection import Connection

active_connections = []


class Server:
    """docstring for Server"""
    def __init__(self):
        reading_socket = create_tcp_socket(('localhost', 5000))
        writing_socket = create_tcp_socket(('localhost', 10000))

        reading_thread = threading.Thread(target=self.accept_connections, args=(reading_socket,))
        writing_thread = threading.Thread(target=self.wait_for_start_message, args=(writing_socket,))

        reading_thread.start()
        writing_thread.start()

    def accept_connections(self, reading_socket: socket):
        reading_socket.listen(20)
        while True:
            client_socket, address = reading_socket.accept()
            client_connection = threading.Thread(target=self.communication_handler, args=(client_socket,))
            client_connection.start()

    def communication_handler(self, client_socket: socket):
        while True:
            client_message = client_socket.recv(4096).decode('utf-8')
            if not client_message:
                break
            sender_username = client_message.split()[0]

            if is_exit(client_message):
                for active_connection in active_connections:
                    active_connection.connection_socket.sendall(f'{sender_username} has disconnected.'.encode('utf-8'))

                for active_connection in active_connections:
                    if active_connection.username == sender_username:
                        active_connections.remove(active_connection)

            if is_broadcast(client_message):
                for active_connection in active_connections:
                    active_connection.connection_socket.sendall(f'{sender_username} -> all: {client_message.split(" ", 3)[3]}'.encode('utf-8'))

            if is_private(client_message):
                receiver_username = client_message.split()[2]
                for active_connection in active_connections:
                    if active_connection.username == receiver_username:
                        active_connection.connection_socket.sendall(f'{sender_username} -> {receiver_username}: '
                                                                    f'{client_message.split(" ", 3)[3]}'.encode('utf-8'))

    def wait_for_start_message(self, writing_socket: socket):
        writing_socket.listen(20)
        while True:
            connection_socket, address = writing_socket.accept()
            client_message = connection_socket.recv(4096).decode('utf-8')
            username = client_message.split()[0]
            if not client_message:
                continue

            active_connections.append(Connection(username, connection_socket))
            for active_connection in active_connections:
                active_connection.connection_socket.sendall(f'{username} has joined.'.encode('utf-8'))


def is_exit(data: str):
    return data.__contains__('EXIT')


def is_broadcast(data: str):
    return data.__contains__('ALL')


def is_private(data: str):
    return data.__contains__('PRIVATE')


def print_active_connections():
    print('ACTIVE CONNECTIONS:')
    print('~ ' * 10)
    for connection in active_connections:
        print(f'username: {connection.username}')
        print(f'connection: {connection.connection_socket}')
        print()


def create_tcp_socket(socket_address: tuple) -> socket.socket:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # handles sending messages
    new_socket.bind(socket_address)
    return new_socket


if __name__ == '__main__':
    server = Server()
