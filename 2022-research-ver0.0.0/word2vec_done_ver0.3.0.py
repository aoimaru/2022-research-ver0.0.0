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
from libs.to_csv import *

"""
    - 効率を考えて今回はグローバルに定義
"""

from libs.evaluations import *


def do(args, target, top=20, seed="tmp"):
    test_obj = TestCase.get("{target}.json".format(target=target))
    # ここはパッチっぽい
    sample_cases = SampleDataVer000.get(run=args.sample)
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
            # print(e)
            continue
        else:
            print("OK")
            limits = [
                0.9, 0.85, 0.8, 0.75, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1
            ]
            results = dict()
            while True:
                limit = limits.pop(0)
                result = Evaluation.get_similar_objs(
                    requires=test_obj["requires"], 
                    model=model,
                    sample_cases=sample_cases,
                    test_cases=test_obj["cases"],
                    num_of_true=num_of_true,
                    limit=limit,
                    size=parameter["size"]
                )
                results.update(result)
                if len(results) > top:
                    break
            
            results = sorted(results.items(), reverse=True)
            data = list()
            data.append(["result", "description"])
            for result in results[:top]:
                print(result[1])
                tokens = SampleDataVer000._patch_get_original(result[0])
                words = ""
                for token in tokens:
                    words += token
                data.append([result[1], words])

            ToCSV.do(
                parameter=parameter,
                data=data,
                sample_case_version="tmp",
                target=target,
                top_lim=top,
                seed=seed
            )



def main(args):
    pass
    # do(args, target="APT-GET_INSTALL_ver0.0.0", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.0.0", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.0.0", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.0.0", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.1.0", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.1.0", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.1.0", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.1.0", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.1.1", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.1.1", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.1.1", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.1.1", top=40, seed="min_count")

    do(args, target="GPG_KEY_ver0.0.1", top=10, seed="min_count")
    do(args, target="GPG_KEY_ver0.0.1", top=20, seed="min_count")
    do(args, target="GPG_KEY_ver0.0.1", top=30, seed="min_count")
    do(args, target="GPG_KEY_ver0.0.1", top=40, seed="min_count")

    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=10, seed="min_count")
    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=20, seed="min_count")
    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=30, seed="min_count")
    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=40, seed="min_count")

    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=10, seed="size")
    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=20, seed="size")
    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=30, seed="size")
    # do(args, target="CONFIG_USE_EXPLICIT_ver0.0.0", top=40, seed="size")

    # do(args, target="APT-GET_INSTALL_ver0.2.0", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.2.0", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.2.0", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.2.0", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.2.1", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.2.1", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.2.1", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.2.1", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.3.0", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.3.0", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.3.0", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.3.0", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.3.1", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.3.1", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.3.1", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.3.1", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.4.0", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.4.0", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.4.0", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.4.0", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.4.1", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.4.1", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.4.1", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.4.1", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.5.0", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.5.0", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.5.0", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.5.0", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.5.1", top=10, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.5.1", top=20, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.5.1", top=30, seed="min_count")
    # do(args, target="APT-GET_INSTALL_ver0.5.1", top=40, seed="min_count")

    # do(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0", top=10, seed="min_count")
    # do(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0", top=20, seed="min_count")
    # do(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0", top=30, seed="min_count")
    # do(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0", top=40, seed="min_count")

    # do(args, target="APT-GET_INSTALL_ver0.1.0")
    # do(args, target="GPG_KEY_ver0.0.0")
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