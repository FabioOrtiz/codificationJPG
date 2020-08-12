def union(matriz_decodificada):
    linea = []
    matriz_dividida = []
    matriz_resultado = []
    iterador = 0
    for i in matriz_decodificada:
        iterador3 = 0
        iterador4 = 0
        while iterador4<8:
            iterador2 = 0
            while iterador2 < 8:
                agregar = matriz_decodificada[iterador][iterador3]
                linea.append(agregar)
                iterador2 = iterador2 + 1
                iterador3 = iterador3 + 1
            iterador4 = iterador4 + 1
            matriz_dividida.append(linea)
            linea = []
        iterador = iterador + 1
        matriz_resultado.append(matriz_dividida)
        matriz_dividida = []

    return matriz_resultado