import numpy as np

class FEspacial:
    def __init__(self, matriz: list[list] | np.ndarray):
        self.matriz: np.ndarray = np.array(matriz)
        if self.matriz.shape[0] != self.matriz.shape[1]:
            raise ValueError("La matriz no es cuadrada")
        self.size = self.matriz.shape[0]

    @classmethod
    def get_vecinos(cls, matriz, rango:tuple[int, int]) -> list:
        return FEspacial(matriz)._get_vecinos(*rango)

    def _get_vecinos(self, i:int, j:int) -> list:
        vecinos = []
        for d_i, d_j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (+1, 0), (1, 1)):
            if 0 <= i+d_i < len(self.matriz) and 0 <= j+d_j < len(self.matriz[i]):
                vecinos.append(self.matriz[i+d_i][j+d_j])
            else: vecinos.append(0)
        return vecinos

    def aplicar_filtro(self, mascara: list[list]) -> np.ndarray :
        n = self.size
        matriz_cambiada = np.zeros((n,n))
        
        for i in range(n):
            for j in range(n):
                vecinos:list = self._get_vecinos(i, j)
                vecinos.insert(4, self.matriz[i][j])
                
                vecinos_arr = np.array(vecinos).reshape((3,3))
                resultado = vecinos_arr * mascara
                
                matriz_cambiada[i][j] = np.sum(resultado)
        return matriz_cambiada
    
    def reescalar(self, x:int, y:int) -> np.ndarray:
        maximo = np.max(self.matriz)
        minimo = np.min(self.matriz)

        pendiente = (y - x) / (maximo - minimo)
        b = (x - pendiente) * minimo
        
        print(f"pendiente:{y-x}/{maximo-minimo}\necuacion: y = {pendiente} * r + {b}")
        
        matriz_reescalada = pendiente * self.matriz + b
        matriz_reescalada = np.round(matriz_reescalada).astype(int)
        return matriz_reescalada
