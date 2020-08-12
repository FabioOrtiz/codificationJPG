def devolverMatrices(matrices):
    provisional = []
    verificador = 0
    matrices_completas = []

    for i in matrices:
        for j in i:
            if verificador < 8:
                provisional.insert(len(provisional), j)
                verificador = verificador + 1
                if verificador == 8:
                    matrices_completas.insert(len(matrices_completas), provisional)
                    provisional=[]
                    verificador = 0

    return matrices_completas