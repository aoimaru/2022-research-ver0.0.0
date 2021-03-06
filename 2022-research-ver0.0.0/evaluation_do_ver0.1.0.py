import argparse
import glob
import json
import pprint
import os

from libs.configs import Config
from libs.parameters import Parameter
from libs.graphs import *
from libs.charts import *

import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod




def per_size(args, target):
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/{}/".format(target)
    parameters = Parameter.get("evaluation_done_ver0.1.0.json", "size_ver0.0.0")
    datas = dict()
    for parameter in parameters:
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            # sample=args.sample,
            sample=1,
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
        try:
            with open(file_path, mode="r") as f:
                data = json.load(f)
        except Exception as e:
            print(e)
        else:
            datas[parameter["size"]] = data
        
    
    RPChart.draw(datas, n_high=2, n_wide=3, recognize="size", target=target, description="50*n")
    FmChart.draw(datas, n_high=2, n_wide=3, recognize="size", target=target, description="50*n")

def per_min_count(args, target):
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/{}/".format(target)
    parameters = Parameter.get("evaluation_done_ver0.1.0.json", "size_ver0.0.2")
    datas = dict()
    for parameter in parameters:
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            # sample=args.sample,
            sample=1,
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
        try:
            with open(file_path, mode="r") as f:
                data = json.load(f)
        except Exception as e:
            print(e)
        else:
            datas[parameter["min_count"]] = data
    RPChart.draw(datas, n_high=2, n_wide=3, recognize="min_count", target=target, description="10*n")
    FmChart.draw(datas, n_high=2, n_wide=3, recognize="min_count", target=target, description="10*n")

def per_window(args, target):
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/{}/".format(target)
    parameters = Parameter.get("evaluation_done_ver0.1.0.json", "window_ver0.0.0")
    datas = dict()
    for parameter in parameters:
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            # sample=args.sample,
            sample=1,
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
        try:
            with open(file_path, mode="r") as f:
                data = json.load(f)
        except Exception as e:
            print(e)
        else:
            datas[parameter["window"]] = data
        
    
    RPChart.draw(datas, n_high=1, n_wide=4, recognize="window", target=target, description="10*n")
    FmChart.draw(datas, n_high=1, n_wide=4, recognize="window", target=target, description="10*n")




def main(args):
    pass
    # per_size(args, target="APT-GET_INSTALL_ver0.0.0")
    # per_size(args, target="APT-GET_INSTALL_ver0.1.0")
    # per_size(args, target="GPG_KEY_ver0.0.0")
    # per_size(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0")

    # per_min_count(args, target="APT-GET_INSTALL_ver0.0.0")
    # per_min_count(args, target="APT-GET_INSTALL_ver0.1.0")
    # per_min_count(args, target="GPG_KEY_ver0.0.0")
    # per_min_count(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0")

    # per_min_count(args, target="APT-GET_INSTALL_ver0.1.1")
    # per_min_count(args, target="APT-GET_INSTALL_ver0.2.0")
    # per_min_count(args, target="APT-GET_INSTALL_ver0.3.0")
    # per_min_count(args, target="APT-GET_INSTALL_ver0.4.0")
    # per_min_count(args, target="APT-GET_INSTALL_ver0.5.0")

    # per_size(args, target="APT-GET_INSTALL_ver0.1.1")
    # per_size(args, target="APT-GET_INSTALL_ver0.2.0")
    # per_size(args, target="APT-GET_INSTALL_ver0.3.0")
    # per_size(args, target="APT-GET_INSTALL_ver0.4.0")
    # per_size(args, target="APT-GET_INSTALL_ver0.5.0")
    per_size(args, target="APT-GET_INSTALL_ver0.2.1")
    per_size(args, target="APT-GET_INSTALL_ver0.3.1")
    per_size(args, target="APT-GET_INSTALL_ver0.4.1")
    per_size(args, target="APT-GET_INSTALL_ver0.5.1")

    # per_window(args, target="APT-GET_INSTALL_ver0.0.0")
    # per_window(args, target="APT-GET_INSTALL_ver0.1.0")
    # per_window(args, target="GPG_KEY_ver0.0.0")
    # per_window(args, target="APK_ADD_USE_NO_CACHE_ver0.0.0")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vec????????????????????????????????????????????????")
    parser.add_argument("--version", help="??????????????????????????????????????????", type=str, default="ver0.0.0")
    parser.add_argument("--sample", help="????????????RUN??????????????????????????????????????????", type=int, default=1)
    args = parser.parse_args() 
    main(args)