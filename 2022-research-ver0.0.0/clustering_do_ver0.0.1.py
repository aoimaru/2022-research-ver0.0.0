import argparse
import json

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

def get_parameters():
    params = {
        "source": ["gold"],
        "run": [0, 1],
        "sg": [0, 1],
        "size": [100, 200, 300],
        "min_count": [50, 100],
        "window": [5, 10],
        "cluster": [10, 20, 30, 40, 50]
    }
    products = [cnt for cnt in itertools.product(*params.values())]
    parameters = [dict(zip(params.keys(), cnt)) for cnt in products]
    return parameters

def clustering(args):
    model = BaseW2V.load(sg=args.sg, size=args.size, min_count=args.min_count, window=args.window, name=args.source, run=args.run)

    vocab = list(model.wv.vocab.keys())
    vectors = [model.wv[word] for word in vocab]
    n_clusters = args.cluster
    kmeans_model = KMeans(n_clusters=n_clusters, verbose=1, random_state=42, n_jobs=-1)
    kmeans_model.fit(vectors)
    
    cluster_labels = kmeans_model.labels_
    cluster_to_words = defaultdict(list)
    for cluster_id, word in zip(cluster_labels, vocab):
        cluster_to_words[cluster_id].append(word)
    
    return cluster_to_words

def main(args):
    cluster_to_words = clustering(args)

    file_name = "/data/clustering/{}/sg-{}.size-{}.min_count-{}.window-{}.run-{}.clustering-{}.json".format(args.source, args.sg, args.size, args.min_count, args.window, args.run, args.cluster)
    file_path = Config.ROOT_PATH+file_name

    obj = dict()
    for key, words in cluster_to_words.items():
        obj[str(key)] = words
    
    with open(file_path, mode="w") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)
        


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

    parser.add_argument("--cluster", help="クラスタの数を指定", type=int, default=10)

    args = parser.parse_args() 
    main(args)