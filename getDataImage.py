import cv2


def caracteristicas(ruta):
    data = []
    img = cv2.imread(ruta)
    height, width, channels = img.shape
    matrices_largo = width / 8
    matrices_bajo = height / 8
    data.append(height)
    data.append(width)
    data.append(int(matrices_largo))
    data.append(int(matrices_bajo))
    return data
