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

class RPChart(Chart):
    @staticmethod
    def view(datas, n_high, n_wide, recognize):
        def do(rcs, prs, lims, rcs_label, prs_label, title):
            rcs = np.array(rcs)
            prs = np.array(prs)
            lims = np.array(lims)

            lims = lims*10

            width_bar=0.2
            rcs_wb = lims-width_bar
            prs_wb = lims+width_bar

            plt.title(title, fontsize=12)
            plt.xlabel("recall and precision", fontsize=12)
            plt.ylabel("score", fontsize=12)
            plt.grid(True)
            plt.tick_params(labelsize=6)

            plt.bar(rcs_wb, rcs, align="center", color = "c", label=rcs_label, width=width_bar) # 棒グラフの描画
            plt.bar(prs_wb, prs, align="center", color = "r", label=prs_label, width=width_bar) # 棒グラフの描画
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
            do(
                rcs=recalls,
                prs=precisions,
                lims=limits,
                title="score by {recognize}:{key}".format(recognize=recognize, key=key),
                rcs_label="recalls",
                prs_label="presicions"
            )
        plt.show()
    
    @staticmethod
    def draw(datas, n_high, n_wide, recognize, target, description):
        def do(rcs, prs, lims, rcs_label, prs_label, title):
            rcs = np.array(rcs)
            prs = np.array(prs)
            lims = np.array(lims)

            lims = lims*10

            width_bar=0.2
            rcs_wb = lims-width_bar
            prs_wb = lims+width_bar

            plt.title(title, fontsize=12)
            plt.xlabel("recall and precision", fontsize=12)
            plt.ylabel("score", fontsize=12)
            plt.grid(True)
            plt.tick_params(labelsize=6)

            plt.bar(rcs_wb, rcs, align="center", color = "c", label=rcs_label, width=width_bar) # 棒グラフの描画
            plt.bar(prs_wb, prs, align="center", color = "r", label=prs_label, width=width_bar) # 棒グラフの描画
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
            do(
                rcs=recalls,
                prs=precisions,
                lims=limits,
                title="score by {recognize}:{key}".format(recognize=recognize, key=key),
                rcs_label="recalls",
                prs_label="presicions"
            )

        STORAGE_PATH = Config.ROOT_PATH+"/data/chart/{target}/{recognize}/recall_and_precision_{description}.png".format(
            target=target,
            recognize=recognize,
            description=description
        )
        plt.savefig(STORAGE_PATH)
    

class FmChart(Chart):
    @staticmethod
    def view(datas, n_high, n_wide, recognize):
        def do(fms, lims, fms_label, title):
            fms = np.array(fms)
            lims = np.array(lims)

            lims = lims*10


            plt.title(title, fontsize=12)
            plt.xlabel("f_measure", fontsize=12)
            plt.ylabel("score", fontsize=12)
            plt.grid(True)
            plt.tick_params(labelsize=6)

            # plt.bar(rcs_wb, rcs, align="center", color = "c", label=rcs_label, width=width_bar) # 棒グラフの描画
            # plt.bar(prs_wb, prs, align="center", color = "r", label=prs_label, width=width_bar) # 棒グラフの描画
            plt.bar(lims, fms, align="center", color = "c", label=fms_label, width=0.2) # 棒グラフの描画
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
            do(
                fms=f_measures,
                lims=limits,
                title="score by {recognize}:{key}".format(recognize=recognize, key=key),
                fms_label="f_measure"
            )
        plt.show()

    @staticmethod
    def draw(datas, n_high, n_wide, recognize, target, description):
        def do(fms, lims, fms_label, title):
            fms = np.array(fms)
            lims = np.array(lims)

            lims = lims*10


            plt.title(title, fontsize=12)
            plt.xlabel("f_measure", fontsize=12)
            plt.ylabel("score", fontsize=12)
            plt.grid(True)
            plt.tick_params(labelsize=6)

            # plt.bar(rcs_wb, rcs, align="center", color = "c", label=rcs_label, width=width_bar) # 棒グラフの描画
            # plt.bar(prs_wb, prs, align="center", color = "r", label=prs_label, width=width_bar) # 棒グラフの描画
            plt.bar(lims, fms, align="center", color = "c", label=fms_label, width=0.2) # 棒グラフの描画
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
            do(
                fms=f_measures,
                lims=limits,
                title="score by {recognize}:{key}".format(recognize=recognize, key=key),
                fms_label="f_measure"
            )
        STORAGE_PATH = Config.ROOT_PATH+"/data/chart/{target}/{recognize}/f_measures_{description}.png".format(
            target=target,
            recognize=recognize,
            description=description
        )
        plt.savefig(STORAGE_PATH)

