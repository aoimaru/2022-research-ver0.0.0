import argparse

from libs.word2vecs import *
from functions.functions import *
from libs.vectors import *

from collections import defaultdict
from gensim.models.keyedvectors import KeyedVectors
from sklearn.cluster import KMeans


import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
from sklearn.decomposition import PCA

from libs.configs import Config
from libs.parameters import Parameter
from libs.vec2pcas import Vec2PCA

from libs.datas import *


def main(args):
    model = BaseW2V.load(sg=1, size=100, min_count=10, window=5, name="gold", run=1)
    gold_cases = TestData.get(source="gold", run=1)
    Vec2PCA._patch(model, training_datas=gold_cases)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word2vecで学習させる際のパラメータを指定")
    parser.add_argument("--source", help="goldデータを使うか, githubデータを使うか, gold, githubで選択", choices=["github", "gold"])
    parser.add_argument("--run", help="run命令のみを対象にするなら1, 全てを対象にするなら0", type=int, default=0)
    parser.add_argument("--sg", help="skip-gramモデルを指定するなら1, cbowモデルを使うなら0", type=int, default=1)
    parser.add_argument("--size", help="単語ベクトルの次元数", type=int, default=100)
    parser.add_argument("--min_count", help="n回未満登場する単語を破棄", type=int, default=100)
    parser.add_argument("--window", help="学習に使う前後の単語数", type=int, default=5)
    parser.add_argument("--alpha", help="初期学習率: 学習の進行に伴ってmin_alphaに落ち着く", type=float, default=0.025)
    parser.add_argument("--min_alpha", help="最小学習率", type=float, default=0.0001)
    parser.add_argument("--iter", help="エポック数", type=int, default=5)
    parser.add_argument("--hs", help="学習に階層化ソフトマックスを使用するかどうか: もしネガティブサンプリングを使用する場合はhs=0を設定しなければならない", type=int, default=0)
    parser.add_argument("--negative", help="ネガティブサンプリングに用いる単語数: hsを使わない場合に設定する。word2vecに与えたコーパスの語彙の中から対象単語の周辺に出現しない単語を、類似していない単語として学習させる", type=int, default=5)
    parser.add_argument("--cbow_mean", help="単語ベクトルの平均ベクトルを使うか合計を使うか？: cbow_mean=1なら平均ベクトルcbow_mean=0なら合計", type=int, default=1)

    # parser.add_argument("--cluster", help="クラスタの数を指定", type=int, default=10)
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    args = parser.parse_args() 
    main(args)