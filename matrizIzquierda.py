def multiplicacionMatriz(matrizEscalar, matriz):
    matriz_nueva2 = []
    for iterador4 in range(0, len(matriz)):
        matriz_individual = []
        for iterador3 in range(0, 8):
            linea = []
            for iterador2 in range(0, 8):
                valor_acumulado1 = 0
                valor_acumulado2 = 0
                valor_acumulado3 = 0
                individual = []
                for iterador in range(0,8):
                    valor = matrizEscalar[iterador][iterador2] * matriz[iterador4][iterador3][iterador][0]
                    valor_acumulado1 = valor + valor_acumulado1
                    valor = matrizEscalar[iterador][iterador2] * matriz[iterador4][iterador3][iterador][1]
                    valor_acumulado2 = valor + valor_acumulado2
                    valor = matrizEscalar[iterador][iterador2] * matriz[iterador4][iterador3][iterador][2]
                    valor_acumulado3 = valor + valor_acumulado3
                individual.append(round (valor_acumulado1, 2))
                individual.append(round(valor_acumulado2, 2))
                individual.append(round(valor_acumulado3, 2))
                linea.append(individual)
            matriz_individual.append(linea)
        matriz_nueva2.append(matriz_individual)
    return matriz_nueva2