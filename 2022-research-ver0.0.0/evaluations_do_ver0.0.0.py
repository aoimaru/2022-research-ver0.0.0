import glob
import json
import pprint

from libs.configs import Config


def main():
    file_path_0 = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.0.0/sample-1.sg-0.size-100.min_count-50.window-10.source-gold.name-gold.run-0.json"
    file_path_1 = Config.ROOT_PATH+"/data/evaluations/APT-GET_INSTALL_ver0.0.0/sample-1.sg-0.size-200.min_count-50.window-5.source-github.name-gold.run-1.json"

    with open(file_path_0, mode="r") as f:
        data = json.load(f)
    pprint.pprint(data)



if __name__ == "__main__":
    main()