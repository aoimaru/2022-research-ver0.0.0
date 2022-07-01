import glob
import json
from libs.configs import Config

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
    j_obj = dict()
    j_obj["file_sha"] = file_shas

    file_name = "0b-deduplicated-dockerfile-sources-sha-github-ver0.0.0.json"
    with open(GITHUB_VER000_METADATA_PATH+file_name, mode="w") as f:
        json.dump(j_obj, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()