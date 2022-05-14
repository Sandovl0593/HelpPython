"""Un ejemplo del uso del paquete 'cv2': 
-- Denominado 'openCV', brinda edicion de imagenes y modelos de graficos."""
import cv2
import matplotlib.pyplot as plt
import numpy as np

lil = r"C:\Users\ASUS\Desktop\ApCodes\Python\HelpPython\PackagesUse\torreEiffel.bmp"

imagen_open = cv2.imread(lil)
cv2.imshow('image', imagen_open)
cv2.waitKey(0)
# cv2.destroyAllWindows()