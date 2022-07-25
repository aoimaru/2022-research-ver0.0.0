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

def do(args, target, top=20):    
    test_obj = TestCase.get("{target}.json".format(target=target))
    # ここはパッチっぽい
    sample_cases = SampleDataVer000._patch_get_v2(run=args.sample)
    num_of_true = Evaluation.count_true(requires=test_obj["requires"], cases=sample_cases)
    # pprint.pprint(test_obj)
    try:
        model = BaseW2V.load(
            sg=1, 
            size=100, 
            min_count=10, 
            window=5, 
            name="gold", 
            run=1
        )
    except Exception as e:
        print(e)
    else:
        print("OK")
        limits = [
            0.9, 0.85, 0.8, 0.75, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1
        ]
        results = dict()
        results = Evaluation.get_similar_objs_v2(
            requires=test_obj["requires"], 
            model=model,
            sample_cases=sample_cases,
            test_cases=test_obj["cases"],
            num_of_true=num_of_true,
            limit=0.8,
            size=100
        )

        results = sorted(results.items(), reverse=True)
        for result in results[:top]:
            print(result[1])
            pprint.pprint(SampleDataVer000._patch_get_original_v2(result[0]))
                


def main(args):
    # do(args, target="APT-GET_INSTALL_ver0.0.0", top=10)
    do(args, target="APT-GET_INSTALL_ver0.6.3", top=20)
    # do(args, target="GPG_KEY_ver0.0.0")
    do(args, target="GPG_KEY_ver0.0.1", top=20)
    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=20)
    # do(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0")
    # do(args, target="APT-GET_INSTALL_ver0.1.1")
    # do(args, target="APT-GET_INSTALL_ver0.2.0")
    # do(args, target="APT-GET_INSTALL_ver0.3.0")
    # do(args, target="APT-GET_INSTALL_ver0.4.0")
    # do(args, target="APT-GET_INSTALL_ver0.0.0")
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