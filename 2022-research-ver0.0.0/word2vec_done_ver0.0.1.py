import pprint
from libs.parameters import Parameter
from libs.datas import *

import numpy as np
from numpy import dot
from numpy.linalg import norm

from libs.word2vecs import BaseW2V
from libs.vectors import Vector
from functions.functions import *

"""
    - 効率を考えて今回はグローバルに定義
"""
training_data = SampleDataVer001.get(run=1)
gold_cases = W2VFunction.get_test_gold_data_filter_run()
model = BaseW2V.load(sg=1, size=100, min_count=10, window=5, name="gold", run=1)

def _test_0():
    pass


def _test_1():
    test_case = training_data[1]
    print("test_case")
    pprint.pprint(test_case)
    test_case_vector_obj = Vector(contexts=test_case, model=model, size=100)
    test_case_vector = test_case_vector_obj.vector
    for gold_case in gold_cases:
        gold_case_vector_obj = Vector(contexts=gold_case, model=model, size=100)
        gold_case_vector = gold_case_vector_obj.vector
        try:
            result = dot(test_case_vector, gold_case_vector)/(norm(test_case_vector)*norm(gold_case_vector))
        except Exception as e:
            pritn(e)
        else:
            if result > 0.9:
                print("result:", result, ", ", )
                pprint.pprint(gold_case)
                





def main():    
    _test_1()



if __name__ == "__main__":
    main()