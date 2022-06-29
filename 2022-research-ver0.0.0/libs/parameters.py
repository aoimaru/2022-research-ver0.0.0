import json
import itertools

from abc import ABC, abstractmethod

from libs.configs import Config

PARAMETER_PATH = Config.ROOT_PATH+"/data/parameters/"

class Parameter(object):
    @staticmethod
    def get(file_name, version):
        file_path = PARAMETER_PATH+file_name
        with open(file_path, mode="r") as f:
            data = json.load(f)
        params = data[version]
        products = [cnt for cnt in itertools.product(*params.values())]
        parameters = [dict(zip(params.keys(), cnt)) for cnt in products]
        return parameters


