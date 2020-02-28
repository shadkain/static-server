import socket
import multiprocessing
from config import *

def main():
    conf = Config.autodetect()
    socket = open_connection(host=conf.host, port=conf.port)

def open_connection(host: str, port: int) -> socket.socket:
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(512)
    s.setblocking(False)

    print(f'Server running on: {host}:{port}')

    return s

if __name__ == '__main__':
    main()