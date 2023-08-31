import numpy as np
from ..procesamiento import FEspacial

class FMediana:
    def __init__(self, matriz: np.ndarray):
        self.matriz = matriz
        self.n = matriz.shape[0]

    def ejecutar(self) -> np.ndarray:
        nueva_matriz = np.zeros(self.matriz.shape)
        for f in range(self.n):
            for c in range(self.n):
                vecinos:list = FEspacial.get_vecinos(self.matriz, (f, c))
                vecinos.insert(4,  self.matriz[f, c])
                nueva_matriz[f, c] = np.median(np.array(vecinos), axis=0)
        return nueva_matriz