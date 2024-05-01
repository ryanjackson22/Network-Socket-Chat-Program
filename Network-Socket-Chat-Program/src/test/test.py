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

    def test_is_broadcast_false(self):
        expected = False
        actual = src.main.server.is_broadcast("allsaexitasdf")
        self.assertEqual(expected, actual)

    def test_is_broadcast_true(self):
        expected = True
        actual = src.main.server.is_broadcast("ALL asdfsaexitasdf")
        self.assertEqual(expected, actual)

    def test_is_private_false(self):
        expected = False
        actual = src.main.server.is_private("aasdfasfaprivatesaexitasdf")
        self.assertEqual(expected, actual)

    def test_is_private_true(self):
        expected = True
        actual = src.main.server.is_private("PRIVATE asdfsaexitasdf")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
