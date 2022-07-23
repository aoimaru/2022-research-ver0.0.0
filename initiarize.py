import glob
import copy
import json
import pprint
import os


def recursive(objs):
    paths = list()
    def do(objs, path=str()):
        if isinstance(objs, str):
            path += "/" + objs
            paths.append(path)
        if isinstance(objs, dict):
            for name, obj in objs.items():
                tmp_path = copy.copy(path)
                do(obj, tmp_path+"/"+name)
        if isinstance(objs, list):
            for obj in objs:
                tmp_path = copy.copy(path)
                do(obj, tmp_path)
    do(objs)
    return paths


def count():
    count = 0
    for file_path in glob.glob("data/**/*", recursive=True):
        count += 1
    print("count:", count)
    count = 0
    for file_path in glob.glob("2022-research-ver0.0.0/**/*", recursive=True):
        count += 1
    print("count:", count)

def make_dir():
    with open("./data_level.json", mode="r") as f:
        obj = json.load(f)

    file_paths = recursive(obj["levels"])
    root_path = os.getcwd()
    for file_path in file_paths:
        try:
            print(root_path+file_path)
            os.makedirs(root_path+file_path)
        except Exception as e:
            print(e)


def main():
    make_dir()


if __name__ == "__main__":
    main()