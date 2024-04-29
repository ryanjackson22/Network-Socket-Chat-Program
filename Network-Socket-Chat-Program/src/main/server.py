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
            print(1)
            try:
                client_connection, client_address = self.recv_socket.accept()
                client_data = client_connection.recv(4096).decode('UTF-8')

                if not is_data_valid(client_data):
                    client_connection.sendall(b'Invalid Command')
                    continue

                client_username = client_data[:client_data.find('-') - 1]
                client_message_type = client_data[client_data.find('-') + 1:]
                client_message_contents = client_data[:client_data.find('-') + 1]

                if client_message_type == 'h':  # server commands
                    continue
                if client_message_type == 'p':  # private message
                    continue
                if client_message_type == 'a':  # message to all connections
                    continue
                if client_message_type == 's':  # start connection
                    self.new_connection(client_connection, client_username)
                if client_message_type == 'e':  # end connection
                    continue

            except ConnectionAbortedError:
                break

    def new_connection(self, client_connection, username):
        self.add_connection(username, client_connection)
        self.print_active_connections()
        client_connection.sendall(b'Connection Confirmed')
        while True:
            data = client_connection.recv(4096).decode('UTF-8')
            print(data)
            if not data:
                break
            client_connection.sendall(data.encode('UTF-8'))

    def add_connection(self, username: str, client_socket: socket.socket) -> None:
        self.active_connections.append(Connection(username, client_socket))

    def remove_connection(self):
        pass

    def print_active_connections(self):
        print('Active Connections:')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for connection in self.active_connections:
            print(f'Username: {connection.username}')
            print(f'Connected to: {connection.write_socket}')
            print()


def create_socket(host: str, port: int) -> socket:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((host, port))
    return new_socket


def is_data_valid(client_data: str) -> bool:
    if is_message_type_not_found(client_data):
        return False

    if not client_data[0].isalnum():
        return False

    return True


def is_message_type_not_found(client_data) -> bool:
    return client_data.find('-') == -1


if __name__ == '__main__':
    server = Server("localhost", 10000)
    server.accept_connections()
