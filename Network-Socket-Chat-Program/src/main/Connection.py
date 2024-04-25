import server


class Connection:
    def __init__(self, read_socket, write_socket, username):
        self.username = username
        self.read_socket = read_socket
        self.write_socket = write_socket
