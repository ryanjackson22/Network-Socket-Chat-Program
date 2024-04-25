import socket
import unittest
import threading


class MyTestCase(unittest.TestCase):
    def test_accept_connections(self, username='Hello World! -a'):
        expected = b'Connection Confirmed'
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.connect(("localhost", 10000))

        test_socket.sendall(username.encode('UTF-8'))
        actual = test_socket.recv(4096)
        self.assertEqual(expected, actual)
        test_socket.close()

    def test_connect_to_server(self):
        expected = b'Connection Confirmed'

        thread1 = threading.Thread(target=connect_to_server(username='Thread 1 -b'), args=())
        thread2 = threading.Thread(target=connect_to_server(username='Thread 2 -c'), args=())

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        self.assertTrue(True)

    def test_no_message_type(self, username='Bad Listener'):
        expected = b'Invalid Type'
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.connect(("localhost", 10000))

        test_socket.sendall(username.encode('UTF-8'))
        actual = test_socket.recv(4096)
        self.assertEqual(expected, actual)
        test_socket.close()

def connect_to_server(username='Hello World!'):
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_socket.connect(("localhost", 10000))

    test_socket.sendall(username.encode('UTF-8'))
    actual = test_socket.recv(4096)
    test_socket.close()


if __name__ == '__main__':
    unittest.main()
