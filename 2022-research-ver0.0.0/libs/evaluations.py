from libs.datas import *

import numpy as np
from numpy import dot
from numpy.linalg import norm
import json


from libs.vectors import Vector
from libs.configs import Config


EVALUATION_PATH = Config.ROOT_PATH+"/data/evaluations/"
EVALUATION_PATH_V2 = Config.ROOT_PATH+"/data/evaluations_v2/"
EVALUATION_PATH_V3 = Config.ROOT_PATH+"/data/evaluations_v3/"

class Evaluation(object):
    @staticmethod
    def do(requires, model, sample_cases, test_cases, num_of_true, limit, size=100):
        test_case_vector_obj = Vector(contexts=test_cases, model=model, size=size)
        test_case_vector = test_case_vector_obj.vector
        positive = 0
        true_positive = 0
        for sample_case in sample_cases:
            sample_case_vector_obj = Vector(contexts=sample_case, model=model, size=size)
            sample_case_vector = sample_case_vector_obj.vector
            try:
                result = dot(test_case_vector, sample_case_vector)/(norm(test_case_vector)*norm(sample_case_vector))
            except Exception as e:
                print(e)
            else:
                if result >= limit:
                    positive += 1
                    comps = dict()
                    for require in requires:
                        comps[require] = 0
                    for word in sample_case:
                        for require in requires:
                            if require in word:
                                comps[require] += 1
                    flag = 1
                    for check in comps.values():
                        if check <= 0:
                            flag = 0
                    if flag == 1:
                        true_positive += 1
        
        # print("limit:", limit)
        # print("positive:", positive)
        # print("true_positive:", true_positive)
        try:
            recall = true_positive/num_of_true
        except:
            recall = 0
        try:
            precision = true_positive/positive
        except:
            precision = 0
        # print("recall:", recall)
        # print("precition:", precision)
        try:
            f_measure = (2*recall*precision)/(recall+precision)
        except:
            f_measure = 0
        # print("f_measure:", f_measure)
        evaluation = {
            "limit": limit,
            "positive": positive,
            "true_positive": true_positive,
            "recall": recall,
            "precition": precision,
            "f_measure": f_measure
        }
        return evaluation
        

    @staticmethod
    def count_true(requires, cases):
        """
            - true?????????????????????
        """
        count = 0
        for case in cases:
            comps = dict()
            for require in requires:
                comps[require] = 0
            for word in case:
                for require in requires:
                    if require in word:
                        comps[require] += 1
            flag = 1
            for check in comps.values():
                if check <= 0:
                    flag = 0
            if flag == 1:
                count += 1
        return count

    @staticmethod
    def to_file(parameter, evaluations, sample, folder):
        file_name = "sample-{}.".format(sample)
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            sample=sample,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            source=parameter["source"],
            run=parameter["run"]
        )
        file_path = EVALUATION_PATH+folder+"/"+file_name
        with open(file_path, mode="w") as f:
            json.dump(evaluations, f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def to_file_v2(parameter, evaluations, sample, folder):
        file_name = "sample-{}.".format(sample)
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            sample=sample,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            source=parameter["source"],
            run=parameter["run"]
        )
        file_path = EVALUATION_PATH_V2+folder+"/"+file_name
        with open(file_path, mode="w") as f:
            json.dump(evaluations, f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def to_file_v3(parameter, evaluations, sample, folder):
        file_name = "sample-{}.".format(sample)
        file_name = "sample-{sample}.sg-{sg}.size-{size}.min_count-{min_count}.window-{window}.source-{source}.run-{run}.json".format(
            sample=sample,
            sg=parameter["sg"],
            size=parameter["size"],
            min_count=parameter["min_count"],
            window=parameter["window"],
            source=parameter["source"],
            run=parameter["run"]
        )
        file_path = EVALUATION_PATH_V3+folder+"/"+file_name
        with open(file_path, mode="w") as f:
            json.dump(evaluations, f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def get_similar_objs(requires, model, sample_cases, test_cases, num_of_true, limit, size=100):
        test_case_vector_obj = Vector(contexts=test_cases, model=model, size=size)
        test_case_vector = test_case_vector_obj.vector
        positive = 0
        true_positive = 0
        result_obj = dict()
        for idx, sample_case in sample_cases.items():
            sample_case_vector_obj = Vector(contexts=sample_case, model=model, size=size)
            sample_case_vector = sample_case_vector_obj.vector
            try:
                result = dot(test_case_vector, sample_case_vector)/(norm(test_case_vector)*norm(sample_case_vector))
            except Exception as e:
                print(e)
            else:
                if result >= limit:
                    # result.append(idx)
                    result_obj[idx] = result
        
        return result_obj
    

    @staticmethod
    def get_similar_objs_v2(requires, model, sample_cases, test_cases, num_of_true, limit, size=100):
        test_case_vector_obj = Vector(contexts=test_cases, model=model, size=size)
        test_case_vector = test_case_vector_obj.vector
        positive = 0
        true_positive = 0
        result_obj = dict()
        for idx, sample_case in sample_cases.items():
            print()
            pprint.pprint(sample_case)
            sample_case_vector_obj = Vector(contexts=sample_case, model=model, size=size)
            sample_case_vector = sample_case_vector_obj.vector
            try:
                result = dot(test_case_vector, sample_case_vector)/(norm(test_case_vector)*norm(sample_case_vector))
            except Exception as e:
                print(e)
            else:
                if result >= limit:
                    # result.append(idx)
                    result_obj[idx] = result
        
        return result_obj
                    




