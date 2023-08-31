def ecualizar_histograma(histograma:dict, num_canales) -> dict:
    total:int = sum(histograma.values())
    L = num_canales - 1
    ecualizado = {}
    acumulado = 0
    for rk, nk in histograma.items():
        pr = round(nk / total, 3)
        acumulado += round(L * pr, 3)
        sk = round(acumulado)
        if sk in ecualizado: ecualizado[sk] += pr
        else: ecualizado[sk] = pr
    return ecualizado
