# *Paquetes Python*

- ### `argparse` -- Construcción de argumentos de interfaces en la línea de comandos con *`ArgumentParser`*
    ```py
    parser = argparse.ArgumentParser()
    parser.add_argument("nums", type=int, nargs="+")
    result = parser.parse_args("5 4 2 1".split())
    ```
    > #### `add_argument` Asigna un argumento indicador o de posición
    ![argparse](Imagenes\argparse.png)
    > #### `parse_args` Usa argumentos en el editor

- ### `array` -- Define un arreglo por tipo de objeto específico con *`array`*
    ```py
    cater = "Welcome"
    arr = array.array("u", cater)
    arr = list(arr)
    ```
    ![array](imagenes\array.png)

- ### `calendar` -- Distribución de datos del calendario
    ```py
    # Iteración de fechas en conjuntos
    root = calendar.Calendar()
    diasFalt = list(root.itermonthdays(2012, 3))
    # Formato en texto de las fechas
    root2 = calendar.TextCalendar()
    diasName = root2.formatmonthname(2012, 3)
    ```
    > #### `calendar.Calendar` -- Class sobre iteraciones de fechas
    > #### `calendar.TextCalendar` -- Class sobre estructuras del calendario

- ### `cmd` -- Soporte de intérpretes de la línea de comandos con el class *`Cmd`*
    ```py
    class prueba(cmd.Cmd):
        intro = "Bienvenido..."
        prompt = "(Cmd)"
        def do_print(self, arg):
            print("Hola mundo")
    prueba().cmdloop()
    ```
    > #### `cmdloop` : Ejecuta el terminal de entradas repetitivas
    > #### `intro` : Genera un banner o título
    > #### `prompt` : El aviso inicial para emitir entradas
    ![cmd](imagenes\cmd.png)

- ### `csv` -- Lectura y escritura de archivos .csv
    ![csv](imagenes\csv.preview.png)
    > #### `reader` : lee el archivo
    > #### `csv.DictReader` : class sobre analisis del archivo
    ```py
    with open("pok.csv", newline='') as arch:
        reader = csv.DictReader(arch)
        print("Ultima columna:", tuple(x["Edad"] for x in reader))
    with open("pok.csv", newline='') as arch:
        linea = csv.reader(arch, delimiter=',')
        print("Ultima fila:\t", ", ".join(x for x in list(linea)[2]))
    ```
    ![csv](imagenes\csv.png)
    > #### `writer` : agrega texto al archivo
    > #### `csv.DictWriter` : class sobre edición del archivo
    ```py
    with open("pok.csv", "w", newline='') as arch:
        distribucion = ["Nombre", "Apellido", "Edad"]
        writer = csv.DictWriter(arch, fieldnames=distribucion)
        writer.writeheader()
        writer.writerow({"Nombre": "Grass", "Apellido":"Ruiz Tamadera", "Edad":"39"})
        linea = csv.writer(arch, delimiter=',')
        linea.writerow(["Andres", "Gomez Dario", "45"])
    ```

- ### `curses`
    > 

- ### `curses_util`
    > 

- ### `datetime`
    > 

- ### `difflib`
    > 

- ### `distutils` : crea módulos ejecutables
    > 

- ### `email`
    > 

- ### `flask`
    > 

- ### `getpass`
    > 

- ### `glob`
    > 

- ### `html`
    > 

- ### `idlelib`
    > 

- ### `imageio`
    > 

- ### `io`
    > 

- ### `itertools`
    > 

- ### `json`
    > 

- ### `keyword`
    > 

- ### `math`
    > 

- ### `numpy`
    > 

- ### `matplotlib` : Biblioteca de creación de gráficos, animaciones y visores 3D

    - #### `matplotlib.animation` Configuración de la animación del gráfico
    - #### `matplotlib.patches` Personalización de las etiquetas de los ejes cartesianos
    - #### `matplotlib.pyplot` Configuración del gráfico cartesiano
        > #### `bar` Asigna barras verticales al gráfico.
        > #### `barh` Asigna barras horizontales al gráfico.
        > #### `figure` Asigna la ventana matplotlib.
        > #### `plot` Configura una variable cuantitativa al gráfico. 
        > #### `scatter` Asigna coordenadas que unen lineas al gráfico.

- ### `openpyxl`
    > 

- ### `os`
    - #### `os.path`
        > 

- ### `pandas`
    > 

- ### `perlin_noise`
    > 

- ### `PIL`
    > 

- ### `platform`
    > 

- ### `playsound`
    > 

- ### `pprint`
    > 

- ### `processing_py`
    > 

- ### `py2exe` no tiene funciones, crea ejecutables Path
    > 

- ### `pyautogui`
    > 

- ### `pylab`
    >

- ### `pygame`
    > 

- ### `pystyle`
    > 

- ### `pyttsx3`
    > 

- ### `pywhatkit`
    > 

- ### `random`
    > 

- ### `re`
    > 

- ### `readline`
    > 

- ### `requests`
    > 

- ### `secrets`
    > 

- ### `simpleaudio`
    > 

- ### `shutil`
    > 

- ### `statistics`
    > 

- ### `string`
    > 

- ### `stringprep`
    > 

- ### `subprocess`
    > 

- ### `sys`
    > 

- ### `test`
    > 

- ### `time`
    > 

- ### `tkinter`
    > 

- ### `turtle`
    > 

- ### `unittest`
    > 

- ### `urllib`
    > 

- ### `ursina`
    > 

- ### `webbrowser`
    > 

- ### `wikipedia`
    > 

- ### `zlib`
    > 

- ### `zipfile`
    > 
