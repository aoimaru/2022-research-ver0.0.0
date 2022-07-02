import pprint
from functions.functions import *
from abc import ABC, abstractmethod

"""
    - sampleデータを検証するためのパッチ
"""
from libs.metadatas import MetaData
from libs.files import SampleAST

class Data(object):
    @staticmethod
    @abstractmethod
    def get():
        pass

class TrainingData(Data):
    @staticmethod
    def get(source, run):
        if source == "github":
            if run == 1:
                training_data = W2VFunction.get_training_github_data_filter_run()
            else:
                training_data = W2VFunction.get_training_github_data()
        else:
            if run == 1:
                training_data = W2VFunction.get_training_gold_data_filter_run()
            else:
                training_data = W2VFunction.get_training_gold_data()
        return training_data

class TestData(Data):
    @staticmethod
    def get(source, run):
        if source == "github":
            if run == 1:
                test_data = W2VFunction.get_test_github_data_filter_run()
            else:
                test_data = W2VFunction.get_test_github_data()
        else:
            if run == 1:
                test_data = W2VFunction.get_test_gold_data_filter_run()
            else:
                test_data = W2VFunction.get_test_gold_data()
        return test_data


class SampleData(object):
    @staticmethod
    @abstractmethod
    def get():
        pass

class SampleDataVer001(SampleData):
    @staticmethod
    def get(run):
        file_shas = MetaData.get_github_ver001_path()
        sample_data = list()
        for file_sha in file_shas:
            try:
                ast_obj = SampleAST(file_sha)
            except Exception as e:
                print(e)
            else:
                if run == 1:
                    for child in ast_obj.children:
                        if not child["type"] == "DOCKER-RUN":
                            continue
                        sequence = Recursive.do(child)
                        sequence = [word[2:] for word in sequence]
                        sample_data.append(sequence)
                else:
                    for child in ast_obj.children:
                        sequence = Recursive.do(child)
                        sample_data.append(sequence)
                
        return sample_data
        


