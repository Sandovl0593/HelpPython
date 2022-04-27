"Un ejemplo del uso del paquete 'argparse'"
import argparse
import os.path, random as rd
import string as st

parser = argparse.ArgumentParser()
parser.add_argument("--nums", type=int, nargs="+")
parser.add_argument("--validfile", "-vf", type=str)
parser.add_argument("--writefile", "-wf", type=str)

result = parser.parse_args()

def writeNums(nums:list):
    "imprime los numeros en el archivo"
    with open("register.txt", "w") as file:
        for num in nums:
            file.write(str(num) + " ")
        file.write("\n---------\n")

def validFile(file):
    "Valida si el archivo existe"
    if os.path.isfile(file):
        print("+ existing file")
        return True
    else:
        print("- file not found")
        return False

def writeFile(file, nums:list):
    "Cada iteracion se imprime un conjunto signo"
    if validFile(file):
        for num in nums:
            printRandomStr(file, num, nums)
        print("+ Typed file")
    
def printRandomStr(file, num, nums:list):
    "Imprimer un signo random despues de espacios"
    cters = st.punctuation
    index = rd.randint(0, num*2)
    espaces = " "*(50//len(nums))
    for _ in range(num):
        write = f"{cters[index]}{espaces}"*num + "\n"
        with open(file, "a") as arch:
            arch.write(write)

def examNums(file):
    "Examina los numeros en el archivo"
    with open(file, "r") as file:
        for line in file.readlines():
            return list(map(int, line.split()))

if __name__ == "__main__":
    if result.nums != None:
        writeNums(result.nums)
    if result.validfile != None:
        bool = validFile(result.validfile)
    if result.writefile != None:
        numbers = examNums(result.writefile)
        writeFile(result.writefile, numbers)
