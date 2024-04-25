"""Docstring goes here."""

import socket
import threading

class Client:
    """docstring for Client"""
    def __init__(self):
        # recv socket
        self.recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recv_socket.listen(20)
        # send socket
        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_socket.connect(("localhost", 10000))

        send_thread = threading.Thread(target=self.send_message(), args=())
        send_thread.start()

        recv_thread = threading.Thread(target=self.recv_message(), args=())
        recv_thread.start()

    def recv_message(self):
        server_connection, server_address = self.recv_socket.accept()
        while True:
            data = server_connection.recv(4096)
            print(data.decode('utf-8'))

    def send_message(self):
        while True:
            message = input("<username> (-option) message")
            self.send_socket.sendall(message.encode('UTF-8'))


if __name__ == '__main__':
    client = Client()