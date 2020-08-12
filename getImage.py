from PIL import Image

# Insercion

def insertarImagen(ruta):
    myImage = Image.open(ruta)
    image_sequence = myImage.getdata()
    image_list_pixels = list(image_sequence)
    return image_list_pixels
