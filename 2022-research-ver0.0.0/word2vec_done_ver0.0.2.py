import pprint
from libs.parameters import Parameter
from libs.datas import *

import numpy as np
from numpy import dot
from numpy.linalg import norm

from libs.word2vecs import BaseW2V
from libs.vectors import Vector
from functions.functions import *
from libs.cases import *

"""
    - 効率を考えて今回はグローバルに定義
"""


    
                


def main():    
    test_obj = TestCase.get("APT-GET_INSTALL_ver0.0.0.json")
    pprint.pprint(test_obj)



if __name__ == "__main__":
    main()