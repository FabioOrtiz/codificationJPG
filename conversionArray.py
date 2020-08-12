def convertir(matriz, ancho):
    ancho = int(ancho)
    cantidad = len(matriz[0]) * len(matriz)
    data = []
    iterador2 = 0
    iterador = 0

    inicial = 0
    comprobante = 0
    i = 0
    while i < cantidad:
        for j in range(0, len(matriz[0][0])):
            valor = tuple(matriz[iterador2][iterador][j])
            data.append(valor)
        if comprobante < ancho-1:
            comprobante = comprobante + 1
            iterador2 = iterador2 + 1
        else:
            iterador = iterador + 1
            comprobante = 0
            iterador2 = inicial

            if iterador == len(matriz[0]):
                iterador = 0
                iterador2 = ancho + iterador2
                inicial = inicial + ancho
        i = i + 1
    return data