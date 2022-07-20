import argparse
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

from libs.evaluations import *

def do(args, target):    
    test_obj = TestCase.get("{target}.json".format(target=target))
    # ここはパッチっぽい
    sample_cases = SampleDataVer001.get(run=args.sample)
    num_of_true = Evaluation.count_true(requires=test_obj["requires"], cases=sample_cases)
    # pprint.pprint(test_obj)
    parameters = Parameter.get("word2vec_done_ver0.1.0.json", args.version)
    for parameter in parameters:
        print(parameter)
        try:
            model = BaseW2V.load(
                sg=parameter["sg"], 
                size=parameter["size"], 
                min_count=parameter["min_count"], 
                window=parameter["window"], 
                name=parameter["source"], 
                run=parameter["run"]
            )
        except Exception as e:
            print(e)
            # print(e)
            continue
        else:
            print("OK")
            limits = [
                0.9, 0.85, 0.8, 0.75
            ]
            evaluations = list()
            # for limit in limits:
            #     print("limit:", limit)
            Evaluation.get_similar_objs(
                requires=test_obj["requires"], 
                model=model,
                sample_cases=sample_cases,
                test_cases=test_obj["cases"],
                num_of_true=num_of_true,
                limit=0.9,
                size=parameter["size"]
            )
                



def main(args):
    # do(args, target="APT-GET_INSTALL_ver0.0.0")
    # do(args, target="APT-GET_INSTALL_ver0.1.0")
    # do(args, target="GPG_KEY_ver0.0.0")
    # do(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0")
    # do(args, target="APT-GET_INSTALL_ver0.1.1")
    # do(args, target="APT-GET_INSTALL_ver0.2.0")
    # do(args, target="APT-GET_INSTALL_ver0.3.0")
    # do(args, target="APT-GET_INSTALL_ver0.4.0")
    do(args, target="APT-GET_INSTALL_ver0.0.0")
    # do(args, target="APT-GET_INSTALL_ver0.3.1")
    # do(args, target="APT-GET_INSTALL_ver0.4.1")
    # do(args, target="APT-GET_INSTALL_ver0.5.1")
    # done()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vecで学習させる際のパラメータを指定")
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    parser.add_argument("--sample", help="サンプルRUNのみかそれ以外も含むかを指定", type=int, default=1)
    args = parser.parse_args() 
    main(args)