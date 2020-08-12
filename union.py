def union(escrito):
    matriz_decodificada = []
    entrada = []
    matriz_entradas = []
    iterador = 0

    for i in escrito:
        iterador2 = 0
        while iterador2 < 64:
            entrada.append(escrito[iterador][0][iterador2])
            entrada.append(escrito[iterador][1][iterador2])
            entrada.append(escrito[iterador][2][iterador2])
            matriz_entradas.append(entrada)
            entrada = []
            iterador2 = iterador2 + 1
        matriz_decodificada.append(matriz_entradas)
        matriz_entradas = []
        iterador = iterador + 1

    return matriz_decodificada