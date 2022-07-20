import glob
import shutil
import os
# import json
# import pprint

def main():
    src_path = "data/original/github/"
    dst_path = "data/original/github_ver0.0.0/"
    for file_path in glob.glob("./data/ast/github_ver0.0.0/**/*", recursive=True):
        file_path = src_path+os.path.basename(file_path)
        to_path = dst_path+os.path.basename(file_path)
        print(file_path)
        print(to_path)
        shutil.copyfile(file_path, to_path)
        

    # shutil.copyfile("initiarize.py", "tests/initiarize.py")



if __name__ == "__main__":
    main()