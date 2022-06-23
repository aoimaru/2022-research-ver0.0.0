import numpy as np


class Vector(object):
    def __init__(self, contexts, model, size=100):
        """
        """
        self._contexts = contexts
        self._model = model
        self._size = size

        tokens = list()
        for context in contexts:
            tokens.extend(context)
        vector = np.zeros(self._size)
        ignores = list()
        for token in tokens:
            try:
                vec = model.wv[token]
            except Exception as e:
                print(e)
                ignores.append(token)
            else:
                vector += vec
        self._ignores = ignores
        self._vector = vector
    
    @property
    def vector(self):
        pass

    @vector.getter
    def vector(self):
        return self._vector
    
    @property
    def contexts(self):
        pass
    
    @contexts.getter
    def contexts(self):
        return self._contexts


        
        


