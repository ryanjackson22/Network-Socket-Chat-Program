"""Docstring goes here."""

import socket
import threading


def is_username_invalid(username: str) -> bool:
    if not username:
        return True

    return False


class Client:
    """docstring for Client"""
    def __init__(self, host: str, port: int) -> None:
        # Todo The client should first start by letting the user pick a screen name for their client,
        self.username = set_username()

        writing_socket = self.create_tcp_socket(('localhost', 5000))
        reading_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # handles receiving messages
        reading_socket.connect(('localhost', 10000))

        listen_thread = threading.Thread(target=self.listen_user_input, args=(writing_socket,))
        receiving_thread = threading.Thread(target=self.receiving_thread_handler, args=(reading_socket,))

        listen_thread.start()
        receiving_thread.start()

    def create_tcp_socket(self, socket_address: tuple) -> socket.socket:
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # handles sending messages
        new_socket.connect(socket_address)
        return new_socket

    def receiving_thread_handler(self, receiving_socket: socket) -> None:
        self.send_start_message(receiving_socket)
        self.wait_for_server_message(receiving_socket)

    def send_start_message(self, sending_socket: socket):
        sending_socket.sendall(f"{self.username} START CONNECTION_DETAILS".encode('utf-8'))
        print(f'sent START message to {sending_socket}')

    def wait_for_server_message(self, receiving_socket: socket):
        print("Waiting for server message...")
        while True:
            message = receiving_socket.recv(4096).decode('utf-8')
            print(f'USERNAME (PUBLIC/PRIVATE): {message}')

    def listen_user_input(self, sending_socket: socket):
        while True:
            message_to_server = input("Enter message to: ")
            if message_to_server.__contains__('EXIT'):
                sending_socket.sendall('EXIT'.encode('utf-8'))
                break
            if message_to_server.__contains__('ALL'):
                sending_socket.sendall(f'ALL {message_to_server}'.encode('utf-8'))
            if message_to_server.__contains__('PRIVATE'):
                sending_socket.sendall(f'PRIVATE USERNAME {message_to_server}'.encode('utf-8'))
            print("Message sent to: ", sending_socket)


def set_username() -> str:
    username = ""
    while is_username_invalid(username):
        username = input("Enter a Server Username: ")
    return username


if __name__ == '__main__':
    client = Client("localhost", 10000)
