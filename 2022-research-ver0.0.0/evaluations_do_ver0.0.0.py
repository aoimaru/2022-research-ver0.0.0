import glob
import json
import pprint
import os

from libs.configs import Config


def main():
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.0.1/**/*.json"

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
        






if __name__ == "__main__":
    main()