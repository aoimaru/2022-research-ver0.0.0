import os
import json

from libs.configs import Config
from libs.exceptions import (
    AstOpenException,
    BaseException
)

AST_GOLD_PATH = Config.ROOT_PATH + "/data/ast/gold/"
AST_GITHUB_PATH = Config.ROOT_PATH + "/data/ast/github/"

AST_GITHUB_VER001_PATH = Config.ROOT_PATH + "/data/ast/github_ver0.0.0/"

class File(object):
    pass


class Ast(File):
    def __init__(self, file_sha):
        file_path = "{}{}.json".format(AST_GITHUB_PATH, file_sha)
        print(file_path)
        try:
            with open(file_path, mode="r") as f:
                data = json.load(f)
        except Exception as e:
            raise AstOpenException("no such file") from e
        else:
            self._children = data
            self._file_sha = file_sha
    
    @property
    def children():
        pass
    @children.getter
    def children(self):
        return self._children

class SampleAST(File):
    def __init__(self, file_sha):
        file_path = "{}{}.json".format(AST_GITHUB_VER001_PATH, file_sha)
        print(file_path)
        try:
            with open(file_path, mode="r") as f:
                data = json.load(f)
        except Exception as e:
            raise AstOpenException("no such file") from e
        else:
            self._children = data
            self._file_sha = file_sha
    
    @property
    def children():
        pass
    @children.getter
    def children(self):
        return self._children


