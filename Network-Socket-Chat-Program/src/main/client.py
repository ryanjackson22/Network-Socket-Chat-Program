"""Client connection to network chat server."""

import socket
import threading


def is_username_invalid(username: str) -> bool:
    """Check if username is invalid.
    param username: str username to check.
    """
    if not username:
        return True

    return False


class Client:
    """Client connection, creates and runs threads that handle sending and receiving."""
    def __init__(self) -> None:
        self.username = set_username()

        writing_socket = create_tcp_socket(('localhost', 5000))
        reading_socket = create_tcp_socket(('localhost', 10000))

        listen_thread = threading.Thread(target=self.listen_user_input, args=(writing_socket,))
        receiving_thread = threading.Thread(target=self.receiving_thread_handler, args=(reading_socket,))

        listen_thread.start()
        receiving_thread.start()

    def receiving_thread_handler(self, receiving_socket: socket) -> None:
        """Called by thread to send start message and handle additional ones.
        param receiving_socket: socket to receive data from server.
        """
        self.send_start_message(receiving_socket)
        self.wait_for_server_message(receiving_socket)

    def send_start_message(self, sending_socket: socket) -> None:
        """Sends a start message to initialize the connection.
        param sending_socket: socket to send data to the server.
        """
        sending_socket.sendall(f"{self.username} START".encode('utf-8'))

    def wait_for_server_message(self, receiving_socket: socket) -> None:
        """Wait for server to send data and print to client's console.
        param receiving_socket: socket to receive data from server.
        """
        print("Waiting for server message...")
        while True:
            server_message = receiving_socket.recv(4096).decode('utf-8')
            if not server_message:
                return
            print(f'{server_message}')

    def listen_user_input(self, sending_socket: socket) -> None:
        """Listens for user input via console, determines how to send to server.
        param sending_socket: socket to send data to the server.
        """
        while True:
            message_to_server = input()
            if message_to_server.__contains__('EXIT'):
                confirmation = input("Are you sure that you want to end session? (Y/n): ")
                if confirmation.lower() in ['y', 'yes']:
                    sending_socket.sendall(f'{self.username} EXITED'.encode('utf-8'))
                    break
            if message_to_server.__contains__('ALL'):
                sending_socket.sendall(f'{self.username} (ALL): {message_to_server}'.encode('utf-8'))
            if message_to_server.__contains__('PRIVATE'):
                sending_socket.sendall(f'{self.username} {message_to_server}'.encode('utf-8'))


def create_tcp_socket(socket_address: tuple) -> socket.socket:
    """Creates TCP using socket_address tuple.
    param socket_address: hostname and port tuple.
    """
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # handles sending messages
    new_socket.connect(socket_address)
    return new_socket


def set_username() -> str:
    """Sets username in loop, external call to verify username.
    """
    username = ""
    while is_username_invalid(username):
        username = input("Enter a Server Username: ")
    return username


if __name__ == '__main__':
    client = Client()
