"""Un ejemplo del uso del paquete 'curses': 
-- Maneja el estado de los terminales y ejecuciones funcionales."""
import curses as cs
import pyautogui as pg
import time

def nameInput():
    tipocnt = {"pbmv": 0, "f": 0, "td": 0, "szrln": 0, "yñ": 0, "kcxgj": 0, "aeiou": 0}
    pala = input("Ingrese una frase: ")
    for ctr in pala:
        for tp in tipocnt.keys():
            if ctr in tp:
                tipocnt[tp] += 1;  break
    return tipocnt.values(), pala

def porcVocal():
    counts, palabra = nameInput()
    nametipo = ["bilabiales", "dentilabiales", "dentales", "alveolares",
                "palatares", "velares", "vocales"]
    printPorc(palabra, counts, nametipo)
    print("[+] Register complete...")
    cs.beep()

def printPorc(palabra, counts, nametipo):
    cs.initscr()
    def mainCurses(stdscr):
        cs.init_pair(1, cs.COLOR_BLUE, cs.COLOR_WHITE)
        resultado = palabra +"\n-----------------\n"
        stdscr.addstr(resultado, cs.color_pair(1))
        # Realiza el tipeo de consola flotante
        for tipo, name in zip(counts, nametipo):
            porc = round((tipo/len(palabra))*100)
            resultado = name + ":  " + "|"*porc + str(porc) + "%\n"
            stdscr.addstr(resultado, cs.color_pair(1))
            stdscr.refresh()
            time.sleep(0.1)
        pg.write("\n")
        time.sleep(3)
        stdscr.getch()
    cs.wrapper(mainCurses)

if __name__ == "__main__":
    porcVocal()