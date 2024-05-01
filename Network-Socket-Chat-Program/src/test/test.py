import socket
import unittest
import threading
import src.main.server


class MyTestCase(unittest.TestCase):
    def test_is_exit_false(self):
        expected = False
        actual = src.main.server.is_exit("asdfsaexitasdf")
        self.assertEqual(expected, actual)

    def test_is_exit_true(self):
        expected = True
        actual = src.main.server.is_exit("EXIT asdfsaexitasdf")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
