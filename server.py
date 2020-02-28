import socket
import multiprocessing

from config import *


class Server(object):
    def __init__(self):
        self.__conf = Config.autodetect()

    def run(self):
        self.__open_conn()

        print(f'Server is running on: http://{self.__conf.host}:{self.__conf.port}')

    def __open_conn(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.__conf.host, self.__conf.port))
        sock.setblocking(False)
        sock.listen(512)

        self.__sock = sock

