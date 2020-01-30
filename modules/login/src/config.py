import json


def config():
    with open('/conf/config.json') as config_file:
        return json.load(config_file)
