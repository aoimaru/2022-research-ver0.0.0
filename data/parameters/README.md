```bash

    "ver0.0.0": {
        "sg": [0, 1],
        "size": [100, 200, 300],
        "min_count": [50, 100],
        "window": [5, 10]
    },
    "ver0.0.1": {
        "sg": [0, 1],
        "size": [100, 200, 300],
        "min_count": [10],
        "window": [5, 10]
    },
    "size_ver0.0.0": {
        "sg": [1],
        "size": [50, 100, 150, 200, 250, 300],
        "min_count": [5],
        "window": [5]
    },
    "size_ver0.0.1": {
        "sg": [0],
        "size": [50, 100, 150, 200, 250, 300],
        "min_count": [5],
        "window": [5]
    },
    "min_count_ver0.0.0": {
        "sg": [0],
        "size": [100],
        "min_count": [2, 4, 6, 8, 10],
        "source": ["gold"],
        "window": [5],
        "run": [1]
    },
    "min_count_ver0.0.1": {
        "sg": [0],
        "size": [100],
        "min_count": [20, 40, 60, 80, 100],
        "source": ["gold"],
        "window": [5],
        "run": [1]
    },
    "window_ver0.0.0": {
        "sg": [0],
        "size": [100],
        "min_count": [5],
        "source": ["gold"],
        "window": [5, 10, 15, 20],
        "run": [1]
    }



    "size_ver0.0.0": {
        "sg": [1],
        "size": [50, 100, 150, 200, 250, 300],
        "min_count": [5],
        "window": [5]
    }

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

```