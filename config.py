import os
import json


class Config(object):
    __data = {}

    @staticmethod
    def autodetect():
        path = os.environ.get(key='STATIC_SERVER_CONFIG_PATH', default='config.json')
        config = Config()
        config.read(path)
        config.__autocomplete()

        return config

    @property
    def host(self) -> str:
        return self.__data['host']

    @property
    def port(self) -> int:
        return self.__data['port']

    @property
    def cpu_limit(self) -> int:
        return self.__data['cpu-limit']

    def read(self, path: str):
        with open(path, 'r') as file:
            self.__data = json.load(file)

    def __autocomplete(self):
        self.__complete(key='cpu-limit', default=2)
        self.__complete(key='host', default='0.0.0.0')
        self.__complete(key='port', default=5000)

    def __complete(self, key: str, default):
        if not key in self.__data:
            self.__data[key] = default
