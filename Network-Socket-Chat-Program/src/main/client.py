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
        self.username = ""
        while is_username_invalid(self.username):
            self.username = input("Enter a Server Username: ")

        self.sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # handles sending messages
        self.sending_socket.connect((host, port))
        self.receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # handles receiving messages
        self.receiving_socket.connect((host, port))

        # todo These sockets should be passed to their own threads to handle communication between the client and server

        # todo sending_thread:
        #  This should listen for user input and decide how to send that input to the server
        listen_thread = threading.Thread(target=self.listen_user_input(self.sending_socket), args=())
        listen_thread.start()

        # todo Receiving Thread: This thread should do two things:
        receiving_thread = threading.Thread(target=self.receiving_thread_handler(), args=())
        receiving_thread.start()

    def receiving_thread_handler(self):
        self.send_start_message()
        self.wait_for_server_message()

    def send_start_message(self):
        self.sending_socket.sendall(f"{self.username} START CONNECTION_DETAILS".encode('utf-8'))

    def wait_for_server_message(self):
        while True:
            message = self.receiving_socket.recv(4096).decode('utf-8')
            print(f'USERNAME (PUBLIC/PRIVATE): {message}')

    def listen_user_input(self, sending_socket):
        pass


if __name__ == '__main__':
    client = Client("localhost", 10000)
