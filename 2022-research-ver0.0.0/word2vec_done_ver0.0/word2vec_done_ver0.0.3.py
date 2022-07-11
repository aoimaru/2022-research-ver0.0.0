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
# training_data = SampleDataVer001.get(run=1)
training_data = W2VFunction.get_test_gold_data_filter_run()
gold_cases = TestData.get(source="gold", run=1)
gold_cases = SampleDataVer001.get(run=1)
model = BaseW2V.load(sg=1, size=100, min_count=10, window=5, name="gold", run=1)

def _test_0():
    print()
    test_cases = training_data[23]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[24]
    for test_case in test_cases:
        print(test_case)

    print()
    test_cases = training_data[25]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[26]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[27]
    for test_case in test_cases:
        print(test_case)

    print()
    test_cases = training_data[28]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[29]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[30]
    for test_case in test_cases:
        print(test_case)

    print()
    test_cases = training_data[31]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[32]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[33]
    for test_case in test_cases:
        print(test_case)
    
    print()
    test_cases = training_data[34]
    for test_case in test_cases:
        print(test_case)
    


def _test_1():
    test_case = training_data[11]
    test_case = [['SC-SET', 'SC-SET-F-E'],
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
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:IMAGEMAGICK'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBBZ2-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBC6-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBCURL4-OPENSSL-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBDB-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBEVENT-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBFFI-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBGDBM-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBGEOIP-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBGLIB2.0-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBGMP-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBJPEG-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBKRB5-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBLZMA-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBMAGICKCORE-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBMAGICKWAND-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBNCURSES5-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBNCURSESW5-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBPNG-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBPQ-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBREADLINE-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBSQLITE3-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBSSL-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBTOOL'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBWEBP-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBXML2-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBXSLT-DEV'],
                ['SC-APT-GET-INSTALL',
                'SC-APT-GET-PACKAGES',
                'SC-APT-GET-PACKAGE:LIBYAML-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:MAKE'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:PATCH'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:UNZIP'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:XZ-UTILS'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:ZLIB1G-DEV'],
                ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE'],
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
                'ABS-GLOB-STAR']]

    print("test_case")
    pprint.pprint(test_case)
    test_case_vector_obj = Vector(contexts=test_case, model=model, size=100)
    test_case_vector = test_case_vector_obj.vector
    count = 0
    for gold_case in gold_cases:
        gold_case_vector_obj = Vector(contexts=gold_case, model=model, size=100)
        gold_case_vector = gold_case_vector_obj.vector
        try:
            result = dot(test_case_vector, gold_case_vector)/(norm(test_case_vector)*norm(gold_case_vector))
        except Exception as e:
            pritn(e)
        else:
            if result > 0.8:
                # print("result:", result)
                # pprint.pprint(gold_case)
                flag_0 = 0
                flag_1 = 0
                flag_2 = 0
                flag_3 = 0
                for comp in gold_case:
                    if 'SC-APT-GET-INSTALL' in comp:
                        flag_0 = 1
                    if 'SC-RM' in comp:
                        flag_1 = 1
                    if 'SC-APT-GET-UPDATE' in comp:
                        flag_2 = 1
                    if 'SC-APT-GET-F-YES' in comp:
                        flag_3 = 1
                if flag_0==1 and flag_1==1 and flag_2==1 and flag_3==1:
                    pprint.pprint(gold_case)
                    count += 1
    print(count)
                # diff_vector = gold_case_vector-test_case_vector
                # pprint.pprint(diff_vector)
                # pprint.pprint(model.wv["SC-APT-GET-UPDATE"])
                # try:
                #     result = dot(diff_vector, model.wv["SC-APT-GET-UPDATE"])/(norm(diff_vector)*norm(model.wv["SC-APT-GET-UPDATE"]))
                # except Exception as e:
                #     print(e)
                # else:
                #     print("diff_result:", result)

def _test_2():
    test_case = training_data[11]
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
                print("result:", result)
                # pprint.pprint(gold_case)

def _test_3():
    count = 0
    for gold_case in gold_cases:
        print()
        print()
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        for comp in gold_case:
            if 'SC-APT-GET-INSTALL' in comp:
                flag_0 = 1
            if 'SC-RM' in comp:
                flag_1 = 1
            if 'SC-APT-GET-UPDATE' in comp:
                flag_2 = 1
            if 'SC-APT-GET-F-YES' in comp:
                flag_3 = 1
        if flag_0==1 and flag_1==1 and flag_2==1 and flag_3==1:
            pprint.pprint(gold_case)
            count += 1
    print(count)
        

def _test_4():
    for test_cases in training_data:
        flag = 0
        for test_case in test_cases:
            if 'SC-GPG' in test_case:
                flag = 1
        if flag == 1:
            print()
            for test_case in test_cases:
                print(test_case)

def main():    
    _test_4()



if __name__ == "__main__":
    main()