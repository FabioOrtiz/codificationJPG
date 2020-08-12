
def modoLectura(matriz):
    cantidad = len(matriz)
    iterador = 0
    color = []
    trio = []
    matriz_final = []

    while iterador < cantidad:
        iterador2 = 0

        while iterador2 < 3:
            iterador3 = 0
            iterador4 = 0
            iterador5 = 0
            while iterador5 < 64:
                valor = matriz[iterador][iterador4][iterador3][iterador2]
                if iterador3 == 7:
                    iterador4 = iterador4 + 1
                    iterador3 = 0
                else:
                    iterador3 = iterador3 + 1
                color.append(valor)
                iterador5 = iterador5 + 1
            trio.append(color)
            color = []
            iterador2 = iterador2 + 1
        matriz_final.append(trio)
        trio = []
        iterador = iterador + 1
    return matriz_final