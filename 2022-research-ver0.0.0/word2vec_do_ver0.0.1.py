import argparse

from libs.word2vecs import *
from functions.functions import *
import itertools
import pprint

def get_training_data(source, run):
    """

    """
    if source == "github":
        if run == 1:
            training_data = W2VFunction.get_training_github_data_filter_run()
        else:
            training_data = W2VFunction.get_training_github_data()
    else:
        if run == 1:
            training_data = W2VFunction.get_training_gold_data_filter_run()
        else:
            training_data = W2VFunction.get_training_gold_data()
    
    return training_data



def get_parameters():
    params = {
        "source": ["gold"],
        "run": [0, 1],
        "sg": [0, 1],
        "size": [100, 200, 300],
        "min_count": [50, 100],
        "window": [5, 10]
    }

    products = [cnt for cnt in itertools.product(*params.values())]
    parameters = [dict(zip(params.keys(), cnt)) for cnt in products]
    return parameters

def main(args):
    parameters = get_parameters()
    for parameter in parameters:
        training_data = get_training_data(parameter["source"], parameter["run"])
        BaseW2V.do(corpus=training_data, sg=parameter["sg"], size=parameter["size"], min_count=parameter["min_count"], window=parameter["window"], name=parameter["source"], run=parameter["run"])


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
    args = parser.parse_args() 
    main(args)