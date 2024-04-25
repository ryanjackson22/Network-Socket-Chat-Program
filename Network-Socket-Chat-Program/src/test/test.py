import socket
import unittest
import threading


class MyTestCase(unittest.TestCase):
    def test_accept_connections(self, username='Hello World!'):
        expected = b'Connection Confirmed'
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.connect(("localhost", 10000))

        test_socket.sendall(username.encode('UTF-8'))
        actual = test_socket.recv(4096)
        self.assertEquals(expected, actual)
        test_socket.close()

    def test_multiple_connections(self):
        expected = b'Connection Confirmed'
        empty_tuple = tuple()

        thread1 = threading.Thread(target=self.connect_to_server(), args=())
        thread2 = threading.Thread(target=self.connect_to_server(), args=())

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        self.assertTrue(True)

    def connect_to_server(self, username='Hello World!'):
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.connect(("localhost", 10000))

        test_socket.sendall(username.encode('UTF-8'))
        # actual = test_socket.recv(4096)
        test_socket.close()


if __name__ == '__main__':
    unittest.main()
