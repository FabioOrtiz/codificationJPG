def divisionFilas(lista):
    provisional = []
    verificador = 0
    filas = []
    for i in lista:
        if verificador != 7:
            provisional.insert(len(provisional), i)
            verificador = verificador + 1
        elif verificador == 7:
            provisional.insert(len(provisional), i)
            filas.insert(len(filas), provisional)
            provisional = []
            verificador=0

    return filas