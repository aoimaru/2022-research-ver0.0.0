import os
import json
import glob
import pprint
from libs.configs import Config
from libs.recursives import *

ORIGINAL_GOLD_PATH = Config.ROOT_PATH + "/data/original/gold/"
AST_GOLD_PATH = Config.ROOT_PATH + "/data/ast/gold/"
# ORIGINAL_GOLD_PATH = Config.ROOT_PATH + "/data/original/github_ver0.0.0/"


def get_file_contents(file_path):
    try:
        with open(file_path, mode="r") as f:
            data = json.load(f)
    except Exception as e:
        print(e)
        return dict()
    else:
        return data


def reference_original(search_words):
    for file_path in glob.glob(ORIGINAL_GOLD_PATH+"**/*", recursive=True):
        contents = get_file_contents(file_path)
        # pprint.pprint(contents)
        # print()
        for cnt, content in enumerate(contents):
            if content["type"] != "DOCKER-RUN":
                continue
            run_commands = content["children"][0]["value"]
            for search_word in search_words:
                if not search_word in run_commands:
                    break
            else:
                print()
                file_sha = os.path.basename(file_path)
                file_sha = file_sha.replace(".json", "")
                print(file_sha)
                print(cnt)
                reference_ast(file_sha, cnt)

            

def reference_ast(file_sha, cnt):
    file_path = AST_GOLD_PATH+"{}.json".format(file_sha)
    contents = get_file_contents(file_path)
    ignores = [
        "DOCKER-RUN",
        "BASH-SCRIPT",
        "BASH-AND-IF",
        "BASH-AND-MEM"
        # "UNKNOWN"
    ]
    for dnt, content in enumerate(contents):
        if dnt == cnt:
            sequences = Recursive.do(content)
            FLAG = "INIT"
            for sequence in sequences:
                sequence = [word for word in sequence if not word in ignores]
                if "UNKNOWN" in sequence:
                    continue
                if not sequence:
                    continue
                if sequence[0] != FLAG:
                    FLAG = sequence[0]
                    print()
                print(sequence)



def main():
    words = [
        "apt-get",
        "update",
        "install",
        "-y",
        "--no-install-recommends"
    ]
    words = [
        "./configure",
        "--build="
    ]
    # words = [
    #     "rm",
    #     "-r",
    #     "/root/.gem/"
    # ]
    # words = [
    #     "gem",
    #     "install",
    #     "bundler"
    # ]
    # words = [
    #     "pip",
    #     "install",
    #     "--no-cache-dir"
    # ]
    reference_original(search_words=words)



if __name__ == "__main__":
    main()