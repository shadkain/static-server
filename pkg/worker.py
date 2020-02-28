from socket import socket


class Worker(object):
    def __init__(self, sock: socket, root: str):
        self.__sock = sock
        self.__root = root

    def run(self):
        pass