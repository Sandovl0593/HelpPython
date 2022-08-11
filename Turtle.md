# *Funciones Turtle*

> ## **Mover y dibujar :**

- ### `forward`
```python
# Mueve en línea recta una distancia
forward(100)
```
- ### `right` , `left`
```python
# Gira el icono en su misma posición
right(45) # ángulo a la derecha
left(45) # ángulo a la izquierda
```
- ### `goto`
```python
# Mueve hacia una posición (x, y)
goto(x=60, y=30)
```
- ### `setx` , `sety`
```python
# Variable de la coor x
setx(x=80)
# Variable de la coor y
sety(y=50)
```
- ### `home`
```python
# Vuelve al origen
home() # en la coor (0, 0)
```
- ### `circle`
```python
# Dibuja un circulo
circle(rad=100, # radio del circulo
           extent=20, # angulo de extension, opcional
           steps=100) # pasos a seguir, opcional
```
- ### `dot`
```python
# Dibuja un punto
dot(size=6, # tamaño del punto
        color="blue") # nombre o tupla de color
```
- ### `undo`
```python
# Deshace una acción
undo()
```
- ### `speed`
```python
# Indica la velocidad de trazado
speed(6) # a mayor número mayor velocidad
```
- ### `pos` o `position`
```python
# Variable con la coor de posición actual
pos()
```

> ## **Control del lápiz :**

- ### `penup` , `pendown`
```python
# Deja de trazar el lápiz 
penup()
# Vuelve a trazar el lápiz
pendown()
```
- ### `pensize`
```python
# Grosor del trazo
pensize(10)
```
- ### `pen`
```python
# Diccionario con las configuraciones del trazo
pen(pendown=False,
        pencolor="green",
        speed=8)
lapiz = pen()
```
- ### `color`
```python
# Colores del trazo y relleno respect.
color("green",
      "lightgreen")
color("#a0c8f0") # Un parámetro para trazo y relleno
```
- ### `begin_fill` , `end_fill`
```python
# Se llama como inicio de la figura a rellenar
begin_fill()
# Se llama para rellenar la figura
end_fill()
```
- ### `reset`
```python
# Restablece las configuraciones
# ... y borra el dibujo de la pantalla
reset()
```
- ### `clear`
```python
# SOLO borra el dibujo actual de la pantalla
clear()
```

> ## **Estado y apariencia del icono :**

- ### `hideturtle` , `showturtle`
```python
# Desapaece el icono durante el dibujo
hideturtle()
# Muestra el icono
showturtle()
```
- ### `shapesize`
```python
# Configuración del icono
shapesize(stretch_wid=5, # Anchura del icono
              stretch_len=5, # Altura del icono
              outline=12) # Grosor del contorno
```
- ### `shape`
```python
# Icono personalizado
shape("square")
```
- ### `tilt` , `tiltangle`
```python
# Gira el icono sin afectar la dirección actual
tilt(180)
# Variable
angulo3 = tiltangle()
```

> ## **Métodos especiales :**

- ### `onclick` , `onrelease` , `ondrag`
```python
# Permite realizar acciones con el mouse
onclick() # mediante clicks
onrelease() # click pulsando
ondrag() # Pulsando en movimiento
'''
(fun=Draw()  # función con parametros x e y,
 btn=1  # botón del mouse)
'''

# clicks al icono
tapiz = Turtle()                                # definir clase
tapiz.onclick(); onclick()                      # implementar onclick

# clicks a la pantalla
ventana = TurtleScreen(); ventana = Screen()    # definir clase
ventana.onclick()                               # implementar onclick
```
- ### `begin_poly` , `end_poly` , `get_poly`
```python
# Comienza a grabar la figura
begin_poly()
# Deja de grabar
end_poly()
# Variable con la figura guardada
figura = get_poly()
```
- ### `clone`
```python
# Crea un clon del icono de igual configuración
copia = clone()
```
- ### `onkey` , `onkeypress`
```python
# Permite realizar acciones con el teclado
onkey() # Con teclas
onkeypress() # Tecla pulsando
```
- ### `tracer`
```python
# Configura la animacion durante el trazo
tracer(n=8, # acciones por actualizado
           delay=25) # segundos de transición
```

> ## **Control de ventana :**

- ### `bgcolor`
```python
# Color de fondo de pantalla
bgcolor("orange") # nombre o tupla de color
```
- ### `bgpic`
```python
# Imagen o gif como fondo de pantalla
bgpic("troll.gif") # Si describe "nopic", borra la imagen
```
- ### `clearscreen`
```python
# Restablece la configuración de pantalla
clearscreen()
```
- ### `screensize`
```python
# redimensiona la ventana a mayor 
# ... escala con barras de desplazamiento
screensize(width=2000, # Anchura
               height=1500) # Altura
```
- ### `mainloop`
```python
# Mantiene la ventana abierta
mainloop()
```
- ### `textinput`
```python
# Abre una ventana input
textinput(title="PythonDraw", # Nombre de ventana
              prompt="Ingrese su carrera: ") # Descripción
```
- ### `numinput`
```python
# Abre una ventana int(input)
numinput(title="CountPyPy", # Nombre de ventana
             prompt="Copas actuales: ", # Descripción
             default=500, # Dato por defecto, opcional
             min=100, # mínimo dato
             max=30000) # máximo dato
```
- ### `setup`
```python
# Configuración de la ventana a la medida del monitor
setup(width=200, # Anchura
          height=200, # Altura
          starx=0, # Centra en coor x, opcional
          starty=0) # Centra en coor y, opcional
```
- ### `title`
```python
# Titulo de la ventana
title("Bienvenido dibujante")
```

# *Clases Turtle*

### **`Turtle`**

 Interacciona con los métodos del tapiz y trazado:
 
 `back` `backward` `bk` `circle` `clear` `clearstamp` `clearstamps` `clone` `color` `degrees` `distance` `dot` `down` `fd` `fillcolor` `filling` `forward` `getpen` `getscreen` `getturtle` `goto` `heading` `hideturtle` `home` `ht` `isdown` `isvisible` `left` `lt` `onclick` `ondrag` `onrelease` `pd` `pen` `pencolor` `pendown` `pensize` `penup` `pos` `position` `pu` `radians` `reset` `resizemode` `right` `rt` `screens` `seth` `setheading` `setpos` `setposition` `settiltangle` `setundobuffer` `setx` `sety` `shape` `shapesize` `shapetransform` `shearfactor` `showturtle` `speed` `st` `stamp` `tilt` `tiltangle` `towards` `turtlesize` `undo` `undobufferentries` `up` `width` `write` `xcor` `ycor`

### **`TurtleScreen`**

Interacciona con los métodos de la ventana:

`addshape` `bgcolor` `bgpic` `clear` `clearscreen` `colormode` `delay` `getcanvas` `getshapes` `listen` `mainloop` `mode` `numinput` `onclick` `onkey` `onkeypress` `onkeyrelease` `onscreenclick` `ontimer` `reset` `resetscreen` `screensize` `setworldcoordinates` `textinput` `tracer` `turtles` `update`

### **`Screen`**

Subclase con nuevos métodos del `TurtleScreen`:

`bye` `canvheight` `canvwidth` `cv` `exitonclick` `setup` `title` `xscale` `yscale`

### **`Shape`**

Solo tiene a `addcomponent`