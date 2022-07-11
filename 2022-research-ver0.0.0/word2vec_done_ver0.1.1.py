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
    
                


def main(args):    
    test_obj = TestCase.get("GPG_KEY_ver0.0.0.json")
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
                0.9, 0.85, 0.8, 0.75, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1
            ]
            evaluations = list()
            for limit in limits:
                print("limit:", limit)
                evaluation = Evaluation.do(
                    requires=test_obj["requires"], 
                    model=model,
                    sample_cases=sample_cases,
                    test_cases=test_obj["cases"],
                    num_of_true=num_of_true,
                    limit=limit,
                    size=parameter["size"]
                )
                pprint.pprint(evaluation)
                evaluations.append(evaluation)
            Evaluation.to_file(
                parameter=parameter,
                evaluations=evaluations,
                sample=args.sample,
                folder="GPG_KEY_ver0.0.0"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vecで学習させる際のパラメータを指定")
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    parser.add_argument("--sample", help="サンプルRUNのみかそれ以外も含むかを指定", type=int, default=1)
    args = parser.parse_args() 
    main(args)