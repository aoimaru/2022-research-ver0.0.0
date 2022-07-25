from abc import ABC, abstractmethod
from gensim.models import word2vec
import csv

from libs.configs import Config
from libs.exceptions import *

MODEL_PATH = Config.ROOT_PATH + "/data/model"

ROOT_PATH = Config.ROOT_PATH + "/data/top_cases"
ROOT_PATH_V2 = Config.ROOT_PATH + "/data/top_cases_v2"
ROOT_PATH_V3 = Config.ROOT_PATH + "/data/top_cases_v3"

class ToCSV():
    @staticmethod
    def do(parameter, data, sample_case_version, target, top_lim, seed):
        file_path = "{root_path}/{version}/{target}/top_{top_lim}/{seed}/sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.run-{run}.csv".format(
            root_path=ROOT_PATH,
            version=sample_case_version,
            target=target,
            top_lim=top_lim,
            seed=seed,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            run=parameter["run"]
        )
        try:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except Exception as e:
            print(e)
        else:
            print("OK")
    
    @staticmethod
    def do_v2(parameter, data, sample_case_version, target, top_lim, seed):
        file_path = "{root_path}/{version}/{target}/top_{top_lim}/{seed}/sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.run-{run}.csv".format(
            root_path=ROOT_PATH_V2,
            version=sample_case_version,
            target=target,
            top_lim=top_lim,
            seed=seed,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            run=parameter["run"]
        )
        try:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except Exception as e:
            print(e)
        else:
            print("OK")

    @staticmethod
    def do_v3(parameter, data, sample_case_version, target, top_lim, seed):
        file_path = "{root_path}/{version}/{target}/top_{top_lim}/{seed}/sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.run-{run}.csv".format(
            root_path=ROOT_PATH_V3,
            version=sample_case_version,
            target=target,
            top_lim=top_lim,
            seed=seed,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            run=parameter["run"]
        )
        try:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except Exception as e:
            print(e)
        else:
            print("OK")

