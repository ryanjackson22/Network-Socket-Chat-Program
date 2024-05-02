"""Server that manages messages sent between clients."""

import socket
import threading
from src.main.connection import Connection

active_connections = []


class Server:
    """Instance of server class, handles communication between clients"""
    def __init__(self):
        reading_socket = create_tcp_socket(('localhost', 5000))
        writing_socket = create_tcp_socket(('localhost', 10000))

        reading_thread = threading.Thread(target=self.accept_connections, args=(reading_socket,))
        writing_thread = threading.Thread(target=self.wait_for_start_message, args=(writing_socket,))

        reading_thread.start()
        writing_thread.start()

    def accept_connections(self, reading_socket: socket):
        """Accepts connections from clients
        param reading_socket: receives data from client
        """
        reading_socket.listen(20)
        while True:
            client_socket, address = reading_socket.accept()
            client_connection = threading.Thread(target=self.communication_handler, args=(client_socket,))
            client_connection.start()

    def communication_handler(self, client_socket: socket):
        """Handles communication between client and server
        param client_socket: client connection with server"""
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
                    active_connection.connection_socket.sendall(f'{sender_username} -> all: '
                                                                f'{client_message.split(" ", 3)[3]}'.encode('utf-8'))

            if is_private(client_message):
                receiver_username = client_message.split()[2]
                for active_connection in active_connections:
                    if active_connection.username == receiver_username or active_connection.username == sender_username:
                        active_connection.connection_socket.sendall(f'{sender_username} -> {receiver_username}: '
                                                                    f'{client_message.split(" ", 3)[3]}'
                                                                    .encode('utf-8'))

    def wait_for_start_message(self, writing_socket: socket):
        """Waits in a loop until client sends a START message.
        param writing_socket: listens for client messages.
        """
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
    """Checks if the data contains EXIT command
    param data: message from client.
    """
    return data.__contains__('EXIT')


def is_broadcast(data: str):
    """Checks if the data contains ALL command
        param data: message from client.
        """
    return data.__contains__('ALL')


def is_private(data: str):
    """Checks if the data contains PRIVATE command
        param data: message from client.
        """
    return data.__contains__('PRIVATE')


def print_active_connections():
    """Prints all the connections stored in active_connections().
    """
    print('ACTIVE CONNECTIONS:')
    print('~ ' * 10)
    for connection in active_connections:
        print(f'username: {connection.username}')
        print(f'connection: {connection.connection_socket}')
        print()


def create_tcp_socket(socket_address: tuple) -> socket.socket:
    """Creates a TCP and binds it to socket_address."""

    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # handles sending messages
    new_socket.bind(socket_address)
    return new_socket


if __name__ == '__main__':
    server = Server()
