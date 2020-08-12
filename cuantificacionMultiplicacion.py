def multiplicar(matriz_prueba, matriz_cuantificacion):
    iterador4=0
    for i in matriz_prueba:
        iterador3=0
        for j in i:
            iterador2=0
            for k in j:
                iterador=0
                for h in k:
                    matriz_prueba[iterador4][iterador3][iterador2][iterador] = round(matriz_prueba[iterador4][iterador3][iterador2][iterador]*matriz_cuantificacion[iterador3][iterador2])
                    iterador=iterador+1
                iterador2=iterador2+1
            iterador3=iterador3+1
        iterador4=iterador4+1

    return matriz_prueba