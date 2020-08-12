
def multiplicacionMatriz(matrizEscalar, matrices_completas):
    matriz = matrices_completas
    matriz_d = []
    for iterador3 in range(0, len(matrices_completas)):
        matriz_individual = []
        for iterador2 in range(0, 8):
            linea = []
            for iterador4 in range(0, 8):
                conversion = []
                for iterador5 in range(0, 3):
                    valor_acumulado = 0
                    for iterador in range(0, 8):
                        valor = matrizEscalar[iterador2][iterador] * matriz[iterador3][iterador][iterador4][iterador5]
                        valor_acumulado = valor + valor_acumulado
                    valor_acumulado = round(valor_acumulado, 2)
                    conversion.append(valor_acumulado)
                linea.append(conversion)
            matriz_individual.append(linea)
        matriz_d.append(matriz_individual)

    return matriz_d