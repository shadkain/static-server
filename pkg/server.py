import socket
from multiprocessing import Process

from pkg.config import Config
from pkg.worker import Worker


class Server(object):
    def __init__(self, config_path: str):
        self.__conf = Config.autodetect(config_path)

    def run(self):
        self.__open_conn()
        self.__spawn_workers()

        print(f'Server is running on: http://{self.__conf.host}:{self.__conf.port}')

    def __open_conn(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.__conf.host, self.__conf.port))
        sock.setblocking(False)
        sock.listen(512)

        self.__sock = sock

    def __spawn_workers(self):
        workers = []

        for i in range(self.__conf.cpu_limit):
            worker = Process(
                target=Worker(
                    sock=self.__sock,
                    root=self.__conf.root
                ).run
            )

            workers.append(worker)
            print(f'{i} worker loaded')
