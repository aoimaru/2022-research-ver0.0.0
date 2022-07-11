import argparse
import glob
import json
import pprint
import os

from libs.configs import Config
from libs.parameters import Parameter
from libs.graphs import *


def _test_0():
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.0.0/**/*.json"

    for file_path in glob.glob(FILE_PATH, recursive=True)[:10]:
        # print(file_path)
        with open(file_path, mode="r") as f:
            datas = json.load(f)
        PRGraph.view(datas)

def _test_1():
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.0.0/**/*.json"

    for file_path in glob.glob(FILE_PATH, recursive=True)[:10]:
        # print(file_path)
        with open(file_path, mode="r") as f:
            datas = json.load(f)
        basename = os.path.basename(file_path)
        basename = basename.replace(".json", "")
        print(basename)
        PRGraph.do(datas)       

def main(args):
    _test_0()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vecで学習させる際のパラメータを指定")
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    parser.add_argument("--sample", help="サンプルRUNのみかそれ以外も含むかを指定", type=int, default=1)
    args = parser.parse_args() 
    main(args)