
def codificar(matriz):
    lista_numeros = []
    parrafo = ''
    devolucion = []
    # Capturar todos los valores de la lista

    iteraciones = len(matriz) * len(matriz[0])

    it = 0
    it2 = 0
    it3 = 0

    libro = []

    while it < iteraciones:
        while it2 < len(matriz):
            it3 = 0
            while it3 < len(matriz[0]):
                for i in matriz[it2][it3]:
                    valor = i
                    if i in lista_numeros:
                        valor = i
                    else:
                        lista_numeros.append(i)

                # Organizar de mayor a menor de acuerdo a su peso

                # Crearemos nodos

                numero = []
                elemento = []
                for i in lista_numeros:
                    cantidad = matriz[it2][it3].count(i)
                    elemento.append(i)
                    elemento.append(cantidad)
                    numero.append(elemento)
                    elemento = []

                # Organizar de mayor a menor

                lista = numero
                for dato in range(len(lista) - 1, 0, -1):
                    for i in range(dato):
                        if lista[i][1] > lista[i + 1][1]:
                            temp = lista[i]
                            lista[i] = lista[i + 1]
                            lista[i + 1] = temp

                lista.reverse()
                # Lista Ordenada
                diccionario = []

                palabra = []

                letra = '0'
                clave = 2
                indicador = 1

                for i in lista:
                    if lista.index(i) == 0:
                        palabra.append(i[0])
                        palabra.append('1')
                        diccionario.append(palabra)
                        palabra = []
                    else:
                        if lista.index(i) % 2:
                            temporal = letra + '0'
                            palabra.append(i[0])
                            palabra.append(temporal)
                            diccionario.append(palabra)
                            palabra = []
                            letra = letra + '1'
                            referencia2 = letra
                        else:
                            temporal = letra + '1'
                            palabra.append(i[0])
                            palabra.append(temporal)
                            diccionario.append(palabra)
                            palabra = []
                            letra = letra + '0'
                            referencia4 = letra

                if len(diccionario) % 2 !=0:
                    diccionario[len(diccionario)-1][1] = referencia2
                else:
                    try:
                        diccionario[len(diccionario) - 1][1] = referencia4
                    except:
                        referencia2 = referencia2[0:len(referencia2)-1]
                        referencia2 = referencia2 + '0'
                        diccionario[len(diccionario) - 1][1] = referencia2


                # Reemplazar
                iterador5=0
                while iterador5 < 64:
                    condicion = 0
                    iterador4 = 0
                    h = matriz[it2][it3][iterador5]
                    while condicion == 0:
                        if h == diccionario[iterador4][0]:
                            palabra = diccionario[iterador4][1]
                            condicion = 1
                        else:
                            iterador4 = iterador4 + 1
                    matriz[it2][it3][iterador5] = palabra
                    iterador5 = iterador5 + 1

                # Pasar a un sólo Array

                libro.append(diccionario)

                frase = ''

                for i in matriz[it2][it3]:
                    frase = frase + str(i)
                #print(frase)
                parrafo= parrafo + frase
                it3 = it3 + 1
                lista_numeros = []
            it2 = it2 + 1
        it = it +1
    devolucion.append(parrafo)
    devolucion.append(libro)
    return devolucion