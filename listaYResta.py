
def devolucionMatriz(matrices_completas):
    iterador4=0

    for i in matrices_completas:
        iterador3=0
        for j in i:
            iterador2=0
            for k in j:
                iterador=0
                matrices_completas[iterador4][iterador3][iterador2] = list(matrices_completas[iterador4][iterador3][iterador2])
                for h in k:
                    nuevo_valor = h - 127
                    matrices_completas[iterador4][iterador3][iterador2][iterador] = nuevo_valor
                    iterador=iterador+1
                matrices_completas[iterador4][iterador3][iterador2] = tuple(matrices_completas[iterador4][iterador3][iterador2])
                iterador2=iterador2+1
            iterador3=iterador3+1
        iterador4=iterador4+1

    return matrices_completas