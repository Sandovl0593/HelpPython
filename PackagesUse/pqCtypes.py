"""Un ejemplo del uso del paquete 'ctypes': 
-- Proporciona funciones foráneas desde librerias C/C++ y otorga funcionalidades con ellos."""
import math, time
from ctypes.wintypes import *
from ctypes import *

def MoverCursor():
    "Mueve el cursor automaticamente en foma de espiral"
    for i in range(200):
        x = int(500 + math.cos(i / 5) * i)
        y = int(500 + math.sin(i / 5) * i)
        windll.user32.SetCursorPos(x, y)
        time.sleep(1)

def PresentWInput(contenido, resp):
    "Presenta una ventana de formato de cebecera de Windows con el input"
    prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
    paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)
    MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)
    return MessageBox(0, contenido, resp, 0)

def medicion_dodecaedro(arista):
    dll = CDLL("./mainDodec/dodecaedro.dll")
    dll.med_Dodecaedro.argtypes = c_float
    dll.med_Dodecaedro.restype = [c_float, c_float]

    dll.minor_rest.argtypes  = [c_float, c_float]
    dll.minor_rest.restype = c_float

    resp = dll.med_Dodecaedro(arista)
    result = dll.minor_rest(resp[0], resp[1])
    PresentWInput("El resultado sería "+str(result), "Respuesta")