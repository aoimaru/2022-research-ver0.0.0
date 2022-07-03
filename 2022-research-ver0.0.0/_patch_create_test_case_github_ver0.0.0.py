import glob
import json
import pprint

from libs.configs import Config
from libs.files import SampleAST
from libs.recursives import Recursive

GITHUB_VER000_ROOT_PATH = Config.ROOT_PATH+"/data/ast/github_ver0.0.0"
GITHUB_VER000_METADATA_PATH = Config.ROOT_PATH+"/data/metadata/"

def _get_file_sha():
    file_shas = list()
    for file_path in glob.glob(GITHUB_VER000_ROOT_PATH+"/**/*", recursive=True):
        file_tokens = file_path.split("/")
        file_sha = file_tokens[-1].replace(".json", "")
        file_shas.append(file_sha)
    return file_shas


def main():
    file_shas = _get_file_sha()
    for file_sha in file_shas:
        print(file_sha)
        try:
            ast_obj = SampleAST(file_sha)
        except Exception as e:
            print(e)
        else:
            obj_dict = dict()
            for idx, child in enumerate(ast_obj.children):
                if not child["type"] == "DOCKER-RUN":
                    continue
                sequence = Recursive.do(child)
                sequence = [word[2:] for word in sequence]
                obj_dict[str(idx)] = sequence
            pprint.pprint(obj_dict, indent=4)



if __name__ == "__main__":
    main()