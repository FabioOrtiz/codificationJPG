def devolucionMatrices(filas):

    verificador = 0
    matriz0 = []
    matriz1 = []
    matriz2 = []
    matriz3 = []
    matriz4 = []
    matriz5 = []
    matriz6 = []
    matriz7 = []
    matrices = []

    for i in filas:
        if verificador == 0:
            matriz0.insert(len(matriz0), i)
            verificador = verificador + 1
        elif verificador == 1:
            matriz1.insert(len(matriz1), i)
            verificador = verificador + 1
        elif verificador == 2:
            matriz1.insert(len(matriz1), i)
            verificador = verificador + 1
        elif verificador == 3:
            matriz1.insert(len(matriz1), i)
            verificador = verificador + 1
        elif verificador == 4:
            matriz1.insert(len(matriz1), i)
            verificador = verificador + 1
        elif verificador == 5:
            matriz1.insert(len(matriz1), i)
            verificador = verificador + 1
        elif verificador == 6:
            matriz1.insert(len(matriz1), i)
            verificador = verificador + 1
        elif verificador == 7:
            matriz1.insert(len(matriz1), i)
            verificador = 0

    matrices.insert(len(matrices), matriz0)
    matrices.insert(len(matrices), matriz1)
    matrices.insert(len(matrices), matriz2)
    matrices.insert(len(matrices), matriz3)
    matrices.insert(len(matrices), matriz4)
    matrices.insert(len(matrices), matriz5)
    matrices.insert(len(matrices), matriz6)
    matrices.insert(len(matrices), matriz7)

    return matrices