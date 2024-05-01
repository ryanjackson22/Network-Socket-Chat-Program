"""Docstring goes here. """

import socket
import threading

active_connections = []


class Server:
    """docstring for Server"""
    def __init__(self):
        reading_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        reading_socket.bind(('localhost', 5000))

        writing_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        writing_socket.bind(('localhost', 10000))

        reading_thread = threading.Thread(target=self.accept_connections, args=(reading_socket,))
        writing_thread = threading.Thread(target=self.wait_for_start_message, args=(writing_socket,))

        reading_thread.start()
        writing_thread.start()

    def accept_connections(self, reading_socket: socket):
        reading_socket.listen(20)
        while True:
            client_socket, address = reading_socket.accept()
            print(f'Connected to {client_socket}')
            client_connection = threading.Thread(target=self.communication_handler, args=(client_socket,))
            client_connection.start()

    def communication_handler(self, client_socket: socket):
        print(f'Handling Communication for {client_socket}')
        while True:
            try:
                data = client_socket.recv(4096).decode('utf-8')
                if not data:
                    continue
                if is_exit(data):
                    pass
                if is_broadcast(data):
                    print_active_connections()
                    for active_connection in active_connections:
                        active_connection.sendall(f'USERNAME (PUBLIC/PRIVATE): {data}'.encode('utf-8'))
                        print(f'Sent Message to {active_connection}')
                if is_private(data):
                    pass
            except OSError:
                continue

    def wait_for_start_message(self, writing_socket: socket):
        print("Waiting for start message...")
        writing_socket.listen(20)
        connection_socket, address = writing_socket.accept()
        while True:
            message = connection_socket.recv(4096).decode('utf-8')
            if not message:
                continue
            active_connections.append(connection_socket)


# def create_socket(host: str, port: int) -> socket:
#     new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     new_socket.bind((host, port))
#     return new_socket


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
        print(connection)


if __name__ == '__main__':
    server = Server()
