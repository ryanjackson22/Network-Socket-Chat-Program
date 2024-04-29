from abc import ABC, abstractmethod


class Message:
    def __init__(self, message_type: str, message_contents: str):
        pass

    @abstractmethod
    def send(self):
        pass


class Private(Message):
    def __init__(self):
        pass

    def send(self):
        pass
