import os
import json

def autodetect() -> dict:
    path = os.environ.get(key='STATIC_SERVER_CONFIG_PATH', default='config.json')
    data = read(path)
    __autocomplete(data)

    return data

def read(path: str) -> dict:
    with open(path, 'r') as file:
        return json.load(file)

def __autocomplete(data: dict):
    __complete(data, key='cpu-limit', default=2)
    __complete(data, key='host', default='0.0.0.0')
    __complete(data, key='port', default=5000)

def __complete(data: dict, key: str, default):
    if data.get(key) is None: data[key] = default