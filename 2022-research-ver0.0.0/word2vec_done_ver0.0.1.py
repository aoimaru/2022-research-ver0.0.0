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
test_data = W2VFunction.get_test_gold_data_filter_run()
model = BaseW2V.load(sg=1, size=100, min_count=10, window=5, name="gold", run=1)

def _test_0():
    pass


def _test_1():
    pass




def main():    
    pprint.pprint(training_data[0])
    print()
    pprint.pprint(training_data[1])



if __name__ == "__main__":
    main()