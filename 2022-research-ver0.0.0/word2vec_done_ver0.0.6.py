import argparse
import pprint
from libs.parameters import Parameter
from libs.datas import *

import numpy as np
from numpy import dot
from numpy.linalg import norm

from libs.word2vecs import BaseW2V
from libs.vectors import Vector
from functions.functions import *

from libs.evaluations import *

"""
    - 効率を考えて今回はグローバルに定義
"""

sample_cases = SampleDataVer001.get(run=1)
# sample_cases = TestData.get(source="gold", run=1)
model = BaseW2V.load(sg=1, size=100, min_count=10, window=5, name="gold", run=1)


def _test_0(limit=0.9):
    words = [
        'SC-APT-GET-INSTALL',
        'SC-APT-GET-F-NO-INSTALL-RECOMMENDS',
        'SC-RM',
        'SC-APT-GET-UPDATE',
        'SC-APT-GET-F-YES',
        'SC-RM-F-RECURSIVE',
        'SC-RM-F-FORCE',
        'SC-APT-GET-PACKAGES'
    ]
    test_case = [
        ['SC-SET', 'SC-SET-F-E'],
        ['SC-SET', 'SC-SET-F-X'],
        ['SC-APT-GET-UPDATE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-YES'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-F-NO-INSTALL-RECOMMENDS'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:AUTOCONF'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:AUTOMAKE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:BZIP2'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:DPKG-DEV'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:FILE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE'],
        ['SC-APT-GET-INSTALL', 'SC-APT-GET-PACKAGES', 'SC-APT-GET-PACKAGE:GCC'],
        ['SC-RM', 'SC-RM-F-RECURSIVE'],
        ['SC-RM', 'SC-RM-F-FORCE'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-MAYBE-PATH'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-APT-LISTS'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-PATH-VAR'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-LITERAL',
        'ABS-PATH-ABSOLUTE'],
        ['SC-RM',
        'SC-RM-PATHS',
        'SC-RM-PATH',
        'BASH-CONCAT',
        'BASH-GLOB',
        'ABS-GLOB-STAR']
    ]

    num_of_true = Evaluation.count_true(requires=words, cases=sample_cases)
    evaluation = Evaluation.do(
        requires=words, 
        model=model,
        sample_cases=sample_cases,
        test_cases=test_case,
        num_of_true=num_of_true,
        limit=limit,
        size=100
    )
    pprint.pprint(evaluation)
                



def main(args):    
    # _test_1()
    """
        _test_1 = 45
        _test_1 = 373
    """
    limits = [
        0.9, 0.85, 0.8, 0.75, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1
    ]
    for limit in limits:
        print()
        _test_0(limit=limit)
    




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
    parser.add_argument("--version", help="パラメータのバージョンを指定", type=str, default="ver0.0.0")
    args = parser.parse_args() 
    main(args)