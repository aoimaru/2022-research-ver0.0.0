import json
import pprint
from libs.configs import Config


METADATA_GITHUB_PARH = Config.ROOT_PATH + "/data/metadata/0b-deduplicated-dockerfile-sources-sha-github.json"
METADATA_GOLD_PARH = Config.ROOT_PATH + "/data/metadata/0b-deduplicated-dockerfile-sources-sha-gold.json"

class MetaData(object):
    """
        - 解析結果のファイルのshaのリストを取得するクラス
    """
    @staticmethod
    def get_gold_path():
        with open(METADATA_GOLD_PARH, mode="r") as f:
            data = json.load(f)
        return data["file_sha"]

    @staticmethod
    def get_github_path():
        with open(METADATA_GITHUB_PARH, mode="r") as f:
            data = json.load(f)
        return data["file_sha"]

def main():
    pass

if __name__ == "__main__":
    main()