from .agudizamiento import FLaplaciano, Sobel, MascarasSobel
from .suavizado import FMedia, FMediana, MascaraMedia
import numpy as np

class Filtro:
    def __init__(self, matriz:np.ndarray[np.ndarray] | list[list]):
        self.matriz = np.array(matriz)
    
    def laplaciano(self) -> FLaplaciano:
        self.resultado = FLaplaciano(self.matriz).ejecutar()
        return self.resultado
    
    def soble(self, mascara:np.ndarray[np.ndarray] | list[list] = MascarasSobel.Fy) -> Sobel:
        self.resultado = Sobel(self.matriz).ejecutar(mascara)
        return self.resultado

    def media(self, mascara:np.ndarray[np.ndarray] | list[list] = MascaraMedia.FUsual) -> np.ndarray:
        self.resultado = FMedia(self.matriz).ejecutar(mascara)
        return self.resultado
    
    def mediana(self) -> np.ndarray:
        self.resultado = FMediana(self.matriz).ejecutar()
        return self.resultado