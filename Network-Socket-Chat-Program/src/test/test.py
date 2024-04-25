import socket
import unittest
from src.main.server import create_socket
from src.main.server import Server


class MyTestCase(unittest.TestCase):
    def test_accept_connections(self):
        expected = b'Connection Confirmed'
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.connect(("localhost", 10000))

        test_socket.sendall('Hello World!'.encode('UTF-8'))
        actual = test_socket.recv(4096)
        self.assertEquals(expected, actual)
        test_socket.close()


if __name__ == '__main__':
    unittest.main()
