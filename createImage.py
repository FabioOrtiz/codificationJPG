import numpy as np
from PIL import Image

def crearImagen(data, hh, w):
    data = np.asarray(data)
    data = np.reshape(data, (hh, w, 3))
    img = Image.fromarray(data.astype('uint8'), 'RGB')
    img.save('./imgs/Prueba.jpg')