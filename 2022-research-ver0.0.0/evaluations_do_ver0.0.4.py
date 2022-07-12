import argparse
import glob
import json
import pprint
import os

from libs.configs import Config
from libs.parameters import Parameter
from libs.graphs import *

import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class Chart(object):
    @staticmethod
    @abstractmethod
    def do():
        pass

class BarChart(Chart):
    @staticmethod
    def draw_by_size_rp(datas, n_high, n_wide):
        def bar_rp(firsts, seconds, thirds, title, x_label, y_label):
            """
                - firsts: recalls
                - seconds: precisions
                - thirds: limits
            """
            thirds = np.array(thirds)
            thirds = thirds*10

            firsts = np.array(firsts)
            seconds = np.array(seconds)
            width_bar=0.2
            thirds_firsts=thirds-width_bar
            thirds_seconds=thirds+width_bar

            plt.title(title, fontsize=12)
            plt.xlabel("recall and precision", fontsize=12)
            plt.ylabel("score", fontsize=12)
            plt.grid(True)
            plt.tick_params(labelsize=6)

            plt.bar(thirds_firsts, firsts, align="center", color = "c", label=x_label, width=width_bar) # 棒グラフの描画
            plt.bar(thirds_seconds, seconds, align="center", color = "r", label=y_label, width=width_bar) # 棒グラフの描画
            plt.legend()

        plt.figure(figsize=(12, 8)) # (1)描画領域を指定
        plt.subplots_adjust(wspace=0.6, hspace=0.6) # (2)間隔指定
        
        count = 0
        for key, data in datas.items():
            count += 1
            recalls = list()
            precisions = list()
            limits = list()
            for tmp in data:
                recalls.append(tmp["recall"])
                precisions.append(tmp["precition"])
                limits.append(tmp["limit"])

            plt.subplot(n_high, n_wide, count)
            bar_rp(
                firsts=recalls,
                seconds=precisions,
                thirds=limits,
                title="score by size:{}".format(key),
                x_label="recalls",
                y_label="presicions"
            )
        plt.show()
    
    @staticmethod
    def draw_by_size_f(datas, n_high, n_wide):
        def bar_f(firsts, seconds, title, x_label, y_label):
            """
            """
            seconds = np.array(seconds)
            seconds = seconds*10

            firsts = np.array(firsts)
            # thirds = np.array(thirds)
            # thirds = thirds*10

            # firsts = np.array(firsts)
            # seconds = np.array(seconds)
            # width_bar=0.2
            # thirds_firsts=thirds-width_bar
            # thirds_seconds=thirds+width_bar

            plt.title(title, fontsize=12)
            plt.xlabel("f_measure", fontsize=12)
            plt.ylabel("score", fontsize=12)
            plt.grid(True)
            plt.tick_params(labelsize=6)

            plt.bar(seconds, firsts, align="center", color = "c", label=x_label, width=0.2) # 棒グラフの描画
            # plt.bar(thirds_seconds, seconds, align="center", color = "r", label=y_label, width=width_bar) # 棒グラフの描画
            plt.legend()

        plt.figure(figsize=(12, 8)) # (1)描画領域を指定
        plt.subplots_adjust(wspace=0.6, hspace=0.6) # (2)間隔指定
        
        count = 0
        for key, data in datas.items():
            count += 1
            f_measures = list()
            limits = list()
            for tmp in data:
                f_measures.append(tmp["f_measure"])
                limits.append(tmp["limit"])

            plt.subplot(n_high, n_wide, count)
            bar_f(
                firsts=f_measures,
                seconds=limits,
                title="score by size:{}".format(key),
                x_label="recalls",
                y_label="presicions"
            )
        plt.show()




def _test_0_by_size(args, target):
    FILE_PATH = Config.ROOT_PATH+"/data/evaluations/{}/".format(target)
    # parameters = Parameter.get("word2vec_done_ver0.1.0.json", args.version)
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
        with open(file_path, mode="r") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(e)
            else:
                datas[parameter["size"]] = data
    
    for key, value in datas.items():
        print(key)
        pprint.pprint(value)

    BarChart.draw_by_size_rp(datas, n_high=2, n_wide=3)
    BarChart.draw_by_size_f(datas, n_high=2, n_wide=3)



def main(args):
    _test_0_by_size(args, target="APT-GET_INSTALL_ver0.1.0")
    _test_0_by_size(args, target="APT-GET_INSTALL_ver0.0.0")
    _test_0_by_size(args, target="GPG_KEY_ver0.0.0")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vecで学習させる際のパラメータを指定")
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    parser.add_argument("--sample", help="サンプルRUNのみかそれ以外も含むかを指定", type=int, default=1)
    args = parser.parse_args() 
    main(args)