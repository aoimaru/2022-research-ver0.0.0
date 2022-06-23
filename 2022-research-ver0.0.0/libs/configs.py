import pathlib

class Config(object):
    """
        - プロジェクト内で使う定数を扱うクラス
    """
    ROOT_PATH = str(pathlib.Path(__file__).parents[2])
    
    