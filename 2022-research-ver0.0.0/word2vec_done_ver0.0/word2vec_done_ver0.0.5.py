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

sample_cases = SampleDataVer001.get(run=1)
# sample_cases = TestData.get(source="gold", run=1)
model = BaseW2V.load(sg=1, size=100, min_count=10, window=5, name="github", run=1)


def _test_0(limit=0.9):
    print("limit:", limit)
    words = [
        'SC-APT-GET-INSTALL',
        'SC-APT-GET-F-NO-INSTALL-RECOMMENDS',
        'SC-RM',
        'SC-APT-GET-UPDATE',
        'SC-APT-GET-F-YES',
        'SC-RM-F-RECURSIVE',
        'SC-RM-F-FORCE',
        'SC-APT-GET-PACKAGES'
    ]
    test_case = [
        ['SC-SET', 'SC-SET-F-E'],
        ['SC-SET', 'SC-SET-F-X'],
        ['SC-APT-GET-UPDATE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-YES'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-NO-INSTALL-RECOMMENDS'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:AUTOCONF'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:AUTOMAKE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:BZIP2'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:DPKG-DEV'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:FILE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:GCC'],
        ['SC-RM', 'SC-RM-F-RECURSIVE'],
        ['SC-RM', 'SC-RM-F-FORCE'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-MAYBE-PATH'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-APT-LISTS'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-PATH-VAR'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-PATH-ABSOLUTE'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-GLOB',
        'ABS-GLOB-STAR']
    ]


    test_case_vector_obj = Vector(contexts=test_case, model=model, size=100)
    test_case_vector = test_case_vector_obj.vector
    count_0 = 0
    count_1 = 0
    for sample_case in sample_cases:
        sample_case_vector_obj = Vector(contexts=sample_case, model=model, size=100)
        sample_case_vector = sample_case_vector_obj.vector
        try:
            result = dot(test_case_vector, sample_case_vector)/(norm(test_case_vector)*norm(sample_case_vector))
        except Exception as e:
            # print(e)
            pass
        else:
            if result > limit:
                count_1 += 1
                comps = dict()
                for word in words:
                    comps[word] = 0
                for comp in sample_case:
                    for word in words:
                        if word in comp:
                            comps[word] += 1
                flag = 1
                for check in comps.values():
                    if check <= 0:
                        flag = 0
                if flag == 1:
                    count_0 += 1
    print("count_0:", count_0)
    print("count_1:", count_1)
    recall = count_0/45
    precision = count_0/count_1
    print("recall:", recall)
    print("precision:", precision)
    f_val = (2*recall*precision)/(recall+precision)
    print("f_val:", f_val)
    
                

def _test_1():
    words = [
        'SC-APT-GET-INSTALL',
        'SC-APT-GET-F-NO-INSTALL-RECOMMENDS',
        'SC-RM',
        'SC-APT-GET-UPDATE',
        'SC-APT-GET-F-YES',
        'SC-RM-F-RECURSIVE',
        'SC-RM-F-FORCE',
        'SC-APT-GET-PACKAGES'
    ]
    count = 0
    for sample_case in sample_cases:
        comps = dict()
        for word in words:
            comps[word] = 0
        for comp in sample_case:
            for word in words:
                if word in comp:
                    comps[word] += 1
        flag = 1
        for check in comps.values():
            if check <= 0:
                flag = 0
        if flag == 1:
            count += 1

    print(count)
        



def main():    
    # _test_1()
    """
        _test_1 = 45
        _test_1 = 373
    """
    limits = [
        0.9, 0.85, 0.8, 0.75, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1
    ]
    for limit in limits:
        print()
        _test_0(limit=limit)



if __name__ == "__main__":
    main()