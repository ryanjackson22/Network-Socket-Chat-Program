"""Docstring goes here."""

import socket
import threading


class Client:
    """docstring for Client"""
    def __init__(self):
        # Todo The client should first start by letting the user pick a screen name for their client,
        #  apply restrictions as needed

        # todo The client should next create two sockets,
        #  one to handle sending messages
        #  another to handle receiving messages

        # todo These sockets should be passed to their own threads to handle communication between the client and server
        # todo sending_thread:
        #  This should listen for user input and decide how to send that input to the server

        # todo Receiving Thread: This thread should do two things:
        #  1. It should start by sending a START message to the server
        #  (this should allow your server to collect the screen name
        #  and socket data it needs to send messages to this client).
        #  2. It should then sit in a loop waiting for messages from the server.
        #  When it receives one, it should print it to the console.
        #  This message should include:
        #  + the screen name of the sender when printed,
        #  + indication as to whether the message was private or not.

        # recv socket
        self.recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recv_socket.listen(20)
        # send socket
        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_socket.connect(("localhost", 10000))

        send_thread = threading.Thread(target=self.send_message(), args=())
        send_thread.start()
        server_connection, server_address = self.recv_socket.accept()
        recv_thread = threading.Thread(target=self.recv_message(server_connection), args=())
        recv_thread.start()

    def recv_message(self, server_connection):
        while True:
            data = server_connection.recv(4096)
            print(data.decode('utf-8'))

    def send_message(self):
        while True:
            message = input("<username> (-option) message")
            self.send_socket.sendall(message.encode('UTF-8'))


if __name__ == '__main__':
    client = Client()