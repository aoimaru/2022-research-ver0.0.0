import pprint
import sys

from abc import ABC, abstractmethod

from libs.metadatas import MetaData
from libs.files import Ast
from libs.recursives import Recursive

class Function(ABC):
    @staticmethod
    @abstractmethod
    def get_training_gold_data():
        pass
    
    @staticmethod
    @abstractmethod
    def get_training_github_data():
        pass
    
    @staticmethod
    @abstractmethod
    def get_training_gold_data_filter_run():
        pass
    
    @staticmethod
    @abstractmethod
    def get_training_github_data_filter_run():
        pass

    @staticmethod
    @abstractmethod
    def get_test_gold_data():
        pass
    
    @staticmethod
    @abstractmethod
    def get_test_github_data():
        pass
    
    @staticmethod
    @abstractmethod
    def get_test_gold_data_filter_run():
        pass
    
    @staticmethod
    @abstractmethod
    def get_test_github_data_filter_run():
        pass

class W2VFunction(Function):
    @staticmethod
    def get_training_gold_data() -> list:
        file_shas = MetaData.get_gold_path()
        training_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    sequence = Recursive.do(child)
                    for word in sequence:
                        training_data.append(word)
        return training_data
    
    @staticmethod
    def get_training_github_data() -> list:
        file_shas = MetaData.get_github_path()
        training_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    sequence = Recursive.do(child)
                    for word in sequence:
                        training_data.append(word)
        return training_data
    
    @staticmethod
    def get_training_gold_data_filter_run() -> list:
        file_shas = MetaData.get_gold_path()
        training_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    if not child["type"] == "DOCKER-RUN":
                        continue
                    sequence = Recursive.do(child)
                    for word in sequence:
                        training_data.append(word[2:])
        return training_data
    
    @staticmethod
    def get_training_github_data_filter_run() -> list:
        file_shas = MetaData.get_github_path()
        training_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    if not child["type"] == "DOCKER-RUN":
                        continue
                    sequence = Recursive.do(child)
                    for word in sequence:
                        training_data.append(word[2:])
        return training_data
    

    @staticmethod
    def get_test_gold_data() -> list:
        file_shas = MetaData.get_gold_path()
        test_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    sequence = Recursive.do(child)
                    test_data.append(sequence)
        return test_data
    
    @staticmethod
    def get_test_github_data() -> list:
        file_shas = MetaData.get_github_path()
        test_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    sequence = Recursive.do(child)
                    test_data.append(sequence)
        return test_data
    
    @staticmethod
    def get_test_gold_data_filter_run() -> list:
        file_shas = MetaData.get_gold_path()
        test_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    if not child["type"] == "DOCKER-RUN":
                        continue
                    sequence = Recursive.do(child)
                    sequence = [word[2:] for word in sequence]
                    test_data.append(sequence)
        return test_data
    
    @staticmethod
    def get_test_github_data_filter_run() -> list:
        file_shas = MetaData.get_github_path()
        test_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = Ast(file_sha)
            except BaseException as e:
                print(e)
            else:
                for child in ast_obj.children:
                    if not child["type"] == "DOCKER-RUN":
                        continue
                    sequence = Recursive.do(child)
                    sequence = [word[2:] for word in sequence]
                    test_data.append(sequence)
        return test_data