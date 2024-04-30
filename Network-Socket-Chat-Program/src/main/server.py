"""Docstring goes here. """

import socket
from src.main.connection import Connection
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
        reading_thread = threading.Thread(target=self.accept_connections(), args=())

        writing_thread = threading.Thread(target=None, args=())
        # Todo sit in a loop waiting for START messages from client receiving threads.

        # Todo When it receives such a message,
        #  it should add this socket to the above global variable

    def accept_connections(self):
        # TODO This should sit in a loop accepting connections from client sending threads.

        # TODO When a client connection is accepted,
        #  this thread should create a new thread that will handle communication with that particular client

        # TODO Each new thread should accept messages from the accept socket it has been given,
        #  determine what sort of messages they are (BROADCAST? PRIVATE? EXIT?)
        #  choose the appropriate action.
        pass

def create_socket(host: str, port: int) -> socket:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((host, port))
    return new_socket


if __name__ == '__main__':
    server = Server("localhost", 10000)
