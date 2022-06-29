import pprint
from functions.functions import *
from abc import ABC, abstractmethod

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
