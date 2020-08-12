def traducir(lectura, libro):
    palabra = ''

    traduccion = []
    texto = []
    iterador = 0
    escrito = []

    # print(lectura)

    for i in lectura:
        palabra = palabra + i
        iterador2 = 0

        while iterador2 < len(libro[iterador]):
            if palabra == libro[iterador][iterador2][1]:
                traduccion.append(libro[iterador][iterador2][0])
                palabra = ''
            iterador2 = iterador2 + 1
        if len(traduccion) == 64:
            iterador = iterador + 1
            texto.append(traduccion)
            traduccion = []
        if len(texto)== 3:
            escrito.append(texto)
            texto = []

    return escrito