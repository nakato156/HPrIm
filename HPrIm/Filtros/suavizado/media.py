import numpy as np
from ..procesamiento import FEspacial

class MascaraMedia:
    FUsual = (1/9) * np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ])
    F16 = (1/16) * np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1],
    ])

class FMedia:
    def __init__(self, matriz:np.ndarray[np.ndarray] | list[list]) -> None:
        self.matriz = np.array(matriz)
        self.n = self.matriz.shape[0]
    
    def ejecutar(self, mascara:np.ndarray[np.ndarray] | list[list] = MascaraMedia.FUsual) -> np.ndarray:
        self.resultado = FEspacial(self.matriz).aplicar_filtro(mascara)
        return self.resultado