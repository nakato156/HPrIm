from ..procesamiento import FEspacial
import numpy as np

class MascaraLaplaciana:
    F8 = [
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ]
    F4 = [
        [0, -1, 0,],
        [-1, 4, -1,],
        [0, -1, 0,]
    ]


class FLaplaciano:
    """
    Clase que implementa el filtrado Laplaciano
    """
    
    def __init__(self, matriz: np.ndarray, mascara: MascaraLaplaciana | np.ndarray[np.ndarray] | list[list]):
        self.matriz = matriz
        self.mascara = mascara
        self.filtro:FEspacial = FEspacial(self.matriz)
    
    def ejecutar(self) -> np.ndarray:
        self.resultado = self.filtro.aplicar_filtro(self.mascara)
        return self
    
    def get_resultado(self) -> np.ndarray:
        return self.resultado
    
    def reescalar(self, rango:tuple[int, int]):
        self.resultado = self.filtro.reescalar(*rango)
        return self

    def __repr__(self) -> str:
        if getattr(self, "resultado"):
            return f"Matriz con filtro:\n{self.resultado}"
        return "No se ha ejecutado el filtro"