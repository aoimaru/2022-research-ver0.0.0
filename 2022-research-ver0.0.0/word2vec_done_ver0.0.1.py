import argparse

import numpy as np
from numpy import dot
from numpy.linalg import norm

from libs.word2vecs import *
from functions.functions import *
from libs.vectors import *


def get_test_data(args):
    """

    """
    if args.source == "github":
        if args.run == 1:
            test_data = W2VFunction.get_test_github_data_filter_run()
        else:
            test_data = W2VFunction.get_test_github_data()
    else:
        if args.run == 1:
            print("OK")
            test_data = W2VFunction.get_test_gold_data_filter_run()
        else:
            test_data = W2VFunction.get_test_gold_data()
    
    return test_data

def main(args):
    test_data = get_test_data(args)
    model = BaseW2V.load(sg=args.sg, size=args.size, min_count=args.min_count, window=args.window, name=args.source, run=args.run)
    test_case = [
        ['SC-APT-GET-UPDATE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-YES'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-NO-INSTALL-RECOMMENDS'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:LIBNSS-WRAPPER']
    ]
    testCaseVec = Vector(contexts=test_case, model=model, size=args.size)
    # print(testCaseVec._contexts)
    tcVec = testCaseVec.vector
    for test_ in test_data:
        testDataVec = Vector(contexts=test_, model=model, size=args.size)
        tdVec = testDataVec.vector
        result = dot(tcVec, tdVec)/(norm(tcVec)*norm(tdVec))
        if result > 0.8:
            print("result:", result)
            for context in testDataVec.contexts:
                print(context)
            print()

    
    
    


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