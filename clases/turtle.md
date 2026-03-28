# Guía docente: clase completa de Turtle en Python

> Material pensado para el profesor. Esta guía está escrita para que puedas leerla desde el móvil mientras das la clase. El objetivo no es impresionar con teoría, sino ayudarte a llevar una clase visual, ordenada y práctica.

---

# 1. Objetivo general de la clase

El objetivo de esta clase es que los estudiantes:

- entiendan qué es `turtle`
- vean por primera vez programación visual en Python
- aprendan a mover un objeto en pantalla
- relacionen lo que ya saben de variables, bucles, condicionales y funciones con algo visual
- salgan de clase habiendo hecho al menos figuras y, si da tiempo, una pequeña interacción o mini proyecto

Esta clase también está pensada para ti como docente que viene de usar Python y Tkinter, pero no Turtle. Así que la guía incluye explicaciones prácticas para que aprendas la librería al mismo tiempo que la enseñas.

---

# 2. Qué es Turtle y cómo explicárselo al grupo

## Explicación sencilla para los alumnos

Puedes explicar Turtle así:

> Turtle es una forma de dibujar con Python. Imaginemos que hay una tortuga o un lápiz en pantalla. Nosotros le damos órdenes: avanza, gira, cambia color, levanta el lápiz, baja el lápiz. Con esas órdenes podemos dibujar figuras y hacer programas visuales.

## Explicación un poco más técnica para ti

`Turtle` es un módulo de Python orientado a enseñanza. Permite mover un cursor gráfico en una ventana. Ese cursor va dejando un trazo si el “lápiz” está abajo. Está muy bien para enseñar:

- secuencia de instrucciones
- coordenadas
- bucles
- funciones
- parámetros
- eventos
- animación simple

## Idea pedagógica clave

Turtle funciona muy bien porque cada línea de código produce un cambio visible. Eso es exactamente lo que suele necesitar un grupo principiante para mantenerse motivado.

---

# 3. Lo mínimo que debes saber tú antes de empezar

Estas son las ideas básicas de Turtle:

- la tortuga está dentro de una ventana
- tiene posición
- tiene dirección
- puede avanzar o girar
- puede dibujar o moverse sin dibujar
- podemos cambiar color, grosor y velocidad

## Coordenadas básicas

La pantalla funciona como un plano cartesiano:

- `x` controla izquierda y derecha
- `y` controla arriba y abajo
- el centro suele ser `(0, 0)`

No hace falta dar una clase profunda de matemáticas. Solo que entiendan que un objeto puede moverse por coordenadas.

---

# 4. Qué instalar o preparar antes de la clase

En la mayoría de instalaciones normales de Python, `turtle` ya viene incluido.

Prueba antes de la clase este código:

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.forward(100)

pantalla.mainloop()
```

Si se abre la ventana y dibuja una línea, ya estás listo.

## Consejo importante

Ejecuta tú mismo todos los ejemplos antes de la clase.

---

# 5. Estructura sugerida para la clase de mañana

## Opción de clase larga

### Parte 1. Introducción corta a métodos de strings (si quieres cerrar ese pendiente)
Duración sugerida: 15 a 25 minutos

Solo lo más útil:

- `.lower()`
- `.upper()`
- `.strip()`
- `.replace()`
- `.split()`

Esto te sirve para cerrar el tema pendiente sin robarle demasiado tiempo a Turtle.

### Parte 2. Introducción a Turtle
Duración sugerida: 20 minutos

- qué es Turtle
- ventana y tortuga
- avanzar y girar
- primeros dibujos simples

### Parte 3. Turtle con bucles
Duración sugerida: 25 a 35 minutos

- cuadrado
- triángulo
- polígonos simples
- patrones repetitivos

### Parte 4. Turtle con funciones
Duración sugerida: 20 a 30 minutos

- `dibujar_cuadrado()`
- `dibujar_triangulo()`
- parámetros para tamaño y color

### Parte 5. Personalización visual
Duración sugerida: 15 a 25 minutos

- color
- grosor
- velocidad
- mover sin dibujar

### Parte 6. Si sobra tiempo
Duración sugerida: 20 a 30 minutos

- coordenadas
- mover a posiciones concretas
- mini proyecto o interacción simple

---

# 6. Guion docente para explicar Turtle por primera vez

Puedes decir algo como esto:

> Hasta ahora hemos trabajado con consola: texto, números, decisiones, bucles, funciones. Hoy vamos a empezar a ver programación visual. Vamos a usar Turtle, que nos permite controlar una tortuga en pantalla como si fuera un lápiz. Le daremos órdenes con código y veremos el resultado inmediatamente.

> Lo importante no es memorizar todos los comandos. Lo importante es entender que seguimos usando la misma lógica de siempre: instrucciones, repetición, decisiones y funciones, solo que ahora el resultado se ve en pantalla.

---

# 7. Primer programa con Turtle

## Código mínimo

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.forward(100)

pantalla.mainloop()
```

## Cómo explicarlo

- `import turtle`: trae la librería
- `turtle.Screen()`: crea la ventana
- `turtle.Turtle()`: crea la tortuga
- `t.forward(100)`: avanza 100 píxeles
- `pantalla.mainloop()`: mantiene la ventana abierta

## Comentario docente

No hace falta entrar a explicar internamente qué es un objeto con profundidad. Puedes decir simplemente:

> `t` es nuestra tortuga, y a través de `t` le damos órdenes.

---

# 8. Comandos básicos de Turtle

## Mover hacia adelante

```python
t.forward(100)
```

La tortuga avanza 100.

## Mover hacia atrás

```python
t.backward(50)
```

Retrocede.

## Girar a la derecha

```python
t.right(90)
```

Gira 90 grados.

## Girar a la izquierda

```python
t.left(90)
```

Gira hacia la izquierda.

## Levantar el lápiz

```python
t.penup()
```

Se mueve sin dibujar.

## Bajar el lápiz

```python
t.pendown()
```

Vuelve a dibujar.

## Ir a una posición

```python
t.goto(100, 50)
```

Va directamente a esas coordenadas.

## Cambiar color

```python
t.color("red")
```

## Cambiar grosor

```python
t.pensize(3)
```

## Cambiar velocidad

```python
t.speed(3)
```

`1` suele ser lento y `10` más rápido. También se usa `0` para lo más rápido posible.

## Borrar dibujo

```python
t.clear()
```

## Volver al origen

```python
t.home()
```

Regresa a `(0, 0)` mirando hacia la derecha.

---

# 9. Primeros ejercicios inmediatos

## Ejercicio 1: línea y giro

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)

pantalla.mainloop()
```

### Qué reforzar

- secuencia
- órdenes paso a paso
- relación entre código y resultado visual

## Ejercicio 2: dibujar una L

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)

pantalla.mainloop()
```

---

# 10. Dibujar figuras básicas

## Cuadrado sin bucle

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

pantalla.mainloop()
```

## Cómo explicarlo

Aquí el alumno ve repetición. Es el momento perfecto para preguntar:

> ¿No estamos repitiendo demasiado?

Y ahí introduces el bucle.

## Cuadrado con bucle

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

pantalla.mainloop()
```

## Idea docente importante

Aquí conectas directamente con lo que ya saben de `for`.

---

# 11. Triángulo, pentágono y otras figuras

## Triángulo

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

for _ in range(3):
    t.forward(100)
    t.left(120)

pantalla.mainloop()
```

## Pentágono

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

for _ in range(5):
    t.forward(80)
    t.left(72)

pantalla.mainloop()
```

## Regla útil para explicar

Si una figura tiene `n` lados, el giro exterior suele ser:

```text
360 / n
```

No hace falta profundizar demasiado. Solo úsalo como curiosidad útil si el grupo va bien.

---

# 12. Patrones con bucles

## Espiral simple

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

for i in range(50):
    t.forward(i * 5)
    t.right(90)

pantalla.mainloop()
```

## Figura repetitiva con cambio de color

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

colores = ["red", "blue", "green", "purple"]

for i in range(20):
    t.color(colores[i % 4])
    t.forward(100)
    t.right(95)

pantalla.mainloop()
```

## Qué trabajar aquí

- bucles
- listas
- módulo `%`
- experimentación

---

# 13. Uso de funciones con Turtle

Este es uno de los puntos más importantes de la clase porque refuerza muy bien el tema que ya viste.

## Función para dibujar un cuadrado

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

def dibujar_cuadrado():
    for _ in range(4):
        t.forward(100)
        t.right(90)

dibujar_cuadrado()

pantalla.mainloop()
```

## Cómo explicarlo

Puedes decir:

> La función nos permite guardar una serie de pasos para reutilizarlos cuando queramos.

## Función con parámetro

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

def dibujar_cuadrado(lado):
    for _ in range(4):
        t.forward(lado)
        t.right(90)

dibujar_cuadrado(50)

dibujar_cuadrado(120)

pantalla.mainloop()
```

## Función con varios parámetros

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

def dibujar_cuadrado(lado, color):
    t.color(color)
    for _ in range(4):
        t.forward(lado)
        t.right(90)

dibujar_cuadrado(80, "red")
t.penup()
t.goto(150, 0)
t.pendown()
dibujar_cuadrado(120, "blue")

pantalla.mainloop()
```

## Idea pedagógica clave

Aquí es donde los alumnos entienden de verdad para qué servían las funciones.

---

# 14. Mover la tortuga sin dibujar

## Código ejemplo

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.forward(100)

t.penup()
t.goto(-100, 100)
t.pendown()

t.circle(50)

pantalla.mainloop()
```

## Qué explicar

`penup()` sirve para cambiar la posición sin dejar línea.

Esto es muy útil para:

- dibujar varias figuras separadas
- colocar la tortuga donde queremos
- organizar mejor la pantalla

---

# 15. Dibujar círculos y escribir texto

Los círculos son importantes en Turtle porque permiten hacer mucho más que figuras geométricas rectas. Con círculos puedes hacer:

- ruedas
- caras
- ojos
- soles
- pelotas
- botones dibujados
- patrones circulares
- composiciones más artísticas

## Círculo básico

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.circle(50)

pantalla.mainloop()
```

### Cómo explicarlo

`circle(50)` dibuja un círculo de radio 50.

No hace falta dar una explicación matemática profunda. Basta con decir:

> Turtle sabe dibujar un círculo si le damos el tamaño del radio.

## Círculo más grande o más pequeño

```python
t.circle(20)
t.circle(80)
```

Aquí puedes reforzar la idea de parámetro: cambiamos el número y cambia el tamaño.

## Varios círculos en distintas posiciones

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

t.circle(40)

t.penup()
t.goto(120, 0)
t.pendown()
t.circle(60)

t.penup()
t.goto(-120, 0)
t.pendown()
t.circle(30)

pantalla.mainloop()
```

### Qué trabajas aquí

- círculos
- coordenadas
- `penup()` y `pendown()`
- composición visual

## Círculo relleno

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.color("black", "orange")
t.begin_fill()
t.circle(50)
t.end_fill()

pantalla.mainloop()
```

Esto queda muy bien para hacer soles, botones, pelotas o caras.

## Medio círculo y arcos

Esto es muy útil y normalmente sorprende bastante.

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

t.circle(80, 180)

pantalla.mainloop()
```

### Cómo explicarlo

Cuando pones un segundo valor, Turtle no dibuja el círculo completo. Dibuja solo una parte.

- `t.circle(80, 180)` dibuja medio círculo
- `t.circle(80, 90)` dibuja un cuarto de círculo

Esto sirve muchísimo para:

- sonrisas
- arcos
- pétalos
- nubes
- decoraciones

## Ejemplo: carita simple

```python
import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

# Cara
t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Ojo izquierdo
t.penup()
t.goto(-35, 20)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Ojo derecho
t.penup()
t.goto(35, 20)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Sonrisa
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.pensize(4)
t.circle(50, 120)

pantalla.mainloop()
```

Este ejemplo queda excelente en clase porque mezcla:

- círculos
- relleno
- posiciones
- arco

## Función para dibujar un círculo

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

def dibujar_circulo(radio, color):
    t.color(color)
    t.circle(radio)

dibujar_circulo(40, "blue")
t.penup()
t.goto(120, 0)
t.pendown()
dibujar_circulo(70, "red")

pantalla.mainloop()
```

Esto te permite reforzar funciones con parámetros de una manera muy visual.

## Escribir texto

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.write("Hola, Turtle!", font=("Arial", 16, "normal"))

pantalla.mainloop()
```

## Posible uso en clase

Puedes hacer una tarjeta simple, una carita o una pantalla con título.

---

# 16. Personalización visual

## Color de línea y relleno

```python
t.color("blue")
```

También puedes usar dos colores:

```python
t.color("black", "yellow")
```

El primero es el borde y el segundo el relleno.

## Rellenar una figura

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.color("black", "yellow")
t.begin_fill()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

pantalla.mainloop()
```

## Cambiar forma del cursor

```python
t.shape("turtle")
```

Otras formas comunes:

- `arrow`
- `classic`
- `circle`
- `square`
- `triangle`
- `turtle`

---

# 17. Coordenadas en Turtle

Este bloque es importante porque hace el puente entre lógica y movimiento en pantalla.

## Ejemplo básico con `goto`

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.goto(100, 100)
t.goto(-100, 100)
t.goto(0, 0)

pantalla.mainloop()
```

## Cómo explicarlo

- `(0, 0)` es el centro
- si `x` aumenta, vamos a la derecha
- si `x` disminuye, vamos a la izquierda
- si `y` aumenta, subimos
- si `y` disminuye, bajamos

## Ejercicio sugerido

Haz que los estudiantes coloquen la tortuga en:

- `(100, 0)`
- `(-100, 0)`
- `(0, 100)`
- `(0, -100)`

---

# 18. Métodos útiles para saber dónde está la tortuga

## Posición actual

```python
t.pos()
```

## Coordenada X

```python
t.xcor()
```

## Coordenada Y

```python
t.ycor()
```

## Dirección actual

```python
t.heading()
```

No hace falta enseñar todos estos en profundidad en la primera clase, pero es bueno que tú sepas que existen.

---

# 19. Fondo de pantalla y personalización de la ventana

## Cambiar color de fondo

```python
pantalla.bgcolor("lightblue")
```

## Cambiar título

```python
pantalla.title("Mi primera clase con Turtle")
```

## Cambiar tamaño de la ventana

```python
pantalla.setup(width=800, height=600)
```

## Ejemplo completo

```python
import turtle

pantalla = turtle.Screen()
pantalla.title("Dibujo con Turtle")
pantalla.bgcolor("lightblue")
pantalla.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(3)

for _ in range(4):
    t.forward(100)
    t.right(90)

pantalla.mainloop()
```

---

# 20. Eventos de teclado básicos y clics

Esto puede ser muy motivador, pero no es obligatorio si no da tiempo. Si llegas aquí, genial.

Primero puedes enseñar teclado, y después clics con ratón. Los clics son muy buenos porque el alumno siente que ya está interactuando con una interfaz real.

## Ejemplo: mover con teclas

```python
import turtle

pantalla = turtle.Screen()
pantalla.setup(width=600, height=400)

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def mover_arriba():
    t.setheading(90)
    t.forward(20)

def mover_abajo():
    t.setheading(270)
    t.forward(20)

def mover_izquierda():
    t.setheading(180)
    t.forward(20)

def mover_derecha():
    t.setheading(0)
    t.forward(20)

pantalla.listen()
pantalla.onkey(mover_arriba, "Up")
pantalla.onkey(mover_abajo, "Down")
pantalla.onkey(mover_izquierda, "Left")
pantalla.onkey(mover_derecha, "Right")

pantalla.mainloop()
```

## Qué explicar

- definimos funciones
- cada función mueve la tortuga
- asociamos una tecla a una función
- `listen()` hace que la ventana escuche el teclado

## Valor pedagógico

Aquí los alumnos entienden:

- funciones
- eventos
- relación entre entrada del usuario y resultado en pantalla


## Eventos de clic con ratón

Aquí empieza una parte muy interesante porque Turtle permite detectar en qué lugar de la pantalla hizo clic el usuario.

### Idea simple para explicarlo

Puedes decir:

> Igual que podemos reaccionar cuando alguien pulsa una tecla, también podemos reaccionar cuando alguien hace clic en la pantalla.

## Ejemplo 1: imprimir coordenadas del clic

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

def mostrar_click(x, y):
    print("Hiciste clic en:", x, y)

pantalla.onscreenclick(mostrar_click)

pantalla.mainloop()
```

### Qué explicar

- la función recibe dos parámetros: `x` y `y`
- esos valores indican dónde se hizo clic
- `onscreenclick()` conecta el clic con una función

Esto viene muy bien para reforzar parámetros en funciones.

## Ejemplo 2: mover la tortuga al lugar del clic

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def mover_al_click(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

pantalla.onscreenclick(mover_al_click)

pantalla.mainloop()
```

### Qué enseñar aquí

- coordenadas reales
- relación entre clic y posición
- reutilización de `goto()`

## Ejemplo 3: dibujar un punto o círculo donde hagan clic

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

def dibujar_circulo_click(x, y):
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.circle(20)

pantalla.onscreenclick(dibujar_circulo_click)

pantalla.mainloop()
```

### Nota para ti

Se usa `y - 20` para que el círculo quede centrado aproximadamente donde el usuario hizo clic. Si no ajustas eso, el círculo empieza a dibujarse desde un borde.

## Ejemplo 4: poner texto donde se hace clic

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

def escribir_click(x, y):
    t.penup()
    t.goto(x, y)
    t.write("Hola", font=("Arial", 14, "normal"))

pantalla.onscreenclick(escribir_click)

pantalla.mainloop()
```

Esto les suele gustar mucho porque ya parece una mini aplicación interactiva.

## Posibles ejercicios con clics

1. Mostrar las coordenadas donde se hace clic.
2. Mover la tortuga a donde el usuario haga clic.
3. Dibujar un círculo en cada clic.
4. Dibujar estrellas en cada clic.
5. Escribir el nombre del alumno en el punto del clic.
6. Cambiar de color cada vez que hagan clic.

## Mini proyecto con clics: sellos de colores

```python
import turtle
import random

pantalla = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

colores = ["red", "blue", "green", "purple", "orange"]

def sello(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colores))
    t.dot(30)

pantalla.onscreenclick(sello)

pantalla.mainloop()
```

Aquí mezclas:

- eventos
- funciones
- coordenadas
- `random`

Y además es muy vistoso.

## Error típico con clics

Muchos alumnos hacen una función sin parámetros:

```python
def mover():
    t.goto(100, 100)
```

Y luego la conectan al clic. Eso da problema porque el evento de clic envía `x` y `y`.

La forma correcta es:

```python
def mover(x, y):
    t.goto(x, y)
```

Ese detalle es muy importante y te conviene remarcarlo.

---

# 21. Dibujar una casa simple

Este ejercicio queda muy bien como actividad guiada.

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

# Cuadrado de la casa
for _ in range(4):
    t.forward(100)
    t.left(90)

# Techo
t.left(45)
t.forward(70)
t.left(90)
t.forward(70)

pantalla.mainloop()
```

## Cómo usarlo

Puedes hacerlo paso a paso con el grupo y luego pedirles que:

- cambien el tamaño
- cambien el color
- agreguen puerta o ventana

---

# 22. Dibujar una estrella

```python
import turtle

pantalla = turtle.Screen()
t = turtle.Turtle()

t.color("gold")
t.pensize(3)

for _ in range(5):
    t.forward(150)
    t.right(144)

pantalla.mainloop()
```

Muy buena para impresionar visualmente sin demasiado código.

---

# 23. Mini proyecto 1: patrón artístico

## Objetivo

Que el alumno experimente con:

- color
n- bucles
- giros
- tamaño creciente

## Código base

```python
import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colores = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(60):
    t.color(colores[i % len(colores)])
    t.forward(i * 4)
    t.right(59)

pantalla.mainloop()
```

## Qué pedirles

- cambiar colores
- cambiar ángulo
- cambiar la fórmula del avance

---

# 24. Mini proyecto 2: dibujador con teclado

## Idea

Mueven la tortuga con flechas y dibujan libremente.

### Posibles mejoras

- tecla para levantar lápiz
- tecla para bajar lápiz
- tecla para cambiar color
- tecla para limpiar pantalla

## Código simple

```python
import turtle

pantalla = turtle.Screen()
pantalla.setup(800, 600)

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

def arriba():
    t.setheading(90)
    t.forward(20)

def abajo():
    t.setheading(270)
    t.forward(20)

def izquierda():
    t.setheading(180)
    t.forward(20)

def derecha():
    t.setheading(0)
    t.forward(20)

def levantar():
    t.penup()

def bajar():
    t.pendown()

def limpiar():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

pantalla.listen()
pantalla.onkey(arriba, "Up")
pantalla.onkey(abajo, "Down")
pantalla.onkey(izquierda, "Left")
pantalla.onkey(derecha, "Right")
pantalla.onkey(levantar, "u")
pantalla.onkey(bajar, "d")
pantalla.onkey(limpiar, "c")

pantalla.mainloop()
```

---

# 25. Errores típicos de los estudiantes

## 1. Olvidar importar la librería

```python
import turtle
```

## 2. Escribir mal el nombre de un método

Ejemplos:

- `foward` en vez de `forward`
- `rigth` en vez de `right`

## 3. Olvidar los paréntesis al llamar una función

```python
dibujar_cuadrado
```

En vez de:

```python
dibujar_cuadrado()
```

## 4. Problemas de indentación

Sobre todo dentro de `for` o `def`.

## 5. Confundir girar con avanzar

A veces esperan que `right(90)` dibuje algo por sí solo.

## 6. Repetir demasiado código en vez de usar funciones o bucles

Esto en realidad es una oportunidad para reforzar buena práctica.

## 7. Cerrar la ventana demasiado rápido

Por eso suele ser útil `pantalla.mainloop()`.

---

# 26. Errores típicos tuyos como docente si es tu primera vez con Turtle

## 1. Explicar demasiada teoría al principio

Evítalo. Empieza con código visible cuanto antes.

## 2. Querer explicar orientación a objetos formalmente

No hace falta. Basta con decir:

> `t` representa nuestra tortuga y le damos órdenes a través de `t`.

## 3. Ir demasiado rápido a eventos si el grupo aún no está firme

Primero figuras, luego funciones, y solo después interacción.

## 4. Querer cubrir demasiado

Es mejor que hagan bien un cuadrado, un triángulo y una función, a que toquen quince cosas sin entenderlas.

---

# 27. Preguntas que probablemente te harán los alumnos

## “¿Esto sirve para hacer juegos?”

Respuesta recomendada:

> Sí, juegos simples. No es una librería profesional para videojuegos grandes, pero sí sirve para aprender lógica, movimiento, dibujo, interacción y minijuegos básicos.

## “¿Esto es como una app?”

> No exactamente. Es una ventana gráfica donde dibujamos y controlamos una tortuga. Más adelante hay otras herramientas para interfaces más completas.

## “¿Por qué gira 90?”

> Porque estamos dibujando un cuadrado, y cada esquina necesita un giro recto.

## “¿Se puede cambiar el color?”

> Sí, y es una buena forma de experimentar.

---

# 28. Ejercicios propuestos para clase

## Ejercicios fáciles

1. Dibujar una línea de 150 píxeles.
2. Dibujar una L.
3. Dibujar un cuadrado sin bucle.
4. Dibujar un cuadrado con bucle.
5. Dibujar un triángulo.

## Ejercicios intermedios

6. Dibujar tres cuadrados separados usando `goto()`.
7. Crear una función `dibujar_cuadrado(lado)`.
8. Crear una función `dibujar_triangulo(lado)`.
9. Dibujar una fila de figuras cambiando color.
10. Dibujar una espiral simple.

## Ejercicios un poco más potentes

11. Dibujar una casa.
12. Dibujar una estrella.
13. Mover la tortuga con teclado.
14. Crear un mini dibujador.
15. Dibujar varias figuras de distinto tamaño usando una lista.

---

# 29. Propuesta de desarrollo de la clase paso a paso

## Tramo 1

- explicar qué es Turtle
- correr el ejemplo mínimo
- mover hacia adelante y girar

## Tramo 2

- dibujar una L
- dibujar un cuadrado sin bucle
- preguntar cómo evitar repetir

## Tramo 3

- cuadrado con `for`
- triángulo
- pentágono o estrella si el grupo va bien

## Tramo 4

- crear función para dibujar cuadrado
- agregar parámetro de tamaño
- agregar parámetro de color

## Tramo 5

- usar `penup()` y `goto()`
- dibujar varias figuras en posiciones distintas

## Tramo 6

- si sobra tiempo: teclado y movimiento
- si no sobra tiempo: mini proyecto artístico

---

# 30. Clase puente ideal hacia la próxima sesión

Al final de la clase puedes decir algo como:

> Hoy usamos Python para dibujar y mover objetos en pantalla. En la próxima clase podemos hacer dos caminos: seguir mejorando nuestros dibujos y funciones, o empezar a hacer programas interactivos, por ejemplo, mover la tortuga con el teclado o hacer un mini juego.

Eso deja el terreno listo para:

- Turtle con eventos
- Turtle con listas y colores
- mini juegos
- introducción a interfaces más adelante

---

# 31. Plantilla rápida para copiar durante la clase

```python
import turtle

pantalla = turtle.Screen()
pantalla.title("Mi programa con Turtle")
pantalla.bgcolor("white")
pantalla.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(2)
t.speed(3)

# Tu código aquí

pantalla.mainloop()
```

---

# 32. Ejemplo final recomendado para mañana

Si solo pudieras enseñar un ejemplo completo y bonito, yo elegiría este porque mezcla casi todo.

```python
import turtle

pantalla = turtle.Screen()
pantalla.title("Figuras con Turtle")
pantalla.bgcolor("lightyellow")
pantalla.setup(width=900, height=700)

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.pensize(3)

def dibujar_cuadrado(lado, color):
    t.color(color)
    for _ in range(4):
        t.forward(lado)
        t.right(90)

def dibujar_triangulo(lado, color):
    t.color(color)
    for _ in range(3):
        t.forward(lado)
        t.left(120)

# Primer dibujo

dibujar_cuadrado(100, "red")

# Mover sin dibujar

t.penup()
t.goto(180, 0)
t.pendown()

# Segundo dibujo

dibujar_triangulo(120, "blue")

# Tercer dibujo

t.penup()
t.goto(-180, 0)
t.pendown()

t.color("green")
t.begin_fill()
for _ in range(5):
    t.forward(80)
    t.right(72)
t.end_fill()

pantalla.mainloop()
```

## Por qué este ejemplo es bueno

Porque te permite repasar:

- importación
- ventana
- tortuga
- color
- funciones
- parámetros
- bucles
- mover sin dibujar
- varias figuras en pantalla

---

# 33. Si los alumnos avanzan demasiado rápido

Aquí tienes ideas extra por si el grupo va muy bien:

- usar una lista de colores
- usar `random` para colores o tamaños
- hacer una espiral artística
- hacer un dibujador con teclado
- hacer una carrera entre varias tortugas
- dibujar un plano cartesiano simple
- hacer una función que dibuje círculos en distintas posiciones

## Ejemplo con `random`

```python
import turtle
import random

pantalla = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

colores = ["red", "blue", "green", "orange", "purple"]

for _ in range(20):
    t.color(random.choice(colores))
    t.forward(random.randint(20, 100))
    t.right(random.randint(20, 150))

pantalla.mainloop()
```

---

# 34. Si el grupo se atrasa o se bloquea

Reduce la clase a esto:

1. ejemplo mínimo
2. línea y giro
3. cuadrado con `for`
4. triángulo
5. una función `dibujar_cuadrado()`

Con eso la clase ya habrá valido la pena.

---

# 35. Resumen docente final

## Qué debes lograr mañana sí o sí

Como mínimo:

- que entiendan que Turtle es programación visual
- que ejecuten un programa con Turtle
- que dibujen una figura simple
- que usen un bucle para una figura
- que vean una función aplicada a Turtle

## Qué sería un extra muy bueno

- usar `goto()`
- cambiar colores
- dibujar varias figuras
- mover con teclado

## Qué no pasa nada si no llegas a dar

- eventos
- mini juego
- patrones más avanzados
- animaciones

---

# 36. Idea para la próxima clase después de esta

Si mañana sale bien, tu siguiente clase ideal es:

## Turtle 2

- repaso rápido
- funciones con parámetros
- listas de colores
- dibujo repetitivo
- interacción con teclado
- mini proyecto guiado

---

# 37. Cierre sugerido para ti

Tu objetivo mañana no es convertirlos en expertos en Turtle.
Tu objetivo es que por primera vez sientan que programar también puede significar ver algo moverse, dibujarse o construirse en pantalla.

Si logras eso, la clase habrá sido un éxito.
