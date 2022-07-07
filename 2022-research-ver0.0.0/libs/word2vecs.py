from abc import ABC, abstractmethod
from gensim.models import word2vec

from libs.configs import Config
from libs.exceptions import *

MODEL_PATH = Config.ROOT_PATH + "/data/model"

class W2V(object):
    @staticmethod
    @abstractmethod
    def do():
        pass
    
    @staticmethod
    @abstractmethod
    def load():
        pass


class BaseW2V(W2V):
    @staticmethod
    def do(corpus, sg=1, size=100, min_count=100, window=5, name="github", run=0):
        model_path = "{}/{}/sg-{}.size-{}.min_count-{}.window-{}.run-{}.model".format(MODEL_PATH, name, sg, size, min_count, window, run)
        model = word2vec.Word2Vec(
            corpus,
            sg=sg,
            size=size, 
            min_count=min_count, 
            window=window
        )
        model.save(model_path)
    
    @staticmethod
    def load(sg=1, size=100, min_count=100, window=5, name="github", run=0):
        model_path = "{model_path}/{source}/sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.run-{run}.model".format(
            model_path=MODEL_PATH, 
            source=name, 
            sg=sg, 
            size=size, 
            min_count=min_count, 
            window=window, 
            run=run
        )
        try:
            model = word2vec.Word2Vec.load(model_path)
        except Exception as e:
            print(e)
            raise BaseException from e
        else:
            return model
