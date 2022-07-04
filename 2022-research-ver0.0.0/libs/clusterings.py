
import pprint
import json
from collections import defaultdict
from gensim.models.keyedvectors import KeyedVectors
from sklearn.cluster import KMeans

from libs.configs import Config


"""
    - patch
"""
import numpy as np


class Clustering(object):
    @staticmethod
    def do(model, file_name, n_clusters):
        vocab = list(model.wv.vocab.keys())
        vectors = [model.wv[word] for word in vocab]
        kmeans_model = KMeans(n_clusters=n_clusters, verbose=1, random_state=42, n_jobs=-1)
        kmeans_model.fit(vectors)
        
        cluster_labels = kmeans_model.labels_
        cluster_to_words = defaultdict(list)
        for cluster_id, word in zip(cluster_labels, vocab):
            cluster_to_words[str(cluster_id)].append(word)
        pprint.pprint(cluster_to_words, indent=4)

        file_path = Config.ROOT_PATH+"/data/clustering/"+file_name
        with open(file_path, mode="w") as f:
            json.dump(cluster_to_words, f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def _patch(model, training_datas, n_clusters=10):
        vocabs = list()
        vectors = list()
        for training_data in training_datas:
            vector = np.zeros(100)
            vocab = ""
            for words in training_data:
                for word in words:
                    try:
                        vec = model.wv[word]
                    except Exception as e:
                        print(e)
                    else:
                        vector += vec
                        vocab += " "+word
            print(vocab)
            print(vector)
            vocabs.append(vocab)
            vectors.append(vector)
        
        kmeans_model = KMeans(n_clusters=n_clusters, verbose=1, random_state=42, n_jobs=-1)
        kmeans_model.fit(vectors)
        
        cluster_labels = kmeans_model.labels_
        cluster_to_words = defaultdict(list)
        for cluster_id, word in zip(cluster_labels, vocabs):
            cluster_to_words[str(cluster_id)].append(word)
        pprint.pprint(cluster_to_words, indent=4)

        file_path = Config.ROOT_PATH+"/data/clustering/"+"sample8.json"
        with open(file_path, mode="w") as f:
            json.dump(cluster_to_words, f, ensure_ascii=False, indent=4)
                



