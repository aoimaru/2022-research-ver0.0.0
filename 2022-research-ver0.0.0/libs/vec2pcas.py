
from libs.configs import Config
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import numpy as np

class Vec2PCA():
    @staticmethod
    def do(model, file_name):
        vectors = list()
        for word in model.wv.index2word:
            vector = model.wv[word]
            vectors.append(vector)
        pca = PCA(n_components=2)
        pca.fit(vectors)
        data_pca = pca.transform(vectors)
        fig=plt.figure(figsize=(20,12),facecolor='w')

        plt.rcParams["font.size"] = 10
        cnt = 0
        while cnt < len(model.wv.index2word):
            #点プロット
            plt.plot(data_pca[cnt][0], data_pca[cnt][1], ms=5.0, zorder=2, marker="x")
        
            #文字プロット
            plt.annotate(model.wv.index2word[cnt], (data_pca[cnt][0], data_pca[cnt][1]), size=5)
        
            cnt += 1

        file_path = Config.ROOT_PATH+"/data/pca/"+file_name
        plt.savefig(file_path)
    
    @staticmethod
    def _patch(model, training_datas):
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
        pca = PCA(n_components=2)
        pca.fit(vectors)
        data_pca = pca.transform(vectors)
        fig=plt.figure(figsize=(80,48),facecolor='w')

        plt.rcParams["font.size"] = 40
        cnt = 0
        while cnt < len(vocabs):
            #点プロット
            plt.plot(data_pca[cnt][0], data_pca[cnt][1], ms=5.0, zorder=2, marker="x")
        
            #文字プロット
            plt.annotate(str(cnt), (data_pca[cnt][0], data_pca[cnt][1]), size=5)
        
            cnt += 1

        file_path = Config.ROOT_PATH+"/data/pca/"+"sample.png"
        # plt.savefig(file_path)
        for idx, vocab in enumerate(vocabs):
            if idx == 1310:
                print(idx, ":", vocab)
            if idx == 1148:
                print(idx, ":", vocab)
