"""Un ejemplo del uso del paquete 'csv': 
-- Realiza ediciones y lecturas de archivos CSV."""
import csv
import random as rd

def vaciar(file):
    with open(file, "w") as arch:
        arch.write("")

with open("pokemon.csv", "r") as archiv:
    typed = archiv.readlines()

porc = int(input("Porcentaje de mayusculas: "))
while porc > 100:
    porc = int(input("Porcentaje de mayusculas: "))

def coloqueUpper(porc):
    "Rearchiva la hoja de pokemons con mayusculas aleatorias"
    with open("pokemon.csv", "r") as arch:
        distrib = arch.readlines()
        encabez = distrib[0].split(",")
    vaciar("pokemon.csv")
    with open("pokemon.csv", "a") as arch:
        writer = csv.DictWriter(arch, fieldnames=encabez)
        distrib.pop(0)
        writer.writeheader()
        for linea in distrib:
            line = linea.split(",")
            fila = {}
            for red, caract in zip(encabez, line):
                fila[red] = randomMayus(caract, porc).replace('"', '')
            writer.writerow(fila)

def randomMayus(palabra:str, porce):
    "Genera mayusculas aleatorias en una palabra"
    cant = round(len(palabra)*porce/100)
    rm = [];   c = 0
    for _ in range(len(palabra)):
        rdom = rd.choice([True, False]) 
        if rdom:
            rm.append(1);  c+=1
        else:       rm.append(0)
        if c == cant:
            break
    rm += [0 for _ in range(len(palabra)-cant)]

    n_palabra = ""
    for let, vlid in zip(palabra, rm):
        n_palabra += let.upper() if vlid == 1 else let
    return n_palabra

coloqueUpper(porc)