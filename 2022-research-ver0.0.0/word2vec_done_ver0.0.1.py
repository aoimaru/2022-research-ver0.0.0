import pprint
from libs.parameters import Parameter
from libs.datas import *

def main():
    parameters = Parameter.get("word2vec_done_ver0.0.1.json", "ver0.0.0")
    pprint.pprint(parameters)
    training_data = TrainingData.get("gold", 1)
    pprint.pprint(training_data)



if __name__ == "__main__":
    main()