"Un ejemplo del uso del paquete colorama"
from colorama import *
import random as rd

num = int(input("Edad: "))
init()

accions = {"ocioMinor": ["Jugar con tus amigos", "Ver television",
            "Jugar videojuegos", "Leer historias ficticias"],
            "ocioAdol": ["Divertir en fiestas", "Jugar videojuegos",
            "Ser visor amante", "Realizar apuestas"],
            "prodMinor": ["Realizar actos cordiales", "Realizar tus tareas",
            "Ayudar a tus padres", "Realizar ejercicios"],
            "prodAdol": ["Estudiar horas productivas", "Crear un emprendimiento",
            "Ahorrar dinero", "Realizar actos valorables", "Realizar ejrcicios"]}

def valid(opcions):
    eleg = rd.choice(opcions)
    accRd = rd.choice(accions[eleg])
    print(Fore.CYAN +f"Tu accion es: {accRd} ?")
    booll = input(Fore.YELLOW +"si o no?  ").upper()
    if (booll == "SI" and eleg == opcions[0]) or (booll == "N0" and eleg == opcions[1]):
        return Fore.RED + "No estas haciendo buenas acciones"
    else:
        return Fore.GREEN + "Estas haciendo buenas acciones"

if num < 14:
    opcions = ["ocioMinor", "prodMinor"]
    print(valid(opcions))
elif num >= 14 and num < 28:
    opcions = ["ocioAdol", "prodAdol"]
    print(valid(opcions))