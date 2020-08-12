import getImage
import getDataImage
import splitFiles
import matricesGenerales
import matricesCompletas
import listaYResta
import matrizDerecha
import matrizIzquierda
import cuantificacionDivision
import lectura
import huffman
import traduccion
import union
import unirLineas
import cuantificacionMultiplicacion
import suma
import conversionArray
import createImage

# Insertar Imagen y gets de caracteristicas de la imagen

image = getImage.insertarImagen("./imgs/Prueba.tiff")
# print(image)

# Caracteristicas de la imagen

dImage = getDataImage.caracteristicas("./imgs/Prueba.tiff")
# print(dImage)

# Division en Filas

filas = splitFiles.divisionFilas(image)
# print(filas)

# Division en Matrices Generales

matriz = matricesGenerales.devolucionMatrices(filas)

# Reunion en Matrices Completas

matriz = matricesCompletas.devolverMatrices(matriz)

#print(matriz[0][0])

# PROCESAMIENTO

# Se pasa a lista y restamos 127

matriz = listaYResta.devolucionMatriz(matriz)

# print(matriz[0][0])

# CONVERSION COSENO ORIGINAL * MATRIZ * INVERSA

matriz_original =[[0.3536,  0.3536,  0.3536,  0.3536,  0.3536,  0.3536,   0.3536,  0.3536],
                  [0.4904,  0.4157,  0.2778,  0.0975, -0.0975, -0.2778,  -0.4157, -0.4904],
                  [0.4619,  0.1913, -0.1913, -0.4619, -0.4619, -0.1913,   0.1913,  0.4619],
                  [0.4157, -0.0975, -0.4904, -0.2778,  0.2778,  0.4904,   0.0975, -0.4157],
                  [0.3536, -0.3536, -0.3536,  0.3536,  0.3536, -0.3536,  -0.3536,  0.3536],
                  [0.2778, -0.4904,  0.0975,  0.4157, -0.4157, -0.0975,   0.4904, -0.2778],
                  [0.1913, -0.4619,  0.4619, -0.1913, -0.1913,  0.4619,  -0.4619,  0.1913],
                  [0.0975, -0.2778,  0.4157, -0.4904,  0.4904, -0.4157,   0.2778, -0.0975]
]


matriz = matrizDerecha.multiplicacionMatriz(matriz_original, matriz)

# print(len(matriz))
# print(matriz[0][0])

matriz_inversa = [[0.356,  0.4904,  0.4619,  0.4157,  0.3536,  0.2778,  0.1913,  0.0975],
                  [0.356,  0.4157,  0.1913, -0.0975, -0.3536, -0.4904, -0.4619, -0.2778],
                  [0.356,  0.2778, -0.1913, -0.4904, -0.3536,  0.0975,  0.4619,  0.4157],
                  [0.356,  0.0975, -0.4619, -0.2778,  0.3536,  0.4157, -0.1913, -0.4904],
                  [0.356, -0.0975, -0.4619,  0.2778,  0.3536, -0.4157, -0.1913,  0.4904],
                  [0.356, -0.2778, -0.1913,  0.4904, -0.3536, -0.0975,  0.4619, -0.4157],
                  [0.356, -0.4157,  0.1913,  0.0975, -0.3536,  0.4904, -0.4619,  0.2778],
                  [0.356, -0.4904,  0.4619, -0.4157,  0.3536, -0.2778,  0.1913, -0.0975]
                  ]

matriz = matrizIzquierda.multiplicacionMatriz(matriz_inversa, matriz)

# print(len(matriz))
# print(matriz[0][0])

# CUANTIFICACION

matriz_cuantificacion = [[16, 11, 10, 16,  24,  40,  51,  61],
                         [12, 12, 14, 19,  26,  58,  60,  55],
                         [14, 13, 16, 24,  40,  57,  69,  56],
                         [14, 17, 22, 29,  51,  87,  80,  62],
                         [18, 22, 37, 56,  68, 109, 103,  77],
                         [24, 35, 55, 64,  81, 104, 113,  92],
                         [49, 64, 78, 87, 103, 121, 120, 101],
                         [72, 92, 95, 98, 112, 100, 103,  99]
]

matriz = cuantificacionDivision.divisionCuantificacion(matriz, matriz_cuantificacion)

# print(len(matriz))
# print(matriz[0][0])

# LECTURA EN LISTA DE LOS DATOS

matriz = lectura.modoLectura(matriz)
# print(len(matriz[0]))
# print(matriz[0][0])

codificacion = huffman.codificar(matriz)

codigo = codificacion[0]
enciclopedia = codificacion[1]

# print(codigo)
# print(enciclopedia[0])

# Regresar Enciclopedia
def devolver_enciclopedia(self):
        return enciclopedia

# INSCRIPCION

# file = open("./txt/prueba.txt", "w")
# file.write(codigo)

# Traduccion

codigoTraducido = traduccion.traducir(codigo, enciclopedia)

# print(len(codigoTraducido[0][0]))
# print(codigoTraducido[0][0])

# UNION RGB

matriz = union.union(codigoTraducido)

# print(len(matriz[0][0]))
# print(matriz[0][0])

matriz = unirLineas.union(matriz)

# print(len(matriz[0][0]))
# print(matriz[0][0])
# print(matriz[0][0][0])

# CUANTIFICACION MULTIPLICAR

matriz = cuantificacionMultiplicacion.multiplicar(matriz, matriz_cuantificacion)
# print(matriz[0][0])

# CUANTIFICACION COSENO INVERSA:   INVERSA * MATRIZ * ORIGINAL

matriz = matrizDerecha.multiplicacionMatriz(matriz_inversa, matriz)
# print(matriz[0][0])

matriz = matrizIzquierda.multiplicacionMatriz(matriz_original, matriz)
# print(matriz[0][0])

# SUMA 127

matriz = suma.suma(matriz)
# print(matriz[0][0])

# CONVERSION ARRAY

ancho = dImage[2]

data = conversionArray.convertir(matriz, ancho)
# print(data)
# print(len(data))

# CREATE IMAGE

# createImage.crearImagen(data, dImage[0], dImage[1])