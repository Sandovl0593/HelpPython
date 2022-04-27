import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x200")
ventana.title("Paquetes de Python")

paquetName = []
paquetFunc = [] # lista de paquetes

description = tk.Label(ventana, text="Escoge un paquete:",
                       font=("Cascadia Code", 16))
description.pack()

inputs = tk.Entry(ventana, font=("Cascadia Code", 14))
inputs.pack()

button = tk.Button(ventana, text="Mostrar", font=("Cascadia Code", 14),
                  activebackground="lightgreen", command=ventana.quit)
button.pack()

ventana.mainloop()

for func in paquetName:
    index = paquetName.index(func)
    if func == inputs.get():
        paquetFunc[index]()
        break