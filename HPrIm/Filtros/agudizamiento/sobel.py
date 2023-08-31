import numpy as np
from ..procesamiento import FEspacial

class MascarasSobel:
    Fy = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]

    Fx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

class Sobel:
    def __init__(self, matriz: list[list]) -> None:
        self.matriz = np.array(matriz)
        self.n = self.matriz.shape[0]
        self.__filtro:FEspacial = FEspacial(self.matriz)
    
    def ejecutar(self, mascara: list[list] ) -> np.ndarray:
        self.resultado = self.__filtro.aplicar_filtro(mascara)
        return self.resultado
    
    def reescalar(self, rango:tuple[int, int]):
        self.resultado = self.__filtro.reescalar(*rango)
        return self