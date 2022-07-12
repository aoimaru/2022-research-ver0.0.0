### 複数の棒グラフを横に並べて表示
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class Graph(object):
    @staticmethod
    @abstractmethod
    def view():
        pass
    
    @staticmethod
    @abstractmethod
    def do():
        pass



class PRGraph(Graph):
    @staticmethod
    def view(datas):
        recalls = list()
        precisions = list()
        limits = list()
        for data in datas:
            recalls.append(data["recall"])
            precisions.append(data["precition"])
            limits.append(data["limit"])
        
        limits = np.array(limits)

        width_bar = 0.2

        limits=limits*10

        limits_recalls = limits-width_bar
        limits_precisions = limits+width_bar

        recalls = np.array(recalls)
        precisions = np.array(precisions)

        fig = plt.figure(figsize = (5,5))
        plt.xlabel('limits')
        plt.ylabel('values')

        plt.bar(limits_recalls, recalls, label='recalls', width=width_bar, align="center")
        plt.bar(limits_precisions, precisions, label='precision', width=width_bar, align="center")
        # plt.set_title("hello")
        plt.legend()
        plt.show()
    
    @staticmethod
    def do(datas):
        recalls = list()
        precisions = list()
        limits = list()
        for data in datas:
            recalls.append(data["recall"])
            precisions.append(data["precition"])
            limits.append(data["limit"])
        
        limits = np.array(limits)

        width_bar = 0.2

        limits=limits*10

        limits_recalls = limits-width_bar
        limits_precisions = limits+width_bar

        recalls = np.array(recalls)
        precisions = np.array(precisions)

        fig = plt.figure(figsize = (5,5))
        plt.xlabel('limits')
        plt.ylabel('values')

        plt.bar(limits_recalls, recalls, label='recalls', width=width_bar, align="center")
        plt.bar(limits_precisions, precisions, label='precision', width=width_bar, align="center")
        
        plt.legend()
        plt.save()




    @staticmethod
    def do_by_limit(datas):
        pass

