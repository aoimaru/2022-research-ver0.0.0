import argparse
import glob
import json
import pprint
import os

from libs.configs import Config
from libs.parameters import Parameter


def _test_0():
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.1.0/**/*.json"

    limit = 0.9
    result = dict()
    for file_path in glob.glob(FILE_PATH, recursive=True):
        # print(file_path)
        with open(file_path, mode="r") as f:
            datas = json.load(f)
        basename = os.path.basename(file_path)
        basename = basename.replace(".json", "")
        for data in datas:
            if data["limit"] == 0.9:
                result[basename] = data["f_measure"]
        
    outputs = sorted(result.items(), key=lambda i: i[1], reverse=True)
    # pprint.pprint(outputs)
    for num, output in enumerate(outputs[:30]):
        print(num, ":", output)
        
def _test_1(args):
    RESULT_PATH = Config.ROOT_PATH + "/data/evaluations/APT-GET_INSTALL_ver0.1.0"
    parameters = Parameter.get("word2vec_done_ver0.1.0.json", args.version)
    result = dict()
    for parameter in parameters:
        pprint.pprint(parameter)
        file_path = "{result_path}/sample-0.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            result_path=RESULT_PATH, 
            source=parameter["source"], 
            sg=parameter["sg"], 
            size=parameter["size"], 
            min_count=parameter["min_count"], 
            window=parameter["window"], 
            run=1
        )
        try:
            with open(file_path, mode="r") as f:
                datas = json.load(f)
        except Exception as e:
            print(e)
        else:
            basename = os.path.basename(file_path)
            basename = basename.replace(".json", "")
            for data in datas:
                if data["limit"] == 0.9:
                    result[basename] = data["f_measure"]

    outputs = sorted(result.items(), key=lambda i: i[1], reverse=True)
    # pprint.pprint(outputs)
    for num, output in enumerate(outputs[:30]):
        print(num, ":", output)

def main(args):
    _test_1(args)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vecで学習させる際のパラメータを指定")
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    parser.add_argument("--sample", help="サンプルRUNのみかそれ以外も含むかを指定", type=int, default=1)
    args = parser.parse_args() 
    main(args)