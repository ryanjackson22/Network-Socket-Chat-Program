import socket
import unittest
from src.main.server import create_socket
from src.main.server import Server


class MyTestCase(unittest.TestCase):
    def test_accept_connections(self):
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.connect(("localhost", 10000))

        test_socket.sendall('Hello World!'.encode('UTF-8'))
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
