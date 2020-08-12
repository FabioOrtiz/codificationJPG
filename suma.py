def suma(matriz_nueva2):
    iterador = 0
    for i in matriz_nueva2:
        iterador2 = 0
        for j in i:
            iterador3 = 0
            for k in j:
                iterador4 = 0
                for h in k:
                    matriz_nueva2[iterador][iterador2][iterador3][iterador4] = round (matriz_nueva2[iterador][iterador2][iterador3][iterador4] + 127)

                    if matriz_nueva2[iterador][iterador2][iterador3][iterador4]>255:
                        matriz_nueva2[iterador][iterador2][iterador3][iterador4] = 255

                    iterador4 = iterador4 + 1
                iterador3 = iterador3 + 1
            iterador2 = iterador2 + 1
        iterador = iterador + 1

    return matriz_nueva2