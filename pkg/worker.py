import asyncio
from socket import socket

from pkg.config import Config
from pkg.request import Request
from pkg.response import Response
from pkg.responder import Responder


class Worker(object):
    def __init__(self, sock: socket, conf: Config):
        self.__sock = sock
        self.__conf = conf

        self.__resp = Responder(conf)

    def run(self):
        self.__loop = asyncio.get_event_loop()
        self.__loop.run_until_complete(self.__cycle())
        
    async def __cycle(self):
        while True:
            conn, _ = await self.__loop.sock_accept(self.__sock)
            conn.settimeout(10)
            conn.setblocking(False)
            self.__loop.create_task(self.__handle(conn))

    async def __handle(self, conn: socket):
        try:
            raw_request = await self.__loop.sock_recv(conn, 1024)
            req = Request(raw_request.decode('utf-8'))
            res = self.__resp.make_response(req)
            await res.send(self.__loop, conn)
        except:
            pass
        finally:
            conn.close()