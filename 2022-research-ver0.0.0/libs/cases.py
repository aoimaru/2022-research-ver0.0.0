import pprint
import json
from functions.functions import *
from abc import ABC, abstractmethod

from libs.configs import Config

"""
    - sampleデータを検証するためのパッチ
"""
from libs.metadatas import MetaData
from libs.files import SampleAST


TEST_CASE_PATH = Config.ROOT_PATH+"/data/test_case/"

class Case(object):
    @staticmethod
    @abstractmethod
    def get():
        pass

class TestCase(Case):
    @staticmethod
    def get(file_name):
        file_path = TEST_CASE_PATH+file_name
        with open(file_path, mode="r") as f:
            data = json.load(f)
        return data



        






