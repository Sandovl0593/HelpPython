"""Un ejemplo del uso del paquete 'colorsys': 
-- Realiza conversiones bidireccionales de color."""
import colorsys as cys
import imageio
import numpy as np

def leer_imagen(ruta:str):
    """La funciopn recibe la ruta de una imagen BMP y retorna una tupla de
    tres dimensiones con el mapa de bits de la imagen y retorna como lista numpy."""
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d

def deteccion_color(ruta:str):
    lista_3d = leer_imagen(ruta)
    dimY = len(lista_3d)
    dimX = len(lista_3d[0])
    count = 0
    for fila in lista_3d:
        for color in fila:
            h,s,v = color
            newnum = cys.rgb_to_hsv(h, s, v)
            if newnum[0] > 200 or newnum[1] > 200 or newnum[2] > 200:
                count += 1
    porcMar = count*100/(dimX*dimY)
    print("A Maria le apreció en un:", round(porcMar, 2), "% de tu imagen")

# deteccion_color("torreEiffel.bmp")