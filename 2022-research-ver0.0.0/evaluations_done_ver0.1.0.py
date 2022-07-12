import argparse
import glob
import json
import pprint
import os

from libs.configs import Config
from libs.parameters import Parameter
from libs.graphs import *


def _test_0(args):
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/GPG_KEY_ver0.0.0/"
    parameters = Parameter.get("word2vec_done_ver0.1.0.json", args.version)
    for parameter in parameters:
        print(parameter)
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            sample=args.sample,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            source=parameter["source"],
            run=parameter["run"]
        )
        print(file_name)
        file_path = FILE_PATH+file_name
        with open(file_path, mode="r") as f:
            try:
                datas = json.load(f)
            except Exception as e:
                print(e)
            else:
                PRGraph.view(datas)

def _test_1(args):
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.1.0/"
    parameters = Parameter.get("word2vec_done_ver0.1.0.json", args.version)
    for parameter in parameters:
        print(parameter)
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            sample=args.sample,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            source=parameter["source"],
            run=parameter["run"]
        )
        print(file_name)
        file_path = FILE_PATH+file_name
        with open(file_path, mode="r") as f:
            try:
                datas = json.load(f)
            except Exception as e:
                print(e)
            else:
                PRGraph.view(datas)

def _test_2(args):
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.1.0/"
    parameters = Parameter.get("word2vec_done_ver0.1.0.json", args.version)
    datas = list()
    for parameter in parameters:
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            sample=args.sample,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            source=parameter["source"],
            run=parameter["run"]
        )
        file_path = FILE_PATH+file_name
        basename = os.path.basename(file_path)
        basename = basename.replace(".json", "")
        with open(file_path, mode="r") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(e)
            else:
                datas.append(data)




def main(args):
    _test_2(args)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vecで学習させる際のパラメータを指定")
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    parser.add_argument("--sample", help="サンプルRUNのみかそれ以外も含むかを指定", type=int, default=1)
    args = parser.parse_args() 
    main(args)